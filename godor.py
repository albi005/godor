from distutils.file_util import write_file

class Melyseg:
    def __init__(self, index, melyseg) -> None:
        self.index = index
        self.melyseg = melyseg

file = open("melyseg.txt", "r")
lines = file.readlines()

melysegek = []
for line in lines:
    melysegek.append(int(line))

print("1. feladat:")
print(f"A fájl adatainak száma: {len(melysegek)}")

print("2. feladat")
index = int(input("Adjon meg egy távolságértéket! ")) - 1
print(f"Ezen a helyen a felszín {melysegek[index]} méter mélyen van.")

print("3. feladat")
erintetlen = sum(1 for x in melysegek if x == 0)
arany = erintetlen / len(melysegek)
print(f"Az érintetlen terület aránya: {arany * 100:.2f}%")

godrok: list[list[Melyseg]] = []
index_to_godor: dict[int, list[Melyseg]] = {}
i = 0
while True:
    while i < len(melysegek) and melysegek[i] == 0:
        i += 1
    if (i == len(melysegek)):
        break
    godrok.append([])
    while melysegek[i] != 0:
        godrok[-1].append(Melyseg(i, melysegek[i]))
        index_to_godor[i] = godrok[-1]
        i += 1
write_file("godrok.txt", (" ".join(str(melyseg.melyseg) for melyseg in godor) for godor in godrok))

print("5. feladat")
print(f"A gödrök száma: {len(godrok)}")

print("6. feladat")
if melysegek[index] == 0:
    print("Az adott helyen nincs gödör.")
else:
    print("a)")
    godor = index_to_godor[index]
    print(f"A gödör kezdete: {godor[0].index + 1} méter, a gödör vége: {godor[-1].index + 1} méter.")

    print("b)")
    legmelyebb = max(godor, key=lambda melyseg: melyseg.melyseg)
    legmelyebb_index = legmelyebb.index
    szmcs = sorted(godor[:legmelyebb_index], key=lambda melyseg: melyseg.melyseg) == godor[:legmelyebb_index]
    szmn = sorted(godor[legmelyebb_index:], key=lambda melyseg: melyseg.melyseg, reverse=True) == godor[legmelyebb_index:]
    if szmcs and szmn:
        print("Folyamatosan mélyül.")
    else:
        print("Nem mélyül folyamatosan.")

    print("c)")
    print(f"A legnagyobb mélysége {legmelyebb.melyseg} méter.")

    print("d)")
    print(f"A térfogata {sum(melyseg.melyseg for melyseg in godor) * 10} m^3.")

    print("e)")
    print(f"A vízmennyiség {(sum(melyseg.melyseg for melyseg in godor) - len(godor))* 10} m^3.")