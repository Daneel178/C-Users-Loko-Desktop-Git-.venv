def what_to_wear():
    temperature = input("Температура выше 20 градусов и меньше 30? (yes/no): ")
    if temperature == "yes":
        is_rain = input("Есть осадки? (yes/no): ")
        if is_rain == "no":
            print("Футболку и шорты")
        else:
            print("Футболку, шорты, дождевик")
    else:
        temperature = input("Температура выше 0 градусов? (yes/no): ")
        if temperature == "no":
            print("Пуховик")
        else:
            is_rain = input("Есть осадки? (yes/no): ")
            if is_rain == "no":
                print("Пальто")
            else:
                is_strong_rain = input("Осадки сильные? (yes/no): ")
                if is_strong_rain == "no":
                    print("Пальто и дождевик")
                else:
                    print("Пальто, резиновые сапоги и зонт")

what_to_wear()