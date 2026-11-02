from pydantic import BaseModel, ConfigDict, Field

from app.models.ticket import TicketStatus

class TicketCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1)

class TicketResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    title: str
    description: str
    status: TicketStatus
    user_id: int

class TicketUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, min_length=1)
    status: TicketStatus | None = None