from random import choice

Enter_counter = 0

while True:
    user_choice = input("Введіть 'stone', 'scissors' або 'paper': ")
    random_choice = choice(["stone", "scissors", "paper"])

    win_message = (f"Ви перемогли! Комп'ютер обрав '{random_choice}'")
    lose_message = (f"Ви програли! Комп'ютер обрав '{random_choice}'")
    draw_message = (f"Нічия! Комп'ютер обрав '{random_choice}'")

    match user_choice:
        case "stone":
            if random_choice == "scissors":
                print(win_message)
            elif random_choice == "paper":
                print(lose_message)
            else:
                print(draw_message)
        case "scissors":
            if random_choice == "paper":
                print(win_message)
            elif random_choice == "stone":
                print(lose_message)
            else:
                print(draw_message)
        case "paper":
            if random_choice == "stone":
                print(win_message)
            elif random_choice == "scissors":
                print(lose_message)
            else:
                print(draw_message)
        case "exit":
            print("Дякую за гру!")
            break
        case _:
            Enter_counter += 1
            print("Невідома дія")
            if Enter_counter == 3:
                print("Гру завершено!")
                break