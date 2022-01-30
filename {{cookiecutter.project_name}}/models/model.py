from pydantic import BaseModel, Extra, validator
from datetime import datetime
import hashlib
from typing import List, Optional


class Model(BaseModel, extra=Extra.allow):
    title: str
    datetime: str = datetime.now().isoformat()
    id: Optional[str] = ""

    @validator("id", pre=True)
    def set_id(cls, v, values):
        return create_unique_id(values["title"])


def create_unique_id(title: str):
    return hashlib.md5(title.encode("utf-8")).hexdigest()
