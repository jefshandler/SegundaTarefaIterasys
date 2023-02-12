import json

import requests

# variaveis publicas
urlbase = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}

def teste_login_usuario():
    # 1 -   Configura
    # 1.1 - dados de Entrada -> Virao do arquivo add_login.json
    # 1.2 - Resultado Esperado
    username = ""
    password = ""
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = 'logged in user session:'

    # Executa

    resultado_obtido = requests.get(
        url=f'{urlbase}/login?username={username}&password={password}',
        headers=headers,
        data = open(r'../vendors/json/user_login.json')
    )

    # Valida
    print(f'{username}**{password}')
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == code_esperado
    assert corpo_do_resultado_obtido['type'] == type_esperado
    # assert corpo_do_resultado_obtido['message'].find(mensagem_esperada)
    assert mensagem_esperada.find(corpo_do_resultado_obtido['message'])

    # Extrai
    mensagem_extraida = corpo_do_resultado_obtido.get('message')
    print(f'A mensagem a ser Extraida = {mensagem_extraida}')
    token = mensagem_extraida[23:]
    print(f'o token = {token}')
