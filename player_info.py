import json
import requests


class Summoner:

    v4_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    v5_url = "https://americas.api.riotgames.com/lol/match/v5/matches/"
    api_key = "RGAPI-1ffc8d54-b922-40a0-842c-1f22946ac1f9"

    def __init__(self, summoner_name):
        self.summoner_name = summoner_name
        self.summoner_level = None
        self.puuid = None
        self.match_history = None
        self.latest_match = None
        self.set_summoner(self.summoner_name)
        self.set_match_history()
        self.player_index = None
        self.latest_match_kills = None
        self.latest_match_deaths = None
        self.latest_match_assists = None
        self.latest_match_cs = None
        self.set_latest_match_stats()

    """constructor then uses set_summoner method below to initialize username right away"""
    
    def set_summoner(self, summoner_name):

        api_url = f"{Summoner.v4_url}{self.summoner_name}?api_key={Summoner.api_key}"
        resp = requests.get(api_url)
        player_info = resp.json()
        self.summoner_level = player_info['summonerLevel']
        self.puuid = player_info['puuid']
        self.set_match_history()
        self.set_latest_match_stats()

    def set_match_history(self):
        api_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{self.puuid}/ids?start=0&count=20&api_key={Summoner.api_key}"
        resp = requests.get(api_url)
        self.match_history = resp.json()
        self.latest_match = self.match_history[0]

    def set_latest_match_stats(self):
        api_url = Summoner.v5_url + self.latest_match + "?api_key=" + Summoner.api_key
        resp = requests.get(api_url)
        match_data = resp.json()
        match_data.keys()

        self.player_index = match_data['metadata']['participants'].index(self.puuid)
        """gets user position"""

        self.latest_match_kills = match_data['info']['participants'][self.player_index]['kills']
        self.latest_match_deaths = match_data['info']['participants'][self.player_index]['deaths']
        self.latest_match_assists = match_data['info']['participants'][self.player_index]['assists']
        
    def get_summoner_name(self):
        return self.summoner_name

    def get_summoner_level(self):
        return self.summoner_level

    def get_summoner_puuid(self):
        return self.puuid

    def get_latest_match(self):
        return self.latest_match

    def get_player_index(self):
        return self.player_index

    def get_latest_match_kills(self):
        return self.latest_match_kills

    def get_latest_match_deaths(self):
        return self.latest_match_deaths

    def get_latest_match_assists(self):
        return self.latest_match_assists

    
