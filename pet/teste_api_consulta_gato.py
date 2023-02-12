import json

import pytest
import requests

# variaveis publicas
urlbase = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

def teste_consultar_pet():
    # 1 Parte é dividido em 2 partes entradas e Resultados esperados
    # configura - prepara
    # Dados de entrada provem do arquivo json (gato.json)

    # Entradas
    pet_id = '110220232143'
    # Resultados esperados
    # 2 Parte
    status_code_esperado = 200
    pet_id_esperado = 110220232143
    pet_nome_categoria_esperado = "Gato"
    pet_nome_esperado = "Bichento"
    pet_tag_esperado = "vacinado"

    # Executa

    resultado_obtido = requests.get(
        url=urlbase + '/' + pet_id,
        headers=headers
    )

    # 3 Parte
    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperado
