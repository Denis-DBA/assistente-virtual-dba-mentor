# 🎤 Pitch do Projeto

## DBA Mentor — Assistente Virtual para SQL e Banco de Dados

Muitos estudantes e profissionais em transição de carreira encontram dificuldades para aprender SQL, compreender mensagens de erro e construir consultas corretamente.

Pensando nesse problema, foi desenvolvido o **DBA Mentor**, um assistente virtual criado para apoiar o aprendizado de SQL, MySQL e conceitos fundamentais de Banco de Dados.

O assistente utiliza uma base de conhecimento organizada com conceitos, comandos, erros comuns e exemplos de consultas. A partir da pergunta do usuário, ele pesquisa essas informações e apresenta uma resposta de forma didática e objetiva.

Entre suas principais funcionalidades, o DBA Mentor pode:

- Explicar comandos SQL;
- Apresentar exemplos práticos;
- Ajudar na correção de erros;
- Diferenciar conceitos de Banco de Dados;
- Alertar sobre comandos perigosos;
- Informar quando não possui dados suficientes para responder.

Um dos diferenciais do projeto é o foco em segurança. Ao identificar comandos como `DELETE`, `UPDATE`, `DROP`, `ALTER` ou `TRUNCATE`, o assistente apresenta um alerta antes da execução.

A primeira versão foi desenvolvida com Python, Streamlit e arquivos JSON e CSV. Esses arquivos funcionam como uma base de conhecimento local, permitindo que o protótipo responda sem depender inicialmente de uma API externa.

Durante a avaliação, foram testadas perguntas sobre `JOIN`, chave estrangeira, exclusão de dados e consultas incompletas. O assistente apresentou respostas compatíveis com a base, alertas de segurança e mensagens solicitando mais contexto quando necessário.

Como melhorias futuras, o projeto poderá receber integração com modelos de Inteligência Artificial, busca semântica, validação automática de consultas e suporte a outros bancos de dados, como PostgreSQL, Oracle e SQL Server.

O DBA Mentor demonstra como a Inteligência Artificial pode apoiar o aprendizado técnico, tornando o estudo de Banco de Dados mais acessível, seguro e prático.
