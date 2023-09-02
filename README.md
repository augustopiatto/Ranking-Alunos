# DNC

## Visão Geral do Projeto

Este é um projeto que usa:

Front - Vue, Javascript, Vite e Vuetify

Back - Django, Python

Banco - PostgreSQL

É uma stack de desenvolvimento web moderna que é rápida e eficiente para construir aplicativos web escaláveis.

## Preview

O projeto permite adicionar alunos à base do projeto, associar notas em suas tarefas, desafios e projetos e mostra ao usuário quem são os top 3 alunos de todos as Escolas e o top 10 alunos de cada Escola.

### Telas

#### Home

![image](https://github.com/augustopiatto/dnc-processoseletivo/assets/77405968/dd5dd507-2e80-4b40-9286-7fd2b6dca64f)

### Popups

![image](https://github.com/augustopiatto/dnc-processoseletivo/assets/77405968/13f4da8b-eaf7-4e35-8c37-c7129761c931)

![image](https://github.com/augustopiatto/dnc-processoseletivo/assets/77405968/d10dff24-2b37-46a9-b07b-389203989f6a)

## Modelo Entidade Relacionamento (MER)

![image](https://github.com/augustopiatto/dnc-processoseletivo/assets/77405968/a86d244a-0cfe-446f-a31b-78be7619b336)

## System Design

## Começando

Para iniciar o projeto, siga os passos abaixo:

- Clone o repositório em sua máquina local

Front:

- Vá até a pasta `front`
- Execute `npm install` para instalar as dependências do projeto (utilizado node v20.1.0 e npm v9.6.6)
- Execute `npm run dev` para iniciar o servidor de desenvolvimento

Back:

- Vá até a pasta `back`
- Crie uma virtualenv com python (utilizado 3.10.11)
- Rode `pip install -r requirements.txt` para instalar as dependências
- Execute `python manage.py runserver` OU execute `docker-compose build` e `docker-compose up`
- Rode `python manage.py migrate` OU `docker-compose exec web python manage.py migrate` para aplicação dos modelos no ambiente local
- Rode `python manage.py dev_db` OU `docker-compose exec web python manage.py dev_db` para popular seu banco local
- Caso queira rodar os testes localmente, execute `sudo service postgresql start` para o acesso ao banco de teste
- Abra seu navegador e acesse `http://localhost:5173/` para ver a aplicação funcionando

## Estrutura de pasta

```
├── back                     # Arquivos do backend
│   ├── backend              # Projeto do backend
│   │   ├── forms            # Formulários de Pydantic
│   │   ├── management       # Arquivos de comandos
│   │   ├── migrations       # Migrações do banco
│   │   ├── serializers      # Serializers das views
│   │   ├── services         # Camada de lógica de serviços
│   │   ├── tests            # Testes de view e service
│   │   ├── views            # Camada de validação de dados e serialização
│   │   ├── models.py        # Modelos do banco
│   │   ├── settings.py      # Configurações do projeto
│   │   ├── urls.py          # Camada de conversa entre backend e frontend
│   ├── docker-compose.yml   # Arquivo de controle do docker
│   ├── Dockerfile           # Arquivo de comandos do docker
│   ├── manage.py            # Arquivo de execução de comandos do Django
│   ├── requirements.txt     # Requerimentos para funcionamento do projeto

├── front                    # Arquivos do frontend
├── public                   # Assets públicos
├── src                      # Código fonte
│   ├── api                  # API
│   ├── apimock              # API (nesse caso mock da API)
│   ├── assets               # Assets estáticos
│   │   ├── style.scss       # Estilos gerais
│   │   ├── images           # Pasta de imagens
│   ├── components           # Componentes reutilizáveis
│   ├── App.vue              # Componente raiz
│   └── main.ts              # Entry point
├── index.html               # Arquivo de acesso do JS
├── package.json             # Dependências e scripts
├── vite.config.ts           # Configuração do Vite
└── README.md                # Documentação do projeto
```

## Tecnologias e Funcionalidades

### Tecnologias

O projeto inclui as seguintes tecnologias:

Front:

- Vue para reatividade
- Javascript para escalabilidade
- Vite para desenvolvimento e construção rápidos e eficientes
- Vuetify como biblioteca para UI
- Axios para chamadas HTTP
- SASS para estruturação do CSS

Back:

- Django para desenvolvimento rápido e estruturação de fluxo de processo
- Python como linguagem de alto-nível e de fácil leitura
- PostgreSQL para armazenamento de informações de forma segura e escalável
- Pydantic para validação de dados entre frontend e backend
- Docker para padronização de ambiente e agilidade de definição de ambiente
- Pytest para testes e prevenção de bugs

### Funcionalidades

O projeto possui as seguintes funcionalidades:

- Componentes Funcionais
- Eventos

## Scripts

O projeto inclui os seguintes scripts:

Front:

- `npm run dev`: Inicia o servidor de desenvolvimento
- `npm run build`: Builda o aplicativo pronto para produção
- `npm run lint`: Linta e corrige os arquivos

Back:

- `python manage.py dev_db`: Popula o banco de dados local

## Melhorias futuras

Front:

- Validação de cada campo do formulário
- Exibição dos erros do backend (por agora está no console.log)
- Adição do peso da nota para cálculo da média
- CSS de forma geral, para mostrar carregamento de componentes e atenuação dos botões
- Testes

Back:

- Implementação de kubernetes (essencial, era must-have do projeto)
- Correção do docker para pytest rodar sem depender de subir o banco por fora
- Definições dos cookies em métodos POST e remover os `csrf_exempt`
