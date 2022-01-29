from dataclasses import dataclass, asdict
import json


@dataclass
class Model:
    name: str

    def __post_init__(self):
        pass

    def to_json(self):
        return json.dumps(asdict(self))
