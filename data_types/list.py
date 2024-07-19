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
