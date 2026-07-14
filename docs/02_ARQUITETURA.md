# 02 - ARQUITETURA

Última atualização: 13/07/2026

Responsável: Gabriel Toledo

---

# Visão Geral

A plataforma Funcionários Digitais foi construída para ser multiempresa, escalável e modular.

Cada empresa possui seus próprios Funcionários Digitais, conhecimento, memória e configurações, sem interferir nas demais.

A arquitetura foi projetada para permitir que novos módulos sejam adicionados sem necessidade de reescrever funcionalidades existentes.

---

# Fluxo Geral

Cliente

↓

Canal de comunicação

(WhatsApp, Instagram, Site, etc.)

↓

API Funcionários Digitais

↓

Identificação da empresa

↓

Funcionário Digital

↓

Memória

↓

Conhecimento

↓

Ferramentas

↓

Modelo de IA

↓

Resposta

↓

Cliente

---

# Componentes

## API

Responsável por receber todas as mensagens vindas dos canais de comunicação.

Não contém regras de negócio.

Sua função é apenas validar dados, identificar o destino da solicitação e encaminhá-la para os serviços responsáveis.

---

## Client Registry

Responsável por identificar qual empresa deve atender aquela conversa.

Exemplos:

- número de WhatsApp
- domínio do site
- token
- chave da API

Retorna o company_id.

---

## Knowledge Service

Carrega todo o conhecimento da empresa.

Exemplos:

- empresa
- FAQ
- médicos
- especialidades
- documentos
- políticas
- produtos

O conhecimento nunca deve ficar escrito diretamente no código.

---

## Memory Service

Gerencia o histórico da conversa.

Cada usuário possui sua própria memória.

A implementação pode mudar ao longo do tempo (JSON, banco de dados, Redis, etc.) sem alterar o restante do sistema.

---

## LLM Service

Responsável por conversar com o modelo de Inteligência Artificial.

Ele monta o contexto utilizando:

- conhecimento
- memória
- instruções
- mensagem do usuário

Depois envia tudo para o modelo e retorna a resposta.

---

## Ferramentas (Tools)

São recursos que o Funcionário Digital pode utilizar durante o atendimento.

Exemplos:

- consultar agenda
- criar agendamento
- cancelar consulta
- enviar documentos
- consultar preços
- gerar boleto
- consultar estoque

As ferramentas são independentes do modelo de IA.

---

## Funcionário Digital

Representa um colaborador virtual especializado.

Cada funcionário possui:

- função
- personalidade
- conhecimento
- memória
- ferramentas autorizadas

Exemplos:

- Recepcionista
- Comercial
- Financeiro
- Pós-venda

---

# Estrutura da Plataforma

clientes/

Contém todas as empresas cadastradas.

Cada empresa possui seu próprio conhecimento.

---

conversas/

Armazena o histórico das conversas.

Cada usuário possui sua própria memória.

---

src/

Contém todo o código da plataforma.

Nenhum conhecimento do cliente deve ficar dentro desta pasta.

---

docs/

Contém toda a documentação oficial do projeto.

---

# Objetivos da Arquitetura

- Separação clara de responsabilidades.
- Facilidade para adicionar novas empresas.
- Facilidade para adicionar novos Funcionários Digitais.
- Independência entre módulos.
- Facilidade de manutenção.
- Escalabilidade.
- Código reutilizável.

---

# Princípio Fundamental

Toda informação da empresa pertence ao cliente.

Toda inteligência pertence à plataforma.

Essa separação é o principal pilar da arquitetura Funcionários Digitais.