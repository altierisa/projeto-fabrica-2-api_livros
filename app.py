from flask import Flask, jsonify, make_response, request
from bd_livros import livros  # Importa a lista de livros do arquivo bd_livros.py

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # Mantém a ordem original dos dados JSON

# Rota para listar todos os livros (GET)
@app.route('/livros', methods=['GET'])
def get_livros():
    return make_response(jsonify(
        mensagem='Lista de Livros Cadastrados',
        dados=livros
    ), 200)

# Rota para buscar um livro pelo ID (GET)
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            return make_response(jsonify(
                mensagem=f'Livro de ID {id} encontrado',
                dados=livro
            ), 200)
    return make_response(jsonify(mensagem='Livro não encontrado'), 404)

# Rota para adicionar um novo livro (POST)
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    livro = request.get_json()
    livros.append(livro)
    return make_response(jsonify(
        mensagem=f'Livro de ID {livro["id"]} adicionado com sucesso.',
        dados=livro
    ), 201)

# Rota para atualizar um livro completamente (PUT)
@app.route('/livros/<int:id>', methods=['PUT'])
def update_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            novo_dados = request.json
            livro.update(novo_dados)
            return make_response(jsonify(
                mensagem=f'Livro ID {id} atualizado com sucesso. (PUT)',
                dados=livro
            ), 200)
    return make_response(jsonify(mensagem='Livro não encontrado'), 404)

# Rota para atualizar parcialmente um livro (PATCH)
@app.route('/livros/<int:id>', methods=['PATCH'])
def patch_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            dados = request.json
            livro.update(dados)
            return make_response(jsonify(
                mensagem=f'Livro ID {id} atualizado parcialmente. (PATCH)',
                dados=livro
            ), 200)
    return make_response(jsonify(mensagem='Livro não encontrado'), 404)

# Rota para deletar um livro pelo ID (DELETE)
@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            livros.remove(livro)
            return make_response(jsonify(
                mensagem=f'Livro ID {id} removido com sucesso.',
                dados=livro
            ), 200)
    return make_response(jsonify(mensagem='Livro não encontrado'), 404)

# Inicia o servidor Flask em modo debug (auto-recarrega quando o código muda)
if __name__ == '__main__':
    app.run(debug=True)
