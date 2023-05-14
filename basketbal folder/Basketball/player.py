import Basketball

class Player:
    new_team = []
    def __init__(self, data):
        self.name = data["name"]
        self.age =data['age']
        self.position = data['position']
        self.team = data['team']
        Player.new_team.append(self)

    @classmethod
    def get_team (cls, team_list):
        new_list = []
        for playerz in team_list:
            new_list.append(playerz)
        print(new_list)

kevin = {
    	"name": "Kevin Durant",
    	"age":34,
    	"position": "small forward",
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum",
    	"age":24,
    	"position": "small forward",
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving",
    	"age":32, "position": "Point Guard",
    	"team": "Brooklyn Nets"
}

# Create your Player instances here!
# player_jason = ???


# player_kevin=Player(kevin)
# print(player_kevin.name)

# player_jason = Player(jason)
# print(player_jason.name)

# player_kyrie = Player(kyrie)
# print(player_kyrie.name)


# new_list = []
# for player in Basketball.players:
#     new_list.append(player)

# print(new_list[2]["name"])


# player_jason = Player(Basketball.players[1])
Player.get_team(Basketball.players)
