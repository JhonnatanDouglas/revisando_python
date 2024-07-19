# dict é a mesma coisa de Objeto no js


def dict_fundamentals():
    print("Fundamento Dicionarios")

    # forma literal
    my_dict = {"nome": "Lucira", "modulo": 5}
    print(my_dict)

    # forma builtin
    my_dict_2 = dict()
    print(my_dict_2)

    # tipo
    print(type(my_dict))

    # chamando o item no dicionario
    print(my_dict["nome"])  # my_obj.nome - js

    # mudando o item no dicionario
    my_dict["nome"] = "Leonhart"
    print(my_dict)

    # adicionando a chave nova
    my_dict["linguagem"] = "Python"
    print(my_dict)

    # adicionando a chave nova builtin
    my_dict.update({"id": 2})
    print(my_dict)


def dict_looping():
    print()
    my_dict = {"nome": "Lucira", "modulo": 5}

    for key in my_dict:
        print(key)
        print(my_dict[key])

    print()  # obj.keys()
    for key in my_dict.keys():
        print(key)

    print()  # obj.values()
    for key in my_dict.values():
        print(key)

    print()  # obj.entries()
    for key in my_dict.items():
        print(key)
