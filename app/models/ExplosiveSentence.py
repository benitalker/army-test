from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.models import Base


class ExplosiveSentence(Base):
    __tablename__ = 'explosive_sentences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="explosive_sentences")
