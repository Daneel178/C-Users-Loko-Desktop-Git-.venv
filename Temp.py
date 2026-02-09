def what_to_wear():
    temperature = float(input("Введите температуру: "))
    if temperature < 0:
        print("Пуховик")
    elif temperature < 20:
        print("Пальто")
    elif temperature < 30:
        is_rain = input("Есть осадки? (yes/no): ")
        if is_rain == "yes":
            is_strong_rain = input("Осадки сильные? (yes/no): ")
            if is_strong_rain == "yes":
                print("Пальто, резиновые сапоги и зонты")
            else:
                print("Пальто и дождевик")
        else:
            print("Футболку и шорты")
    else:
        print("Футболку и шорты")

what_to_wear()