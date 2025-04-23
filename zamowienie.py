import pandas as pd


def pobierzZamowienie():
    
    print('Podaj dane zamówienia:\n')

    while True:
        try:
            dystans = float(input('Odległość (km): '))
            break
        except ValueError:
            print('Podana wartość musi być liczbą >= 0')

    while True:
        try:
            czas_p = int(input('Czas przygotowania (min): '))
            break
        except ValueError:
            print('Podana wartość musi być liczbą >= 0')

    while True:
        try:
            doswiadczenie = int(input('Doświadczenie kuriera (lata): '))
            break
        except ValueError:
            print('Podana wartość musi być liczbą >= 0')

    z = {
    'Distance_km': [dystans],
    'Preparation_Time_min': [czas_p],
    'Courier_Experience_yrs': [doswiadczenie],
    'Weather_Clear':[0],
    'Weather_Foggy':[0],
    'Weather_Rainy':[0],
    'Weather_Snowy':[0],
    'Weather_Windy':[0],
    'Traffic_Level_High':[0],
    'Traffic_Level_Low':[0],
    'Traffic_Level_Medium':[0],
    'Time_of_Day_Afternoon':[0],
    'Time_of_Day_Evening':[0],
    'Time_of_Day_Morning':[0],
    'Time_of_Day_Night':[0],
    'Vehicle_Type_Bike':[0],
    'Vehicle_Type_Car':[0],
    'Vehicle_Type_Scooter':[0],
    }

    while True:
        pogoda = input('Pogoda: clear/foggy/snowy/windy\n: ').capitalize()
        if f'Weather_{pogoda}' in z:
            z[f'Weather_{pogoda}'][0] = 1
            break
        else:
            print('Konieczne jest wpisanie jednej z ww. opcji')

    while True:
        ruch = input('Natężenie ruchu: low/medium/high\n: ').capitalize()
        if f'Traffic_Level_{ruch}' in z:
            z[f'Traffic_Level_{ruch}'][0] = 1
            break
        else:
            print('Konieczne jest wpisanie jednej z ww. opcji')

    while True:
        pora_dnia = input('Pora dnia: morning/afternoon/evening/night\n: ').capitalize()
        if f'Time_of_Day_{pora_dnia}' in z:
            z[f'Time_of_Day_{pora_dnia}'][0] = 1
            break
        else:
            print('Konieczne jest wpisanie jednej z ww. opcji')

    while True:
        pojazd = input('Pojazd dostawcy: bike/car/scooter\n: ').capitalize()
        if f'Vehicle_Type_{pojazd}' in z:
            z[f'Vehicle_Type_{pojazd}'][0] = 1
            break
        else:
            print('Konieczne jest wpisanie jednej z ww. opcji')

    df_z = pd.DataFrame(z)

    return df_z
