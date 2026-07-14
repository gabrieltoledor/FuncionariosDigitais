# RFC-006 — Conversation Engine

## Status

Draft

---

# Objetivo

O Conversation Engine é responsável por orquestrar uma conversa completa entre um usuário e um Funcionário Digital.

Ele é o coração do sistema.

O Funcionário Digital representa quem está conversando.

O Conversation Engine representa como a conversa acontece.

---

# Responsabilidades

O Conversation Engine deve:

- Receber a mensagem do usuário.
- Recuperar a memória da conversa.
- Preparar o contexto.
- Conversar com o LLM.
- Executar ferramentas quando solicitado.
- Enviar o resultado das ferramentas novamente ao LLM.
- Persistir a memória.
- Retornar a resposta final.

---

# Não é responsabilidade

O Conversation Engine nunca deve:

- Conhecer FastAPI.
- Conhecer WhatsApp.
- Conhecer Instagram.
- Conhecer banco de dados.
- Ler arquivos JSON diretamente.
- Criar Funcionários Digitais.
- Saber como uma Tool funciona internamente.

---

# Componentes utilizados

- MemoryService
- ToolManager
- LLMService

---

# Componentes desconhecidos

O Conversation Engine não conhece:

- OpenAI
- Anthropic
- Gemini
- API
- Webhook
- Canal de comunicação

Ele apenas recebe uma mensagem e devolve uma resposta.

---

# Fluxo

Mensagem

↓

Memória

↓

LLM

↓

Tool Call (opcional)

↓

ToolManager

↓

LLM

↓

Persistência da memória

↓

Resposta

---

# Objetivo de longo prazo

Toda conversa da plataforma deverá passar pelo Conversation Engine.

Independentemente do canal utilizado.

WhatsApp

Instagram

Site

Telegram

Voz

Aplicativo

Todos utilizam exatamente o mesmo fluxo.