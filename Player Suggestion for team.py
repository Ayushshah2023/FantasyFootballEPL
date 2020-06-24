import pandas as pd
import numpy as np
data=pd.read_csv('england-premier-league-players-2018-to-2019-stats.csv')
#print(data)
#print(list(data.columns))
data_we_need=data[["full_name","position","Current Club","appearances_overall","goals_overall","assists_overall","penalty_goals","penalty_misses", 'clean_sheets_overall','yellow_cards_overall', 'red_cards_overall','Total_Price']]
#print(data_we_need)

indexNames = pd.DataFrame()
#Running part of the code to be added at the start of the code
print("Welcome to the FPL Helper")
print("This will help you decide which player to keep in your team")
print("Please enter the Details of your team")
max_money_goalkeepers = 10
max_money_defenders = 26
max_mooney_midfielders = 42
max_money_forwards = 22
#This will leave a line
print("")
#this number should be between 3 to 5
total_team=[]

###################################################GOALKEEPERS###################################################

goalkeepers=data_we_need[data_we_need["position"]=="Goalkeeper"]
count_row = goalkeepers.shape[0]

def calculate_points(row):
    return ((row["appearances_overall"]*2)+(row["goals_overall"]*6)+(row["assists_overall"]*3)+(row["penalty_goals"]*5)+(row["penalty_misses"]*-2)+(row["clean_sheets_overall"]*4)+(row['yellow_cards_overall']*-1)+(row['red_cards_overall']*-2))

goalkeepers["Points"] = goalkeepers.apply(calculate_points,axis=1)
#print(goalkeepers)
goalkeeper=[]
no_of_goalkeepers=int(input("Enter the number of goalkeepers you want in your team:  "))
no_of_goalkeepers_selected=int(input("Enter the number of goalkeepers you have already added in your team:  "))
no_of_gk_comp_suggest=int(no_of_goalkeepers-no_of_goalkeepers_selected)
print("No of suggestions in goalkeepers needed are: "+str(no_of_gk_comp_suggest))
for i in range(0,no_of_goalkeepers_selected):
    temps_for_goalkeeper = str(input("Enter the player's name:  "))
    goalkeeper.append(temps_for_goalkeeper)
    indexNames = goalkeepers[goalkeepers['full_name'] == temps_for_goalkeeper ]
    temp_indexes = goalkeepers[goalkeepers['full_name'] == temps_for_goalkeeper ].index
    # Delete these row indexes from dataFrame
    goalkeepers.drop(temp_indexes , inplace=True)


#print(goalkeeper)
goalkeepers = goalkeepers.sort_values('Points',ascending=False)
selected_goalkeepers = goalkeepers.head(2)
#print(selected_goalkeepers)
#for i in range(no_of_gk_comp_suggest):
goalkeepers = goalkeepers.head(no_of_gk_comp_suggest)
    #df[df['A'] == 2]['B']
indexNames = indexNames.append(goalkeepers)
#print("Final Selected Goalkeepers")
#print(indexNames)

################################################### DEFENDERS ###################################################

defenders=data_we_need[data_we_need["position"]=="Defender"]
count_row = defenders.shape[0]

def calculate_points(row):
    return ((row["appearances_overall"]*2)+(row["goals_overall"]*5)+(row["assists_overall"]*3)+(row["penalty_goals"]*5)+(row["penalty_misses"]*-2)+(row["clean_sheets_overall"]*4)+(row['yellow_cards_overall']*-1)+(row['red_cards_overall']*-2))

defenders["Points"] = defenders.apply(calculate_points,axis=1)
#print(defenders)
defender=[]
no_of_defenders=int(input("Enter the number of defenders you want in your team:  "))
no_of_defenders_selected=int(input("Enter the number of defenders you have already added in your team:  "))
no_of_gk_comp_suggest=int(no_of_defenders-no_of_defenders_selected)
print("No of suggestions in defenders needed are: "+str(no_of_gk_comp_suggest))
for i in range(0,no_of_defenders_selected):
    temps_for_defenders = str(input("Enter the player's name:  "))
    defender.append(temps_for_defenders)
    defenders_temping = defenders[defenders['full_name'] == temps_for_defenders ]
    indexNames = indexNames.append(defenders_temping)
    temp_indexes = defenders[defenders['full_name'] == temps_for_defenders ].index
    # Delete these row indexes from dataFrame
    defenders.drop(temp_indexes , inplace=True)


#print(defender)
defenders = defenders.sort_values('Points',ascending=False)
selected_defenders = defenders.head(2)
#print(selected_defenders)
#for i in range(no_of_gk_comp_suggest):
defenders = defenders.head(no_of_gk_comp_suggest)
    #df[df['A'] == 2]['B']
indexNames = indexNames.append(defenders)
#print("Final Selected Defenders")
#print(indexNames)

################################################### MIDFIELDERS ###################################################

midfielders=data_we_need[data_we_need["position"]=="Midfielder"]
count_row = midfielders.shape[0]

def calculate_points(row):
    return ((row["appearances_overall"]*2)+(row["goals_overall"]*4)+(row["assists_overall"]*3)+(row["penalty_goals"]*5)+(row["penalty_misses"]*-2)+(row["clean_sheets_overall"]*4)+(row['yellow_cards_overall']*-1)+(row['red_cards_overall']*-2))

midfielders["Points"] = midfielders.apply(calculate_points,axis=1)
#print(midfielders)
midfielder=[]
no_of_midfielders=int(input("Enter the number of midfielders you want in your team:  "))
no_of_midfielders_selected=int(input("Enter the number of midfielders you have already added in your team:  "))
no_of_gk_comp_suggest=int(no_of_midfielders-no_of_midfielders_selected)
print("No of suggestions in midfielders needed are: "+str(no_of_gk_comp_suggest))
for i in range(0,no_of_midfielders_selected):
    temps_for_midfielder = str(input("Enter the player's name:  "))
    midfielder.append(temps_for_midfielder)
    midfielders_temping = midfielders[midfielders['full_name'] == temps_for_midfielder ]
    indexNames = indexNames.append(midfielders_temping)
    temp_indexes = midfielders[midfielders['full_name'] == temps_for_midfielder ].index
    # Delete these row indexes from dataFrame
    midfielders.drop(temp_indexes , inplace=True)


#print(midfielder)
midfielders = midfielders.sort_values('Points',ascending=False)
selected_midfielders = midfielders.head(2)
#print(selected_midfielders)
#for i in range(no_of_gk_comp_suggest):
midfielders = midfielders.head(no_of_gk_comp_suggest)
    #df[df['A'] == 2]['B']
indexNames = indexNames.append(midfielders)
#print("Final Selected Midfielders")
#print(indexNames)

###################################################GOALKEEPERS###################################################

forwards=data_we_need[data_we_need["position"]=="Forward"]
count_row = forwards.shape[0]

def calculate_points(row):
    return ((row["appearances_overall"]*2)+(row["goals_overall"]*4)+(row["assists_overall"]*3)+(row["penalty_goals"]*5)+(row["penalty_misses"]*-2)+(row["clean_sheets_overall"]*4)+(row['yellow_cards_overall']*-1)+(row['red_cards_overall']*-2))

forwards["Points"] = forwards.apply(calculate_points,axis=1)
#print(forwards)
forward=[]
no_of_forwards=int(input("Enter the number of forwards you want in your team:  "))
no_of_forwards_selected=int(input("Enter the number of forwards you have already added in your team:  "))
no_of_gk_comp_suggest=int(no_of_forwards-no_of_forwards_selected)
print("No of suggestions in forwards needed are: "+str(no_of_gk_comp_suggest))
for i in range(0,no_of_midfielders_selected):
    temps_for_forward = str(input("Enter the player's name:  "))
    forward.append(temps_for_forward)
    forwards_temping = forwards[forwards['full_name'] == temps_for_forward ]
    indexNames = indexNames.append(forwards_temping)
    temp_indexes = forwards[forwards['full_name'] == temps_for_forward ].index
    # Delete these row indexes from dataFrame
    forwards.drop(temp_indexes , inplace=True)


#print(forward)
forwards = forwards.sort_values('Points',ascending=False)
selected_forwards = forwards.head(3)
#print(selected_forwards)
#for i in range(no_of_gk_comp_suggest):
forwards = forwards.head(no_of_gk_comp_suggest)
    #df[df['A'] == 2]['B']
indexNames = indexNames.append(forwards)
print("Final Selected Team will be")
Total_price_of_players = indexNames['Total_Price'].sum()
Total_Points = indexNames['Points'].sum()
print("The total price of the players  :"+str(Total_price_of_players))
print("The total points of the players  :"+str(Total_Points))
print(" ")
print(" ")
print("Team points per week  :"+str(int(Total_Points/38)))
if(Total_price_of_players > 102):
    print("You need more money to achieve this team which isn't possible so make some compromises")
print(indexNames)



################################################### FINAL TEAM PRINT ###################################################

#total_team.append(defenders)
#total_team.append(midfielders)
#total_team.append(forwards)
#print(total_team)


'''
#here we will start data analysis
data=pd.read_csv('england-premier-league-players-2018-to-2019-stats.csv')
#print(data)
#print(list(data.columns))
data_we_need=data[["full_name","position","Current Club","appearances_overall","goals_overall","assists_overall","penalty_goals","penalty_misses", 'clean_sheets_overall','yellow_cards_overall', 'red_cards_overall']]
print(data_we_need)




#goalkeepers
goalkeepers=data[data_we_need["position"]=="Goalkeepers"]
number_goalkeepers=len(goalkeepers)
#print(number_goalkeepers)
count=0
team_goalkeeper=[]
for x in range(number_goalkeepers):
    gk=data[(data_we_need["full_name"]!=goalkeepers)&(data_we_need["position"]=="Goalkeepers")]
    gk_name=gk['Name'].tolist()
    gk_value=gk['Value'].values.tolist()
    #######print(type(gk))
    count=count+1
    if(count<no_of_gk_comp_suggest):
        team_goalkeeper.append(gk_name[count-1])
        gk=0
total_team.append(team_goalkeeper)
######print(goalkeepers)
#print(team_goalkeeper)
#print(gk_name)
print(total_team)
'''
