from knowledge_base import carregar_base_conhecimento, buscar_na_base


# Carrega os arquivos da pasta data apenas uma vez.
BASE_CONHECIMENTO = carregar_base_conhecimento()


def formatar_resultado(resultado):
    """
    Transforma um item encontrado na base em texto legível.

    Parâmetros:
        resultado: dicionário contendo categoria e conteúdo.

    Retorno:
        Texto formatado.
    """

    categoria = resultado["categoria"]
    conteudo = resultado["conteudo"]

    linhas = [f"Categoria: {categoria}"]

    for chave, valor in conteudo.items():
        nome_campo = chave.replace("_", " ").title()
        linhas.append(f"{nome_campo}: {valor}")

    return "\n".join(linhas)


def gerar_resposta_local(pergunta):
    """
    Gera uma resposta usando somente a base de conhecimento local.

    Parâmetros:
        pergunta: dúvida informada pela pessoa usuária.

    Retorno:
        Resposta produzida pelo DBA Mentor.
    """

    if not pergunta or not pergunta.strip():
        return (
            "Digite uma dúvida sobre SQL, MySQL ou Banco de Dados "
            "para que eu possa ajudar."
        )

    resultados = buscar_na_base(
        pergunta=pergunta,
        base_conhecimento=BASE_CONHECIMENTO
    )

    if not resultados:
        return (
            "Não encontrei informações suficientes na minha base de "
            "conhecimento para responder com segurança.\n\n"
            "Envie mais detalhes, como:\n"
            "- estrutura das tabelas;\n"
            "- nomes das colunas;\n"
            "- consulta SQL utilizada;\n"
            "- mensagem de erro apresentada."
        )

    # Limita a quantidade de resultados para evitar respostas muito extensas.
    resultados_limitados = resultados[:3]

    respostas_formatadas = [
        formatar_resultado(resultado)
        for resultado in resultados_limitados
    ]

    resposta = (
        "Encontrei estas informações relacionadas à sua dúvida:\n\n"
        + "\n\n---\n\n".join(respostas_formatadas)
    )

    if identificar_comando_perigoso(pergunta):
        resposta += (
            "\n\n⚠️ Atenção: sua pergunta envolve um comando que pode "
            "alterar ou excluir dados. Faça backup e valide a condição "
            "com um SELECT antes de executar."
        )

    return resposta


def identificar_comando_perigoso(pergunta):
    """
    Verifica se a pergunta contém comandos que podem alterar ou excluir dados.

    Retorno:
        True quando encontrar um comando de risco.
        False quando não encontrar.
    """

    comandos_perigosos = [
        "delete",
        "update",
        "drop",
        "truncate",
        "alter"
    ]

    pergunta_normalizada = pergunta.lower()

    return any(
        comando in pergunta_normalizada
        for comando in comandos_perigosos
    )


if __name__ == "__main__":
    pergunta_teste = input("Digite uma dúvida sobre SQL: ")

    resposta = gerar_resposta_local(pergunta_teste)

    print("\nResposta do DBA Mentor:\n")
    print(resposta)
