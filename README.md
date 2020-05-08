## pythonzadania-pitersikora

Do egzekucji programów należy używać interpretera Python w wersji 3.

1. 23_02_2020

    * Program do symulacji "Problemu Józefa Flawiusza" - w parametrach startowych programu należy podać liczbę rycerzy biorących udział w symulacji. `rycerze.py`

    * Program do symulacji "Problemu Wołów Newtona" - w parametrach startowych programu należy podać liczbę morgów pola dostępnego do wypasu oraz liczbę tygodni przez jaki odbywa się wypas. `woly_newtona.py`

    * Program testujący `rycerze.py` z wykorzystaniem modułu **pytest**:

    Instalacja modułu odbywa się z użyciem komendy bash'owej:

    ``` sh
    pip install --user -U pytest
    ```

    Egzekucja testów poprzez użycie komendy bash'owej:

    ```sh
    pytest rycerze_test.py
    ```


1. 01_03_2020

    * Program obliczający równanie liniowe oraz kwadratowe, wykonujący testy sprawdzające czy dany wynik jest prawidłowy `equation.py`

    * Zmienna opisujące dzień, miesiąc i rok. Mając dwie daty, wypisze która wystąpiła wcześniej `date.py`

1. 22_03_2020

    * Program do sprawdzania, czy liczba całkowita jest kwadratem innej liczby `square.py`

    * Program do sprawdzania, czy liczba całkowita jest liczbą pierwszą `prime_number.py`

    * Program wyznaczający dowolną liczbę Fibonacciego iteracyjnie `fibonacci.py`

    * Program wyznaczający dowolną liczbę Fibonacciego metodą potęgowania macierzy `fibo_matrix.py`

    * Program sortujący podaną listę liczb metodą bąbelkową `bubblesort.py`

    * Program sortujący podaną listę liczb metodą wstawiania `insertsort.py`

    * Program obliczający wyrażenie arytmetyczne podane w odwrotnej notacji polskiej `postfix.py`

1. Do programu Python World w wersji final dodaj nowe typy organizmów:

    * Antylopa: zachowuje się jak owca, z tym, że jeżeli w jej otoczeniu pojawi wilk, to ucieka od niego o dwa pola (kierunek odwrotny do występowania wilka), jeżeli ucieczka nie jest możliwa, atakuje wilka.
    * Żółw: posiada wolny metabolizm, zjada rośliny, może zatruć się grzybem, rozmnaża się rzadko i długo żyje, po zjedzeniu przez inne zwierze, znika na jedną turę ale jako niejadalny zostaje wypluty przez zjadającego w kolejnej turze i żyje sobie dalej.
    * Kosmita: porusza się po planszy i zatrzymuje czas na polach, które są wokół niego (odstęp 1), tj. mijające tury nie mają wpływu na organizmy wokół kosmity, kosmita nie zjada niczego ani nic nie zjada kosmity.
    * Dodaj funkcjonalność ochrona przyrody. Polega ona na tym, że świat stara się zachować zdrowe proporcje poszczególnych gatunków, promując ginące a utrudniając życie zbyt ekspansywnym. Ustalenie proporcji może być parametrem powstania świata.
    * Zaimplementować możliwość dodania po dowolnej turze dowolnego nowego organizmu na dowolne wolne pole.

    Zalecane jest zapoznanie się z komentarzami dodanymi do zmodyfikowanego kodu programu: [Link do commita](https://github.com/TBorzyszkowskiForEducation/pythonzadania-pitersikora/commit/8837d71fd7c02c5f73a36b225bcfd5bb611b382e).
