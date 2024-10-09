from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from sqlalchemy import create_engine
from .models import Movie, Person, MoviePerson
from .serializers import MovieSerializer, PersonSerializer
from .models import User
from .sqlalchemy_config import SessionLocal
from django.contrib.auth.hashers import make_password


class LoginView(APIView):
    def post(self, request):
        session = SessionLocal()

        username = request.data.get('username')
        password = request.data.get('password')

        user = session.query(User).filter(User.username == username).first()

        if user and user.password == password: 
            refresh = RefreshToken.for_user(user)
            session.close()
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        session.close()
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class MovieSearchView(APIView):
    def get(self, request):
        year = request.query_params.get('year')
        genre = request.query_params.get('genre')
        person_name = request.query_params.get('person_name')
        title_type = request.query_params.get('type')

        session = SessionLocal()

        query = session.query(Movie)

        if year:
            query = query.filter(Movie.start_year == year)
        if genre:
            query = query.filter(Movie.genres.ilike(f'%{genre}%'))
        if person_name:
            person_subquery = session.query(Person).filter(
                Person.primary_name.ilike(f'%{person_name}%')
            ).subquery()
            query = query.join(MoviePerson).filter(MoviePerson.person_id == person_subquery)

        if title_type:
            query = query.filter(Movie.title_type == title_type)

        movies = query.all()

        serializer = MovieSerializer(movies, many=True)

        response_data = []
        for movie in serializer.data:
            associated_people = session.query(Person).join(MoviePerson).filter(
                MoviePerson.movie_id == movie['tconst']
            ).all()
            people_names = [person.primary_name for person in associated_people]

            response_data.append({
                "Title": movie['primary_title'],
                "Year Released": movie['start_year'],
                "Type": movie['title_type'],
                "Genre": movie['genres'],
                "List of People Associated with the title": people_names
            })

        return Response(response_data, status=status.HTTP_200_OK)


class PersonSearchView(APIView):
    def get(self, request):
        session = SessionLocal()
        query = session.query(Person)

        movie_title = request.query_params.get('movie_title')
        name = request.query_params.get('name')
        profession = request.query_params.get('profession')
        
        if movie_title:
            query = query.filter(Person.known_for_titles.like(f'%{movie_title}%'))  
        if name:
            query = query.filter(Person.primary_name.like(f'%{name}%'))
        if profession:
            query = query.filter(Person.primary_profession == profession)
        
        persons = query.all()
        serializer = PersonSerializer(persons, many=True)

        session.close()  
        return Response(serializer.data)