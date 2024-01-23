import pyautogui
import time
import math

# Funkcja do uzyskania aktualnej pozycji kursora
def pobierz_pozycje_startowa():
    print("Umieść kursor myszy w miejscu startowym.")
    time.sleep(5)  # Poczekaj 5 sekund, aby użytkownik miał czas umieścić kursor myszy
    pozycja = pyautogui.position()
    print("Pozycja startowa ustawiona na:", pozycja)
    return pozycja

# Nowy promień koła (zmień na dowolną inną wartość)
promien_kola = 150

# Zwiększona liczba punktów na okręgu
liczba_punktow = 18

# Skrócony czas trwania ruchu
czas_trwania_ruchu = 0.000000000001

# Funkcja do rysowania większego koła w Paint jednym płynnym ruchem
def rysuj_kolo(startowa_pozycja):
    # Przesuń kursor do punktu początkowego koła
    x_start = startowa_pozycja[0] + promien_kola
    y_start = startowa_pozycja[1]
    pyautogui.moveTo(x_start, y_start, duration=1)
    
    # Wciśnij lewy przycisk myszy na początku
    pyautogui.mouseDown()

    # Narysuj koło w jednym płynnym ruchu
    for i in range(liczba_punktow + 1):
        kat = i * (360 / liczba_punktow)
        x = startowa_pozycja[0] + promien_kola * math.cos(math.radians(kat))
        y = startowa_pozycja[1] - promien_kola * math.sin(math.radians(kat))
        pyautogui.moveTo(x, y, duration=czas_trwania_ruchu / liczba_punktow)

    # Puść lewy przycisk myszy na końcu
    pyautogui.mouseUp()

# Uzyskaj aktualną pozycję kursora jako startową
startowa_pozycja = pobierz_pozycje_startowa()

# Otwórz Paint przed uruchomieniem tego kodu

# Wywołanie funkcji
rysuj_kolo(startowa_pozycja)
