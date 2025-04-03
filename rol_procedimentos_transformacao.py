import pdfplumber
import csv
import zipfile
import os

# Função para substituir abreviações
def substituir_abreviacoes(data):
    legenda = {
        "OD": "Odontologia",
        "AMB": "Ambulatório"
    }
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value in legenda:
                data[i][j] = legenda[value]
    return data

# Função para extrair dados do PDF e salvar em CSV
def extrair_dados_pdf(pdf_path, csv_path):
    with pdfplumber.open(pdf_path) as pdf:
        todas_tabelas = []
        
        # Iterar sobre todas as páginas do PDF
        for page in pdf.pages:
            tabelas = page.extract_tables()
            for tabela in tabelas:
                todas_tabelas.extend(tabela)
        
        # Substituir abreviações
        dados_processados = substituir_abreviacoes(todas_tabelas)
        
        # Salvar em CSV
        with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(dados_processados)
        
        print(f"Dados salvos em {csv_path}")

# Função para compactar o CSV em ZIP
def compactar_csv_em_zip(csv_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))
    
    print(f"Arquivo ZIP criado: {zip_path}")

# Caminho para o PDF (Anexo I)
pdf_path = "anexos/Anexo_1.pdf"
csv_path = "rol_procedimentos.csv"
zip_path = "Teste_felipe.zip"

# Executar a extração e compactação
extrair_dados_pdf(pdf_path, csv_path)
compactar_csv_em_zip(csv_path, zip_path)
