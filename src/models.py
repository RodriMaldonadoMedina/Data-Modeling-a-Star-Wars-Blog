import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    password = Column(String(8), nullable=False, unique=True)
    email = Column(String(40), nullable=False)
    suscription = Column(datetime(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "user_last_name": self.last_name,
            "suscription": self.suscription
            # do not serialize the password, its a security breach
        }

class Personaje(Base):
    __tablename__='personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    birth_date = Column(String(15), nullable=True)
    gender = Column(String(10), nullable=True)
    height = Column(String(6), nullable=True)
    eye_color = Column(String(15), nullable=True)
    skin_color = Column(String(15), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "height": self.height,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color
        }

class Planeta(Base):
    __tablename__='planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    diametro = Column(String(15), nullable=True)
    clima = Column(String(10), nullable=True)
    gravedad = Column(String(6), nullable=True)
    habitantes = Column(String(15), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "diametro": self.diametro,
            "clima": self.clima,
            "gravedad": self.gravedad,
            "habitantes": self.habitantes
        }

class Nave(Base):
    __tablename__='nave'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    costo_creditos = Column(int(15), nullable=False)
    pasajeros = Column(int(10), nullable=True)
    capacidad_carga = Column(int(20), nullable=True)
    clase = Column(String(15), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "costo_creditos": self.costo_creditos,
            "pasajeros": self.pasajeros,
            "capacidad_carga": self.capacidad_carga,
            "clase": self.clase
        }

class Personaje_Favorito(Base):
    __tablename__='personaje_favorito'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(user.id))
    personaje_id = Column(integer, ForeignKey(personaje.id))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "personaje_id": self.personaje_id,
        }

class Planeta_Favorito(Base):
    __tablename__='planeta_favorito'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(user.id))
    planeta_id = Column(integer, ForeignKey(planeta.id))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planeta_id": self.planeta_id,
        }

class Nave_Favorito(Base):
    __tablename__='nave_favorito'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(user.id))
    nave_id = Column(integer, ForeignKey(nave.id))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "nave_id": self.nave_id,
        }

"""class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

"""
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')