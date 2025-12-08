<<<<<<< HEAD
# API de Gerenciamento de Pedidos

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.30-red?logo=python)](https://docs.sqlalchemy.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.29.0-purple?logo=python)](https://www.uvicorn.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.7.1-blue?logo=python)](https://docs.pydantic.dev/)

---

## Descrição

Este projeto é uma API REST para gerenciamento de pedidos, construída com FastAPI, SQLAlchemy e Pydantic. O código está organizado em camadas para facilitar manutenção, testes e escalabilidade.

---

## Estrutura de Pastas e Arquivos

```
IWS/
└── rest/
    ├── [`IWS/rest/app.py`](IWS/rest/app.py )                # Arquivo principal da aplicação FastAPI
    ├── config/
    │   └── database.py       # Configuração do banco de dados (SQLAlchemy)
    ├── models/
    │   └── base.py           # Modelos ORM (tabelas)
    ├── repositories/
    │   └── pedido_repository.py # Regras de acesso ao banco de dados
    ├── services/
    │   └── pedido_service.py # Lógica de negócio
    ├── controllers/
    │   └── pedido_controller.py # Controladores das rotas
    └── schemas/
        └── schema.py         # Schemas Pydantic para validação e resposta
```

---

## Camadas do Projeto

- **Model:** Define as tabelas e entidades do banco de dados.
- **Repository:** Responsável pela comunicação direta com o banco (CRUD).
- **Service:** Implementa as regras de negócio e validações.
- **Controller:** Recebe as requisições das rotas e chama os serviços.
- **Schema:** Define os formatos de entrada e saída de dados (Pydantic).
- **Config:** Configuração do banco de dados.

---

## Pacotes Utilizados

- [FastAPI](https://fastapi.tiangolo.com/) - Framework para APIs rápidas e assíncronas.
- [SQLAlchemy](https://docs.sqlalchemy.org/) - ORM para manipulação do banco de dados.
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI para rodar a aplicação FastAPI.
- [Pydantic](https://docs.pydantic.dev/) - Validação de dados e criação de schemas.

---

## Como Rodar o Projeto

1. **Instale os pacotes necessários:**
   ```bash
   pip install fastapi sqlalchemy uvicorn pydantic

   pip install -r requirements.txt
   ```

2. **Execute o servidor:**
   ```bash
   python app.py
   ```

3. **Acesse a documentação automática:**
   - [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
   - [http://localhost:8000/redoc](http://localhost:8000/redoc) (Redoc)

---

## Testando as Rotas

Utilize o Swagger UI ou ferramentas como Postman, Insomnia, ou curl para testar as rotas:

- `GET /pedidos` - Lista todos os pedidos
- `GET /pedidos/{pedido_id}` - Detalha um pedido
- `POST /pedidos` - Cria um novo pedido
- `PUT /pedidos/{pedido_id}` - Atualiza um pedido
- `DELETE /pedidos/{pedido_id}` - Remove um pedido

---

## Observações

- O projeto utiliza SQLite por padrão, mas pode ser adaptado para outros bancos.
- O código segue boas práticas de separação de responsabilidades.
- Para rodar no Windows, o loop de eventos é ajustado automaticamente.

---
## Prints dos métodos

1. Tela do Swagger
<img width="1917" height="967" alt="1 swagger" src="https://github.com/user-attachments/assets/1322ac18-0d1d-4709-8e7a-c2a84eea07f6" />

2. Parte de baixo da tela do Swagger
<img width="1919" height="969" alt="2 swagger" src="https://github.com/user-attachments/assets/3a96a09a-cc49-4884-a94d-faa067e13d00" />

3. Tela do Redoc
<img width="1919" height="968" alt="3 Redoc" src="https://github.com/user-attachments/assets/bf6c30d9-871a-4198-801a-ade32f4880d4" />

4.1 Criar Cliente
<img width="1915" height="898" alt="4 1criar_clientes" src="https://github.com/user-attachments/assets/102d0e28-b87c-4b04-95aa-0b583f47a3a3" />

4.2 Cria Cliente
<img width="1915" height="909" alt="4 2criar_clientes" src="https://github.com/user-attachments/assets/06a50c49-8432-4f46-a374-876ffe62edb6" />

5.1 Listar Cliente
<img width="1919" height="907" alt="5 1listar_clientes" src="https://github.com/user-attachments/assets/8455c465-6e32-42da-b933-99af04807dac" />

6.1 Ler Cliente
<img width="1917" height="910" alt="6 1ler_cliente" src="https://github.com/user-attachments/assets/1fc8d754-f277-4743-8ebb-2a7581388605" />

7.1 Atualizar Cliente
<img width="1919" height="913" alt="8 1atualizar_cliente" src="https://github.com/user-attachments/assets/d24862f0-501d-4da0-9a62-373a8cd62211" />

8.1 Deletar Cliente
<img width="1917" height="912" alt="9 1delete_cliente" src="https://github.com/user-attachments/assets/8cfea922-c4e4-4d2e-abd5-09f5773abd3b" />

9.1 Criar Pedido
<img width="1908" height="911" alt="10 criar_pedido" src="https://github.com/user-attachments/assets/eca5c17e-9b04-42f3-bb21-836c1689a9fc" />

10. Listar Pedido
<img width="1919" height="907" alt="11 listar_pedido" src="https://github.com/user-attachments/assets/f78a9206-d4d2-410e-8305-4f21a6912987" />

11. Ler Pedido
<img width="1919" height="901" alt="12 ler_pedido" src="https://github.com/user-attachments/assets/f2680c97-ff6f-4889-9275-3d54dbfcd0bb" />

12. Atualizar Pedido
<img width="1913" height="907" alt="13 atualizar_pedido" src="https://github.com/user-attachments/assets/bea0e22b-15a6-4af1-912c-40733961248d" />

13. Deletar Pedido
<img width="1912" height="896" alt="14 deletar_pedido" src="https://github.com/user-attachments/assets/0765d312-edb8-44f5-8eaa-c483c23ada64" />




















