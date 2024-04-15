from langchain_community.chat_message_histories.in_memory import ChatMessageHistory

from langchain.pydantic_v1 import BaseModel, Field
from langchain.schema import (
    BaseChatMessageHistory,
)
from langchain.schema.messages import BaseMessage


class ChatMessageHistory(BaseChatMessageHistory, BaseModel):
    """In memory implementation of chat message history.

    Stores messages in an in memory list.
    """

    messages: List[BaseMessage] = Field(default_factory=list)

    def add_message(self, message: BaseMessage) -> None:
        """Add a self-created message to the store"""
        self.messages.append(message)

    def clear(self,k=0) -> None:
        if k:
            del(self.messages[:-(k*2)])
        else:
            self.messages = []

__all__ = ["ChatMessageHistory"]
