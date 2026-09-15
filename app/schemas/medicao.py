from pydantic import BaseModel


class MedicaoCreate(BaseModel):
    host_id: int
    latencia_ms: float | None = None
    perda_pacotes: float