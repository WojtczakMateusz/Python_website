# Projekt: Klasyfikacja obrazów MNIST

## 1. Typ zadania
Zadaniem projektu jest klasyfikacja obrazów cyfr pisanych ręcznie (0–9)
z wykorzystaniem dwóch sieci neuronowych o różnej złożoności.

## 2. Zestaw danych
Wykorzystano zbiór MNIST zawierający 70 000 obrazów w skali szarości
o rozmiarze 28×28 pikseli.
- zbiór treningowy: 60 000
- zbiór testowy: 10 000
Dane podzielono na zbiory treningowe, walidacyjne i testowe.

## 3. Architektury i proces uczenia

| Model | Architektura | Epoki | Accuracy |
|-----|-------------|------|---------|
| Prosty CNN | Conv2D + Dense | 5 | ~98% |
| Zaawansowany CNN | Conv2D + Augmentacja | 10 | ~99% |

Zastosowano optymalizator Adam oraz funkcję straty
sparse_categorical_crossentropy.

## 4. Wnioski
Model zaawansowany osiągnął lepszą dokładność kosztem dłuższego
czasu uczenia. Augmentacja danych poprawiła odporność sieci
na zniekształcenia obrazów.
