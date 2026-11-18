# 📚 Desafio – Análise de Vulnerabilidades com o DIO Agent

## 📖 O que o desafio pedia
- Criar uma **skill** `vulnerability‑analysis` que analisasse vulnerabilidades, avaliasse risco (impacto, probabilidade, severidade) e sugerisse mitigações.
- Acrescentar um **knowledge file** com conceitos de segurança (CIA, OWASP, MITRE ATT&CK) e uma matriz de risco.
- Atualizar a configuração do agente (`AGENTS.md`) e a documentação (`README.md`).
- Documentar o fluxo de uso com **screenshots** (antes × depois) e incluir trechos dos arquivos Python vulnerável e seguro.

## ✅ O que foi entregue
- **Skill**: `skills/vulnerability-analysis/SKILL.md` (fluxo completo, modelo de relatório padronizado). 
- **Knowledge base**: `agent/knowledge/security-basics.md` (tríade CIA, OWASP, MITRE, matriz de risco, checklist). 
- **AGENTS.md**: linha adicionada à tabela de skills. 
- **README** da raiz: já contém a skill na tabela de skills. 
- **Screenshots organizadas** em `docs/screenshots/initial/` e `docs/screenshots/posterior/`.
- **Documentação das screenshots**: `docs/screenshots/README.md` com imagens embutidas, explicação dos estágios e trechos dos arquivos Python antes (`connect-db-insecure.py`) e depois (`connect-db-secure.py`).

## 📂 Como visualizar a documentação completa
Abra o arquivo abaixo, que reúne todas as capturas de tela e os trechos de código:

[📸 Screenshots e documentação detalhada](docs/screenshots/README.md)

## 📦 Próximos passos (opcional)
- Inserir referências a essas screenshots no `README.md` da raiz ou em um portfólio.
- Compartilhar o repositório público e divulgar o trabalho nas redes (LinkedIn, GitHub). 

---

> **Nota:** As imagens foram geradas usando o harness **OpenCode**. As etapas “inicial” mostram a coleta de contexto e a detecção da vulnerabilidade; as etapas “posterior” mostram a re‑análise após a aplicação das correções.
