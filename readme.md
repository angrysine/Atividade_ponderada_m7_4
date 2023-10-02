# Descrição do projeto

O projeto é um sistema de login simples que da acesso a um gráfico da quantidade de fails no sistema de bleed da aeronave mensalmente.

## Tecnologias utilizadas

Foi utilizado fastapi para a criação da api, e para o front-end foi utilizado next.js. Para o banco de dados foi utilizado o postgres.

## Como rodar o projeto

Seguem aqui as instruções para rodar o projeto na cloud :

### Backend

Para rodar o backend, é necessário ter o uma instância no IC2 de linux. Após isso, basta rodar o comando abaixo na pasta raiz do projeto:

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
git clone https://github.com/angrysine/Atividade_ponderada_m7_4.git
cd Atividade_ponderada_m7_4
cd backend_rds
pip3 install -r requirements.txt
python3 migration.py
python3 app.py
```

Também é necessario adicionar uma regra de entrada a sua instância  do tipo tcp personalizada na porta 8000 permitindo seu ip usar a aplicação.

### Frontend

Para rodar o frontend, é necessário ter o uma instância no IC2 de linux. Após isso, basta rodar o comando abaixo na pasta raiz do projeto:

```bash
sudo apt update
sudo apt upgrade
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
. ~/.nvm/nvm.sh
nvm install node
git clone https://github.com/angrysine/Atividade_ponderada_m7_4.git
cd Atividade_ponderada_m7_4
cd frontend
npm install
npm run dev
```

Também é necessario adicionar uma regra de entrada a sua instância do tipo udp personalizada na porta 3000 permitindo seu ip usar a aplicação.

### Banco de dados

O comando python3 migration.py cria as tabelas necessárias para o funcionamento do sistema e deve ser realizado durante o setup do backend.

### vídeo de demonstração
[link](https://github.com/angrysine/Atividade_ponderada_m7_4/blob/main/whatsapp-video-2023-10-02-at-101333_X6FfW7zJ.mp4)
