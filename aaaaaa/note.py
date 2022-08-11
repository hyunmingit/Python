from multiprocessing import Process
import random
import time

"""
될리가 없는거였다.
메트로놈이 연속적으로 작동하게 바꿔보자
"""

nums = [-1, -1, -1, -1, -1, -1, -1]

ms = 218 / 60


def func0():
    while True:
        r0 = random.random() * ms  # 메트로놈 최대속도
        nums[0] *= -1
        if nums[0] == -1:
            print("\\")
        else:
            print("/")
        time.sleep(r0)


def func1():
    while True:
        r1 = random.random() * ms  # 메트로놈 최대속도
        nums[1] *= -1
        if nums[1] == -1:
            print("  \\")
        else:
            print("  /")
        time.sleep(r1)


def func2():
    while True:
        r2 = random.random() * (218 / 60)  # 메트로놈 최대속도
        nums[2] *= -1
        if nums[2] == -1:
            print("    \\")
        else:
            print("    /")
        time.sleep(r2)


def func3():
    while True:
        r3 = random.random() * (218 / 60)  # 메트로놈 최대속도
        nums[3] *= -1
        if nums[3] == -1:
            print("      \\")
        else:
            print("      /")
        time.sleep(r3)


def func4():
    while True:
        r4 = random.random() * (218 / 60)  # 메트로놈 최대속도
        nums[4] *= -1
        if nums[4] == -1:
            print("        \\")
        else:
            print("        /")
        time.sleep(r4)


def func5():
    while True:
        r5 = random.random() * (218 / 60)  # 메트로놈 최대속도
        nums[5] *= -1
        if nums[5] == -1:
            print("          \\")
        else:
            print("          /")
        time.sleep(r5)


def func6():
    while True:
        r6 = random.random() * (218 / 60)  # 메트로놈 최대속도
        nums[6] *= -1
        if nums[6] == -1:
            print("            \\")
        else:
            print("            /")
        time.sleep(r6)


if __name__ == '__main__':
    p0 = Process(target=func0)
    p1 = Process(target=func1)
    p2 = Process(target=func2)
    p3 = Process(target=func3)
    p4 = Process(target=func4)
    p5 = Process(target=func5)
    p6 = Process(target=func6)

    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
