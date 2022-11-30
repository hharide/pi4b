# imports necessários!
from flask import Flask, request, jsonify

app = Flask(__name__)

# dados!
clientes = [
        {
         "cliente_id" : 1, "nome" : "Juliana Silva",
         "endereco" : "Avenida Bento Gonçalves, 100", "cep" : "12345-00",
        "dataNasc" : "10/01/1990", "telefone" : 991456927},
        {"cliente_id" : 2, "nome" : "Maria Matos",
         "endereco" : "Rua das Flores, 1769", "cep" : "32445-30",
        "dataNasc":"31/12/2001", "telefone":984020001},
        {"cliente_id" : 3, "nome":"Julio Souza", "endereco" : "Avenida Santos Dummont, 2960", "cep":"52395-01",
        "dataNasc" : "15/03/1987", "telefone" : 981100659},
        {"cliente_id" : 4, "nome" : "Gustavo Monteiro", "endereco" : "Rua Santa Cruz, 1007", "cep":"12345-24",
        "dataNasc" : "11/09/1990", "telefone" : 981061002},
        {"cliente_id" : 5, "nome" : "Amanda Rodrigues",
         "endereco" : "Rua Voluntários da Pátria, 890", "cep" : "12447-08",
        "dataNasc" : "28/08/1990", "telefone" : 984623984}
            ]

nextClienteId = 4

# utilizando o método GET!
@app.route('/clientes', methods=['GET'])
def clientes():
  return jsonify(clientes)

## vendo se o cliente é válido!
def cliente_valido(cliente):
  for key in cliente.keys():
    if key != 'nome':
      return False
  return True

# utilizando o método POST!
@app.route('/clientes', methods=['POST'])
def create_cliente():
  global nextClienteId
  cliente = json.loads(request.data)
  if not cliente_valido(cliente):
    return jsonify({ 'erro': 'propriedades invalidas.' }), 400

  cliente['cliente_id'] = nextClienteId
  nextClienteId += 1
  clientes.append(cliente)

  return '', 201, { 'location': f'/clientes/{cliente["cliente_id"]}' }

# utilizando o método PUT!
@app.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id: int):
  cliente = get_cliente(id)
  if cliente is None:
    return jsonify({ 'error': 'esse cliente não existe.' }), 404

  updated_cliente = json.loads(request.data)
  if not cliente_valido(updated_cliente):
    return jsonify({ 'erro': 'propriedades invalidas.' }), 400

  cliente.update(updated_cliente)

  return jsonify(cliente)

# utilizando o método DELETE!
@app.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id: int):
  global clientes
  cliente = get_cliente(id)
  if cliente is None:
    return jsonify({ 'erro': 'cliente não existe.' }), 404

  clientes = [e for c in clientes if c['id'] != id]
  return jsonify(cliente), 200

# rodar a api
app.run()
