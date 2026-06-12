class Player:
    def __init__(self, name):
        self.name = name
        self.runs = []

    def add_runs(self, run):
        self.runs.append(run)

    def total_runs(self):
        return sum(self.runs)

    def average_runs(self):
        return self.total_runs() / len(self.runs)


name = input("Player Name: ")

n = int(input("Number of Matches: "))

player = Player(name)

for i in range(n):
    run = int(input(f"Runs in Match {i+1}: "))
    player.add_runs(run)

print("=" * 50)
print("         PLAYER PERFORMANCE REPORT")
print("=" * 50)
print(f"\nPlayer Name    : {player.name}")
print(f"\nTotal Runs     : {player.total_runs()}")
print(f"Matches Played : {len(player.runs)}")
print(f"Average Runs   : {player.average_runs()}")
print("\n" + "=" * 50)