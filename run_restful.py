from flask import Flask, request
from flask_restful import Resource, Api
import json
from cpf_validador import cpf_valido
from cnpj_validador import cnpj_valido

app = Flask(__name__)
api = Api(app)

class CEP(Resource):
    def put(self):
        dado_str = json.loads(request.data)
        dado = ''.join(digito for digito in dado_str if digito.isdigit())
        if len(dado) != 8:
            mensagem =  f'{dado} não é um CEP válido'
            return {'mensagem': mensagem,
                    'CEP': None}
        else:
            cep = dado[:5] + "-" + dado[5:]
            mensagem = 'CEP válido'
            return {'mensagem': mensagem,
                    'CEP': cep}

class RG(Resource):
    def put(self):
        dado_str = json.loads(request.data)
        dado = ''.join(c for c in dado_str if c.isdigit())
        if len(dado) != 9:
            mensagem = f'{dado} não é um RG válido'
            return {'mensagem': mensagem,
                    'RG': None}
        else:
            rg = f"{dado[:2]}.{dado[2:5]}.{dado[5:8]}-{dado[8:]}"
            mensagem = 'RG válido'
            return {'mensagem': mensagem,
                    'RG': rg}

class CPF(Resource):
    def put(self):
        dado_str = json.loads(request.data)
        dado = ''.join(c for c in dado_str if c.isdigit())    
        if cpf_valido(dado) is False:
            mensagem = f'{dado} não é um CPF válido'
            return {'mensagem': mensagem,
                    'CPF': None}
        else:
            cpf = f"{dado[:3]}.{dado[3:6]}.{dado[6:9]}-{dado[9:]}"
            mensagem = 'CPF válido'
            return {'mensagem': mensagem,
                    'CPF': cpf}

class CNPJ(Resource):
    def put(self):
        dado_str = json.loads(request.data)
        dado = ''.join(c for c in dado_str if c.isdigit())    
        if cnpj_valido(dado) is False:
            mensagem = f'{dado} não é um CNPJ válido'
            return {'mensagem': mensagem,
                    'CNPJ': None}
        else:
            cnpj = f"{dado[:2]}.{dado[2:5]}.{dado[5:8]}/{dado[8:12]}-{dado[12:]}"
            mensagem = 'CNPJ válido'
            return {'mensagem': mensagem,
                    'CNPJ': cnpj}


api.add_resource(CEP, '/cep/')
api.add_resource(RG, '/rg/')
api.add_resource(CPF, '/cpf/')
api.add_resource(CNPJ, '/cnpj/')


if __name__ == "__main__":
    app.run(debug=True)
 