from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.models import Base

class HostageSentence(Base):
    __tablename__ = 'hostage_sentences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    sentence_text = Column(Text, nullable=False)

    user = relationship("User", back_populates="hostage_sentences")