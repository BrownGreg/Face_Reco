from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    face_encoding = Column(String, nullable=False)  # Stocke l'encodage du visage

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"