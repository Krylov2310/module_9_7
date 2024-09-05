print('\033[30m\033[47mДомашнее задание по теме "Декораторы"\033[0m')
print('\033[30m\033[47mЗадание: Декораторы в Python.\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


def is_prime(func):
    def wrapper(*args):
        set_res = func(*args)
        set_prime = None
        for j in range(2, int(set_res)):
            if j == 1:
                continue
            if int(set_res) % j == 0:
                set_prime = 'Составное'
                break
            else:
                set_prime = 'Простое'
        print(set_prime)
        return set_res
    return wrapper


@is_prime
def sum_three(a, b, c):
    res = a + b + c
    return res


# Пример:
result = sum_three(2, 3, 6)
print(result)
print()
print(thanks)
