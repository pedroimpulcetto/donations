from enum import Enum


class Status(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN PROGRESS"
    FINISHED = "FINISHED"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
