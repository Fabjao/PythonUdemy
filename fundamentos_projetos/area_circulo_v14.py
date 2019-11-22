from math import pi
import sys
import errno


def circulo(raio):
    return pi * (float(raio) ** 2)


def help():
    print("É necessário informar o raio do circulo.")
    print("Sintaxe: {0} <raio>".format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print('O raio de ser um valor númerico')
        sys.exit(errno.EINVAL)

        raio = sys.argv[1]
        print(circulo(raio))
