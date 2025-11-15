from random import randint
p44 = [
    1234, 1243, 1324, 1342, 1423, 1432,
    2134, 2143, 2314, 2341, 2413, 2431,
    3124, 3142, 3214, 3241, 3412, 3421,
    4123, 4132, 4213, 4231, 4312, 4321
]

def gen(width=8, height=8):
    vis = [0] * (width * height + 10)
    wall = [1] * (width * height * 2 + 10)
    ds = [0, -1, 1, width, -width]
    d_wall = [0, -1, 0, width, -width]
    stack = [p44[randint(0, 23)]]  # + (width // 2 + height // 2 * width) * 10000]
    vis[0] = 1
    # step_cnt = 0
    max_len=0
    while (len(stack) > 0):
        max_len=max(len(stack),max_len)
        # step_cnt += 1
        #  i = len(stack) - 1
        #  if randint(0, 1) == 0:
        #      i = randint(0, i)
        val = stack.pop()
        p = val // 10000
        dirs = val % 10000
        done = False
        for i in range(4):
            if done:
                continue
            d_idx = dirs % 10
            dirs = dirs // 10
            if d_idx == 0:
                continue
            d = ds[d_idx]
            if p % width == 0 and d == -1:
                continue
            if p % width == (width - 1) and d == 1:
                continue
            new_p = p + d
            if new_p < 0 or new_p >= width * height:
                continue
            #  print(new_p, p, d)
            if vis[new_p] == 1:
                continue
            idx_wall = (p % width) + (p // width) * 2 * width + d_wall[d_idx]
            wall[idx_wall] = 0
            if dirs > 0:
                stack.append(p * 10000 + dirs)
            stack.append(new_p * 10000 + p44[randint(0, 23)])
            vis[new_p] = 1
            done = True
    res = []
    for y in range(0, height * 2 - 1):
        a = 0
        for x in range(0, width - (y % 2 == 0)):
            a = (a << 1) + wall[y * width + x]
        res.append(a)
    #  print(vis)
    return res, max_len


def print_maze(res, width=8, height=8):
    print("#" * (width * 2 + 1))
    for y in range(0, height * 2 - 1):
        print("#", end="")
        if y % 2 == 0:
            for x in range(0, width - 1):
                print(" ", end="")
                if (res[y] >> x) % 2 == 1:
                    print("#", end="")
                else:
                    print(" ", end="")
            print(" #")
        else:
            for x in range(0, width):
                if (res[y] >> x) % 2 == 1:
                    print("#", end="")
                else:
                    print(" ", end="")
                print("#", end="")
            print(" ")
    print("#" * (width * 2 + 1))
    return


def stats(W=8, H=8):
    res = []
    for i in range(1000):
        res.append(gen(width=W, height=H)[1])
    print(max(res), sum(res) / 1000)
    return max(res)


def stats2():
    res = []
    for i in range(1000):
        res.append(stats())
    print(max(res))
    return


if __name__ == "__main__":
    #  print_maze(gen()[0])
    stats2()
    pass