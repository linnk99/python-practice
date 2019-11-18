# -*- coding: utf-8 -*-

def foreing_exchange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print("CALCULADORA DE DIVISAS")
    print("Convierte pesos mexicanos a pesos mexicanos")
    print('')

    ammount = float(input("Input the amount of MXN pesos to convert: "))

    result = foreing_exchange_calculator(ammount)

    print("${} mexican pesos are ${}".format(ammount, result))
    print('')

if __name__ == '__main__':
    run()