import csv
import json
from pathlib import Path


# Localiza a pasta principal do projeto.
BASE_DIR = Path(__file__).resolve().parent.parent

# Localiza a pasta que contém os arquivos da base de conhecimento.
DATA_DIR = BASE_DIR / "data"


def carregar_json(nome_arquivo):
    """
    Carrega e retorna o conteúdo de um arquivo JSON.

    Parâmetros:
        nome_arquivo: nome do arquivo localizado dentro da pasta data.

    Retorno:
        Lista ou dicionário com os dados do arquivo JSON.
    """

    caminho_arquivo = DATA_DIR / nome_arquivo

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return []

    except json.JSONDecodeError:
        print(f"Erro ao interpretar o arquivo JSON: {caminho_arquivo}")
        return []


def carregar_csv(nome_arquivo):
    """
    Carrega e retorna o conteúdo de um arquivo CSV.

    Parâmetros:
        nome_arquivo: nome do arquivo localizado dentro da pasta data.

    Retorno:
        Lista de dicionários com os dados do arquivo CSV.
    """

    caminho_arquivo = DATA_DIR / nome_arquivo

    try:
        with open(
            caminho_arquivo,
            "r",
            encoding="utf-8-sig",
            newline=""
        ) as arquivo:

            leitor = csv.DictReader(arquivo)
            return list(leitor)

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return []


def carregar_base_conhecimento():
    """
    Carrega todos os arquivos da base de conhecimento.

    Retorno:
        Dicionário contendo conceitos, comandos, erros e exemplos.
    """

    return {
        "conceitos": carregar_json("conceitos_sql.json"),
        "comandos": carregar_csv("comandos_sql.csv"),
        "erros": carregar_json("erros_comuns.json"),
        "exemplos": carregar_json("exemplos_consultas.json")
    }


def buscar_na_base(pergunta, base_conhecimento):
    """
    Procura palavras da pergunta dentro da base de conhecimento.

    Parâmetros:
        pergunta: texto informado pelo usuário.
        base_conhecimento: dicionário com os arquivos carregados.

    Retorno:
        Lista de itens encontrados.
    """

    pergunta_normalizada = pergunta.lower()
    resultados = []

    for categoria, itens in base_conhecimento.items():
        for item in itens:
            texto_item = " ".join(
                str(valor) for valor in item.values()
            ).lower()

            if any(
                palavra in texto_item
                for palavra in pergunta_normalizada.split()
                if len(palavra) > 2
            ):
                resultados.append(
                    {
                        "categoria": categoria,
                        "conteudo": item
                    }
                )

    return resultados
