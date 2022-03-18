from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player_object):
        if player_object.guild == "Unaffiliated":
            self.players.append(player_object)
            player_object.guild = self.name
            return f"Welcome player {player_object.name} to the guild {self.name}"
        elif player_object.guild == self.name:
            return f"Player {player_object.name} is already in the guild."
        return f"Player {player_object.name} is in another guild."

    def kick_player(self, player_name):
        for player_object in self.players:
            if player_object.name == player_name:
                self.players.remove(player_object)
                player_object.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players = ""
        for p in self.players:
            players += f"{p.player_info()}\n"
        info = f"Guild: {self.name}\n" \
               f"{players}"
        return info


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())

guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
