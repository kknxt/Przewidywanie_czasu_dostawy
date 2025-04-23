import argparse
import sys
import eda
import przetwarzanieDanych
import model
import zamowienie


def main(arguments):
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--eda', action='store_true', help='wyświetl analizę eksploracyjną danych')
    parser.add_argument('-m', '--mse', action='store_true', help='wyświetl błędy średniokwadratowe modeli')
    args = parser.parse_args(arguments[1:])

    df, d0, d1, d2, x, y = przetwarzanieDanych.run()

    if args.eda:
        eda.wyswietlEda(df, d0, d1, d2)

    x_ucz, x_test, y_ucz, y_test = model.podzial(x, y)
    rl, mse_rl = model.regLin(x_ucz, x_test, y_ucz, y_test)
    d, mse_d = model.regTree(x_ucz, x_test, y_ucz, y_test)
    r, mse_r = model.ridge(x_ucz, x_test, y_ucz, y_test)

    if args.mse:
        model.wyswietlPre(x_ucz, x_test, mse_rl, mse_d, mse_r)

    df_z = zamowienie.pobierzZamowienie()

    model.przewiduj(df_z, rl, d, r, mse_rl, mse_d, mse_r)


if __name__ == "__main__":
    main(sys.argv)