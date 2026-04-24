print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
bidders_list = {}
condition =  True
winner = 0
winner_name = "Not decided"
while condition:
    name = input("What is your name?\n").lower()
    bid_value = int(input("What is your bid amount?:\n"))
    more = input("Are there any more bidders?\n").lower()
    bidders_list[name] = bid_value
    if more == "yes":
        condition = True
    elif more == "no":
        for name in bidders_list:
            if bidders_list[name] > winner:
                winner = bidders_list[name]
                winner_name = name
        print("The bid has ended!")
        print(f"The winner is {winner_name} and the bid amount is {winner}")
        condition = False
    else:
        print("Try again")