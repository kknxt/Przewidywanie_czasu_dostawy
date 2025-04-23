from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from math import sqrt, ceil


def przewiduj(df_z, rl, d, r, mse_rl, mse_d, mse_r):
    
    # przewidywanie czasu dostawy w oparciu o każdy z 3 modeli
    rl_p = rl.predict(df_z)
    d_p = d.predict(df_z)
    r_p = r.predict(df_z)

    e_rl = ceil(sqrt(mse_rl))
    e_d = ceil(sqrt(mse_d))
    e_r = ceil(sqrt(mse_r))

    print(f'Czas dostawy przewidywany przez model regresji liniowej: {ceil(rl_p[0])} +/- {e_rl} min')
    print(f'Czas dostawy przewidywany przez model drzewa regresyjnego: {ceil(d_p[0])} +/- {e_d} min')
    print(f'Czas dostawy przewidywany przez model Ridge: {ceil(r_p[0])} +/- {e_r} min')

def podzial(x, y):
    
    # podział 30% - zbiór testowy/70% - zbiór uczący 
    x_ucz, x_test, y_ucz, y_test = train_test_split(x, y, test_size = 0.3, random_state = 7)
    
    return x_ucz, x_test, y_ucz, y_test

def regLin(x_ucz, x_test, y_ucz, y_test):
    # tworzenie modelu regresji liniowej
    rl = LinearRegression()
    # uczenie modelu
    rl.fit(x_ucz, y_ucz)

    # predykcja na podstawie uczenia 
    y_przewidywane_rl = rl.predict(x_test)

    # błąd średniokwadratowy
    mse_rl = mean_squared_error(y_test, y_przewidywane_rl)

    return rl, mse_rl

def regTree(x_ucz, x_test, y_ucz, y_test):
    
    d = DecisionTreeRegressor(max_depth = 4)
    d.fit(x_ucz, y_ucz)
    y_przewidywane_d = d.predict(x_test)

    mse_d = mean_squared_error(y_test, y_przewidywane_d)

    return d, mse_d

def ridge(x_ucz, x_test, y_ucz, y_test):
    
    r = Ridge()
    r.fit(x_ucz, y_ucz)
    y_przewidywane_r = r.predict(x_test)

    mse_r = mean_squared_error(y_test, y_przewidywane_r)

    return r, mse_r


def wyswietlPre(x_ucz, x_test, mse_rl, mse_d, mse_r):

    print(f'Rozmiar zbioru uczącego (rozmiar, kolumny): {x_ucz.shape}\nRozmiar zbioru testowego: {x_test.shape}')

    print(f'Błąd średniokwadratowy dla modelu regresji liniowej: {mse_rl:.3f}')
    print(f'Błąd średniokwadratowy dla modelu drzewa regresyjnego: {mse_d:.3f}')
    print(f'Błąd średniokwadratowy dla modelu Ridge: {mse_r:.3f}\n')

