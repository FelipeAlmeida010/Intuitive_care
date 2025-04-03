import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
import os
import zipfile

def baixar_pdf(url, nome_arquivo):
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        with open(nome_arquivo, 'wb') as pdf:
            for chunk in resposta.iter_content(chunk_size=1024):
                pdf.write(chunk)
        print(f"Download concluído: {nome_arquivo}")
    else:
        print(f"Erro ao baixar {nome_arquivo}")

# URL do site da ANS
url_base = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Requisição para obter o HTML da página
resposta = requests.get(url_base)
soup = BeautifulSoup(resposta.text, 'html.parser')

# Encontrar links para os anexos
pdf_links = []
for link in soup.find_all('a', href=True):
    if 'Anexo' in link.text and link['href'].endswith('.pdf'):
        pdf_links.append(link['href'])

# Criar pasta para armazenar os PDFs
os.makedirs("anexos", exist_ok=True) 

# Baixar os PDFs
pdf_files = []
for i, pdf_url in enumerate(pdf_links[:2]):  # Pegamos apenas os dois primeiros (Anexo I e II)
    nome_arquivo = os.path.join("anexos", f"Anexo_{i+1}.pdf")
    baixar_pdf(pdf_url, nome_arquivo)
    pdf_files.append(nome_arquivo)

# Criar um arquivo ZIP
zip_filename = "anexos.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in pdf_files:
        zipf.write(file, os.path.basename(file))

print(f"Arquivos compactados em {zip_filename}")
