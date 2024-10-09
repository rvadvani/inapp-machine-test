from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

class Movie(Base):
    __tablename__ = 'movies'
    
    tconst = Column(String(20), primary_key=True)
    title_type = Column(String(50))
    primary_title = Column(String(255))
    original_title = Column(String(255))
    is_adult = Column(Boolean, default=False)
    start_year = Column(Integer, nullable=True)
    end_year = Column(Integer, nullable=True)
    runtime_minutes = Column(Integer, nullable=True)
    genres = Column(String(255))

    def __repr__(self):
        return f"<Movie(title={self.primary_title})>"


class Person(Base):
    __tablename__ = 'persons'
    
    nconst = Column(String(20), primary_key=True)
    primary_name = Column(String(255))
    birth_year = Column(Integer, nullable=True)
    death_year = Column(Integer, nullable=True)
    primary_profession = Column(String(255))
    known_for_titles = Column(String(255))
    
    movies = relationship("Movie", secondary="movie_person")

    def __repr__(self):
        return f"<Person(name={self.primary_name})>"

class MoviePerson(Base):
    __tablename__ = 'movie_person'
    movie_id = Column(String(20), ForeignKey('movies.tconst'), primary_key=True)
    person_id = Column(String(20), ForeignKey('persons.nconst'), primary_key=True)
