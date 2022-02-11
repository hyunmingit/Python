
loc = input()

X = ord(loc[0]) - 96
Y = int(loc[1])


if 3 <= X <= 6 and 3 <= Y <= 6:
    Count = 8
elif X == 1 and (Y == 1 or Y == 8):
    Count = 2
elif X == 8 and (Y == 1 or Y == 8):
    Count = 2
elif X == 2 and (Y == 7 or Y == 2):
    Count = 4
elif X == 7 and (Y == 7 or Y == 2):
    Count = 4
elif 3 <= X <= 6 and (Y == 2 or Y == 7):
    Count = 6
elif 3 <= Y <= 6 and (X == 2 or X == 7):
    Count = 6
elif 3 <= X <= 6 and (Y == 1 or Y == 8):
    Count = 4
elif 3 <= Y <= 6 and (X == 1 or X == 8):
    Count = 4
elif (X == 2 or X == 7) and(Y ==1 or Y ==8):
    Count = 3
elif (X ==1 or X == 8) and(Y ==2 or Y ==7):
    Count = 3


print(Count)
