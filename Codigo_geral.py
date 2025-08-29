from flask import Flask, request, jsonify
import threading
import requests
import time

app = Flask(__name__)

usuarios = []
current_id = 1


# === ROTAS DA API ===

@app.route('/users', methods=['POST'])
def criar_usuario():
    global current_id
    dados = request.get_json()

    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({'erro': 'Campos "nome" e "email" são obrigatórios'}), 400

    novo_usuario = {
        'id': current_id,
        'nome': dados['nome'],
        'email': dados['email']
    }
    usuarios.append(novo_usuario)
    current_id += 1

    return jsonify(novo_usuario), 201


@app.route('/users', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def obter_usuario(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            return jsonify(usuario), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404


@app.route('/users/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    dados = request.get_json()
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuario['nome'] = dados.get('nome', usuario['nome'])
            usuario['email'] = dados.get('email', usuario['email'])
            return jsonify(usuario), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404


@app.route('/users/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuarios.remove(usuario)
            return jsonify({'mensagem': 'Usuário excluído com sucesso'}), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404


# === MENU DO TERMINAL COM REQUESTS ===

def menu_terminal():
    time.sleep(1)  # Aguarda o servidor iniciar
    while True:
        print("\n===== MENU USUÁRIOS (via API) =====")
        print("1. Inserir novo usuário")
        print("2. Listar todos os usuários")
        print("0. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            payload = {
                "nome": nome,
                "email": email
            }

            resposta = requests.post('http://localhost:5000/users', json=payload)

            if resposta.status_code == 201:
                print("✅ Usuário criado com sucesso!")
                print(resposta.json())
            else:
                print("❌ Erro ao criar usuário:")
                print(resposta.json())

        elif opcao == '2':
            resposta = requests.get('http://localhost:5000/users')
            if resposta.status_code == 200:
                usuarios = resposta.json()
                if not usuarios:
                    print("Nenhum usuário cadastrado.")
                else:
                    print("\n--- Lista de Usuários ---")
                    for u in usuarios:
                        print(f"ID: {u['id']} | Nome: {u['nome']} | Email: {u['email']}")
            else:
                print("Erro ao buscar usuários.")

        elif opcao == '0':
            print("Encerrando menu.")
            break

        else:
            print("❌ Opção inválida!")


# === INICIALIZAÇÃO ===

if __name__ == '__main__':
    # Inicia o menu em uma thread separada
    threading.Thread(target=menu_terminal).start()

    # Inicia o servidor Flask
    app.run(debug=True)
