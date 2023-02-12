import requests
import json

urlbase = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type': 'application/json'}
def teste_vender():
    # 1 -   Configura
    # 1.1 - dados de Entrada -> vem do arquivo add_order1.json
    # 1.2 - Resultado Esperado
    status_code_esperado = 200
    id_pedido_esperado = 1
    id_pet_esperado = 110220232143
    status_pedido_esperado = 'placed'


    # Executa

    resultado_obtido = requests.post(
        url=urlbase + 'store/order',
        headers=headers,
        data=open(r'../vendors/json/user_order.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == id_pedido_esperado
    assert corpo_do_resultado_obtido['petId'] == id_pet_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado

    # extrassao Extrair
    pet_id_extraido = corpo_do_resultado_obtido.get('petId')

    # Realizar a 2 parte Transacao

    # Configura
    # dados de entrada = estraido da 1 transaçao acima

    # Resultado esperado  vamos pegar o nome do animal
    pet_name_esperado = 'Bichento'
    status_code_esperado = 200

    # executa
    resultado_obtido = requests.get(
        url= urlbase + 'pet/' + str(pet_id_extraido),
        headers=headers
    )

    # Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_do_resultado_obtido = resultado_obtido.json()

    assert corpo_do_resultado_obtido['name'] == pet_name_esperado
    print(json.dumps(corpo_do_resultado_obtido, indent=4))