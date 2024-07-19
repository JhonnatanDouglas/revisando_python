<!-- aqui ficara todas as anotações da revisao -->

```py

```

```py
# let, var, const - JS

variavel_1 = 1
variavel_2 = 2

# const no python | porem é so uma convenção, ela é uma variavel simples

VARIAVEL_3 = 2

# variavel/comentario de muitas linhas

"""
Isso é um comentario
"""

string = """
muitiplas linhas 1
muitiplas linhas 2
muitiplas linhas 3
"""
```

<!-- ------------------------------------------------------------------------- -->

```py
if variavel_1 < variavel_2:
print(f"O valor é {variavel_1}") # console.log
elif variavel_2 == variavel_1:
print("possui mesmo valor")
else:
print("sei la o que")

# listas (é como é chamado os arrays)

numeros = [1, 2, 3]

print("----------------------------------------------")

# for

for numero_atual in numeros:
print(numero_atual)

print("----------------------------------------------")

# while

contador = 1

while contador <= 5:
print(f"O contador está em: {contador}")
contador += 1

print("----------------------------------------------")
```

<!-- ------------------------------------------------------------------------- -->

```py
# atributos adicionais das variaveis

string_1 = "Ola mundo"
string_2 = "jabuticaba"

caixa_alta = string_1.upper()
caixa_baixa = string_1.lower()
primeira_letra = string_1[0]

# [0:0] isso é o slice no java script

fatiamento = string_1[0:2] # começa de qual indice e termina contando letras
fatiamento_2 = string_1[:2] # da na mesma do de cima
indo_até_o_final = string_1[0:]

fatiamento_pulando_letras = string_2[0:6:2] # de 0 a 6 pulando de 2 em 2
ultima_letra = string_2[-1]
string_ao_contrario = string_2[::-1]

print(caixa_alta)
print(caixa_baixa)
print(primeira_letra)
print(fatiamento)
print(fatiamento_2)
print(indo_até_o_final)
print(fatiamento_pulando_letras)
print(ultima_letra)
print(string_ao_contrario)
```

<!-- ------------------------------------------------------------------------- -->

# Modulos e pacotes e importação

```py
"""
modulos sao os arquivos.py, e pacotes sao as pastas
"""

"""
todo pacote tem que ter um **init**.py
porque ele é o inicializador do pacote
"""
```

# funções (inicializados com def)

```py
def somar(a, b):
return a + b
```

<!-- Importaçoes absolutas e importaçoes relativas -->

# Absolutas é quando voce chama um modulo de outro pacote

```py
from operações_matematicas.soma import somar
from operações_matematicas.subtrair import subtrair

soma = somar(11, 22)
subtracao = subtrair(22, 11)

print(soma)
print(subtracao)
```

# Relativa é quando voce chama um modulo no mesmo pacote

```py
from .soma import somar

def subtrair(a, b):
    return a - b
```

<!-- ------------------------------------------------------------------------- -->

<!-- Controle de escopo -->

# Se voce criar algo dentro do pacote e nao quer que ele seja executado a nao ser que ele seja chamado, voce deve colocar dentro do pacote o seguinte

```py
def list_fundamentals():
    print("Fundamentos e listas")

# aqui voce ta restringindo o print de ser executado
# assim, somente se voce chamar pelo pacote, ele executará
if __name__ == "__main__":
    print("Modulo de list.py")

```
