API de Gerenciamento de Pedidos
Python FastAPI SQLAlchemy Uvicorn Pydantic

Descrição
Este projeto é uma API REST para gerenciamento de pedidos, construída com FastAPI, SQLAlchemy e Pydantic. O código está organizado em camadas para facilitar manutenção, testes e escalabilidade.

Estrutura de Pastas e Arquivos
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
Camadas do Projeto
Model: Define as tabelas e entidades do banco de dados.
Repository: Responsável pela comunicação direta com o banco (CRUD).
Service: Implementa as regras de negócio e validações.
Controller: Recebe as requisições das rotas e chama os serviços.
Schema: Define os formatos de entrada e saída de dados (Pydantic).
Config: Configuração do banco de dados.
Pacotes Utilizados
FastAPI - Framework para APIs rápidas e assíncronas.
SQLAlchemy - ORM para manipulação do banco de dados.
Uvicorn - Servidor ASGI para rodar a aplicação FastAPI.
Pydantic - Validação de dados e criação de schemas.
Como Rodar o Projeto
Instale os pacotes necessários:

pip install fastapi sqlalchemy uvicorn pydantic

pip install -r requirements.txt
Execute o servidor:

python app.py
Acesse a documentação automática:

http://localhost:8000/docs (Swagger UI)
http://localhost:8000/redoc (Redoc)
Testando as Rotas
Utilize o Swagger UI ou ferramentas como Postman, Insomnia, ou curl para testar as rotas:

GET /pedidos - Lista todos os pedidos
GET /pedidos/{pedido_id} - Detalha um pedido
POST /pedidos - Cria um novo pedido
PUT /pedidos/{pedido_id} - Atualiza um pedido
DELETE /pedidos/{pedido_id} - Remove um pedido
Observações
O projeto utiliza SQLite por padrão, mas pode ser adaptado para outros bancos.
O código segue boas práticas de separação de responsabilidades.
Para rodar no Windows, o loop de eventos é ajustado automaticamente.

## Tela do Swagger UI

