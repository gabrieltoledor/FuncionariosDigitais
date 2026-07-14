# RFC-001 — Employee Registry

## Objetivo

Permitir localizar e carregar funcionários de qualquer empresa.

---

## Requisitos

- Localizar funcionário por empresa
- Suportar múltiplos funcionários
- Retornar erro caso o funcionário não exista
- Não depender de código hardcoded

---

## Estrutura

clientes/

    clinica_demo/

        employees/

            recepcionista.json

            comercial.json

            financeiro.json

---

## Interface

EmployeeRegistry.get(company, employee)

EmployeeRegistry.exists(company, employee)

EmployeeRegistry.list(company)

---

## Status

Draft