# Napisz skrypt pozwalający zasymulować zyski z lokat bankowych przy
# następujących założeniach:
# • własne środki 30 tys. zł,
# • roczna lokata kapitału,
# • kwartalna kapitalizacja odsetek (saldo będzie aktualizowane co 3 miesiące),
# • oprocentowanie roczne dla 3 wariantów: 7,5%, 8% oraz 8,25%,
# • pokazać salda po każdym kwartale,
# • wyliczyć roczny zysk.

# dla kapitalizacji rocznej 7,5%
own_funds = 30_000.
interest = 1.075
interest_quarter = 1.0188
print("Dla  oprocentowania rocznego 7,5%, oprocentowanie jednego kwartału wynosi:", round(7.5 / 4, 2), "%")
print("Saldo końcowe po pierwszym kwartale wynosi:", round(own_funds*interest_quarter, 2), "zł")
print("Saldo końcowe po drugim kwartale wynosi:", round((own_funds*interest_quarter)*interest_quarter, 2), "zł")
print("Saldo końcowe po trzecim kwartale wynosi:", round(((own_funds*interest_quarter)*interest_quarter)*interest_quarter, 2), "zł")
print("Saldo końcowe po czwartym kwartale wynosi:", round((((own_funds*interest_quarter)*interest_quarter)*interest_quarter)*interest_quarter, 2), "zł")
print("Roczny zysk z lokaty wynosi", round(((((own_funds*interest_quarter)*interest_quarter)*interest_quarter)*interest_quarter)-own_funds, 2), "zł")
print()
# dla kapitalizacji rocznej 8%
own_funds = 30_000.
interest = 1.08
interest_quarter = 1.02
print("Dla  oprocentowania rocznego 8%, oprocentowanie jednego kwartału wynosi:", round(8 / 4, 2), "%")
print("Saldo końcowe po pierwszym kwartale wynosi:", round(own_funds*interest_quarter, 2), "zł")
print("Saldo końcowe po drugim kwartale wynosi:", round((own_funds*interest_quarter)*interest_quarter, 2), "zł")
print("Saldo końcowe po trzecim kwartale wynosi:", round(((own_funds*interest_quarter)*interest_quarter)*interest_quarter, 2), "zł")
print("Saldo końcowe po czwartym kwartale wynosi:", round((((own_funds*interest_quarter)*interest_quarter)*interest_quarter)*interest_quarter, 2), "zł")
print("Roczny zysk z lokaty wynosi", round(((((own_funds*interest_quarter)*interest_quarter)*interest_quarter)*interest_quarter)-own_funds, 2), "zł")
print()
# dla kapitalizacji rocznej 8%
own_funds = 30_000.
interest = 1.0825
interest_quarter = 1.0206
print("Dla  oprocentowania rocznego 8,25%, oprocentowanie jednego kwartału wynosi:", round(8.25 / 4, 2), "%")
print("Saldo końcowe po pierwszym kwartale wynosi:", round(own_funds*interest_quarter, 2), "zł")
print("Saldo końcowe po drugim kwartale wynosi:", round((own_funds*interest_quarter)*interest_quarter, 2), "zł")
print("Saldo końcowe po trzecim kwartale wynosi:", round(((own_funds*interest_quarter)*interest_quarter)*interest_quarter, 2), "zł")
print("Saldo końcowe po czwartym kwartale wynosi:", round((((own_funds*interest_quarter)*interest_quarter)*interest_quarter)*interest_quarter, 2), "zł")
print("Roczny zysk z lokaty wynosi", round(((((own_funds*interest_quarter)*interest_quarter)*interest_quarter)*interest_quarter)-own_funds, 2), "zł")

