def happy(number):
    if number < 10:
        return number in (1, 7)
    next_ = sum(int(char) ** 2 for char in str(number))
    return number in (1, 7) if number < 10 else happy(next_)


assert all(happy(n) for n in (1, 10, 100, 97, 130))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))