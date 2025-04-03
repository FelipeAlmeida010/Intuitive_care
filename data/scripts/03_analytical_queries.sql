-- Consulta para despesas no último trimestre
SELECT reg_ans, 
       SUM(vl_saldo_final) AS total_despesas
FROM despesas_contabeis
WHERE descricao = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR'
  AND data BETWEEN '2024-01-01' AND '2024-03-31'  -- Ajustar para o último trimestre real
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;

-- Consulta para despesas no último ano
SELECT reg_ans, 
       SUM(vl_saldo_final) AS total_despesas
FROM despesas_contabeis
WHERE descricao = 'EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR'
  AND data BETWEEN '2023-01-01' AND '2023-12-31'  -- Ajustar para o ano real
GROUP BY reg_ans
ORDER BY total_despesas DESC
LIMIT 10;
