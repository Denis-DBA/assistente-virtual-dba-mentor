# 🤖 Assistente Virtual DBA Mentor

## 📖 Sobre o projeto

O **DBA Mentor** é um assistente virtual com Inteligência Artificial desenvolvido para auxiliar estudantes e iniciantes em Banco de Dados na compreensão de conceitos de SQL e MySQL.

O projeto utiliza uma base de conhecimento organizada para responder dúvidas, explicar comandos SQL e orientar a construção de consultas de forma didática, objetiva e confiável.

---

## 🎯 Objetivos

- Explicar conceitos de SQL e MySQL.
- Auxiliar na construção de consultas SQL.
- Corrigir erros comuns de sintaxe.
- Utilizar uma base de conhecimento para gerar respostas.
- Evitar respostas inventadas (alucinações).
- Orientar o usuário quando não houver informações suficientes.

---

## 📑 Índice

- [📖 Sobre o projeto](#-sobre-o-projeto)
- [🎯 Objetivos](#-objetivos)
- [📝 Documentação do Agente](#-documentação-do-agente)
- [📚 Base de Conhecimento](#-base-de-conhecimento)
- [💬 Prompts do Agente](#-prompts-do-agente)
- [💻 Aplicação Funcional](#-aplicação-funcional)
- [📊 Avaliação e Métricas](#-avaliação-e-métricas)
- [🎤 Pitch](#-pitch)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [👨‍💻 Autor](#-autor)

## 🛠️ Tecnologias Utilizadas

- Python 3
- Streamlit
- JSON
- CSV
- Git
- GitHub
- Visual Studio Code

## 📁 Estrutura do Projeto

```text
assistente-virtual-dba-mentor/
├── README.md
├── requirements.txt
├── .gitignore
├── assets/
├── data/
│   ├── comandos_sql.csv
│   ├── conceitos_sql.json
│   ├── erros_comuns.json
│   └── exemplos_consultas.json
├── docs/
│   ├── documentacao_agente.md
│   ├── metricas.md
│   └── pitch.md
└── src/
    ├── app.py
    ├── chatbot.py
    ├── knowledge_base.py
    └── prompts.py
```

## ▶️ Como Executar

### Clone o repositório

```bash
git clone https://github.com/Denis-DBA/assistente-virtual-dba-mentor.git
```

### Entre na pasta

```bash
cd assistente-virtual-dba-mentor
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

### Execute a aplicação

```bash
streamlit run src/app.py
```

## 💬 Exemplos de Perguntas

```text
Qual a diferença entre INNER JOIN e LEFT JOIN?
```

```text
Como criar uma chave estrangeira?
```

```text
Como funciona o GROUP BY?
```

```text
Como usar HAVING?
```

```text
Explique PRIMARY KEY.
```

```text
Como criar uma VIEW?
```

## 🚀 Funcionalidades

- Explica conceitos de SQL e MySQL.
- Consulta uma base de conhecimento local.
- Apresenta exemplos de código SQL.
- Identifica comandos potencialmente perigosos.
- Solicita mais informações quando necessário.
- Organiza as respostas de forma didática.

## 🔮 Melhorias Futuras

- Integração com APIs de Inteligência Artificial.
- Busca semântica na base de conhecimento.
- Suporte a PostgreSQL, Oracle e SQL Server.
- Histórico persistente de conversas.
- Validação automática de consultas SQL.
- Interface mais moderna.
- Deploy em ambiente de nuvem.

## 👨‍💻 Autor

**Denis André Ramalho**

Projeto desenvolvido durante o Bootcamp **Bradesco - GenAI, Dados & Cyber** da **Digital Innovation One (DIO)**.

GitHub:

```text
https://github.com/Denis-DBA
```
