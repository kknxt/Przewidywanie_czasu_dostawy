import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
import os


def wyswietlEda(df, d0, d1, d2):

    # folder do zapisu wykresów
    os.makedirs("wykresy", exist_ok=True)

    print("Head: ")
    pd.set_option('display.max_columns', None)
    display(df.head())
    print()

    # liczba obiektów
    print("Liczba obiektow:", d1.shape[0])

    # liczba kategorii w kolumnie Weather
    print("Liczba kategorii pogody:", d1.groupby('Weather').ngroups)

    # liczba kategorii w kolumnie Traffic_Level
    print("Liczba kategorii natezenia ruchu:", d1.groupby('Traffic_Level').ngroups)

    # liczba kategorii w kolumnie Vehicle_Type
    print("Liczba kategorii pojazdow:", d1.groupby('Vehicle_Type').ngroups)

    # liczba kategorii w kolumnie Time_of_Day
    print("Liczba kategorii pory dnia:", d1.groupby('Time_of_Day').ngroups, '\n')

    # wypisanie statystyk opisowych dla ramki danych bez order_id 
    print("Podstawowe statystyki opisowe:")
    print(d1.describe())
    print()

    # sprawdzenie liczby brakujacych danych
    print("Brakujace dane w kolumnach:")
    print(d0.isnull().sum())
    print()

    # usuniecie obiektow z brakujacymi danymi
    d1 = d0.dropna()

    # liczba obiektow po usunieciu brakow
    print("Liczba obiektow:", d1.shape[0])
    print()

    print("Ramka z danymi kategorycznymi po przypisaniu im wartości boolean (liczbowych w kontekscie regresji): ")
    display(d2.head())
    print()

    # wydzielenie kolumn zawierających atrybuty liczbowe
    atrNum = ['Delivery_Time_min', 'Distance_km', 'Preparation_Time_min', 'Courier_Experience_yrs']

    # boxploty atrybutów liczbowych
    f, axes = plt.subplots(1, len(atrNum), figsize = (20, 6))
    for i, atrybut in enumerate(atrNum):
        sns.boxplot(y = d1[atrybut], ax = axes[i])
    plt.tight_layout()
    plt.savefig('wykresy/pudelkoweNum.svg')
    plt.close()

    # wydzielenie kolumn zawierających atrybuty kategoryczne
    atrKat = ['Weather', 'Traffic_Level', 'Time_of_Day', 'Vehicle_Type']

    # boxploty zmiennośći czasu dostawy w zależności od poszczególnego atrybutu kategorycznego
    f, axes = plt.subplots(2, 2, figsize = (16, 10))
    axes = axes.flatten()
    for i, atrybut in enumerate(atrKat):
        sns.boxplot(d1, x = atrybut, y = 'Delivery_Time_min', hue = atrybut, ax = axes[i])
        axes[i].set_title(f"Delivery Time i {atrybut}")
    plt.tight_layout()
    plt.savefig("wykresy/pudelkoweTvsKat.svg")
    plt.close()

    # atrNum bez czasu dostawy
    atrNum = ['Distance_km', 'Preparation_Time_min', 'Courier_Experience_yrs']

    # wykresy zależności czasu dostawy od innych atrybutów liczbowych
    f, axes = plt.subplots(1, len(atrNum), figsize=(16, 6))
    for i, atrybut in enumerate(atrNum):
        sns.regplot(data = d1, x = atrybut, y = 'Delivery_Time_min', ax = axes[i], scatter = True, line_kws = {'color': 'red'})
        axes[i].set_title(f"Delivery Time i {atrybut}")
    plt.tight_layout()
    plt.savefig("wykresy/zaleznoscTvsNum.svg")
    plt.close()

    # wszystkie atrybuty liczbowe
    atrNum += ['Delivery_Time_min']

    # wykresy dystrybucji atrybutów liczbowych
    f, axes = plt.subplots(1, len(atrNum), figsize=(16, 6))
    for i, atrybut in enumerate(atrNum):
        if atrybut == 'Distance_km':
            axes[i].set_xlim(0, 21)
        if atrybut == 'Preparation_Time_min':
            axes[i].set_xlim(4, 30)
        if atrybut == 'Courier_Experience_yrs':
            axes[i].set_xlim(0, 9)
        sns.histplot(d1[atrybut], bins = 20, edgecolor = 'white', kde = True, kde_kws = dict(cut = 3), ax = axes[i])
        axes[i].set_title(f"Rozkład atrybutu {atrybut}", fontsize = 12)
    plt.tight_layout()
    plt.savefig("wykresy/dystrybucjeNum.svg")
    plt.close()

    # macierz korelacji atrybutów liczbowych
    plt.figure(figsize = (10, 8))
    macierzKorelacji = d1[['Delivery_Time_min', 'Distance_km', 'Preparation_Time_min', 'Courier_Experience_yrs']].corr()
    sns.heatmap(macierzKorelacji, annot = True)
    plt.tight_layout()
    plt.title('Macierz korelacji')
    plt.savefig("wykresy/korelacja.svg")
    plt.close()

