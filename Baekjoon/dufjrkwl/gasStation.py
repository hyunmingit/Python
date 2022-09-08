"""https://www.acmicpc.net/problem/13305"""
import sys


def input() : return sys.stdin.readline().rstrip()


N = int(input())
dis = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost = cost[0:-1]
res = 0
oil = 0
now = cost[0]
meca = 0
reason = min(cost)
for i in range(N-1):

    if cost[i] == reason:
        oil = cost[i]
        meca = i
        break
    elif cost[i] <= now:
        now = cost[i]
    res += now * dis[i]
dis = dis[meca::]
res += sum(dis) * oil
print(res)

