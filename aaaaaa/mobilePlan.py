
def total(a, b, year):
    # YtoM
    year = year * 12 - 6
    return int(a * 6 + b * year)


skP = 99000
skt = 59000

print("통신 요금")
print("sk 선약 : ", int(total(skP, skt, 2) * 0.75))
print("sk 공시 : ", total(skP, skt, 2))
print("현재 요금 : ", 59000 * 18)