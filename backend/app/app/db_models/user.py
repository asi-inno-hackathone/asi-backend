from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, nullable=False)

    passport = relationship("Passport", back_populates="user", uselist=False)
    entrepreneur = relationship("Entrepreneur", back_populates="user",  uselist=False)
    investor = relationship("Investor", back_populates="user", uselist=False)