from a.sub import f_sub


def f_sub2():
    return "b/f_sub2" + "|" + f_sub()


if __name__ == "__main__":
    print(f_sub2())
