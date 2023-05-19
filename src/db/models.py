from typing import List, Optional
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    source_id: Mapped[int]
    aka_ids: Mapped[List[int]]
    source: Mapped[str] = mapped_column(String(30))  # Telegram, IRC etc.
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    messages: Mapped[List["Message"]] = relationship(back_populates="user")
    attachments: Mapped[List["Attachment"]] = relationship(back_populates="user")
    actions: Mapped[List["Action"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, source_id={self.source_id!r}, aka_ids={self.aka_ids!r}, source={self.source!r}," \
               f"name={self.name!r},fullname={self.fullname!r}), messages={len(self.messages)!r}," \
               f"attachments={len(self.attachments)!r}, actions={len(self.actions)!r}"


class Attachment(Base):
    __tablename__ = "attachment"

    id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str] = mapped_column(String(30))  # Telegram, IRC etc.
    type: Mapped[str] = mapped_column(String(30))
    user: Mapped["User"] = relationship(back_populates="attachments")
    message: Mapped["Message"] = relationship(back_populates="attachments")
    path: Mapped[str] = mapped_column(String)
    thumb_path: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String[30])  # Image, File, Video, Audio, Sticker etc.
    width: Mapped[int] = mapped_column(Integer)
    height: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Attachment(id={self.id!r}, source={self.source!r}, type={self.type!r}, user={self.user!r}, " \
               f"message={self.message.text!r}), path={self.path!r}, thumb_path={self.thumb_path!r}" \
               f"type={self.type!r}, width={self.width!r}, height={self.height!r}"


class Message(Base):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(primary_key=True)
    source_id: Mapped[int]
    source: Mapped[str] = mapped_column(String(30))  # Telegram, IRC etc.
    user: Mapped["User"] = relationship(back_populates="messages")
    date: Mapped[DateTime]
    text: Mapped[str] = mapped_column(String)
    attachment: Mapped["Attachment"] = relationship(back_populates="messages")

    def __repr__(self) -> str:
        return f"Message(id={self.id!r}, source_id={self.source_id!r}, source={self.source!r}, user={self.user!r}, " \
               f"date={self.date!r}), text={self.text!r}, attachment={self.attachment.path!r}"


class Action(Base):
    __tablename__ = "action"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(30))
    target: Mapped["User"] = relationship(back_populates="actions")
    user: Mapped["User"] = relationship(back_populates="actions")
    source: Mapped[str] = mapped_column(String(30))  # Telegram, IRC etc.

    def __repr__(self) -> str:
        return f"Action(id={self.id!r}, type={self.type!r}, source={self.source!r}, user={self.user!r}, " \
               f"target={self.target!r})"
