bagalar = []
y = 0
z = 0

while True:
    x = input("Бағаны енгізіңіз (Болсан 'stop' деп жаз): ")

    if x.lower() == "stop":
        break
    elif not x.isdigit():
        print("Тек сандар енгізіңіз!")
        continue

    grade = int(x)
    y += grade
    bagalar.append(grade)
    z += 1

    current_average = y / z
    print("\nБағалар массиві:", bagalar)
    print("Бағалар қосындысы:", y)
    print("Массив ішіндегі саны:", z)
    print("Ағымдағы орташа мән:", round(current_average, 2))

if z > 0:
    module1 = float(input("\n1-модульдің орташа бағасын енгізіңіз: "))
    module2 = float(input("2-модульдің орташа бағасын енгізіңіз: "))
    exam = float(input("Емтихан бағасын енгізіңіз: "))