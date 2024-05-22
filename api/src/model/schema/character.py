from pydantic import BaseModel, Field
from typing import List, Optional

class Character(BaseModel):
    name: str = Field(..., description="The name of the character.")
    age: int = Field(..., description="The age of the character.")
    gender: str = Field(..., description="The gender of the character.")
    backstory: str = Field(..., description="A brief backstory for the character.")
    skills: List[str] = Field(..., description="List of skills or abilities the character possesses.")



    