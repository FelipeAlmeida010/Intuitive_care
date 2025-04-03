from flask import Blueprint, request, jsonify
import pandas as pd

# Criando o Blueprint para as rotas
bp = Blueprint('api', __name__)

# Carregando o CSV de operadoras
operadoras_df = pd.read_csv('data/operadoras_de_plano_de_saude_ativas.csv')

@bp.route('/search', methods=['GET'])
def search_operadora():
    # Obtém o termo de busca da query string
    termo = request.args.get('termo', '')
    
    # Realiza uma busca simples no nome da operadora
    resultado = operadoras_df[operadoras_df['nome'].str.contains(termo, case=False, na=False)]

    # Retorna o resultado como JSON
    return jsonify(resultado.to_dict(orient='records')), 200
