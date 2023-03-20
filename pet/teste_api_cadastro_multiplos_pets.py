import json
import pytest
import requests
from util.ler_csv import ler_csv


# variaveis publicas
urlbase = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags_id,tags_name,status',
                         ler_csv(r'../vendors/csv/massa_incluir_pet.csv'))
def teste_incluir_pet_em_massa_CSV(pet_id, category_id, category_name, pet_name, tags_id, tags_name, status):
    # 1 configura
    # 1.1 dados de entrada
    # os dados de entrada provem do arquivo massa_incluir_pet_csv
    # 1.2 resultado esperados - os dados de entrada tambem servirao
    # visto que o retorno é um eco
    # 1.1.1 MOntagem do Json dinâmico
    corpo_json = '{'
    corpo_json += f' "id": {pet_id}, '
    corpo_json += ' "category": {'
    corpo_json += f'    "id": {category_id},'
    corpo_json += f'    "name": "{category_name}"'
    corpo_json += '},'
    corpo_json += f' "name": "{pet_name}",'
    corpo_json += ' "photoUrls": ['
    corpo_json += '    "string"'
    corpo_json += '],'
    corpo_json += ' "tags": ['
    corpo_json += '    {'
    corpo_json += f'        "id": {tags_id},'
    corpo_json += f'        "name": "{tags_name}"'
    corpo_json += '    }'
    corpo_json += '],'
    corpo_json += f' "status": "{status}"'
    corpo_json += '}'

    status_code_esperado = 200

    # 2. executa
    resultado_obtido = requests.post(
        url=urlbase,
        headers=headers,
        data=corpo_json
    )

    # 3. valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    assert corpo_do_resultado_obtido['tags'][0]['name'] == tags_name

@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags,status',
                         ler_csv(r'../vendors/csv/massa_incluir_pet_multitags.csv'))
def teste_incluir_multiplos_pets_CSV(pet_id, category_id, category_name, pet_name, tags, status):
    # 1. Configura
    # 1.1 Dados de entrada
    # Os dados de entrada proveem do arquivo massa_incluir_pet_multitags.csv
    # OBS esta parte de gerar json dinâmico foi um trabalho em conjunto com meu amigo, Luciano.
    global itens_lista
    corpo_json = '{'
    corpo_json += f'"id":  "{pet_id}" ,'
    corpo_json += '"category": {'
    corpo_json += f'"id":  "{category_id}",'
    corpo_json += f'"name": "{category_name}"'
    corpo_json += ' },'
    corpo_json += f'"name":  "{pet_name}" ,'
    corpo_json += '"photoUrls": ['
    corpo_json += '"string"'
    corpo_json += '],'
    lista_tags = tags
    json_tag = '"tags": ['
    sub_lista_tags = []
    qtd_tags = lista_tags.count(';') + 1
    if lista_tags.count(';') > 0:
        lista_tags = lista_tags.split(';')
        qtd_el = len(lista_tags)
        print('Quantidade de elementos' + str(qtd_el))

        for i in range(0, qtd_el):
            # Create an index range for l of n items:
            sub_lista_tags.append(lista_tags[i].split(','))
        itens_lista = len(sub_lista_tags)
        # print(f'\nExistem  {itens_lista} tags na lista {sub_lista_tags}')
        for contador in range(0, itens_lista):
            if contador < itens_lista - 1:
                json_tag += '{"id":' + sub_lista_tags[contador][0] + \
                            ',"name":"' + sub_lista_tags[contador][1] + '"},'
            else:
                json_tag += '{"id":' + sub_lista_tags[contador][0] + \
                            ',"name":"' + sub_lista_tags[contador][1] + '"}'
    else:
        lista_tags = lista_tags.split(',')
        json_tag += '{"id":' + lista_tags[0] + ',"name":"' + lista_tags[1] + '"}'

    json_tag += '],'
    corpo_json += json_tag
    corpo_json += f'"status":  "{status}"'
    corpo_json += '}'

    # 1.2 Resultados Esperados
    # Os dados de entrada também servirão como resultados
    # esperados, visto que o retorno é um eco
    status_code_esperado = 200

    # Executa
    resultado_obtido = requests.post(
        url=urlbase,
        headers=headers,
        data=corpo_json
    )

    # Valida
    mostrar_corpo_json = json.loads(corpo_json)
    print(f'\n==== CORPO ENVIADO ====')
    print(json.dumps(mostrar_corpo_json, indent=4))
    print(f'\n==== CORPO OBTIDO ====')
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    # asserts dinamicos de acordo com as tags existentes para um pet
    if qtd_tags > 1:
        # print(f'\nExistem  {itens_lista} tags na lista {sub_lista_tags}')
        for i in range(0, qtd_tags):
            for j in range(2):
                assert corpo_do_resultado_obtido['tags'][i]['name'] == sub_lista_tags[i][1]
    else:
        # print(f'\nExiste 1 tag na lista {lista_tags}')
        assert corpo_do_resultado_obtido['tags'][0]['name'] == lista_tags[1]
