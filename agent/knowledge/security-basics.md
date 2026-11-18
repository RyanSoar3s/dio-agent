# security-basics.md

## 📚 Conceitos Fundamentais de Segurança da Informação

### 1. Tríade CIA
- **Confidencialidade (Confidentiality)** – Garantir que a informação seja acessada apenas por quem tem permissão.
- **Integridade (Integrity)** – Assegurar que os dados não sejam alterados de forma não autorizada.
- **Disponibilidade (Availability)** – Manter os recursos acessíveis quando necessários.

### 2. Tipos de Vulnerabilidades (OWASP Top 10 + extras)
| Categoria | Descrição | Exemplo típico |
|-----------|-----------|----------------|
| **Injeção** | Entrada do usuário é inserida em comandos/queries sem sanitização. | SQL Injection, Command Injection |
| **Autenticação Quebrada** | Falhas na gestão de senhas, tokens ou sessões. | Senhas em texto‑plano, sessão não expirada |
| **Exposição de Dados Sensíveis** | Dados confidenciais são retornados ou armazenados sem proteção. | Dados de cartão sem criptografia |
| **Configurações Inseguras** | Serviços ou componentes deixados com valores padrão ou permissões excessivas. | Banco SQLite aberto ao público |
| **XSS / CSRF** | Falhas que permitem execução de código no cliente ou ações não autorizadas. |
| **Falhas de Controle de Acesso** | Usuário obtém acesso a recursos que não deveria. |
| **Uso de Componentes Vulneráveis** | Dependências com CVEs conhecidos. |
| **Registro e Monitoramento Insuficientes** | Falta de logs ou alertas de incidentes. |

### 3. MITRE ATT&CK – Visão Geral e Técnicas Relevantes
- **Framework** que categoriza técnicas de ataque usadas por adversários. Cada técnica possui um **ID (Txxxx)** e pode ser mapeada a vulnerabilidades específicas.
- Abaixo, as técnicas mais frequentes nas vulnerabilidades que a skill `vulnerability‑analysis` costuma analisar:

| Vulnerabilidade | Técnica ATT&CK (ID) | Descrição resumida |
|-----------------|---------------------|--------------------|
| **SQL Injection** | `T1190 – Exploit Public‑Facing Application` | Explora falhas de injeção em aplicações web para executar consultas arbitrárias no banco. |
| **Command Injection** | `T1059 – Command and Scripting Interpreter` | Executa comandos do sistema operacional a partir de entrada não sanitizada. |
| **Broken Authentication** | `T1110 – Brute Force` (sub‑técnica `T1110.001 – Password Guessing`) | Tentativas de adivinhar credenciais ou uso de credenciais comprometidas. |
| **Credential Dumping** | `T1552 – Unsecured Credentials` (sub‑técnica `T1552.001 – Passwords`) | Exfiltra senhas armazenadas em texto‑plano ou hashes fracos. |
| **XSS** | `T1059.007 – JavaScript` | Injeta scripts maliciosos em páginas web que são executados no navegador da vítima. |
| **Insecure Deserialization** | `T1570 – Lateral Tool Transfer` | Carrega objetos não confiáveis que podem executar código arbitrário. |
| **Security Misconfiguration** | `T1190` (também se aplica a configurações expostas) | Configurações padrão, permissões excessivas ou serviços desnecessários expostos. |

> **Como usar**: a skill deve consultar esta tabela para mapear a vulnerabilidade declarada pelo usuário ao ID ATT&CK correto e inserir o link `https://attack.mitre.org/techniques/<ID>/` no relatório.

### 4. Avaliação de Risco (Impacto × Probabilidade × Severidade)
|      Dimensão     | Escala 1‑5 | O que significa                                                                                            |
|-------------------|------------|------------------------------------------------------------------------------------------------------------|
|    **Impacto**    |     1      | Impacto baixo (ex.: informação pública)  <br>5 = Impacto crítico (ex.: vazamento de dados pessoais)        |
| **Probabilidade** |     1      | Muito improvável (necessita de acesso físico) <br>5 = Altamente provável (explorável remotamente sem auth) |
|  **Severidade**   |     1      | Leve (não afeta operação) <br>5 = Grave (paralisação ou comprometimento total)                             |

**Risk Score** = Impacto × Probabilidade × Severidade (0‑125). Classificação sugerida:
- 0‑20 → Baixa
- 21‑50 → Média
- 51‑125 → Alta

### 5. Boas‑Práticas Gerais (Checklist rápido)
1. **Validação e sanitização** de toda entrada externa.
2. **Consultas parametrizadas** ou ORM seguro.
3. **Hash de senhas** com algoritmos modernos (bcrypt, argon2).
4. **Privilégios mínimos** para bancos e serviços.
5. **Log de auditoria** com níveis adequados e proteção contra tampering.
6. **Atualizações regulares** de dependências (use o gerenciador de pacotes da linguagem, ex.: `pip list --outdated` para Python, `npm outdated` para JavaScript, etc.).
7. **Testes de segurança automáticos** (SAST, DAST) integrados ao CI.
8. **Documentação de risco** – mantenha a matriz acima atualizada por vulnerabilidade.

### 6. Referências
- OWASP Top 10 – https://owasp.org/www-project-top-ten/
- MITRE ATT&CK – https://attack.mitre.org/
- NIST SP 800‑30 – Guia de Avaliação de Risco.

---

**Como usar esta knowledge base**
- A skill `vulnerability‑analysis` deve consultar este arquivo para explicar termos (ex.: “Confidencialidade”) e para mapear vulnerabilidades a técnicas ATT&CK.
- Atualize‑o sempre que novos tipos de vulnerabilidade ou técnicas surgirem.
