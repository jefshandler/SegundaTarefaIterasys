import json

import requests

# variaveis publicas
urlbase = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

def test_incluir_pet():
    # configura - prepara
    # Dados de entrada provem do arquivo json (gato.json)

    # resultados esperados (pertence a configura)
    status_code_esperado = 200
    pet_id_esperado = 110220232143
    pet_nome_categoria_esperado = "Gato"
    pet_nome_esperado = "Bichento"
    pet_tag_esperado = "vacinado"

    # executa
    resultado_obtido = requests.post(
        url=urlbase,
        headers=headers,
        data=open(r'../vendors/json/gato.json')

    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperado