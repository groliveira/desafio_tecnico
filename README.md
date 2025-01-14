# API Star Wars: Planetas e Filmes

API RESTful desenvolvida em Python com Flask e MongoDB para gerenciar planetas e filmes da franquia Star Wars.

## Índice
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Rotas da API](#rotas-da-api)
- [Testes](#testes)
- [Autor](#autor)

---

## Requisitos

- Python 3.8 ou superior
- MongoDB em execução local ou em um servidor
- Bibliotecas Python: `flask`, `flask-pymongo`, `pymongo`, `pytest`

---

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/groliveira/desafio_tecnico.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install flask flask-pymongo pymongo pytest
   ```

---

## Configuração

1. Certifique-se de que o MongoDB está em execução.
2. Crie um banco de dados chamado `starwars`:
   ```bash
   mongo
   use starwars
   ```

---

## Execução

1. Inicie a aplicação:
   ```bash
   python app.py
   ```

2. Acesse a API localmente:
   ```
   http://127.0.0.1:5000
   ```

---

## Rotas da API

### **Planetas**
- **POST /planetas**: Adiciona um novo planeta.
  - Exemplo de corpo da requisição:
    ```json
    {
      "nome": "Tatooine",
      "clima": "Arido",
      "diametro": "10465",
      "populacao": "200000"
    }
    ```
- **GET /planetas**: Lista todos os planetas.
- **GET /planetas/<planet_id>**: Retorna detalhes de um planeta específico.
- **PUT /planetas/<planet_id>**: Atualiza um planeta existente.
- **DELETE /planetas/<planet_id>**: Exclui um planeta.

### **Filmes**
- **POST /filmes**: Adiciona um novo filme.
  - Exemplo de corpo da requisição:
    ```json
    {
      "titulo": "A New Hope",
      "data_lancamento": "1977-05-25",
      "diretor": "George Lucas",
      "planetas": ["<planet_id>"]
    }
    ```
- **GET /filmes**: Lista todos os filmes.
- **GET /filmes/<film_id>**: Retorna detalhes de um filme específico.
- **PUT /filmes/<film_id>**: Atualiza um filme existente.
- **DELETE /filmes/<film_id>**: Exclui um filme.

---

## Testes

1. Execute os testes automatizados:
   ```bash
   pytest -v
   ```

2. Certifique-se de que o MongoDB está vazio antes de rodar os testes para evitar inconsistências.

---

## Autor

Criado por **asp.gabriel@gmail.com** como parte do desafio técnico. 

---
