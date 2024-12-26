from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

class Base(AsyncAttrs, DeclarativeBase):
    pass

class ChatCompletion(Base):
    __tablename__ = "chat_completions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    timestamp: Mapped[str] = mapped_column(String, nullable=False)
    model: Mapped[str] = mapped_column(String, nullable=False)
    total_tokens: Mapped[int] = mapped_column(Integer, nullable=False)
    tool_count: Mapped[int] = mapped_column(Integer, nullable=False)

    chat_completion_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    request: Mapped[str] = mapped_column(String, nullable=False)
    final_response: Mapped[str] = mapped_column(String, nullable=False)

    tool_calls: Mapped[list["ToolCall"]] = relationship("ToolCall", back_populates="chat_completion")

class ToolCall(Base):
    __tablename__ = "tool_calls"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    chat_completion_id: Mapped[int] = mapped_column(Integer, ForeignKey("chat_completions.id"), nullable=False)

    tool_call_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    tool_name: Mapped[str] = mapped_column(String, nullable=False)
    arguments: Mapped[str] = mapped_column(String, nullable=True)
    result: Mapped[str] = mapped_column(String, nullable=True)

    chat_completion: Mapped["ChatCompletion"] = relationship("ChatCompletion", back_populates="tool_calls")
