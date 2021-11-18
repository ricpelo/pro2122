def fact(n):
    def fact_iter(acc):
        nonlocal n
        if n == 0:
            return acc
        else:
            acc *= n
            n -= 1
            return fact_iter(acc)
    return fact_iter(1)

print(fact(5))
