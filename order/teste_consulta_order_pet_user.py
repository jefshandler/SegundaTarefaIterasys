import requests
import json

urlbase = 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json'}
def teste_status_order_pet():
    # 1 -   Configura
    # 1.1 - dados de Entrada -> vem do arquivo add_order1.json
    # 1.2 - Resultado Esperado
    status_code_esperado = 200
    id_pedido_esperado = 1
    id_pet_esperado = 110220232143
    status_pedido_esperado = 'placed'
    order_complete = True


    # Executa

    resultado_obtido = requests.get(
        url=urlbase + '/' + str(id_pedido_esperado),
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == id_pedido_esperado
    assert corpo_do_resultado_obtido['petId'] == id_pet_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado
    assert corpo_do_resultado_obtido['complete'] == order_complete

