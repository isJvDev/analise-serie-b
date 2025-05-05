# Análise do Campeonato Brasileiro Série B - 2025

<h1>Este projeto realiza uma análise automatizada da tabela do Campeonato Brasileiro Série B utilizando a API API-Futebol. O objetivo é demonstrar habilidades em coleta de dados, tratamento, análise e visualização com Python.</h1>

# Tecnologias Utilizadas

Python 3.10+

pandas

matplotlib

requests

API REST (API-Futebol)

# Funcionalidades

Autenticação via token de acesso

Download e leitura da lista de campeonatos

Identificação automática do ID da Série B

Coleta da tabela de classificação da Série B 2025

Criação de DataFrame e ordenação por aproveitamento

Impressão dos 5 times com melhor desempenho

Geração de gráfico de barras e salva como imagem

Exportação dos dados para CSV

# Estrutura do Projeto

.
├── campeonatos.json                   # Lista de campeonatos
├── output/
│   ├── tabela_serie_b.json            # Tabela da Série B 2025
│   ├── serie_b_aproveitamento.csv     # Dados tratados em CSV
│   └── serie_b_aproveitamento_2025.png # Gráfico gerado
├── analise_serie_b.py                # Script principal

# Como Executar

Clone este repositório:

git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

Instale as dependências:

pip install pandas matplotlib requests

Configure o seu token de acesso da API:

headers = {
    "Authorization": "Bearer SEU_TOKEN_AQUI"
}

# Execute o script:

python analise_serie_b.py

Exemplo de Saída

Os 5 times com maior aproveitamento são listados no terminal

Um gráfico como o abaixo é gerado e salvo:



# Licença

Este projeto é de uso livre para fins educacionais.

Desenvolvido por [João Vitor] ❤️
