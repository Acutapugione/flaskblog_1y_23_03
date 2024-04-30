from .. import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, time


class Post(Base):
    __tablename__ = "post"
    created: Mapped[time] = mapped_column(default=datetime.now().time())

    title: Mapped[str]
    content: Mapped[str]