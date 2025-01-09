# Trabalho_Sistemas_Distribuidos
Repositório para os arquivos de Sistemas Distribuídos
## Pré-processamento e Treinamento do Modelo

Para pré-processar os dados e treinar o modelo, navegue até o diretório `Pre_processing&Model_training` e execute os seguintes comandos:

```bash
cd Pre_processing&Model_training
python pre_process.py
python train_model.py
```

## Executando a Aplicação com Docker

Para executar a aplicação usando Docker, siga estes passos:

1. Construa a imagem Docker:

    ```bash
    docker build -t my_application .
    ```

2. Execute o contêiner Docker:

    ```bash
    docker run -p 8000:8000 my_application
    ```

3. Acesse a aplicação em `http://localhost:8000`.

## Estrutura do Repositório

```
/c:/Users/drodm/OneDrive/Documents/GitHub/Trabalho_Sistemas_Distribuidos/
├── Pre_processing&Model_training/
│   ├── pre_process.py
│   ├── train_model.py
├── Dockerfile
├── README.md
```

## Requisitos

- Python 3.x
- Docker

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/yourusername/Trabalho_Sistemas_Distribuidos.git
    ```

2. Instale os pacotes Python necessários:

    ```bash
    pip install -r requirements.txt
    ```

## Licença

Este projeto está licenciado sob a Licença MIT.