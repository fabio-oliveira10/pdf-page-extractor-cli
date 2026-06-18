# PDF Page Extractor Automation Tool

Aplicação desenvolvida em Python para automatizar a extração seletiva de páginas de arquivos PDF, com navegação interativa por diretórios e geração de novos arquivos organizados.

O projeto tem como objetivo reduzir o trabalho manual de recorte e separação de documentos, facilitando rotinas de organização e conferência de arquivos em PDF.

---

## Visão Geral

A aplicação percorre uma estrutura de diretórios local, permite a seleção interativa de pastas e arquivos PDF, e realiza a extração de um intervalo específico de páginas definido pelo usuário.

Ao final, um novo arquivo PDF é gerado contendo apenas o conteúdo selecionado.

---

## Escopo Atual

O projeto foi desenvolvido para operar em estruturas locais de arquivos organizadas em subpastas.

A lógica de navegação foi construída para cenários com múltiplos PDFs distribuídos em diretórios.

A ferramenta atua exclusivamente na manipulação estrutural de PDFs (recorte de páginas).

---

## Funcionalidades

### Navegação de Arquivos

- Listagem automática de subpastas dentro do diretório raiz
- Seleção interativa de pasta e arquivo via terminal
- Identificação de arquivos PDF disponíveis

### Extração de Páginas

- Extração de intervalo específico de páginas
- Validação de limites do documento
- Geração de novo PDF com páginas selecionadas

### Organização de Saída

- Criação automática de pasta de saída no Desktop
- Nomeação padronizada dos arquivos gerados
- Separação entre arquivo original e arquivo processado

### Interface CLI

- Menu interativo em linha de comando
- Entrada baseada em seleção numérica
- Tratamento de erros de entrada do usuário

---

## Fluxo da Aplicação

```text
Diretório Base
     │
     ▼
Listagem de Pastas
     │
     ▼
Seleção de Pasta
     │
     ▼
Listagem de PDFs
     │
     ▼
Seleção de Arquivo
     │
     ▼
Definição de Página Inicial e Final
     │
     ▼
Extração de Páginas
     │
     ▼
Geração de Novo PDF
