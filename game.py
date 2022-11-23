from random import shuffle
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

print(int(config["middle"]["doctor"]))

def role_distribution(peoples) -> dict:
    if 4 <= len(peoples.keys()) <= 5:
        k = "low"
    elif 6 <= len(peoples.keys()) <= 8:
        k = "middle"
    else:
        k = "max"
    roles = int(config[k]["doctor"]) * ["doctor"] + int(config[k]["sheriff"]) * ["sheriff"] + int(
        config[k]["mafia"]) * ["mafia"] + int(config[k]["don"]) * ["don"]
    shuffle(roles)
    for people, role in zip(peoples.keys(), roles):
        peoples[people]["role"] = role
    return peoples


def line_of_speak(peoples) -> list:
    res1 = []
    res2 = []
    for i in list(peoples.keys()):
        res1.append((i, peoples[i]["nickname"]))
        res2.append((i, peoples[i]["nickname"]))
    return res1 + res2


class Mafia:
    def __init__(self):
        self.peoples = {}
        self.situation_now = {
            "title": "Waiting for start",
            "ready for game": 0
        }

    def register_new(self, tech, player_data) -> None:
        """add new player"""
        self.peoples[tech["id"]] = {"role": "player", "nickname": ""}

    def situation(self, tech, player_data) -> dict:
        """return game situation (game side)"""
        return {
            "game_situation": self.situation_now,
            "you": self.peoples[player_data["id"]]
        }

    def annul_client(self, player_data) -> None:
        """annul player in current game"""
        self.peoples[player_data["id"]] = {"role": "player"}

    def ready(self, player_data):
        """mark player as 'ready for game'"""
        if self.peoples[player_data["id"]]["role"] == "player":
            self.peoples[player_data["id"]]["nickname"] = player_data["nickname"]
            self.peoples[player_data["id"]]["role"] = "player_R"
        self.situation_now["ready for game"] += 1
        print(len(self.peoples))
        if len(self.peoples) >= 4 and all([i != "player_R" for i in self.peoples.values()]):
            print("ИГРА НАЧИНАЕТСЯ")
            self.peoples = role_distribution(self.peoples)
            self.situation_now = {
                "title": "main_game",
                "time": "day",
                "players_count": sum([1 for i in self.peoples.values() if i["role"] != "watcher"]),
                "line of speakers": line_of_speak(self.peoples),
                "speak_now": "",
            }
