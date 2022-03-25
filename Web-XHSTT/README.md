# Web-XHSTT

Convertido o XML das instâncias XHSTT para o formato JSON e com ela criado uma API facilitando a manipulação dos dados.

## Pré-Requisitos

Instalar globalmente o pacote json-server.

    npm install -g json-server

Criar um arquivo db.json com os dados no formato JSON.

## Como usar

Executando o comando abaixo, o acesso será através de chamadas a porta localhost:3000/instances

    json-server --watch db.json

