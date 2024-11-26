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
   - Certifique-se de que o MongoDB está instalado e em execução:
     ```bash
     sudo apt update
     sudo apt install -y mongodb
     sudo systemctl start mongodb
     sudo systemctl enable mongodb
     ```

3. **Bibliotecas Python necessárias**:
   - As dependências serão instaladas a partir do arquivo `requirements.txt`.

---

## **Instalação**

Siga as etapas abaixo para configurar o ambiente:

1. Clone o repositório do projeto:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
