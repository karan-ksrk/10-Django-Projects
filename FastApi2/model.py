from sqlalchemy import Column, String, Numeric, Integer, ForeignKey, DateTime, Text, 
from database import Base
from sqlalchemy.orm import relationship
class Genre(Base):
    __tablename__ = "Genre"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    genre = relationship("Music", back_populates="")

class Music(Base):
    __tablename__ = "Music"

    id = Column(Integer, primary_key=True, index=True)
    music_title = Text(length=200)
    file_type = Text(length=300)
