def func_args(*args: int) -> None:
    total = sum(args)
    print(args)
    print(total)


# atençao, voce podde pegar tudo com kwargs ou tirar algo
# tipo, tirar o id abaixo
def func_kwargs(id, **kwargs: dict) -> None:
    print(id, kwargs)
