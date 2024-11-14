from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models import Base


class DeviceInfo(Base):
    __tablename__ = 'device_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String, nullable=False)
    os = Column(String, nullable=False)
    browser = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="device_info")
