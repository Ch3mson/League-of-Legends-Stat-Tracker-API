from player_info import Summoner


username  = str(input("What is your username?"))

si = Summoner(username)

print(si.get_summoner_name())
print(si.get_summoner_level())
print(si.get_summoner_puuid())
print(si.get_latest_match())
print("Kills:" + str(si.get_latest_match_kills()) + " Deaths: " + str(si.get_latest_match_deaths()) + " Assists: " + str(si.get_latest_match_assists()))