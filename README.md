# 🤖 Agente Recrutador Virtual

### Um agente de IA para automatizar e otimizar o processo de recrutamento e seleção, desde a criação da vaga até a entrevista com candidatos.

[](https://github.com/Andrasno/agente_recruiter)
[](https://www.python.org/)
[](https://ai.google.dev/)

## 🎯 Motivação

O processo de recrutamento e seleção é, muitas vezes, repetitivo, demorado e sujeito a vieses inconscientes. Encontrar o candidato ideal para uma vaga exige a análise de dezenas de currículos, triagens e entrevistas iniciais.

O **Agente Recrutador** nasceu para resolver esse problema. Utilizando o poder da Inteligência Artificial Generativa do Google (Gemini), este projeto simula um recrutador virtual capaz de criar descrições de vagas, gerar perfis de candidatos sintéticos e até mesmo conduzir uma entrevista simulada, fornecendo uma análise final sobre a adequação do candidato.

## ✨ Funcionalidades Principais

O agente opera em um fluxo que simula um processo seletivo real:

1.  **Geração de Vaga:** Cria uma descrição de vaga detalhada e atraente com base em um cargo e requisitos simples.
2.  **Criação de Candidato:** Gera um perfil de candidato sintético (currículo) com base na vaga criada, permitindo testar o sistema de forma controlada.
3.  **Análise de Perfil:** Avalia o perfil de um candidato em relação à vaga, extraindo suas competências e experiências mais relevantes.
4.  **Entrevista Virtual:** Conduz uma entrevista simulada com o candidato, fazendo perguntas pertinentes à vaga e à sua experiência.
5.  **Feedback Final:** Após a entrevista, o agente gera um parecer completo, avaliando se o candidato é recomendado para a posição e justificando sua decisão.

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

  * **Python:** Linguagem principal do projeto.
  * **Google Gemini (API):** O cérebro do agente, responsável por toda a geração e análise de texto.
  * **Pandas:** Utilizado para manipulação e armazenamento de dados, como os perfis dos candidatos.
  * **Dotenv:** Para gerenciamento seguro das chaves de API.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o Agente Recrutador em sua máquina local.

### 1\. Pré-requisitos

  * Python 3.10 ou superior
  * Uma chave de API do [Google AI Studio (Gemini)](https://aistudio.google.com/app/apikey).

### 2\. Clone o Repositório

```bash
git clone https://github.com/Andrasno/agente_recruiter.git
cd agente_recruiter
```

### 3\. Instale as Dependências

Crie um ambiente virtual e instale as bibliotecas necessárias.

```bash
# Crie um ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 4\. Configure sua API Key

Renomeie o arquivo `.env.example` para `.env` e insira sua chave da API do Google Gemini.

**Arquivo `.env`:**

```
GOOGLE_API_KEY="SUA_API_KEY_AQUI"
```

### 5\. Execute o Recrutador

Para iniciar o processo completo (gerar vaga, criar candidato e entrevistá-lo), execute o script principal:

```bash
python recrutador_virtual.py
```

O script irá guiar você pelo processo, mostrando cada etapa no console, desde a descrição da vaga gerada até o feedback final da entrevista.

## 📈 Exemplo de Uso

Ao executar o `recrutador_virtual.py`, você verá um output similar a este no seu terminal:

```
--- 1. GERANDO DESCRIÇÃO DA VAGA ---
Vaga para: Engenheiro de Dados Pleno
...
Descrição da Vaga gerada com sucesso!

--- 2. GERANDO PERFIL DE CANDIDATO ---
Candidato sintético para a vaga de Engenheiro de Dados Pleno gerado!
Nome: Juliana Oliveira
...

--- 3. INICIANDO ENTREVISTA VIRTUAL ---
[Agente]: Olá, Juliana! Obrigado por participar. Para começar, fale um pouco sobre sua experiência com pipelines de dados (ETL).
[Candidato]: Olá! Tenho 4 anos de experiência construindo e otimizando pipelines ETL com ferramentas como Apache Airflow, Spark e...
...
(A entrevista continua com mais perguntas e respostas)
...

--- 4. GERANDO FEEDBACK FINAL ---
Analisando a entrevista...

**PARECER FINAL SOBRE O CANDIDATO:**
**Candidato:** Juliana Oliveira
**Recomendação:** Contratar

**Justificativa:** A candidata demonstrou sólida experiência técnica em todas as áreas-chave da vaga... Sua comunicação foi clara e objetiva...
```

## 🔮 Próximos Passos (To-Do)

  - [ ] Integração com APIs de sites de vagas (LinkedIn, Gupy) para buscar candidatos reais.
  - [ ] Implementar um frontend simples com Streamlit ou Flask para uma interação mais amigável.
  - [ ] Adicionar capacidade de analisar currículos em formato PDF.
  - [ ] Salvar o histórico de entrevistas em um banco de dados.

-----

Feito com ❤️ por **Andrasno**.

[](https://www.google.com/search?q=%5Bhttps://github.com/Andrasno%5D\(https://github.com/Andrasno\))
