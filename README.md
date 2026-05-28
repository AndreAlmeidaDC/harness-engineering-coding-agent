# Harness Engineering Coding Agent

**Da intenção de produto ao impacto em produção com agentes de IA.**

Este repositório reúne uma skill operacional portátil para agentes de coding trabalharem com método, rastreabilidade, validação e responsabilidade. Ela foi pensada para qualquer agente capaz de ler arquivos, alterar código, executar comandos e registrar progresso: Claude Code, Codex, Cursor, Windsurf, Gemini CLI, OpenCode, agentes locais ou agentes internos de empresas.

A tese é simples: **modelo bom não basta**. Aplicações reais não nascem apenas de prompts bons. Elas nascem de um ambiente de trabalho bem desenhado: contexto certo, especificação clara, ferramentas seguras, sensores objetivos, logs, critérios de aceite, controle de escopo, revisão e aprendizado pós-lançamento.

> **Código não é software.** Software inclui requisitos, arquitetura, dados, fluxos de usuário, segurança, testes, deployment, observabilidade, manutenção e o processo que mantém tudo coerente ao longo do tempo.

## O que este pacote entrega

| Caminho | Função |
|---|---|
| `SKILL.md` | Skill principal, com frontmatter, gatilhos de uso, workflow, gates e regras não negociáveis. |
| `references/` | Módulos operacionais lidos sob demanda: descoberta de produto, PRD/spec, release/medição e squad mode. |
| `templates/` | Templates reutilizáveis para `AGENTS.md`, contrato, critérios de aceite, plano de testes, estado, avaliação e handoff. |
| `checklists/` | Checklist de execução para uso em revisão ou antes de encerrar uma tarefa. |
| `examples/` | Exemplo mínimo de aplicação da skill em uma tarefa real. |
| `docs/` | Guia conceitual consolidado para humanos entenderem e adaptarem o método. |

## Por que isso existe

A criação de software com IA mudou de fase. Na primeira fase, a pergunta era: “a IA consegue gerar código?”. Hoje a resposta já é óbvia: consegue.

A pergunta relevante agora é outra: **a IA consegue ajudar a construir software que pode ser mantido, testado, lançado, observado e evoluído com segurança?**

A resposta depende menos do modelo e mais do harness ao redor dele.

Sem harness, um agente tende a trabalhar como um dev novato largado numa base de código sem onboarding: ele pode ser rápido, mas não conhece contexto, histórico, arquitetura, riscos, critérios de aceite nem consequências. Com harness, o agente opera dentro de um canteiro: sabe o que construir, onde mexer, o que não tocar, como validar, quando pedir aprovação e como deixar rastros para a próxima sessão.

## Como usar rapidamente

Copie `SKILL.md` para o local de skills, rules, memories ou instruções do seu agente.

```text
.skills/harness-engineering-coding-agent/SKILL.md
.agent-skills/harness-engineering-coding-agent/SKILL.md
.claude/skills/harness-engineering-coding-agent/SKILL.md
.codex/skills/harness-engineering-coding-agent/SKILL.md
.cursor/rules/harness-engineering-coding-agent.md
.windsurf/rules/harness-engineering-coding-agent.md
```

Depois, copie as pastas `references/` e `templates/` junto com o `SKILL.md`, para que o agente consiga consultar os módulos e criar os artefatos quando necessário.

No `AGENTS.md` do projeto, adicione uma instrução curta:

```md
Quando a tarefa envolver descoberta de produto, PRD, alteração de código, feature, bugfix, refatoração, teste, release ou avaliação pós-lançamento, use a skill `harness-engineering-coding-agent`.
```

## Fluxo principal

```text
Product Intent
→ Product Engineering Discovery
→ PRD / Spec / Contract
→ Task Breakdown
→ Implementation Harness
→ Evaluation Gates
→ Release Harness
→ Measurement Loop
→ Learning / Handoff
```

## Modos de execução

A skill funciona em três modos. O modo `solo` é o padrão e serve para tarefas claras e de baixo ou médio risco. O modo `review-pair` separa implementação e avaliação, sendo adequado para autenticação, dados, segurança, lógica de negócio e mudanças sensíveis. O modo `squad` ativa papéis separados para produto, arquitetura, implementação, QA, release e medição quando a tarefa é longa, crítica ou ambígua.

| Modo | Quando usar | Custo de coordenação |
|---|---|---:|
| `solo` | Tarefa clara, local e de baixo risco. | Baixo |
| `review-pair` | Mudança com risco médio ou necessidade de validação independente. | Médio |
| `squad` | Produto, arquitetura, segurança, release e medição em jogo. | Alto |

Comece por `solo`. Suba para `review-pair` ou `squad` apenas quando houver ambiguidade, risco, tarefa longa, impacto em produção, dados sensíveis ou necessidade de medição real.

## Estrutura recomendada no projeto-alvo

A skill pode criar artefatos leves dentro do projeto em que o agente está trabalhando. Ela não exige todos os arquivos em toda tarefa; a matriz no `SKILL.md` define o mínimo por tipo de trabalho.

```text
AGENTS.md
.harness/STATE.md
.harness/CONTRACT.md
.harness/ACCEPTANCE_CRITERIA.md
.harness/TEST_PLAN.md
.harness/EVALUATION_REPORT.md
.harness/HANDOFF.md
.harness/OPEN_QUESTIONS.md
docs/product/PRODUCT_INTENT.md
docs/product/PRD.md
docs/product/METRICS_PLAN.md
docs/product/POST_LAUNCH_REVIEW.md
docs/architecture/ARCHITECTURE.md
docs/decisions/DECISION_LOG.md
docs/release/RELEASE_PLAN.md
```

## Quando usar

Use esta skill quando a tarefa envolver construir uma aplicação com agentes de IA, transformar ideia em especificação, implementar feature com frontend, backend, auth, banco ou integração, corrigir bug com impacto relevante, mexer em arquitetura, segurança, permissões, dados ou produção, refatorar código que precisa continuar funcionando, lançar funcionalidade para usuários reais ou medir adoção, impacto e aprendizado.

## Quando não usar o fluxo completo

Não use o fluxo completo para pergunta simples, snippet descartável, prova de conceito sem compromisso de manutenção, exploração técnica rápida ou tarefa de baixo risco com um único arquivo e sem efeito externo.

Mesmo nesses casos, preserve Git, escopo e critérios básicos de pronto.

## Validação local

Este repositório inclui um script simples de validação local. Para uma checagem mínima antes de publicar alterações, rode:

```bash
python scripts/validate_skill.py
```

A validação verifica a presença de frontmatter no `SKILL.md`, referências obrigatórias e templates essenciais.

## Autor

**André Almeida**

- Site: https://andrealmeidadc.com
- LinkedIn: https://linkedin.com/in/andrealmeidadc

## Licença

MIT. Consulte `LICENSE`.

## Histórico de alterações

| Data | Hora | Motivo |
|---|---|---|
| 2026-05-28 | 13:05 GMT-3 | Reorganização para repositório público portátil, separando skill principal, referências, templates, documentação humana e validação local. |
