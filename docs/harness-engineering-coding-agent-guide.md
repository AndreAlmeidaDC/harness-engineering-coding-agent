# Harness Engineering Coding Agent Guide

Autor: **André Almeida**

## Visão geral

O Harness Engineering Coding Agent é uma skill operacional para orientar agentes de coding em trabalhos reais de software. Ela parte da premissa de que o principal gargalo da IA aplicada ao desenvolvimento não é apenas a geração de código, mas a criação de um ambiente de execução com contexto, especificação, sensores, critérios de aceite, segurança, release e aprendizado.

A skill foi desenhada para ser portátil. Ela pode ser usada por qualquer agente que consiga ler arquivos, editar código, executar comandos e registrar estado. Isso inclui agentes em IDEs, CLIs, ambientes autônomos, agentes internos de empresas e combinações multiagente.

> **Código não é software.** Software é um sistema sociotécnico que envolve intenção de produto, arquitetura, dados, segurança, testes, release, observabilidade, operação e evolução contínua.

## O problema que a skill resolve

Agentes de coding tendem a ser muito bons em tarefas localizadas, mas podem falhar em tarefas reais quando recebem contexto insuficiente, objetivos vagos ou ausência de critérios objetivos de validação. O resultado costuma ser uma entrega que compila, parece funcionar em uma demonstração local, mas não está pronta para produção, manutenção ou evolução.

O harness resolve esse problema criando um conjunto de gates. Antes de codar, o agente entende a intenção. Antes de alterar estrutura, entende o contrato. Antes de declarar sucesso, roda sensores. Antes de lançar, planeja rollback e observabilidade. Antes de encerrar, deixa handoff.

## Arquitetura do pacote

| Componente | Descrição |
|---|---|
| `SKILL.md` | Núcleo operacional. Define quando usar, como classificar tarefa, quais gates seguir e qual é a definição de pronto. |
| `references/product-engineering-discovery.md` | Ajuda o agente a transformar uma ideia vaga em intenção de produto validável. |
| `references/prd-specification-builder.md` | Converte intenção em PRD, contrato, requisitos, critérios de aceite e plano de teste. |
| `references/release-measurement-loop.md` | Organiza rollout, rollback, observabilidade, métricas e revisão pós-lançamento. |
| `references/squad-mode.md` | Define quando separar papéis e como coordenar um squad multiagente. |
| `templates/` | Modelos reutilizáveis para gerar artefatos no projeto-alvo. |
| `checklists/` | Lista prática para revisar a execução antes de encerrar a tarefa. |
| `examples/` | Exemplo mínimo de aplicação do fluxo. |

## Fluxo mental

O fluxo principal é:

```text
Intenção de produto
→ Descoberta de produto
→ PRD / especificação / contrato
→ Quebra em tarefas
→ Implementação controlada
→ Sensores de validação
→ Release seguro
→ Medição pós-lançamento
→ Handoff e aprendizado
```

Esse fluxo não precisa ser executado inteiro em toda tarefa. A skill exige proporcionalidade. Uma correção simples deve continuar simples. Uma mudança que envolve dados, autenticação, produção ou cliente real não deve ser tratada como um snippet.

## Classificação de tarefas

| Tipo | Descrição | Processo recomendado |
|---|---|---|
| `quick-fix` | Correção simples, local e de baixo risco. | Git safety, alteração mínima e verificação objetiva. |
| `feature` | Novo comportamento ou interface. | Contrato, critérios de aceite, plano de teste e handoff. |
| `product-feature` | Feature com ambiguidade de produto. | Descoberta, PRD, contrato, critérios, teste e métricas. |
| `architecture` | Mudança estrutural ou decisão técnica relevante. | Arquitetura, decisão registrada, avaliação e handoff. |
| `security-data` | Auth, permissões, segredos, dados ou pagamentos. | Revisão mais rigorosa, critérios, testes e aprovação quando necessário. |
| `release` | Deploy, rollout, flags, rollback ou observabilidade. | Plano de release, sensores, rollback e medição. |
| `investigation` | Diagnóstico de bug, incidente ou comportamento incerto. | Estado, hipóteses, evidências e relatório de avaliação. |

## Modos de execução

O modo `solo` usa um único agente para executar o loop inteiro. É adequado para tarefas claras, pequenas e de baixo risco. O modo `review-pair` separa implementação e validação, sendo útil quando existe risco técnico ou de negócio. O modo `squad` separa papéis de produto, especificação, arquitetura, implementação, avaliação, release e registro, sendo indicado para tarefas longas, críticas ou ambíguas.

A decisão de modo deve considerar risco, escopo, impacto em produção, sensibilidade dos dados, ambiguidade e custo de coordenação.

## Sensores

A skill diferencia sensores computacionais e sensores inferenciais. Sensores computacionais são testes, lint, typecheck, build, validação de schema, execução local, migração em dry-run, checks de acessibilidade e scans de segurança. Sensores inferenciais são revisões por IA, críticas de arquitetura, raciocínio de segurança e análise de cobertura de requisitos.

Sensores inferenciais são úteis, mas não substituem sensores determinísticos. Quando não houver teste automatizado disponível, o agente deve criar a menor verificação objetiva possível ou registrar claramente a lacuna.

## Padrão de handoff

A skill exige handoff em todo trabalho significativo. O handoff deve permitir que outra pessoa ou outro agente continue sem reconstruir a sessão mental anterior. Um bom handoff informa estado atual, o que mudou, comandos executados, arquivos alterados, riscos, pendências e próxima ação recomendada.

## Como adaptar em ferramentas diferentes

Em agentes baseados em diretório de skills, copie o diretório inteiro da skill. Em agentes que usam regras, copie o conteúdo de `SKILL.md` como regra principal e mantenha `references/` e `templates/` acessíveis. Em agentes internos, trate `SKILL.md` como política de execução e os demais arquivos como módulos lidos sob demanda.

## Histórico de alterações

| Data | Hora | Motivo |
|---|---|---|
| 2026-05-28 | 13:18 GMT-3 | Atualização do guia para refletir a estrutura portátil, removendo dependência de subskills instaláveis e explicando o uso por qualquer agente de coding. |
