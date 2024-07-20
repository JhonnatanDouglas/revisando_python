<!-- MUTABILIDADE -->

```py
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

```

<!-- ---------------------------------------------------------- -->

<!-- PACKING E UNPACKING -->

```py
def packing(a: int, b: int, c: int) -> None:
    values = a, b, c
    total = sum(values)
    print(values)
    print(total)


def unpacking(values: list[int]) -> None:
    # a, b, c, d = values
    # print(a, b, c, d)

    n1, n2, *rest = values  # n1, n2, rest... = values  ||| no js
    print(n1, n2, rest)


def unpacking_dict(values: dict) -> None:
    key_1, key_2, key_3 = values
    print(key_1, key_2, key_3)

```

<!-- ---------------------------------------------------------- -->

<!-- ARGS E KWARGS -->

```py
def func_args(*args: int) -> None:
    total = sum(args)
    print(args)
    print(total)


# atençao, voce podde pegar tudo com kwargs ou tirar algo
# tipo, tirar o id abaixo
def func_kwargs(id, **kwargs: dict) -> None:
    print(id, kwargs)

```
