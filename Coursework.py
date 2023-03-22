import pandas as pd

# function for team 1 inning 1
def team1_inning1():
    count = 1
    total = 0
    total_team = 0
    dff9 = pd.read_csv(team1 + '.csv')
    # Assigning the name column of team1 to a list
    t_name1 = dff9['Name'].tolist()
    dff10 = pd.read_csv(team2 + '.csv')
    # Assigning the ballers column of team2 to a list
    b_name2 = dff10['Ballers'].tolist()

    # random runs generation
    for p in range(11):
        bat = ['out', '1', '2', '3', '4', '5', '6']
        runs = 0
        while runs != 'out':
            count = count + 1
            runs_dev = rd.choice(bat)
            if runs_dev == 'out':
                break
            else:
                runs = runs_dev
            total = total + int(runs)
            if count > 119:
                break

        # random ballers generation
        baller = rd.choice(b_name2)
        while baller == "-":
            baller = rd.choice(b_name2)
        for x in range(5):
            if dff10.loc[x, 'Ballers'] == baller:
                # Updating the wicket column in the csv file
                wicket = dff10.loc[x, 'Wickets']
                wicket += 1
                dff10.loc[x, 'Wickets'] = wicket
                dff10.to_csv(team2 + '.csv', index=False)
        print('       WICKET!!!!       ')
        # printing the name of the baller and name of the batsman related to the wicket
        print(baller,'to',t_name1[p], 'is out!')
        print(t_name1[p], 'is scored', total, 'runs')
        print('Balls','=',count)
        total_team = total_team + total

        for x in range(11):
            if dff9.loc[x, 'Name'] == t_name1[p]:
                dff9.loc[x, 'Runs'] = total
                dff9.to_csv(team1 + '.csv', index=False)

        total = 0
        if count > 119:
            break
    print('Total runs', '=', total_team)
    return total_team

# function for team2 inning 1
def team2_inning1():
    count = 1
    total = 0
    total_team = 0
    dff9 = pd.read_csv(team2 + '.csv')
    # Assigning the name column of team2 to a list
    t_name2 = dff9['Name'].tolist()
    dff10 = pd.read_csv(team1 + '.csv')
    # Assigning the ballers column of team1 to a list
    b_name2 = dff10['Ballers'].tolist()

    # random runs generation
    for p in range(11):
        bat = ['out', '1', '2', '3', '4', '5', '6']
        runs = 0
        while runs != 'out':
            count = count + 1
            runs_dev = rd.choice(bat)
            if runs_dev == 'out':
                break
            else:
                runs = runs_dev
            total = total + int(runs)
            if count > 119:
                break

        # random ballers generation
        baller = rd.choice(b_name2)
        while baller == "-":
            baller = rd.choice(b_name2)
        for x in range(5):
            if dff10.loc[x, 'Ballers'] == baller:
                # Updating the wicket column in the csv file
                wicket = int(dff10.loc[x, 'Wickets'])
                wicket += 1
                dff10.loc[x, 'Wickets'] = wicket
                dff10.to_csv(team1 + '.csv', index=False)
        print('       WICKET!!!!       ')
        # printing the name of the baller and name of the batsman related to the wicket
        print(baller, 'to', t_name2[p], 'is out!')
        print(t_name2[p], 'is scored', total, 'runs')
        print('Balls', '=', count)
        total_team = total_team + total

        for x in range(11):
            if dff9.loc[x, 'Name'] == t_name2[p]:
                dff9.loc[x, 'Runs'] = total
                dff9.to_csv(team2 + '.csv', index=False)

        total = 0
        if count > 119:
            break
    print('Total runs', '=', total_team)
    return total_team

# function for team1 inning 2
def team1_inning2(inning_1):
    count = 1
    total = 0
    total_team = 0
    dff9 = pd.read_csv(team1 + '.csv')
    # Assigning the name column of team1 to a list
    t_name1 = dff9['Name'].tolist()
    dff10 = pd.read_csv(team2 + '.csv')
    # Assigning the ballers column of team2 to a list
    b_name2 = dff10['Ballers'].tolist()

    # random runs generation
    for p in range(11):
        bat = ['out', '1', '2', '3', '4', '5', '6']
        runs = 0
        while runs != 'out':
            count = count + 1
            runs_dev = rd.choice(bat)
            if runs_dev == 'out':
                break
            else:
                runs = runs_dev
            total = total + int(runs)
            total_team = total_team + int(runs)
            # checking the total of runs in inning 2 with the total of runs in inning 1
            if total_team > inning_1:
                baller = rd.choice(b_name2)
                while baller == "-":
                    baller = rd.choice(b_name2)
                for x in range(5):
                    if dff10.loc[x, 'Ballers'] == baller:
                        # Updating the wicket column in the csv file
                        wicket = dff10.loc[x, 'Wickets']
                        wicket += 1
                        dff10.loc[x, 'Wickets'] = wicket
                        dff10.to_csv(team2 + '.csv', index=False)

                for x in range(11):
                    if dff9.loc[x, 'Name'] == t_name1[p]:
                        dff9.loc[x, 'Runs'] = total
                        dff9.to_csv(team1 + '.csv', index=False)

                print('       WICKET!!!!       ')
                # printing the name of the baller and name of the batsman related to the wicket
                print(baller, 'to', t_name1[p], 'is out!')
                print(t_name1[p], 'is scored', total, 'runs')
                print('Balls', '=', count)

                print()
                print('Total runs', '=', total_team)
                print()
                print()
                # Displaying the winner team of the match
                print('------Congratulations!!!------')
                print()
                print(team1,'won the match!!')

                dff9["total"] = total_team
                dff9.to_csv(team1 + '.csv', index=False)

                return total_team
            if count > 119:
                break

        baller = rd.choice(b_name2)
        while baller == "-":
            baller = rd.choice(b_name2)
        for x in range(5):
            if dff10.loc[x, 'Ballers'] == baller:
                # Updating the wicket column in the csv file
                wicket = dff10.loc[x, 'Wickets']
                wicket += 1
                dff10.loc[x, 'Wickets'] = wicket
                dff10.to_csv(team2 + '.csv', index=False)
        print('       WICKET!!!!       ')
        # printing the name of the baller and name of the batsman related to the wicket
        print(baller, 'to', t_name1[p], 'is out!')
        print(t_name1[p], 'is scored', total, 'runs')

        for x in range(11):
            if dff9.loc[x, 'Name'] == t_name1[p]:
                dff9.loc[x, 'Runs'] = total
                dff9.to_csv(team1 + '.csv', index=False)

        total = 0
        if count > 119:
            break
    print('Total runs', '=', total_team)
    print()
    print()
    # Displaying the winner team of the match
    print('------Congratulations!!!------')
    print()
    print(team2, 'won the match!!')
    dff10["total"] = inning_1
    dff10.to_csv(team2 + '.csv', index=False)

# function for team2 inning 2
def team2_inning2(inning_1):
    count = 1
    total = 0
    total_team = 0
    dff9 = pd.read_csv(team2 + '.csv')
    # Assigning the name column of team2 to a list
    t_name2 = dff9['Name'].tolist()
    dff10 = pd.read_csv(team1 + '.csv')
    # Assigning the ballers column of team1 to a list
    b_name2 = dff10['Ballers'].tolist()

    # random runs generation
    for p in range(11):
        bat = ['out', '1', '2', '3', '4', '5', '6']
        runs = 0
        while runs != 'out':
            count = count + 1
            runs_dev = rd.choice(bat)
            if runs_dev == 'out':
                break
            else:
                runs = runs_dev
            total = total + int(runs)
            total_team = total_team + int(runs)
            # checking the total of runs in inning 2 with the total of runs in inning 1
            if total_team > inning_1:
                baller = rd.choice(b_name2)
                while baller == "-":
                    baller = rd.choice(b_name2)
                for x in range(5):
                    if dff10.loc[x, 'Ballers'] == baller:
                        # Updating the wicket column in the csv file
                        wicket = dff10.loc[x, 'Wickets']
                        wicket += 1
                        dff10.loc[x, 'Wickets'] = wicket
                        dff10.to_csv(team1 + '.csv', index=False)

                for x in range(11):
                    if dff9.loc[x, 'Name'] == t_name2[p]:
                        dff9.loc[x, 'Runs'] = total
                        dff9.to_csv(team2 + '.csv', index=False)

                print('       WICKET!!!!       ')
                # printing the name of the baller and name of the batsman related to the wicket
                print(baller, 'to', t_name2[p], 'is out!')
                print(t_name2[p], 'is scored', total, 'runs')
                print('Balls', '=', count)
                print()
                print('Total runs', '=', total_team)
                print()
                print()
                # Displaying the winner team of the match
                print('------Congratulations!!!------')
                print()
                print(team2, 'won the match!!')

                dff9["total"] = total_team
                dff9.to_csv(team2 + '.csv', index=False)

                return total_team
            if count > 119:
                break

        baller = rd.choice(b_name2)
        while baller == "-":
            baller = rd.choice(b_name2)
        for x in range(5):
            if dff10.loc[x, 'Ballers'] == baller:
                # Updating the wicket column in the csv file
                wicket = dff10.loc[x, 'Wickets']
                wicket += 1
                dff10.loc[x, 'Wickets'] = wicket
                dff10.to_csv(team1 + '.csv', index=False)
        print('       WICKET!!!!       ')
        # printing the name of the baller and name of the batsman related to the wicket
        print(baller, 'to', t_name2[p], 'is out!')
        print(t_name2[p], 'is scored', total, 'runs')

        for x in range(11):
            if dff9.loc[x, 'Name'] == t_name2[p]:
                dff9.loc[x, 'Runs'] = total
                dff9.to_csv(team2 + '.csv', index=False)

        total = 0
        if count > 119:
            break
    print('Total runs', '=', total_team)
    print()
    print()
    # Displaying the winner team of the match
    print('------Congratulations!!!------')
    print()
    print(team1, 'won the match!!')

    dff10["total"] = inning_1
    dff10.to_csv(team1 + '.csv', index=False)

# function to edit players or team information
def datafun():
    try:
        edit = input("Do you want to edit players' information:").lower()
        while edit == 'yes':
            country = input("What is the country you want to edit? ").lower()
            if country == 'srilanka':
                change=input("What do you want to change? ").lower()
                if change=='name':
                    name = input("What is the name of the player? ").title()
                    new_value=input("New information:").title()
                    for x in range(11):
                        if df1.loc[x, 'Name'] == name:
                            df1.loc[x, 'Name'] = new_value.title()
                            df1.to_csv('SriLanka.csv', index=False)
                            print(df1)
                            break
                elif change=='age':
                    name = input("What is the name of the player? ").title()
                    new_value=input("New information:")
                    for x in range(11):
                        if df1.loc[x, 'Name'] == name:
                            df1.loc[x, 'Age'] = new_value
                            df1.to_csv('SriLanka.csv', index=False)
                            print(df1)
                            break
                elif change=='ballers':
                    remove_value=input("What is the name you are going to delete:").title()
                    new_value = input("New information:").title()
                    for y in range(5):
                        if df1.loc[y, 'Ballers'] == remove_value:
                            df1.loc[y, 'Ballers'] = new_value
                            df1.to_csv('SriLanka.csv', index=False)
                            print(df1)
                            break
            elif country=='bangladesh':
                name=input("What is the name of the player? ").title()
                change=input("What do you want to change? ").lower()
                if change=='name':
                    new_value=input("New information:").title()
                    for x in range(11):
                        if df2.loc[x, 'Name'] == name:
                            df2.loc[x, 'Name'] = new_value.title()
                            df2.to_csv('Bangladesh.csv', index=False)
                            print(df2)
                            break
                elif change=='age':
                    new_value=input("New information:")
                    for x in range(11):
                        if df2.loc[x, 'Name'] == name:
                            df2.loc[x, 'Age'] = new_value
                            df2.to_csv('Bangladesh.csv', index=False)
                            print(df2)
                            break
                elif change=='ballers':
                    remove_value=input("What is the name you are going to delete:").title()
                    new_value = input("New information:").title()
                    for y in range(5):
                        if df1.loc[y, 'Ballers'] == remove_value:
                            df1.loc[y, 'Ballers'] = new_value
                            df1.to_csv('SriLanka.csv', index=False)
                            print(df1)
                            break
            elif country=='india':
                name=input("What is the name of the player? ").title()
                change=input("What do you want to change? ").lower()
                if change=='name':
                    new_value=input("New information:").title()
                    for x in range(11):
                        if df3.loc[x, 'Name'] == name:
                            df3.loc[x, 'Name'] = new_value.title()
                            df3.to_csv('India.csv', index=False)
                            print(df3)
                            break
                elif change=='age':
                    new_value=input("New information:")
                    for x in range(11):
                        if df3.loc[x, 'Name'] == name:
                            df3.loc[x, 'Age'] = new_value
                            df3.to_csv('India.csv', index=False)
                            print(df3)
                            break
                elif change=='ballers':
                    remove_value=input("What is the name you are going to delete:").title()
                    new_value = input("New information:").title()
                    for y in range(5):
                        if df1.loc[y, 'Ballers'] == remove_value:
                            df1.loc[y, 'Ballers'] = new_value
                            df1.to_csv('SriLanka.csv', index=False)
                            print(df1)
                            break
            elif country=='west indies':
                name=input("What is the name of the player? ").title()
                change=input("What do you want to change? ").lower()
                if change=='name':
                    new_value=input("New information:").title()
                    for x in range(11):
                        if df4.loc[x, 'Name'] == name:
                            df4.loc[x, 'Name'] = new_value.title()
                            df4.to_csv('WestIndies.csv', index=False)
                            print(df4)
                            break
                elif change=='age':
                    new_value=input("New information:")
                    for x in range(11):
                        if df4.loc[x, 'Name'] == name:
                            df4.loc[x, 'Age'] = new_value
                            df4.to_csv('WestIndies.csv', index=False)
                            print(df4)
                            break
                elif change=='ballers':
                    remove_value=input("What is the name you are going to delete:").title()
                    new_value = input("New information:").title()
                    for y in range(5):
                        if df1.loc[y, 'Ballers'] == remove_value:
                            df1.loc[y, 'Ballers'] = new_value
                            df1.to_csv('SriLanka.csv', index=False)
                            print(df1)
                            break
            elif country=='england':
                name=input("What is the name of the player? ").title()
                change=input("What do you want to change? ").lower()
                if change=='name':
                    new_value=input("New information:").title()
                    for x in range(11):
                        if df5.loc[x, 'Name'] == name:
                            df5.loc[x, 'Name'] = new_value.title()
                            df5.to_csv('England.csv', index=False)
                            print(df5)
                            break
                elif change=='age':
                    new_value=input("New information:")
                    for x in range(11):
                        if df5.loc[x, 'Name'] == name:
                            df5.loc[x, 'Age'] = new_value
                            df5.to_csv('England.csv', index=False)
                            print(df5)
                            break
                elif change=='ballers':
                    remove_value=input("What is the name you are going to delete:").title()
                    new_value = input("New information:").title()
                    for y in range(5):
                        if df1.loc[y, 'Ballers'] == remove_value:
                            df1.loc[y, 'Ballers'] = new_value
                            df1.to_csv('SriLanka.csv', index=False)
                            print(df1)
                            break
            elif country == 'newzealand':
                name = input("What is the name of the player? ").title()
                change = input("What do you want to change? ").lower()
                if change == 'name':
                    new_value = input("New information:").title()
                    for x in range(11):
                        if df6.loc[x, 'Name'] == name:
                            df6.loc[x, 'Name'] = new_value.title()
                            df6.to_csv('NewZealand.csv', index=False)
                            print(df6)
                            break
                elif change == 'age':
                    new_value = input("New information:")
                    for x in range(11):
                        if df6.loc[x, 'Name'] == name:
                            df6.loc[x, 'Age'] = new_value
                            df6.to_csv('NewZealand.csv', index=False)
                            print(df6)
                            break
                elif change=='ballers':
                    remove_value=input("What is the name you are going to delete:").title()
                    new_value = input("New information:").title()
                    for y in range(5):
                        if df1.loc[y, 'Ballers'] == remove_value:
                            df1.loc[y, 'Ballers'] = new_value
                            df1.to_csv('SriLanka.csv', index=False)
                            print(df1)
                            break
            elif country=='australia':
                name=input("What is the name of the player? ").title()
                change=input("What do you want to change? ").lower()
                if change=='name':
                    new_value=input("New information:").title()
                    for x in range(11):
                        if df7.loc[x, 'Name'] == name:
                            df7.loc[x, 'Name'] = new_value.title()
                            df7.to_csv('Australia.csv', index=False)
                            print(df7)
                            break
                elif change=='age':
                    new_value=input("New information:")
                    for x in range(11):
                        if df7.loc[x, 'Name'] == name:
                            df7.loc[x, 'Age'] = new_value
                            df7.to_csv('Australia.csv', index=False)
                            print(df7)
                            break
                elif change=='ballers':
                    remove_value=input("What is the name you are going to delete:").title()
                    new_value = input("New information:").title()
                    for y in range(5):
                        if df1.loc[y, 'Ballers'] == remove_value:
                            df1.loc[y, 'Ballers'] = new_value
                            df1.to_csv('SriLanka.csv', index=False)
                            print(df1)
                            break
            elif country=='south africa':
                name=input("What is the name of the player? ").title()
                change=input("What do you want to change? ").lower()
                if change=='name':
                    new_value=input("New information:").title()
                    for x in range(11):
                        if df8.loc[x, 'Name'] == name:
                            df8.loc[x, 'Name'] = new_value.title()
                            df8.to_csv('SouthAfrica.csv', index=False)
                            print(df8)
                            break
                elif change=='age':
                    new_value=input("New information:")
                    for x in range(11):
                        if df8.loc[x, 'Name'] == name:
                            df8.loc[x, 'Age'] = new_value
                            df8.to_csv('SouthAfrica.csv', index=False)
                            print(df8)
                            break
                elif change=='ballers':
                    remove_value=input("What is the name you are going to delete:").title()
                    new_value = input("New information:").title()
                    for y in range(5):
                        if df1.loc[y, 'Ballers'] == remove_value:
                            df1.loc[y, 'Ballers'] = new_value
                            df1.to_csv('SriLanka.csv', index=False)
                            print(df1)
                            break

            edit = input("Do you want to edit players' information again:").lower()
    except ValueError:
        print("Please enter a valid input!!")

# start of the match
print()
print('.....Welcome to Cricket T20 - 2021.....')
print()
print('There are 2 groups in this match')
print('These are the specific teams for each group...')
print()

# Displaying the player or team information
print('          GROUP 1          ')
print('..........SriLanka..........')
print()
df1 = pd.read_csv('SriLanka.csv')
print(df1)
print()
print('..........Bangladesh..........')
print()
df2 = pd.read_csv('Bangladesh.csv')
print(df2)
print()
print('..........India..........')
print()
df3 = pd.read_csv('India.csv')
print(df3)
print()
print('..........West Indies..........')
print()
df4 = pd.read_csv('WestIndies.csv')
print(df4)
print()
print()

print('          GROUP 2          ')
print('..........England..........')
print()
df5 = pd.read_csv('England.csv')
print(df5)
print()
print('..........New Zealand..........')
print()
df6 = pd.read_csv('NewZealand.csv')
print(df6)
print()
print('..........Australia..........')
print()
df7 = pd.read_csv('Australia.csv')
print(df7)
print()
print('..........South Africa..........')
print()
df8 = pd.read_csv('SouthAfrica.csv')
print(df8)
print()


datafun()
print()
print('Are you ready to start the match....')
print()
print("---- LET'S BEGIN----")

# random generation of 4 matches
import random as rd

group1=['SriLanka','Bangladesh','India','WestIndies']
group2=['England','NewZealand','Australia','SouthAfrica']
teams=['SriLanka','Bangladesh','India','WestIndies','England','NewZealand','Australia','SouthAfrica']

# adding a column called 'total' to the teams' csv files
for t in teams:
    dff20 = pd.read_csv(t + '.csv')
    dff20["total"] = 0
    dff20.to_csv(t + '.csv', index=False)

# 1st match
# randomly selecting the 2 teams for the match
team1=rd.choice(group1)
team2=rd.choice(group2)
print()
print('----------------1st Match------------------')
print()
print(team1,'vs',team2)
print()


# random match generation
def rdtoss():
    # randomly generating the toss
    toss = rd.randint(1,2)
    if toss == 1:
        print(team1, 'won the toss!')
        print()
        # randomly generating the state(bat or ball)
        play = rd.randint(1,2)
        if play == 1:
            print(team1,'is going to bat first!')
            print()
            print("-----LET'S START THE MATCH!-----")
            print()
            inning_1 = team1_inning1()
            print(inning_1)
            print()
            print(team2,'is going to bat now!')
            print()
            inning_2 = team2_inning2(inning_1)

        elif play == 2:
            print(team1, 'is going to ball first!')
            print()
            print(team2, 'will bat first!')
            print("-----LET'S START THE MATCH!-----")
            print()
            inning_1 = team2_inning1()
            print(inning_1)
            print()
            print(team1, 'is going to bat now!')
            team1_inning2(inning_1)

    elif toss==2:
        print(team2,'won the toss!')
        print()
        # randomly generating the state(bat or ball)
        play = rd.randint(1, 2)
        if play == 1:
            print(team2,'is going to bat first!')
            print()
            print("-----LET'S START THE MATCH!-----")
            print()
            inning_1 = team2_inning1()
            print(inning_1)
            print()
            print(team1, 'is going to bat now!')
            team1_inning2(inning_1)

        elif play == 2:
            print(team2,'is going to ball first!')
            print()
            print(team1,'will bat first!')
            print("-----LET'S START THE MATCH!-----")
            print()
            inning_1 = team1_inning1()
            print(inning_1)
            print()
            print(team2, 'is going to bat now!')
            team2_inning2(inning_1)


rdtoss()
print()
print()
# removing the played teams from the list
group1.remove(team1)
group2.remove(team2)

# 2nd match
# randomly selecting the 2 teams for the match
team1=rd.choice(group1)
team2=rd.choice(group2)
print()
print('----------------2nd Match-----------------')
print()
print(team1,'vs',team2)

rdtoss()
print()
print()
# removing the played teams from the list
group1.remove(team1)
group2.remove(team2)

# 3rd match
# randomly selecting the 2 teams for the match
team1=rd.choice(group1)
team2=rd.choice(group2)
print()
print('-----------------3rd Match----------------')
print()
print(team1,'vs',team2)

rdtoss()
print()
print()
# removing the played teams from the list
group1.remove(team1)
group2.remove(team2)

# 4th match
# randomly selecting the 2 teams for the match
team1=rd.choice(group1)
team2=rd.choice(group2)
print()
print('-----------------4th Match-----------------')
print()
print(team1,'vs',team2)

rdtoss()
print()
print()
# removing the played teams from the list
group1.remove(team1)
group2.remove(team2)

# Getting the top scored team
max_t = 0
name_c = ''
dff21 = ''
for t in teams:
    dff21 = pd.read_csv(t + '.csv')
    if dff21.loc[0, 'total'] > max_t:
        max_t = dff21.loc[0, 'total']
        name_c = t
    # deleting the column total after getting the maximum value
    dff21.pop('total')
    dff21.to_csv(t + '.csv', index=False)

# Displaying the summary (runs and wickets)
print()
print()
print()
print('T20 - Summary')
print('-------------')
print()
print('          GROUP 1          ')
print('..........SriLanka..........')
print()
df1 = pd.read_csv('SriLanka.csv')
print(df1)
print()
print('..........Bangladesh..........')
print()
df2 = pd.read_csv('Bangladesh.csv')
print(df2)
print()
print('..........India..........')
print()
df3 = pd.read_csv('India.csv')
print(df3)
print()
print('..........West Indies..........')
print()
df4 = pd.read_csv('WestIndies.csv')
print(df4)
print()
print()

print('          GROUP 2          ')
print('..........England..........')
print()
df5 = pd.read_csv('England.csv')
print(df5)
print()
print('..........New Zealand..........')
print()
df6 = pd.read_csv('NewZealand.csv')
print(df6)
print()
print('..........Australia..........')
print()
df7 = pd.read_csv('Australia.csv')
print(df7)
print()
print('..........South Africa..........')
print()
df8 = pd.read_csv('SouthAfrica.csv')
print(df8)
print()

# Displaying best performers
teams=['SriLanka','Bangladesh','India','WestIndies','England','NewZealand','Australia','SouthAfrica']

for t in teams:
    max_r = 0
    max_w = 0
    name_r=''
    name_w=''
    dff11 = pd.read_csv(t + '.csv')
    for x in range(11):
        if dff11.loc[x, 'Runs'] > max_r:
            max_r = dff11.loc[x, 'Runs']
            name_r = dff11.loc[x, 'Name']
    for x in range(5):
        if dff11.loc[x, 'Wickets'] > max_w:
            max_w = dff11.loc[x, 'Wickets']
            name_w = dff11.loc[x, 'Ballers']

    print()
    print("Best Performers")
    print('\t',t)
    print("\t","\t","Best Batsman is",name_r,"(Runs=",max_r,")")
    print("\t", "\t", "Best bowler is", name_w, "(Wickets=", max_w, ")")

# Displaying the best performing team of the tournament
print()
print("\t*****Best performing team*****")
print("\t**Champion of the tournament**")
print("\t\t",name_c,"(Runs=",max_t,")")
print()
print("\t Congratulations",name_c,"!!!!")

# Refreshing the columns 'wickets' and 'runs' before the next match
for t in teams:
    dff11 = pd.read_csv(t + '.csv')
    dff11["Wickets"] = 0
    dff11["Runs"] = 0
    dff11.to_csv(t + '.csv', index=False)
