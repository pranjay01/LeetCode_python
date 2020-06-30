novice = 0

players = int(input('How many players? '))

for counter in range (players):

    hour_played = float(input('How many hours played? '))

    if hour_played < 100.0:

        novice = novice + 1

print ('Number of novice players is: ' , novice)