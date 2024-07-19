# tupla é como se fosse uma lista nao modificavel


def tuple_fundamentals():
    print("Fundamento de Tuplas")

    # maneira literal
    my_tuple = (1, 2, "abacate", [1, 2])
    print(my_tuple)

    # usando builtin
    my_tuple_2 = tuple("string")
    print(my_tuple_2)

    print(my_tuple[0])

    # my_tuple[0] = 5
    # isso nao é possivel, porque nao pode modificar

    print(type(my_tuple))


def tuple_looping():
    my_tuple = (1, 2, "abacate", [1, 2])
    for item in my_tuple:
        print(item)
