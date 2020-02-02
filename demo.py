# coding=utf-8
import random
num = 2

while True:
    ran_num = random.randint(1, 3)
    if ran_num == num:
        random.randint(1, 3)
    else:
        break

# print(ran_num)


def demo1():
    return 1, 2


def demo2(a,b):
    print(a+b)





if __name__ == '__main__':
    res = demo1()
    print(res)
    print(res[0], res[1])
    demo2(res[0], res[1])
