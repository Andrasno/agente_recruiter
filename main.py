# main.py

import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from dotenv import load_dotenv
import pandas as pd

from models import AnaliseRequest, AnaliseResponse
from agent import AgenteRecrutador
from data_loader import carregar_dados_vagas

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gerencia o ciclo de vida da aplicação.
    - Carrega o DataFrame e inicializa o agente na inicialização.
    - Libera os recursos (se necessário) no desligamento.
    """
    print("Iniciando a aplicação...")
    # Carrega os dados e o modelo na inicialização
    app.state.df_vagas = carregar_dados_vagas()
    app.state.agente = AgenteRecrutador()
    yield
    # Código para limpeza (se necessário) ao desligar a aplicação
    print("Finalizando a aplicação...")
    app.state.df_vagas = None
    app.state.agente = None

# Inicializa a aplicação FastAPI com o ciclo de vida definido
app = FastAPI(
    title="🤖 Agente Recrutador API",
    description="Uma API para automatizar a análise de currículos com IA Generativa.",
    version="2.0.0",
    lifespan=lifespan
)

# ---- Funções de Dependência para evitar repetição de código ----
def get_agente() -> AgenteRecrutador:
    return app.state.agente

def get_df_vagas() -> pd.DataFrame:
    return app.state.df_vagas

# ---- Endpoints da API ----

@app.get("/", summary="Verifica a saúde da API")
def read_root():
    """Endpoint raiz para verificar se a API está operacional."""
    return {"status": "ok", "message": "Agente Recrutador API no ar!"}

@app.post("/analisar_candidato", 
          response_model=AnaliseResponse, 
          summary="Realiza a análise de um currículo para uma vaga específica")
def analisar_candidato(
    request: AnaliseRequest,
    agente: AgenteRecrutador = Depends(get_agente),
    df_vagas: pd.DataFrame = Depends(get_df_vagas)
):
    """
    Recebe o ID de uma vaga e o currículo de um candidato, e retorna um
    parecer gerado pela IA.
    """
    try:
        # 1. Encontrar a descrição da vaga no DataFrame
        vaga = df_vagas[df_vagas['id'] == request.id_vaga]
        if vaga.empty:
            raise HTTPException(status_code=404, detail=f"Vaga com ID {request.id_vaga} não encontrada.")
        
        # Pega a descrição completa da vaga (supondo que a coluna se chame 'descricao')
        descricao_completa_vaga = vaga.iloc[0]['descricao']

        # 2. Gerar o parecer usando o agente
        parecer_final = agente.gerar_parecer(
            vaga_descricao=descricao_completa_vaga,
            curriculo_candidato=request.curriculo_candidato
        )
        
        return AnaliseResponse(parecer=parecer_final)

    except HTTPException as http_exc:
        # Re-lança exceções HTTP para que o FastAPI as trate
        raise http_exc
    except Exception as e:
        print(f"Erro inesperado no endpoint /analisar_candidato: {e}")
        # Captura qualquer outro erro e retorna uma resposta genérica de erro do servidor
        raise HTTPException(status_code=500, detail="Ocorreu um erro interno no servidor.")