from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")


class Personality(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    career_id: str
    description: str
    interesting_facts: Optional[str]
    born: date
    died: date
    create_dt: datetime | None = Field(default=None)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "name": "Екатерина Великая",
                "career_id": 1,
                "description": "Императрица и Самодержица Всероссийская (1762—1796). Монарх просвещённого абсолютизма. Дочь князя Ангальт-Цербстского, Екатерина взошла на престол в результате дворцового переворота против своего мужа — Петра III, вскоре погибшего при невыясненных обстоятельствах (возможно, он был убит).",
                "interesting_facts": "Немка на русском пристоле. Не любила сына.",
                "born": "02.05.1729",
                "died": "06.11.1796",
            }
        }

    def to_json(self):
        return {
            "_id": str(self.id),
            "name": self.name,
            "career_id": self.career_id,
            "description": self.description,
            "interesting_facts": self.interesting_facts,
            "born": str(self.born),
            "died": str(self.died),
            "create_dt": str(self.create_dt),
        }


class Event(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    start_date: date
    end_date: date
    create_dt: datetime | None = Field(default=None)
    description: str
    victim_numbers: int
    interesting_facts: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "name": "Вторая мировая война",
                "start_date": "01.09.1939",
                "end_date": "03.09.1945",
                "description": "Война двух мировых военно-политических коалиций, ставшая крупнейшим вооружённым конфликтом в истории человечества. В этой войне участвовали 62 государства из 74 существовавших на тот момент (80 % населения Земного шара[3]). Боевые действия велись на территории Евразии и Африки[~ 2] и в водах всех океанов. Это единственный конфликт, в котором было применено ядерное оружие. В результате войны погибло более 70 миллионов человек, большинство из которых — мирные жители.",
                "victim_numbers": 55000000,
                "interesting_facts": "Самая ужасная война за всю историю человечества",
            }
        }

    def to_json(self):
        return {
            "_id": str(self.id),
            "name": self.name,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "create_dt": str(self.create_dt),
            "description": self.description,
            "victim_numbers": self.victim_numbers,
            "interesting_facts": self.interesting_facts,
        }


class EventsAndPersonality(BaseModel):
    personality_id: int
    event_id: int


class Career(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "json_schema_extra": {
                "name": "Императрица",
            }
        }

    def to_json(self):
        return {"_id": str(self.id), "name": self.name}
