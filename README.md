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

![image](https://github.com/augustopiatto/dnc-processoseletivo/assets/77405968/18ae8e99-b7d6-489c-92ac-03d00ec9b761)

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
- Execute `python manage.py runserver` e `sudo service postgresql start` OU execute `docker-compose build` e `docker-compose up`
- Rode `python manage.py migrate` OU `docker-compose exec web python manage.py migrate` para aplicação dos modelos no ambiente local
- Rode `python manage.py dev_db` OU `docker-compose exec web python manage.py dev_db` para popular seu banco local
- Caso queira rodar os testes localmente, execute `python manage.py runserver` e `sudo service postgresql start` para o acesso ao banco de teste
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

## Decisões técnicas

### Tecnologias

- Vue para o frontend pois é um framework amplamente utilizado e com ótima documentação. Torna os estados reativos e facilita a escrita de código, tornando menos complexo e mais ágil
- Vuetify é uma biblioteca completa (mesmo que a versão 3 ainda esteja sendo desenvolvida e faltem certos componentes), possui uma ótima documentação, o código do GitHub é aberto para se poder analisar cada componente e existem diversos tópicos sobre suas funcionalidades
- Axios para se fazer conexões HTTP com promessas. A conexão HTTP é ideal para esta aplicação pois permite requisições frequentes, visto que os dados podem alterar frequentemente. A forma como o Axios trata promessas ajuda a prevenir bugs e capturar erros que podem acontecer durante o processo
- SASS para estruturação de CSS pois permite organizar uma hierarquia, da mesma forma que os componentes à que ele se refere. Uma outra vantagem, ainda que não utilizada neste projeto, é a facilidade com a definição e uso de variáveis
- Django para o backend pois tem uma boa estrutuação e fluxo de requisição, com camadas de views e serviços, separando responsabilidade. É amplamente utilizado e documentado e fornece uma ORM relativamente fácil de se aprender
- Pydantic foi utilizado pois ambas linguagens utilizadas no projeto não são tipadas, logo se tornou necessário garantir que as informações provindas do usuário (frontend) estivessem no formato adequado para que o backend pudesse trabalhar. O Pydantic rejeita tipagens diferentes das que foram definidas e pode converter algumas (ex: float virar Decimal). Se localiza na pasta `back/backend/forms`
- Pytest é a biblioteca mais comum para testes utilizando Django, facilita principalmente em testes unitários e na criação de mocks. Outra escolha seria unittest, mas acaba por ser mais verboso e exigir mais o uso de classes
- PostgreSQL foi escolhido para que se possa armazenar e acessar dados de forma mais eficiente que o banco original do Django (sqlite), ou seja, foi utilizado pensando em escalabilidade

### Endpoints

- `api/students/`: Listagem de alunos / método - GET e POST
  - GET: parâmetros - None / retorno - JsonResponse<{id: int, name: string}[]>
  - POST: parâmetros - name: string / retorno - JsonResponse<{}>
- `api/top-three-students/`: Listagem dos 3 melhores alunos / método - GET / parâmetros - None / retorno - JsonResponse<{id: int, name: string}[]>
- `api/top-ten-students/`: Listagem dos 10 melhores alunos do curso X / método - GET / parâmetros - school: string / retorno - JsonResponse<{id: int, name: string}[]>
- `api/grades/`:  Criação de Atividade / método - POST / parâmetros - student_id: int, school: string, grade: number, type: string / retorno - JsonResponse<{}>

### Arquitetura em Cloud

Para uma arquitetura escalável em Cloud será necessária as seguintes configurações para o projeto:
- Estrutura: Monólito
- Load Balancer: Irá distribuir o tráfego (requests) para diversas instâncias do monólito, sem que uma instância específica fique sobrecarregada com as requisições de 5 mil alunos
- Instâncias do monólito: São cópias do servidor original que ficarão em máquinas virtuais, para que caso o tráfego seja grande, as requisições possam ser alocadas pelo Load Balancer a fim de não sobrecarregar uma única instância
-  Banco de dados escalável: Assim como o número de instâncias aumenta quando o tráfego é maior, devemos configurar para que o banco de dados cresça conforme maior a quantidade de informações forem armazenados nele
- Cache distribuído: Com as funções atuais da página não é necessário. O mais provável é que as informações sejam atualizadas frequentemente, e o cache atrapalharia nisso
- Autoescalonamento e Monitoramento: Definição de regras no monitoramento da Cloud para que quando o tráfego aumentar ou diminuir, as instâncias sejam criadas ou removidas
- CDN (Content Delivery Network): Para distribuir os conteúdos estáticos e dinâmicos em diferentes locais do país ou mundo, para reduzir latência
- Segurança e Controle de Acesso: Usar os serviços que o provedor da Cloud oferece, por exemplo autenticação e autorização robustas, monitoramento de segurança em tempo real e gerenciamento de chaves

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
