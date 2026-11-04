

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
            
groups = []

def group_name(groups):
    while True:
        try:
            group_is_name=str(input("enter the group name :"))
            raise ValueError
        except ValueError:
            print("Invalid input; please enter text.")
        is_exists = False
        for group in groups:
                if group["name"] == group_is_name:
                    is_exists = True
                    break
        if is_exists:
            print("this name already exists. please enter new name")
            continue
        else:
            return group_is_name
            

def group_id(groups):
    while True:
        try:
            group_id = int(input("Please enter group id: "))
            if group_id <= 0:
                raise ValueError
        except ValueError:
            print("Invalid input musrt be an integer positive.")
        is_exists = False
        for group in groups:
                if group["id"] == group_id:
                    is_exists = True
                    break
        if is_exists:
            print("id already exists")
            continue
        else:
            return group_id         
                

def insert_new_group(groups,g_id,g_name):
    new_group= {
    "id": 0, "name": "", "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
}
    new_group["id"] = g_id
    new_group["name"] = g_name
    groups.append(new_group)

    print("The group was added successfully")
    print(groups)
    return new_group
    




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
        id = group_id(groups)
        name = group_name(groups)
        insert_new_group(groups,id,name)
        

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








