# from package.mutability import int_mutability, list_mutability
# from package.packing_unpacking import packing, unpacking, unpacking_dict
# from package.args_kwargs import func_args


from package.args_kwargs import func_kwargs


def main():
    # number = 10
    # print("Antes da chamada do int_mutability", number)
    # int_mutability(number)
    # print("Depois da chamada do int_mutability", number)
    # print()
    # list = [1, 2, 3, 4, 5, [9, 8, 7]]
    # print("Antes da chamada do list_mutability", list)
    # print(id(list))
    # list_mutability(list)
    # print("Depois da chamada do list_mutability", list)
    # print(id(list))

    # packing(1, 2, 3)
    # print()
    # new_list = [1, 2, 3, 4]
    # unpacking(new_list)
    # print()
    # new_dict = {"name": "Leonhart", "id": 1, "job": "developer"}
    # unpacking_dict(new_dict)

    req_body = {
        "id": 1,
        "name": "mouse",
        "qtd_disponiveis_nas_filiais": [1, 2, 3, 4, 5],
    }
    # func_args(*req_body["qtd_disponiveis_nas_filiais"])

    func_kwargs(**req_body)


if __name__ == "__main__":
    main()
