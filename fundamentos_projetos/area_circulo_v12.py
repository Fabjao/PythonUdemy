from math import pi
import sys


def circulo(raio):
    return pi * (float(raio) ** 2)


def help():
    print("É necessário informar o raio do circulo.")
    print("Sintaxe: {0} <raio>".format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        print(circulo(raio))
