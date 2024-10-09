from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from django.conf import settings

DATABASE_URL = f"postgresql://{settings.DATABASES['default']['USER']}:" \
               f"{settings.DATABASES['default']['PASSWORD']}@" \
               f"{settings.DATABASES['default']['HOST']}:" \
               f"{settings.DATABASES['default']['PORT']}/" \
               f"{settings.DATABASES['default']['NAME']}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
def create_tables():
    from models import Base 
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_tables()
