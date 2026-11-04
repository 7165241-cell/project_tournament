

def menu():
    print("""========== TOURNAMENT MANAGER ==========
    Choose an option:
    1. Add team
    2. Show all teams
    3. Add match result
    4. Show standings
    5. Show leading team
    6. Show best attacking team
    7. Show team success rate
    8. Show teams without wins
    9. Show tournament summary
    10. Check championship potential
    0. Exit
""")




def enter_user():
    while True:
        menu_user=(input("enter a menu 1-10 :"))
        try:
            numbers = int(menu_user)
            if numbers >11 or numbers <0:
                raise ValueError
            return numbers
        except ValueError:
            print("Invalid input please enter only number between 1-10: ") 
            

group_names=[]
def add_team(name):
    
    while True:
        names=input("enter the group name :")  
        try:
            name=str(names)
            if name  not in group_names:
                group_names.append (name)
            else:
                print("please enter a name group ")
                continue
            return group_names
        except ValueError:
            print("eroor please enter a txt")






def  all_teams():
    print("")

def Add_match_result():
    print("")

def show_standings():
    print("")

def show_leading_team():
    print("")

def show_best_attacking_team():
    print("")
def show_team_success_rate():
    print("")

def show_teams_without_wins():
    print("")

def Show_tournament_summary():
    print("")                                                        

def Check_championship_potential():
    print("")

def exit():
    print("")




 
while True:
    menu()
    user_choice = enter_user()
    
    if user_choice == 1:
        add_team(group_names)

    elif user_choice == 2:
        all_teams()

    elif user_choice == 3:
        Add_match_result()

    elif user_choice == 4:
        show_standings()

    elif user_choice == 5:
        show_leading_team()

    elif user_choice == 6:
        show_best_attacking_team()

    elif user_choice == 7:
        show_team_success_rate()

    elif user_choice == 8:
        show_teams_without_wins()

    elif user_choice == 9:
        Show_tournament_summary()

    elif user_choice == 10:
        Check_championship_potential()

    elif user_choice == 0 :
        exit()

    break







