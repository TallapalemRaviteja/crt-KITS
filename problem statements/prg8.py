class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def final_score(self):
        return sum(self.scores)


class Tournament:
    def generate_report(self, player):
        status = "QUALIFIED" if player.final_score() >= 300 else "NOT QUALIFIED"

        print("=" * 50)
        print("            TOURNAMENT REPORT")
        print("=" * 50)
        print(f"\nPlayer Name : {player.name}")
        print(f"\nFinal Score : {player.final_score()}")
        print(f"\nRank Status : {status}")
        print("\n" + "=" * 50)


name = input("Player Name: ")
n = int(input("Number of Matches: "))

player = Player(name)

for i in range(n):
    score = int(input(f"Score {i+1}: "))
    player.add_score(score)

tournament = Tournament()
tournament.generate_report(player)