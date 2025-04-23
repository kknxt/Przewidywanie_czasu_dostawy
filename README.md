# Przewidywanie czasu dostawy zamówienia z restauracji (Python: scikit-learn, pandas)
- Program w Pythonie, wykorzystujący bibliotekę scikit-learn do utworzenia modeli: regresji liniowej, drzewa regresyjnego, Ridge.
- Opcjonalnie wyświetla analizę eksploracyjną danych wykorzystanych do uczenia.
- Utworzony w celu porównania efektywności ww. modeli oraz stworzenia narzędzia szacującego czas dostawy.
- Program szacuje czas od złożenia zamówienia do ukończenia dostawy przez dostawcę.
## Zbiór danych i atrybuty uczenia
Modele uczą się na zbiorze danych udostępnionym w serwisie Kaggle: Food Delivery Time Prediction (https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction) (zawarty w folderze _dane_).  
Atrybuty uczenia maszynowego:
- odległość między restauracją a destynacją kuriera
- czas, przez który restauracja przygotowywała zamówienie
- staż dostawcy
- pogoda w trakcie dostawy
- natężenie ruchu drogowego w trakcie dostawy
- pora dnia
- rodzaj pojazdu dostawcy
## Wymagania do uruchomienia:
Dodatkowe zależności konieczne do działania programu znajdują się w pliku _requirements.txt_:
```
scikit-learn
pandas
matplotlib
seaborn
```
Konieczne również jest pobranie folderu _dane_.
## Tryby i opis działania
```
python main.py -h   
usage: main.py [-h] [-e] [-m]

options:
  -h, --help  show this help message and exit
  -e, --eda   wyświetl analizę eksploracyjną danych
  -m, --mse   wyświetl błędy średniokwadratowe modeli
```
Uruchomienie programu wymaga od użytkownika podania danych zamówienia.
#### Input zamówienia:
```
Podaj dane zamówienia:

Odległość (km): 5
Czas przygotowania (min): 20
Doświadczenie kuriera (lata): 2
Pogoda: clear/foggy/snowy/windy
: clear
Natężenie ruchu: low/medium/high
: medium
Pora dnia: morning/afternoon/evening/night
: evening
Pojazd dostawcy: bike/car/scooter
: bike
```
### Tylko przewidywanie czasu dostawy:
```
python main.py
```
#### Output:
```
Czas dostawy przewidywany przez model regresji liniowej: 45 +/- 11 min
Czas dostawy przewidywany przez model drzewa regresyjnego: 45 +/- 14 min
Czas dostawy przewidywany przez model Ridge: 45 +/- 11 min
````
### Wywołanie z opcjonalnymi flagami -e, -m
```
python main.py -e -m
```
### -e
-e, skrót od --eda (exploratory data analysis). Ta opcja wypisuje na stdout podstawowe statystyki opisowe oraz informacje o zbiorze danych.  
Dodatkowo, tworzy folder _wykresy_, w którym zapisuje wykresy w formacie .svg, wykorzystane do analizy eksploracyjnej danych.
#### Output: 
```
Head: 
   Order_ID  Distance_km Weather Traffic_Level Time_of_Day Vehicle_Type  \
0       522         7.93   Windy           Low   Afternoon      Scooter
1       738        16.42   Clear        Medium     Evening         Bike
2       741         9.52   Foggy           Low       Night      Scooter
3       661         7.44   Rainy        Medium   Afternoon      Scooter
4       412        19.03   Clear           Low     Morning         Bike

   Preparation_Time_min  Courier_Experience_yrs  Delivery_Time_min
0                    12                     1.0                 43
1                    20                     2.0                 84
2                    28                     1.0                 59
3                     5                     1.0                 37
4                    16                     5.0                 68

Liczba obiektow: 883
Liczba kategorii pogody: 5
Liczba kategorii natezenia ruchu: 3
Liczba kategorii pojazdow: 3
Liczba kategorii pory dnia: 4

Podstawowe statystyki opisowe:
       Distance_km  Preparation_Time_min  Courier_Experience_yrs  \
count   883.000000            883.000000              883.000000
mean     10.051586             17.019253                4.639864
std       5.688582              7.260201                2.922172
min       0.590000              5.000000                0.000000
25%       5.130000             11.000000                2.000000
50%      10.280000             17.000000                5.000000
75%      15.025000             23.000000                7.000000
max      19.990000             29.000000                9.000000

       Delivery_Time_min
count         883.000000
mean           56.425821
std            21.568482
min             8.000000
25%            41.000000
50%            55.000000
75%            71.000000
max           141.000000

Brakujace dane w kolumnach:
Distance_km                0
Weather                   30
Traffic_Level             30
Time_of_Day               30
Vehicle_Type               0
Preparation_Time_min       0
Courier_Experience_yrs    30
Delivery_Time_min          0
dtype: int64

Liczba obiektow: 883

Ramka z danymi kategorycznymi po przypisaniu im wartości boolean (liczbowych w kontekscie regresji):
   Distance_km  Preparation_Time_min  Courier_Experience_yrs  \
0         7.93                    12                     1.0
1        16.42                    20                     2.0
2         9.52                    28                     1.0
3         7.44                     5                     1.0
4        19.03                    16                     5.0

   Delivery_Time_min  Weather_Clear  Weather_Foggy  Weather_Rainy  \
0                 43          False          False          False
1                 84           True          False          False
2                 59          False           True          False
3                 37          False          False           True
4                 68           True          False          False

   Weather_Snowy  Weather_Windy  Traffic_Level_High  Traffic_Level_Low  \
0          False           True               False               True
1          False          False               False              False
2          False          False               False               True
3          False          False               False              False
4          False          False               False               True

   Traffic_Level_Medium  Time_of_Day_Afternoon  Time_of_Day_Evening  \
0                 False                   True                False
1                  True                  False                 True
2                 False                  False                False
3                  True                   True                False
4                 False                  False                False

   Time_of_Day_Morning  Time_of_Day_Night  Vehicle_Type_Bike  \
0                False              False              False
1                False              False               True
2                False               True              False
3                False              False              False
4                 True              False               True

   Vehicle_Type_Car  Vehicle_Type_Scooter
0             False                  True
1             False                 False
2             False                  True
3             False                  True
4             False                 False
...
Czas dostawy przewidywany przez model regresji liniowej: 45 +/- 11 min
Czas dostawy przewidywany przez model drzewa regresyjnego: 45 +/- 14 min
Czas dostawy przewidywany przez model Ridge: 45 +/- 11 min
```
#### Wykresy:
Wykresy znajdują się w folderze _wykresy_.
### -m
-m, skrót od --mse (mean squared error). Ta opcja wypisuje na stdout informacje o zbiorze uczącym i testowym, oraz błędy średniokwadratowe modeli uczenia.
#### Output:
```
Rozmiar zbioru uczącego (rozmiar, kolumny): (618, 18)
Rozmiar zbioru testowego: (265, 18)
Błąd średniokwadratowy dla modelu regresji liniowej: 120.340
Błąd średniokwadratowy dla modelu drzewa regresyjnego: 177.792
Błąd średniokwadratowy dla modelu Ridge: 120.380
...
Czas dostawy przewidywany przez model regresji liniowej: 45 +/- 11 min
Czas dostawy przewidywany przez model drzewa regresyjnego: 45 +/- 14 min
Czas dostawy przewidywany przez model Ridge: 45 +/- 11 min
```
