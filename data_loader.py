# data_loader.py

import pandas as pd
import requests
import zipfile
import io

def carregar_dados_vagas() -> pd.DataFrame:
    """
    Baixa o arquivo ZIP do Google Drive, encontra o arquivo .parquet dentro dele,
    e o carrega em um DataFrame do Pandas.
    """
    # URL de compartilhamento do Google Drive
    gdrive_share_url = "https://drive.google.com/file/d/1h8Lk5LM8VE5TF80mngCcbsQ14qA2rbw_/view?usp=drive_link"
    
    # Extrai o ID do arquivo da URL
    file_id = gdrive_share_url.split('/d/')[1].split('/')[0]
    
    # Monta a URL de download direto
    direct_download_url = f'https://drive.google.com/uc?export=download&id={file_id}'

    print(f"Iniciando download do arquivo de: {direct_download_url}")
    
    try:
        # 1. Baixar o conteúdo do ZIP da URL
        response = requests.get(direct_download_url)
        # Lança um erro se o download falhar (ex: 404, 403)
        response.raise_for_status()  

        # 2. Criar um objeto "em memória" a partir dos bytes baixados
        in_memory_zip = io.BytesIO(response.content)

        # 3. Abrir o arquivo ZIP a partir da memória
        with zipfile.ZipFile(in_memory_zip) as zf:
            # Encontrar o primeiro arquivo .parquet dentro do ZIP
            parquet_file_name = next(
                (name for name in zf.namelist() if name.endswith('.parquet')), 
                None
            )
            
            if not parquet_file_name:
                raise ValueError("Nenhum arquivo .parquet encontrado dentro do arquivo ZIP.")

            print(f"Lendo o arquivo '{parquet_file_name}' de dentro do ZIP...")
            # 4. Ler o Parquet diretamente do ZIP para o Pandas
            with zf.open(parquet_file_name) as pf:
                df = pd.read_parquet(pf)
                print("DataFrame carregado com sucesso.")
                return df

    except requests.exceptions.RequestException as e:
        print(f"Erro de rede ao baixar o arquivo: {e}")
        raise
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        raise