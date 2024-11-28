bagalar = []
y = 0
z = 0

while True:
    x = input("Baga engiz (или введите 'stop', чтобы закончить): ")
    if x == "stop":
        break
    else:
        y += int(x)
        bagalar.append(int(x))
        z += 1
        print("\nBagalar masiby:", bagalar)
        print("Bagalar kosyndysi:", y)
        print("Massiv ishindegi san:", z)

if z > 0:
    orta = y / z
    print("\nBagalar ortasy:", orta)
else:
    print("\nMassiv !")
