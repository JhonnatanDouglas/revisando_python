from handle_products.handle import save_product
from database import products


def main():
    # print(get_last_product())
    product = {"id": 11, "name": "tecla de teclado", "price": 50}
    print()
    print(products)
    print()
    print(save_product(product))
    print()
    print(products)


if __name__ == "__main__":
    main()
