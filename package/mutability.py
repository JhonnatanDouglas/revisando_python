# dados mutaveis e dados imutaveis
import copy


# imutavel
def int_mutability(param_number: int) -> None:
    param_number = 3000
    print("Dentro da função int_mutability", param_number)


# mutavel
def list_mutability(param_list: list) -> None:
    # param_list[0] = "demo"
    # print("Dentro da função list_mutability", param_list)
    # print(id(param_list))  # 1842765520448 espaçamento na memoria

    # ------------------------------
    # new_list = param_list.copy()
    # new_list[0] = "demo"
    # print("Dentro da função list_mutability (new_list)", new_list)
    # print("Dentro da função list_mutability", param_list)

    # new_list = param_list[:]  # indice 0 : pega até o ultimo indice
    # new_list[0] = "demo"
    # print("Dentro da função list_mutability (new_list)", new_list)
    # print("Dentro da função list_mutability", param_list)
    # ------------------------------

    # new_list = param_list[:]
    # param_list[-1][0] = 999
    # print("Dentro da função list_mutability (new_list)", new_list)
    # print("Dentro da função list_mutability", param_list)

    new_list = copy.deepcopy(param_list)
    new_list[-1][0] = 999
    print("Dentro da função list_mutability (new_list)", new_list)
    print("Dentro da função list_mutability", param_list)
