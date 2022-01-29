from dataclasses import dataclass


@dataclass
class Model:
    name: str

    def __post_init__(self):
        pass
