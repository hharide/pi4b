from flask import Flask, jsonify, request

app = Flask(__name__)

# lista de clientes
clientes = [
        {'id': 1, 'nome' : 'Juliana Silva', 'endereco' : 'Avenida Bento Goncalves, 100', 'cep' : '12345-00', 
        'dataNasc' : '10/01/1990', 'telefone' : 991456927},
        {'id' : 2, 'nome' : 'Maria Matos', 'endereco' : 'Rua das Flores, 1769', 'cep' : '32445-30', 
        'dataNasc' : '31/12/2001', 'telefone' : 984020001},
        {'id': 3, 'nome' : 'Julio Souza', 'endereco' : 'Avenida Santos Dummont, 2960', 'cep' : '52395-01', 
        'dataNasc' : '15/03/1987', 'telefone' : 981100659},
        {'id' : 4, 'nome' : 'Gustavo Monteiro', 'endereco' : 'Rua Santa Cruz, 1007', 'cep' : '12345-24', 
        'dataNasc' : '11/09/1990', 'telefone' : 981061002},
        {'id' : 5, 'nome' : 'Amanda Rodrigues', 'endereco' : 'Rua Voluntários da Pátria, 890', 'cep' : '12447-08', 
        'dataNasc' : '28/08/1990', 'telefone' : 984623984}
    ]

# método GET para todos!
@app.route('/clientes', methods=['GET'])
def get_todos():
    return jsonify(clientes)

# método GET para cliente por id!
@app.route('/clientes/<int:id>', methods=['GET'])
def get_por_id(id):
    for cliente in clientes:
        if cliente.get('id') == id:
            return jsonify(cliente)

# método PUT
@app.route('/clientes/<int:id>', methods=['PUT'])
def editar_cliente(id):
    alterado = request.get_json()
    for index, cliente in enumerate(clientes):
        if cliente.get('id') == id:
            clientes[index].update(cliente)
            return jsonify(cliente[index])

# método POST!
@app.route('/clientes', methods=['POST'])
def add_cliente():
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)
    return jsonify(clientes)

# método DELETE!
@app.route('/clientes/<int:id>', methods=['DELETE'])
def remover_cliente(id):
    for index,cliente in enumerate(clientes):
        if cliente.get('id') == id:
            del clientes[index]

    return jsonify(clientes)

# rodar a api!
app.run(port=5000, host='localhost', debug=True)