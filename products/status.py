from enum import Enum


class Status(Enum):
    OPEN = "Disponível"
    IN_PROGRESS = "Em andamento"
    FINISHED = "Finalizado"
    CANCELLED = "Cancelado"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)
