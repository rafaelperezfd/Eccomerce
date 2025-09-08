import mercadopago

public_key = "APP_USR-6ee630b0-3115-4384-9516-e456fac8b930"
token = "APP_USR-6067892025695388-121419-ba029c5a69266562b1d9498b82841c68-2156566293"


def criar_pagamento(itens_pedido, link):
    # Configure as credenciais
    sdk = mercadopago.SDK(token)
    # Crie um item na preferência

    # itens que ele está comprando no formato de dicionário
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            "title": nome_produto,
            "quantity": quantidade,
            "unit_price": preco_unitario,
        })

    # valor total
    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": {
            "success": link,
            "pending": link,
            "failure": link,
        }
    }
    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta["response"]["init_point"]
    id_pagamento = resposta["response"]["id"]
    return link_pagamento, id_pagamento