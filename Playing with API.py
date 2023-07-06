import json
import requests
import time

api_key = "RGAPI-1ffc8d54-b922-40a0-842c-1f22946ac1f9"
api_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/JAMAULS%20BBC"

api_url = api_url + '?api_key=' + api_key

resp = requests.get(api_url)
player_info = resp.json()
player_account_id = player_info['accountId']
print(player_info)
print(player_info['summonerLevel'])
"""player info^ """


api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/JxR9JLMxhktNtSTcAn6i-OJdn557OK5MiyMMOqchefDizYxb6QnN1Old-8st9ba4DX-zxbSzLQmlZA/ids?start=0&count=20"

api_url = api_url + "&api_key=" + api_key

resp = requests.get(api_url)
matches = resp.json()
latest_match = matches[0]
print("latest match:")
print(latest_match)

"""player matches ^ """

api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/NA1_4701098083"
api_url = api_url +"?api_key=" + api_key

resp = requests.get(api_url)
match_data = resp.json()
match_data.keys()

match_data['info']['participants'][0]['championName']
"""how to search through dictionary"""

puuid = player_info['puuid']
part_index = match_data['metadata']['participants'].index(puuid)
match_data['info']['participants'][part_index]

print(match_data['info']['participants'][part_index]['assists'])
"""getting match data info"""

def get_match_data(region, match_id, api_ley):
    api_url = (
        "https://" + 
        region +
        ".api.riotgames.com/lol/match/v5/matches/" +
        match_id +
        "?api_key=" +
        api_key
    )
    resp = requests.get(api_url)
    data = resp.json()
    return data

def did_win(puuid, match_data):
    part_indx = match_data['metadata']['participants'].index(puuid)
    return match_data['info']['participants'][part_index]['win']

region = "americas"
match_id = "NA1_4701098083"
api_key = "RGAPI-9b86bbaa-d0a6-41f9-8a16-8cda93096e30"
puuid = "JxR9JLMxhktNtSTcAn6i-OJdn557OK5MiyMMOqchefDizYxb6QnN1Old-8st9ba4DX-zxbSzLQmlZA"

"""print(get_match_data(region, match_id, api_key))"""

for match_id in matches:
    match_data = get_match_data(region, match_id, api_key)
    print(did_win(puuid, match_data))

api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/JxR9JLMxhktNtSTcAn6i-OJdn557OK5MiyMMOqchefDizYxb6QnN1Old-8st9ba4DX-zxbSzLQmlZA/ids?type=ranked&start=0&count=50"

def get_matches(region, puuid, count, api_key):
    api_url = (
        "https://" +
        region +
        ".api.riotgames.com/lol/match/v5/matches/by-puuid/" +
        puuid +
        "/ids" +
        "?type=ranked&" + 
        "start=0&" +
        "count=" +
        str(count) +
        "&api_key=" +
        api_key
    )

    resp = requests.get(api_url)
    return resp.json()

print(get_matches(region, puuid, 100, api_key))