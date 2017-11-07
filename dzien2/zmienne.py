imie = "Joanna"
nazwisko = "Kowalska"
wiek = 34

# print(imie)
#
# print(imie[3:5])
#
# # print(3+7)
# #
# # print(3==5)

# print(imie.lower())
# print(imie.count('a'))

print(imie + '' + nazwisko + 'ma' + str(wiek) + 'lata.')

print(f"{imie} {nazwisko} ma {wiek} lata.")

# w starszej wersji niż python3.6 będzie:
print("{0} {1} ma {2} lata.".format(imie, nazwisko, wiek))

