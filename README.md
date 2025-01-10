# 🪂 Diário online Full-Stack com Python e Django | Projeto 2

<p align="center">
  <img src="https://img.shields.io/badge/made%20by-MIGUEL%20PRETO-04D361?style=flat-square">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/yMiguelzin/psw-returnal-project-2?color=04D361&style=flat-square">
  <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/yMiguelzin/psw-returnal-project-2?color=04D361&style=flat-square">
  <a href="https://opensource.org/licenses/MIT">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-04D361?style=flat-square">
  </a>
</p>

## Tópicos

[Sobre o Projeto](#sobre-o-projeto)

[Tecnologias](#tecnologias)

[Instalação e Uso](#instalação-e-uso)

[Licença](#licença)

<br>

## Sobre o Projeto

Este projeto foi desenvolvido para gerenciar um diário online utilizando Python e Django. O objetivo é permitir que os usuários registrem suas atividades diárias de forma organizada, podendo criar, editar, listar e excluir entradas no diário, além de visualizar um histórico de registros. O projeto utiliza Django como framework principal para o desenvolvimento da aplicação web e foi pensado para fornecer uma interface simples e intuitiva para os usuários.

<br>

<p align="center">
  <img src="images/diario.jpg" alt="Diário Online">
</p>

## Tecnologias

As seguintes tecnologias foram utilizadas no desenvolvimento do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Pillow](https://python-pillow.org/) (para manipulação de imagens)
- [SQLite](https://www.sqlite.org/index.html) (banco de dados padrão para desenvolvimento com Django)

<br>

## Instalação e Uso

### Pré-requisitos

Antes de começar, você precisa ter o Python 3.x instalado no seu sistema. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

### Passos para Configuração e Execução

1. **Clone o repositório**:

   Abra seu terminal e clone o repositório do projeto:

   ```bash
   git clone https://github.com/yMiguelzin/diario-online-fullstack.git

   ```
   
2. **Instale as dependências**:

  Navegue até a pasta do projeto e instale as dependências necessárias:

  ```bash
  cd diario-online-fullstack
  pip install django pillow

  ```

3. **Configuração do Banco de Dados**:

  Agora, configure o banco de dados. Execute os comandos abaixo para criar as migrações necessárias e aplicá-las ao banco de dados:
  
  ```bash
  python manage.py makemigrations
  python manage.py migrate

  ```
4. **Execute o Servidor Django**:

  Inicie o servidor de desenvolvimento para rodar a aplicação localmente:
  
  ```bash
  python manage.py runserver
  O servidor será executado em http://localhost:8000/diario/
  Abra esse endereço no seu navegador para começar a usar a aplicação.
  
  ```

  <br>
  
## Licença
<a href="https://opensource.org/licenses/MIT">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-04D361?style=flat-square">
</a>

<br>

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](/LICENSE) para mais detalhes.

---

Feito com 💚 por [Miguel Preto](https://github.com/yMiguelzin)

