from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .User import User
from .Location import Location
from .DeviceInfo import DeviceInfo
from .HostageSentence import HostageSentence
from .ExplosiveSentence import ExplosiveSentence
