computer-vision-streamlit/
├── app.py                      # Ponto de entrada da aplicação Streamlit (Dashboard e Câmera Principal)
├── pages/
│   └── 1_Historico.py          # Página de histórico de análises, filtros e exportações
├── config/                     # Configurações globais, variáveis de ambiente e setup de logs
│   ├── settings.py
│   └── logging_config.py
├── database/                   # Gerenciamento de conexões, sessão do SQLAlchemy e migrations
│   ├── connection.py
│   ├── alembic.ini
│   └── migrations/
│       ├── env.py
│       └── script.py.mako
├── models/                     # Entidades do banco de dados (SQLAlchemy ORM Models)
│   ├── __init__.py
│   └── analysis.py
├── repositories/               # Camada de Acesso a Dados (DAO / Repository Pattern)
│   ├── __init__.py
│   └── analysis_repository.py
├── services/                   # Regras de Negócio e Pipeline de Visão Computacional
│   ├── __init__.py
│   ├── cv_analyzer.py
│   └── storage_service.py
├── controllers/                # Orquestração entre UI e Serviços
│   ├── __init__.py
│   └── main_controller.py
├── utils/                      # Funções utilitárias e geradores de exportação
│   ├── __init__.py
│   └── exporters.py
├── assets/                     # Recursos estáticos (Logos, CSS customizado, etc.)
│   └── .gitkeep
├── images/                     # Diretório de armazenamento local das fotografias capturadas
│   └── .gitkeep
├── logs/                       # Diretório de logs do sistema
│   └── .gitkeep
├── requirements.txt            # Dependências Python do projeto
├── README.md                   # Documentação completa de uso e deploy
├── .env.example                # Modelo das variáveis de ambiente
├── .gitignore                  # Arquivos ignorados pelo Git
├── render.yaml                 # Configuração do Build e Deploy no Render
└── runtime.txt                 # Especificação da versão do Python

Função de Cada Pasta
config/

Centraliza as configurações globais da aplicação (como leitura do .env, variáveis de ambiente) e a configuração do sistema de logs.

database/

Gerencia a conexão com o PostgreSQL (Neon.tech), a criação de sessões do SQLAlchemy e os arquivos de controle de migrations do Alembic.

models/

Define a estrutura das tabelas e esquemas do banco de dados utilizando classes ORM do SQLAlchemy.

repositories/

Aplica o padrão Repository (DAO), isolando todas as consultas, inserções e exclusões no banco de dados da lógica de negócio.

services/

Contém as regras de negócio da aplicação, incluindo o pipeline de Visão Computacional (OpenCV/Pillow) e o gerenciamento de arquivos salvos em disco.

controllers/

Faz a ponte (orquestração) entre a interface do Streamlit, os serviços de análise e a camada de persistência.

utils/

Guarda funções utilitárias e de suporte, como geradores de arquivos para exportação (CSV e JSON).

pages/

Armazena as páginas adicionais da interface do Streamlit (como a página de Histórico e Dashboards).

assets/

Destinada a arquivos estáticos complementares (imagens estáticas, logos ou estilos CSS customizados).

images/

Diretório onde as fotografias capturadas pela webcam são salvas localmente.

logs/

Diretório onde os arquivos de log de execução da aplicação são armazenados.