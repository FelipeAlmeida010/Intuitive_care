from fastapi import FastAPI, Query
import pandas as pd

# Inicializa a aplicação FastAPI
app = FastAPI()

# Caminho do arquivo CSV
data_file = "intuitive_care/data/dados_cadastrais/Relatorio_cadop.csv"

# Carregar os dados do CSV
try:
    df = pd.read_csv(data_file, delimiter=';', dtype=str)
except Exception as e:
    print(f"Erro ao carregar o arquivo CSV: {e}")

@app.get("/buscar")
def buscar_operadora(query: str = Query(..., min_length=3)):
    """
    Busca textual na lista de operadoras cadastradas.
    """
    resultados = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False).any(), axis=1)]
    
    return resultados.to_dict(orient="records")
