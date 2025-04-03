#!/bin/bash

echo "Iniciando o processo de configuração do banco de dados..."

# Esperar até o PostgreSQL estar completamente pronto
echo "Aguardando o PostgreSQL inicializar..."
until pg_isready -h localhost -p 5432 -U "$POSTGRES_USER"; do
    echo "Aguardando o banco de dados ficar pronto..."
    sleep 2
done
echo "PostgreSQL está pronto para receber conexões!"

# Aguarda um tempo adicional para garantir a estabilidade do banco
echo "Aguardando 10 segundos para garantir a estabilidade do banco..."
sleep 10

# Criar as tabelas no banco de dados
echo "Criando as tabelas..."
if psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -a -f /scripts/01_create_tables.sql; then
    echo "Tabelas criadas com sucesso."
else
    echo "Erro ao criar tabelas. Encerrando o processo."
    exit 1
fi

# Importar os dados dos arquivos CSV
echo "Importando dados..."
if psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -a -f /scripts/02_import_data.sql; then
    echo "Dados importados com sucesso."
else
    echo "Erro ao importar dados. Encerrando o processo."
    exit 1
fi

echo "Configuração do banco de dados concluída com sucesso!"
