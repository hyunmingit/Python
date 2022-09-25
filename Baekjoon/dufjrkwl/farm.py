"""https://www.acmicpc.net/problem/2477"""

import sys
def input() : return sys.stdin.readline().rstrip()


wid = 0
hei = 0
count = {}
N = int(input())
x1 = 0
x2 = 0
y1 = 0
y2 = 0
sr = 0
br = 0
order = []
ll = []
for i in range(6):
    ip, ip2 = map(int, input().split())
    ll.append(ip2)
    try:
        count[ip] += 1
    except:
        count[ip] = 1
    order.append(ip)
    if ip == 1 or ip == 2:
        if ip2 > wid:
            wid = ip2
    else:
        if ip2 > hei:
            hei = ip2
    b1 = ip
    b2 = ip2

sorder = set(order)
print('order : ', order)
print('count : ', count)
print('length : ', ll)
br = wid * hei
print(N * (br - sr))

