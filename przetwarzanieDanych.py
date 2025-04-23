import pandas as pd
from sklearn.model_selection import train_test_split


def run():
    
    # wczytanie pliku
    df = pd.read_csv('dane/Food_Delivery_Times.csv')

    # ramka bez kolumny order_id
    d0 = df.drop(columns = ['Order_ID'])

    d1 = d0.dropna()

    # kodowanie atrybutów kategorycznych na liczbowe
    d2 = pd.get_dummies(d1, columns = ['Weather', 'Traffic_Level', 'Time_of_Day', 'Vehicle_Type'])

    # wszystkie kolumny oprócz czasu dostawy
    x = d2.drop(columns = ['Delivery_Time_min'])
    # tylko kolumna czasu dostawy
    y = (d2['Delivery_Time_min']).to_frame()

    return df, d0, d1, d2, x, y
