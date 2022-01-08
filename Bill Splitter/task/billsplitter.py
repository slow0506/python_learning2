import random
guest_dict = {}
guest_num = int(input("Enter the number of friends joining (including you):\n"))
if guest_num <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:\n")

    for n in range(0, guest_num):
        guest_dict[input()] = 0

    total = int(input("Enter the total bill value:\n"))
    play = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")
    if play == "Yes":
        guest_list = list(guest_dict.keys())
        free = random.choice(guest_list)
        print(f"{free} is the lucky one!")
        split = total / (guest_num - 1)
        guest_dict = dict.fromkeys(guest_dict, round(split, 2))
        guest_dict[free] = 0
        print(guest_dict)

    else:
        print("No one is going to be lucky")
        split = total / guest_num
        guest_dict = dict.fromkeys(guest_dict, round(split, 2))
        print(guest_dict)