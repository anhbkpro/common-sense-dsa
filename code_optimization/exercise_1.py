basketball_players = [
    {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
    {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
    {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
    {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"}
]

football_players = [
    {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
    {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
    {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
    {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"}
]

basketball_player_hash = {}
for player in basketball_players:
    player_name = player['first_name'] + ' ' + player['last_name']
    if player_name not in basketball_player_hash:
        basketball_player_hash[player_name] = player['team']

result = []
for player in football_players:
    player_name = player['first_name'] + ' ' + player['last_name']
    if player_name in basketball_player_hash:
        result.append(player_name)

print(result)
