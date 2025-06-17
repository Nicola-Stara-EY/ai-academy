import pytest
from G1E4_Nicola_Stara import calcola_valori, tutti_positivi, calcola_totale

def test_calcola_valori():
    # Test con input validi
    lista_x = [5, 12, 8, 15]
    lista_y = [6, 4, 7, 2]
    incremento = 10
    expected = [0, 26, 23, 27]
    assert calcola_valori(lista_x, lista_y, incremento) == expected

    # Test con input vuoti
    assert calcola_valori([], [], 10) == []

    # Test con valori limite
    lista_x = [11, 10]
    lista_y = [6, 5]
    incremento = 5
    expected = [22, 25]
    assert calcola_valori(lista_x, lista_y, incremento) == expected

def test_tutti_positivi():
    # Test con tutti valori positivi
    assert tutti_positivi(1, 2, 3, 4) is True

    # Test con un valore negativo
    assert tutti_positivi(1, -2, 3, 4) is False

    # Test con zero
    assert tutti_positivi(0, 1, 2) is False

def test_calcola_totale():
    # Test con valori misti
    lista = [10, -5, 20, -10]
    assert calcola_totale(lista) == 35

    # Test con tutti valori positivi
    lista = [10, 20, 30]
    assert calcola_totale(lista) == 60

    # Test con tutti valori negativi
    lista = [-10, -20, -30]
    assert calcola_totale(lista) == -60

    # Test con lista vuota
    assert calcola_totale([]) == 0