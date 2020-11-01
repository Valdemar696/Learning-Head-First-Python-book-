word = "бутылок"
for beer_num in range (30, 0, -1):
    print(beer_num, word, "пива на стене.")
    print(beer_num, word, "пива.")
    print("Возьми одну.")
    print("Пусти по кругу.")
    if beer_num == 1:
        print("Бутылки с пивом закончились.")
    else:
        new_num = beer_num - 1
        if new_num % 10 == 1:
            word = "бутылка"
        elif new_num % 10 in (2, 3, 4):
            word = "бутылки"
        else:
            word = "бутылок"
        print(new_num, word, "пива на стене.")
    print()