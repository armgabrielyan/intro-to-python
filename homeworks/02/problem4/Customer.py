from Productcheck import check, products


def buy(product, num, price):
    if check(product, num):
        products[product] -= num

        print(f'You bought {product} and spent {num * price}')
    else:
        print(f'Sorry! We are out of "{product}".')


def main():
    buy('candy', 7, 500)
    buy('juice', 8, 800)
    buy('pen', 15, 200)
    buy('candy', 4, 1450)

if __name__ == '__main__':
    main()
