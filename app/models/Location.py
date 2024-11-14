from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from app.models import Base

class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float,nullable=False)
    longitude = Column(Float,nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="location")
