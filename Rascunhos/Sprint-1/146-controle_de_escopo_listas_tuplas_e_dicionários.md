<!-- ---------------------------------------------------------- -->
<!-- Listas -->

```py
# array = lista

# forma literal


my_list = [1, 2, "string", 3.4, ["list", 1]]
my_list_2 = list("String")

print(my_list)  # [1, 2, 'string', 3.4, ['list', 1]]
print(my_list_2)  # ['S', 't', 'r', 'i', 'n', 'g']

print("----------------------------------------------")
# typeof
print(type(my_list))  # <class 'list'>

print("----------------------------------------------")
# slice
print(my_list[-1])  # pega o ultimo item
print(my_list[-2])  # pega o penultimo item
print(my_list[0:3])  # slice começa do 0, vai ate 3

print("----------------------------------------------")
# remover itens
print(my_list)
print(my_list.pop())  # remove o ultimo item
print(my_list)

print(my_list.pop(0))  # remove o do indice 0
print(my_list)


print("----------------------------------------------")
# lista mutavel

my_list[0] = "restou o indice da lista"
print(my_list)

my_str = "pepino"
# my_str[0] = "j" <<< isso nao funcioa porque nao é uma lista e sim uma string

print("----------------------------------------------")


def list_looping():
    my_list = [1, 2, "3", [4, 1], 2.3]

    print("Usando o For in:")
    for item in my_list:
        print(item)

    print()
    print("Usando o For in enumerate:")

    for incice, valor in enumerate(my_list):
        print(f"Este é o indice atual: {incice}.")
        print(f"Este é o valor atual: {valor}.")
        print()

    print()
    print("Usando o For in range:")

    for item in range(5):
        print("Olá!")

    print()
    print("Usando o For in range:")

    # começando do indice 1 ate 5
    for item in range(1, 5):
        print("Olá!")


if __name__ == "__main__":
    print("Modulo de list.py")

```

<!-- ---------------------------------------------------------- -->
<!-- Tuplas -->

```py
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

```

<!-- ---------------------------------------------------------- -->
<!-- Dicionarios -->

```py
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

```

<!-- ---------------------------------------------------------- -->
