# Grupo composto por: Julia Parreiras, Theofilo Mesquita, Kaua Felipe

# Rota para CRIAR um novo usuário (POST /users)
@app.route('/users', methods=['POST'])
def criar_usuario():
    """
    Cria um novo usuário.
    ---
    tags:
      - Usuários
    description: Cria um novo usuário com nome e email.
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: user
        description: Objeto JSON com os dados do usuário
        required: true
        schema:
          type: object
          required:
            - nome
            - email
          properties:
            nome:
              type: string
              example: João Silva
            email:
              type: string
              example: joao@email.com
    responses:
      201:
        description: Usuário criado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nome:
              type: string
              example: João Silva
            email:
              type: string
              example: joao@email.com
      400:
        description: Requisição inválida, faltando nome ou email
        schema:
          type: object
          properties:
            erro:
              type: string
              example: 'Campos "nome" e "email" são obrigatórios'
    """

# Rota para LISTAR todos os usuários (GET /users)
@app.route('/users', methods=['GET'])
def listar_usuarios():
    """
    Lista todos os usuários.
    ---
    tags:
      - Usuários
    produces:
      - application/json
    responses:
      200:
        description: Lista de usuários
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              nome:
                type: string
                example: João Silva
              email:
                type: string
                example: joao@email.com
    """

# Rota para OBTER um usuário pelo ID (GET /users/<user_id>)
@app.route('/users/<int:user_id>', methods=['GET'])
def obter_usuario(user_id):
    """
    Obtém os dados de um usuário pelo ID.
    ---
    tags:
      - Usuários
    produces:
      - application/json
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
        description: ID do usuário
    responses:
      200:
        description: Usuário encontrado
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nome:
              type: string
              example: João Silva
            email:
              type: string
              example: joao@email.com
      404:
        description: Usuário não encontrado
        schema:
          type: object
          properties:
            erro:
              type: string
              example: Usuário não encontrado
    """

# Rota para ATUALIZAR um usuário pelo ID (PUT /users/<user_id>)
@app.route('/users/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    """
    Atualiza os dados de um usuário pelo ID.
    ---
    tags:
      - Usuários
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
        description: ID do usuário
      - in: body
        name: user
        description: Dados para atualizar o usuário
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: João Silva
            email:
              type: string
              example: joao@email.com
    responses:
      200:
        description: Usuário atualizado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nome:
              type: string
              example: João Silva
            email:
              type: string
              example: joao@email.com
      404:
        description: Usuário não encontrado
        schema:
          type: object
          properties:
            erro:
              type: string
              example: Usuário não encontrado
    """

# Rota para DELETAR um usuário pelo ID (DELETE /users/<user_id>)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    """
    Remove um usuário pelo ID.
    ---
    tags:
      - Usuários
    produces:
      - application/json
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
        description: ID do usuário
    responses:
      200:
        description: Usuário excluído com sucesso
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: Usuário excluído com sucesso
      404:
        description: Usuário não encontrado
        schema:
          type: object
          properties:
            erro:
              type: string
              example: Usuário não encontrado
    """
