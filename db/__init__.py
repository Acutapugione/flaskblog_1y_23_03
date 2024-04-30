from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped, mapped_column


engine = create_engine("sqlite://", echo=True)
Session = sessionmaker(engine)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

from .models import Post



def up():
    Base.metadata.create_all(engine)


def down():
    Base.metadata.drop_all(engine)
    
    
down()
up()