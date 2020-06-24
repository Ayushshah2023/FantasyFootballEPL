import pandas as pd
import numpy as np

data=pd.read_csv('england-premier-league-players-2018-to-2019-stats.csv')
#print(data)
#print(list(data.columns))
data_we_need=data[["full_name","position","Current Club","appearances_overall","goals_overall","assists_overall","penalty_goals","penalty_misses", 'clean_sheets_overall','yellow_cards_overall', 'red_cards_overall','Total_Price']]
print(data_we_need)

#goalkeepers idhar daalo

goalkeepers=data_we_need[data_we_need["position"]=="Goalkeeper"]
count_row = goalkeepers.shape[0]

def calculate_points(row):
    return ((row["appearances_overall"]*2)+(row["goals_overall"]*6)+(row["assists_overall"]*3)+(row["penalty_goals"]*5)+(row["penalty_misses"]*-2)+(row["clean_sheets_overall"]*4)+(row['yellow_cards_overall']*-1)+(row['red_cards_overall']*-2))

print(goalkeepers.apply(calculate_points,axis=1))
goalkeepers["Points"] = goalkeepers.apply(calculate_points,axis=1)

descending_goalkeepers = goalkeepers.sort_values('Points',ascending=False)
count = 2
selected_goalkeepers = descending_goalkeepers.head(2)
#for i in range(count):
    
#total_points = []
#goalkeepers["Total Points"] = ((goalkeepers["appearances_overall"]*2)+(goalkeepers["goals_overall"]*6)+(goalkeepers["assists_overall"]*3)+(goalkeepers["penalty_goals"]*5)+(goalkeepers["penalty_misses"]*-2)+(goalkeepers["clean_sheets_overall"]*4)+(goalkeepers['yellow_cards_overall']*-1)+(goalkeepers['red_cards_overall']*-2))
print("Before")
print(goalkeepers)
print("After")
print(descending_goalkeepers)
print("Selected goalkeepers")
print(selected_goalkeepers)


#defenders idhar daalo

defender=data_we_need[data_we_need["position"]=="Defender"]
count_row = defender.shape[0]

def calculate_points(row):
    return ((row["appearances_overall"]*2)+(row["goals_overall"]*6)+(row["assists_overall"]*3)+(row["penalty_goals"]*5)+(row["penalty_misses"]*-2)+(row["clean_sheets_overall"]*4)+(row['yellow_cards_overall']*-1)+(row['red_cards_overall']*-2))

print(defender.apply(calculate_points,axis=1))
defender["Points"] = defender.apply(calculate_points,axis=1)

descending_defender = defender.sort_values('Points',ascending=False)
count = 2
selected_defender = descending_defender.head(5)
#for i in range(count):
    
#total_points = []
#goalkeepers["Total Points"] = ((goalkeepers["appearances_overall"]*2)+(goalkeepers["goals_overall"]*6)+(goalkeepers["assists_overall"]*3)+(goalkeepers["penalty_goals"]*5)+(goalkeepers["penalty_misses"]*-2)+(goalkeepers["clean_sheets_overall"]*4)+(goalkeepers['yellow_cards_overall']*-1)+(goalkeepers['red_cards_overall']*-2))
print("Before")
print(defender)
print("After")
print(descending_defender)
print("Selected defenders")
print(selected_defender)



#midfielders idhar daalo

midfielder=data_we_need[data_we_need["position"]=="Midfielder"]
count_row = midfielder.shape[0]

def calculate_points(row):
    return ((row["appearances_overall"]*2)+(row["goals_overall"]*4)+(row["assists_overall"]*3)+(row["penalty_goals"]*5)+(row["penalty_misses"]*-2)+(row["clean_sheets_overall"]*1)+(row['yellow_cards_overall']*-1)+(row['red_cards_overall']*-2))

print(midfielder.apply(calculate_points,axis=1))
midfielder["Points"] = midfielder.apply(calculate_points,axis=1)

descending_midfielder = midfielder.sort_values('Points',ascending=False)
count = 2
selected_midfielder = descending_midfielder.head(5)
#for i in range(count):
    
#total_points = []
#goalkeepers["Total Points"] = ((goalkeepers["appearances_overall"]*2)+(goalkeepers["goals_overall"]*6)+(goalkeepers["assists_overall"]*3)+(goalkeepers["penalty_goals"]*5)+(goalkeepers["penalty_misses"]*-2)+(goalkeepers["clean_sheets_overall"]*4)+(goalkeepers['yellow_cards_overall']*-1)+(goalkeepers['red_cards_overall']*-2))
print("Before")
print(midfielder)
print("After")
print(descending_midfielder)
print("Selected midfielders")
print(selected_midfielder)


#forwards idhar daalo

forward=data_we_need[data_we_need["position"]=="Forward"]
count_row = forward.shape[0]

def calculate_points(row):
    return ((row["appearances_overall"]*2)+(row["goals_overall"]*4)+(row["assists_overall"]*3)+(row["penalty_goals"]*5)+(row["penalty_misses"]*-2)+(row["clean_sheets_overall"]*0)+(row['yellow_cards_overall']*-1)+(row['red_cards_overall']*-2))

print(forward.apply(calculate_points,axis=1))
forward["Points"] = forward.apply(calculate_points,axis=1)

descending_forward = forward.sort_values('Points',ascending=False)
count = 2
selected_forward = descending_forward.head(3)
#for i in range(count):
    
#total_points = []
#goalkeepers["Total Points"] = ((goalkeepers["appearances_overall"]*2)+(goalkeepers["goals_overall"]*6)+(goalkeepers["assists_overall"]*3)+(goalkeepers["penalty_goals"]*5)+(goalkeepers["penalty_misses"]*-2)+(goalkeepers["clean_sheets_overall"]*4)+(goalkeepers['yellow_cards_overall']*-1)+(goalkeepers['red_cards_overall']*-2))
print("Before")
print(forward)
print("After")
print(descending_forward)
print("Selected forward")
print(selected_forward)


selected_goalkeepers = selected_goalkeepers.append(selected_defender,ignore_index = True)
selected_goalkeepers = selected_goalkeepers.append(selected_midfielder,ignore_index = True)
selected_goalkeepers = selected_goalkeepers.append(selected_forward,ignore_index = True)

print("Final Selected Team")
print(selected_goalkeepers)
