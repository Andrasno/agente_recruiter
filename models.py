# models.py

from pydantic import BaseModel, Field

class AnaliseRequest(BaseModel):
    """Modelo de entrada para a requisição de análise."""
    id_vaga: int = Field(..., description="O ID da vaga para a qual o candidato está aplicando.")
    curriculo_candidato: str = Field(..., description="O texto completo do currículo do candidato.")

class AnaliseResponse(BaseModel):
    """Modelo de saída contendo o parecer da IA."""
    parecer: str