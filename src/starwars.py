import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    birth_date = Column(String(10))
    height = Column(String(10))
    hair_color = Column(String(10))
    homeworld = Column(Integer, ForeignKey('planets.id'))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    population = Column(String(50))
    diameter = Column(String(50))
    characters = Column(Integer, ForeignKey('characters.id'))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    model = Column(String(50))
    manufacturer = Column(String(50))

class FavoriteCharacters(Base):
    __tablename__ = 'favoritecharacters'
    id = Column(Integer, primary_key = True)
    id_character = Column(Integer, ForeignKey('characters.id'))

class FavoritePlanets(Base):
    __tablename__ = 'favoriteplanets'
    id = Column(Integer, primary_key = True)
    id_planet = Column(Integer, ForeignKey('planets.id'))

class FavoriteVehicles(Base):
    __tablename__ = 'favoritevehicles'
    id = Column(Integer, primary_key = True)
    id_vehicle = Column(Integer, ForeignKey('vehicles.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    fav_chars = Column(Integer, ForeignKey('favoritecharacters.id'))
    fav_planets = Column(Integer, ForeignKey('favoriteplanets.id'))
    fav_vehicles = Column(Integer, ForeignKey('favoritevehicles.id'))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
