from sqlmodel import Field, SQLModel
import time
import uuid


class Scan(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    filename: str | None = Field(default=uuid.uuid4().hex + ".png")
