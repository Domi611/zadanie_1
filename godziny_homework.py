#Napisz skrypt pomagający oszacować ile godzin potrzeba na pobranie danych z sieci o rozmiarze 13 TB, jeżeli wiesz,
# że plik o rozmiarze 194 MB udało się pobrać w 5 sekund. Wynik zaokrąglij do pełnych godzin.

a = 13 * 1024 * 1024 #zamiana 13 TB na MB
b = a / 194 #ile razy plik o rozmiarze 194 MB miesci sie w pliku 13 TB
c = b * (5 / 3600) #czas na pobranie pliku o rozmiarze 13 TB w godzinach
print("13 TB to", a, "MB")
print("Jeżeli plik o rozmiarze 194 MB pobrano w 5 sekund, to plik o rozmiarze", a, "MB zostanie pobrany w czasie", round(c), "godzin.")
