# Trabalho_Sistemas_Distribuidos
Repositório para os arquivos de Sistemas Distribuídos

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/Zoiudp/Trabalho_Sistemas_Distribuidos.git
    ```


Não necessario mas caso seja de interesse retreinar o modelo com outros dados seguir o passo a passo a seguir

## Pré-processamento e Treinamento do Modelo
Para pré-processar os dados e treinar o modelo, navegue até o diretório `Pre_processing&Model_training` e execute os seguintes comandos:

```bash
cd Pre_processing&Model_training
python pre_process.py
python train_model.py
```

## Executando a Aplicação com Docker

Para executar a aplicação usando Docker Compose, siga estes passos:

1. Construa e inicie os serviços definidos no `docker-compose.yml`:

    ```bash
    docker-compose up --build
    ```

2. Acesse a aplicação em `http://localhost:3000`.


## Requisitos

- Docker

## Licença

Este projeto está licenciado sob a Licença MIT.