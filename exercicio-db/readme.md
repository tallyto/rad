# Cadastro de Alunos com Python, Tkinter e MySQL

Este é um exemplo de uma aplicação de Cadastro de Alunos em Python, usando a biblioteca Tkinter para a interface gráfica e o MySQL para armazenamento de dados. A aplicação permite adicionar, listar, editar e remover alunos.

## Funcionalidades

1. **Adicionar Aluno:** Você pode adicionar um aluno, fornecendo o nome, as notas das avaliações (AV1, AV2 e AV3) e o criador do registro.

2. **Listar Alunos:** A aplicação exibe a lista de todos os alunos cadastrados, incluindo seus nomes, notas e criadores do registro.

3. **Editar Aluno:** Você pode selecionar um aluno na lista e editar suas informações, incluindo nome, notas e criador do registro.

4. **Remover Aluno:** Ao selecionar um aluno na lista, é possível removê-lo do banco de dados.

## Configuração

Antes de executar a aplicação, siga estas etapas de configuração:

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Instale o MySQL no seu sistema ou crie um contêiner Docker para o MySQL. Para criar um contêiner Docker com o MySQL, você pode usar o seguinte comando:

   ```bash
   docker run -d -e MYSQL_ROOT_PASSWORD=sua-senha -e MYSQL_DATABASE=rad -p 3306:3306 mysql:latest
   ```

   Certifique-se de substituir `sua-senha` pela senha que deseja definir para o MySQL.

3. Clone este repositório:

   ```bash
   git clone https://github.com/tallyto/rad.git
   ```

4. Navegue até o diretório do projeto:

   ```bash
   cd exercicio-db
   ```

5. Atualize as configurações do banco de dados no arquivo `app.py`. Altere as variáveis `host`, `user`, `password` e `database` para corresponder às configurações do seu banco de dados.

   ```python
   # Configurações do banco de dados
   host = "127.0.0.1"
   user = "root"
   password = "sua-senha"
   database = "rad"
   ```

6. Instale as dependências necessárias executando o seguinte comando:

   ```bash
   pip install mysql-connector-python tkinter
   ```

## Executando a Aplicação

Após a configuração, você pode executar a aplicação com o seguinte comando:

```bash
python app.py
```

A aplicação será iniciada, e você verá a interface do Cadastro de Alunos.

## Uso da Aplicação

A aplicação possui uma interface simples e amigável:

- Para **adicionar um aluno**, preencha os campos de nome, AV1, AV2, AV3 e o criador do registro, e clique no botão "Adicionar Aluno".

- Para **listar os alunos**, você verá a lista de alunos na área de exibição de resultados.

- Para **editar um aluno**, selecione um aluno na lista e clique no botão "Editar". Você poderá fazer as edições desejadas e salvar as alterações.

- Para **remover um aluno**, selecione um aluno na lista e clique no botão "Remover". Será exibida uma confirmação antes de remover o aluno.

## Personalização

Sinta-se à vontade para personalizar e expandir a aplicação de acordo com suas necessidades. Você pode adicionar recursos adicionais, como autenticação de usuário, validações, relatórios, ou qualquer outra funcionalidade que desejar.

## Contribuições

Contribuições são bem-vindas! Se você encontrar problemas ou desejar melhorar a aplicação, sinta-se à vontade para abrir problemas ou solicitar pull requests.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter detalhes.
