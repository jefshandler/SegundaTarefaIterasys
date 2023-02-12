import json

import requests


# variaveis publicas
urlbase = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}

def teste_incluir_usuario():
    # 1 -   Configura
    # 1.1 - dados de Entrada -> Virao do arquivo add_user.json
    # 1.2 - Resultado Esperado
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = "110220232156"

    # executa
    resultado_obtido = requests.post(
        url=urlbase,
        headers=headers,
        data=open(r'../vendors/json/user.json')

    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == code_esperado
    assert corpo_do_resultado_obtido['type'] == type_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada
