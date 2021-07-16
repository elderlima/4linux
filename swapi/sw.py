import requests

ENDPOINT_BASE = 'https://swapi.dev/api/'

ENDPOINT_PERSONAGENS = ENDPOINT_BASE + 'people'

ENDPOINT_NAVE = ENDPOINT_BASE + 'starships'


response = requests.get(ENDPOINT_PERSONAGENS)
dados = response.json()

response_nave = requests.get(ENDPOINT_NAVE)
dados_nave = response.json()

# def listar_todos_personagens():
#     url_pagina = ENDPOINT_PERSONAGENS
#     total = 0

#     while url_pagina is not None:
#         response = requests.get(url_pagina)
#         dados = response.json()
        
#         for personagem in dados['results']:
#             #if personagem['species'] == []:
#                 print(personagem['name'])
#                 total = total + 1
            
#         url_pagina = dados['next']
    
#     print(total)

# listar_todos_personagens()

def listar_naves_precos_baixos_de(preco):
    url_pagina = ENDPOINT_NAVE
    total = 0

    while url_pagina is not None:
        response_nave = requests.get(url_pagina)
        dados_nave = response.json()
        
        for nave in dados_nave['results']:
            custo = nave['cost_in_credits']
            if custo != 'unknow' and float(custo) < preco:
                print(nave['name'])
                total = total + 1
            
        url_pagina = dados_nave['next']
    
    print(total)

listar_naves_precos_baixos_de(100_000_000)