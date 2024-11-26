# Sistema de Gerenciamento de Livros e Pedidos

Este é um sistema de gerenciamento de livros e pedidos desenvolvido em Python com MongoDB como banco de dados. Ele permite realizar operações básicas de CRUD para livros e pedidos diretamente no terminal.

## **Requisitos**

Certifique-se de que o ambiente atende aos seguintes requisitos antes de executar o programa:

1. **Python 3.8 ou superior**:
   - Para verificar se o Python está instalado:
     ```bash
     python3 --version
     ```
   - Para instalar:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **MongoDB**:
   - Certifique-se de que o MongoDB está instalado:
     ```bash
     sudo apt update
     sudo apt install -y mongodb
     ```
   - Inicie o MongoDB:
     ```bash
     sudo systemctl start mongodb
     sudo systemctl enable mongodb
     ```

3. **Bibliotecas Python necessárias**:
   - Instale as dependências do projeto:
     ```bash
     pip install pymongo
     ```

---

## **Configuração**

O programa utiliza o MongoDB como banco de dados padrão. Certifique-se de que o MongoDB está em execução antes de iniciar o sistema.

1. **Configuração da string de conexão**:
   - Localize o arquivo `connection/connection.py`.
   - Edite a função `conectar()` para ajustar a string de conexão, se necessário:
     ```python
     from pymongo import MongoClient

     def get_connection():
         return MongoClient("mongodb://localhost:27017/")  # Ajuste para o endereço e porta corretos do MongoDB
     ```

---

## **Execução**

Para iniciar o programa:

1. Navegue até o diretório do projeto:
   ```bash
   cd <NOME_DO_REPOSITORIO>
2-Execute o arquivo principal:
```bash 
python3 main.py

3-Siga as instruções exibidas no terminal para navegar entre as funcionalidades do sistema.
