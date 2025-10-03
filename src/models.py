from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class Participant(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    activity_id: Optional[int] = Field(default=None, foreign_key="activity.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Activity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: Optional[str] = None
    schedule: Optional[str] = None
    max_participants: Optional[int] = None
    participants: List[Participant] = Relationship(back_populates="activity")

# Set back_populates on Participant
Participant.activity = Relationship(back_populates="participants")
