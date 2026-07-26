import streamlit as st

from chatbot import gerar_resposta_local


# Configurações principais da página.
st.set_page_config(
    page_title="DBA Mentor",
    page_icon="🤖",
    layout="centered"
)


# Título da aplicação.
st.title("🤖 DBA Mentor")

# Subtítulo explicativo.
st.subheader("Assistente Virtual para SQL e MySQL")

st.write(
    "Digite uma dúvida sobre SQL, MySQL ou Banco de Dados. "
    "O assistente consultará a base de conhecimento local para responder."
)


# Cria o histórico da conversa.
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# Exibe as mensagens já enviadas.
for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["papel"]):
        st.markdown(mensagem["conteudo"])


# Campo de entrada da pessoa usuária.
pergunta = st.chat_input("Digite sua dúvida sobre SQL...")


if pergunta:
    # Armazena e exibe a pergunta.
    st.session_state.mensagens.append(
        {
            "papel": "user",
            "conteudo": pergunta
        }
    )

    with st.chat_message("user"):
        st.markdown(pergunta)

    # Gera a resposta utilizando a base local.
    resposta = gerar_resposta_local(pergunta)

    # Armazena e exibe a resposta.
    st.session_state.mensagens.append(
        {
            "papel": "assistant",
            "conteudo": resposta
        }
    )

    with st.chat_message("assistant"):
        st.markdown(resposta)


# Barra lateral.
with st.sidebar:
    st.header("📚 Sobre o projeto")

    st.write(
        "O DBA Mentor foi desenvolvido para apoiar estudantes "
        "no aprendizado de SQL, MySQL e conceitos de Banco de Dados."
    )

    st.warning(
        "Comandos como DELETE, UPDATE, DROP, ALTER e TRUNCATE "
        "devem ser testados com cuidado."
    )

    if st.button("Limpar conversa"):
        st.session_state.mensagens = []
        st.rerun()
