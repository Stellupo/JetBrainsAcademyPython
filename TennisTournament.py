n = int(input())
count = 0
NamesWin = []
for _ in range(n):
    games = input()
    games = games.split()
    if games[1] == "win":
        NamesWin += [games[0]]
print(NamesWin)
print(len(NamesWin))
'''or
n = int(input())
games = [input().split() for _ in range(n)]
win_players = [player[0] for player in games if player[1].lower() == 'win']
print(win_players, len(win_players), sep='\n')'''