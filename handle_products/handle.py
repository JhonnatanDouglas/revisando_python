from database import products


def get_last_product() -> dict | str:
    # tratamento de exceçao

    # try/except

    # try:
    #     last_product = products[-1]
    # except:
    #     return "Nenhum produto foi encontrado no banco de dados."

    # try:
    #     last_product = products[-1]
    # except IndexError:
    #     return "Nenhum produto foi encontrado no banco de dados."
    # except TypeError:
    #     return "Soma de str e int nao pode ser feita."

    try:
        last_product = products[-1]
    except IndexError as error:
        return error
    except TypeError:
        return "Soma de str e int nao pode ser feita."

    return last_product


def save_product(data: dict) -> dict:
    # levantamento de excecao

    # data["name"]  # Se a chave nao existir, estoura KeyError
    # data.get("name")  # se a chave existir, retorna None padrão
    # data.get("name", "pepino")  # se a chave existir, pode colocar um valor

    product_name = data.get("name")

    if not product_name:
        raise KeyError("Chave name nao foi encontrada.")  # throw new error

    # try:
    #     product_name = data["name"]
    # except KeyError:
    #     return "Chave name nao foi encontrada"

    # if type(product_name) is not str:
    #     raise TypeError("Chave name deve ser do tipo string.")

    chaves_obrigatorias = ["id", "name", "price"]
    chaves_recebidas = data.keys()

    for chave in chaves_obrigatorias:
        if chave not in chaves_recebidas:
            raise TypeError("Chave name deve ser do tipo string.")

    products.append(data)  # push do js
    return data
