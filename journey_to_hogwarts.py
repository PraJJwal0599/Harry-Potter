descriptions = {
    "diagon alley": "A cobblestoned shopping area for the wizarding world.",
    "gringotts bank": "A bank run by the GOBLINS. Clever as they come, goblins, but not the most friendly of beasts.",
    "flourish and blotts": "Enchanted shelves teeming with magical tomes at the premier book emporium of the wizarding world.",
    "quality quidditch supplies": "where brooms soar and seekers score!",
    "ollivanders": "Wands of wonder await at Ollivanders:Makers of Fine Wands - where every wizard finds their perfect match!"

}

paths = {
    "diagon alley": ["flourish and blotts", "gringotts bank"],
    "gringotts bank": ["flourish and blotts", "diagon alley"],
    "flourish and blotts": ["quality quidditch supplies", "diagon alley"],
    "quality quidditch supplies": ["flourish and blotts", "ollivanders"],
    "ollivanders": ["hogwarts"]
}
current_loc = "diagon alley"
money = False
print( "We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry.\nPlease ensure that atmost attention to be made to the list of requirements attached here with it.\nYour task is to get all the items from the list for Hogwarts.\nWelcome to Diagon Alley.")

while current_loc != "hogwarts":
    print(descriptions[current_loc])
    print(f'You can go to these two locations:{paths[current_loc]}')
    next_loc = input("Which shop do you want to go next? ") .lower()
    
    if current_loc == "diagon alley":
        if next_loc == "flourish and blotts" or next_loc == "gringotts bank":
            current_loc = next_loc
        else:
            print("You cannot leave for Hogwarts without all the iteams from the list.")
    elif current_loc == "flourish and blotts":
        if not money:
            print("You will need money to buy books. Vist Bank.")
            if next_loc == "quality quidditch supplies" or "diagon alley":
              current_loc == next_loc
             
            else:
              print("You cannot leave for Hogwarts without all the iteams from the list.")
    elif current_loc == "gringotts bank":
        if next_loc == "flourish and blotts" or next_loc == "diagon alley":
            current_loc = next_loc
        else:
            print("You cannot leave for Hogwarts without all the iteams from the list.")
            print("You can get money from the bank but for money they will ask you a question.")
            bank_save = input("To get the money answer the question. How many horcruxes are there in Harry Potter? (7/8): ")
            if  bank_save == "8":
                money = True
                print("You have the money to purchase items.")
            else:
                print("You failed to give the correct answer.Please try again.")
    elif current_loc == "quality quidditch supplies":
        if next_loc == "ollivanders" or next_loc == "diagon alley":
            current_loc == next_loc
        else:
            print("You cannot leave for Hogwarts without all the iteams from the list.")
    elif current_loc == "ollivanders":
        if next_loc == "hogwarts":
            current_loc == next_loc
        else:
            print("You cannot leave for Hogwarts without all the iteams from the list.")

print("Congratulations you have all the iteams.\n Have a wonderful wizarding future ahead.")

print("new change: you are learning the basics.")