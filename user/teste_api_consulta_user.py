import json

import pytest
import requests

# variaveis publicas
urlbase = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}

def teste_consultar_pet():
    # 1 Parte é dividido em 2 partes entradas e Resultados esperados
    # configura - prepara
    # Dados de entrada provem do arquivo json (user.json)

    # Entradas
    username_esperado = 'Hermione_Granger'
    # Resultados esperados
    # 2 Parte
    status_code_esperado = 200
    username_esperado = 'Hermione_Granger'
    id_esperado = 110220232156
    firstName_esperado = "Hermione"
    lastName_esperado = "Granger"
    email_esperado = "Hermione_Granger@bb.com"
    password_esperado = "asdqwe123"
    phone_esperado = "123123123"

    # Executa

    resultado_obtido = requests.get(
        url=urlbase + '/' + username_esperado,
        headers=headers
    )

    # 3 Parte
    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == id_esperado
    assert corpo_do_resultado_obtido['username'] == username_esperado
    assert corpo_do_resultado_obtido['firstName'] == firstName_esperado
    assert corpo_do_resultado_obtido['lastName'] == lastName_esperado
    assert corpo_do_resultado_obtido['email'] == email_esperado
    assert corpo_do_resultado_obtido['password'] == password_esperado
    assert corpo_do_resultado_obtido['phone'] == phone_esperado

