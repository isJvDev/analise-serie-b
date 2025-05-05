import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import os

def baixar_lista_campeonatos(headers, output_path):
    url = 'https://api.api-futebol.com.br/v1/campeonatos/'
    try:
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status()
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(resposta.json(), f, ensure_ascii=False, indent=4)
        print(f"\nLista de campeonatos salva em '{output_path}'.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar a lista de campeonatos: {e}")

def buscar_id_serie_b(caminho_arquivo_json):
    try:
        with open(caminho_arquivo_json, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        for campeonato in dados:
            nome = campeonato.get('nome', '').lower()
            if "brasileiro série b" in nome:
                print(f"\nCampeonato encontrado: {campeonato['nome']} (ID: {campeonato['campeonato_id']})")
                return campeonato['campeonato_id']
        print("\nCampeonato Brasileiro Série B não encontrado.")
    except FileNotFoundError:
        print("Arquivo 'campeonatos.json' não encontrado.")
    return None

def baixar_tabela_serie_b(campeonato_id, headers, output_path):
    url = f"https://api.api-futebol.com.br/v1/campeonatos/{campeonato_id}/tabela"
    try:
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status()
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(resposta.json(), f, ensure_ascii=False, indent=4)
        print(f"\nTabela salva com sucesso em '{output_path}'.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar a tabela: {e}")

def analisar_dados_tabela(caminho_arquivo_json):
    with open(caminho_arquivo_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    df = pd.DataFrame(dados)
    df['nome'] = df['time'].apply(lambda x: x['nome_popular'])
    df_ordenado = df.sort_values(by='aproveitamento', ascending=False)

    print("\nTop 5 times com melhor aproveitamento na Série B:")
    print(df_ordenado[['nome', 'pontos', 'jogos', 'aproveitamento']].head())

    return df_ordenado

def gerar_grafico(df_ordenado, output_path):
    plt.figure(figsize=(10, 8))
    plt.barh(df_ordenado['nome'], df_ordenado['aproveitamento'], color='dodgerblue')
    plt.xlabel('Aproveitamento (%)')
    plt.title('Aproveitamento dos times na Série B - 2025')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.show()
    print(f"\nGráfico salvo como '{output_path}'.")

def salvar_csv(df, output_path):
    df.to_csv(output_path, sep=';', index=False, encoding='utf-8-sig')
    print(f"\nArquivo CSV '{output_path}' criado com sucesso!")

# Execução principal
if __name__ == "__main__":
    headers = {
        "Authorization": "Bearer #coloque sua key"
    }

    os.makedirs("output", exist_ok=True)

    # Baixa a lista de campeonatos se ainda não existir
    if not os.path.exists("campeonatos.json"):
        baixar_lista_campeonatos(headers, "campeonatos.json")

    campeonato_id = buscar_id_serie_b("campeonatos.json")

    if campeonato_id:
        baixar_tabela_serie_b(campeonato_id, headers, "output/tabela_serie_b.json")
        df_ordenado = analisar_dados_tabela("output/tabela_serie_b.json")
        gerar_grafico(df_ordenado, "output/serie_b_aproveitamento_2025.png")
        salvar_csv(df_ordenado, "output/serie_b_aproveitamento.csv")
