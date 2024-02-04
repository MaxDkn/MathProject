import time


def main(pnp: int):
    #  This function searches for the first pnp prime numbers that it can
    start = time.time()
    i = 3
    list = [2]
    while len(list) != pnp:
        divisible = False
        for number in list:
            if i % number == 0:
                divisible = True
            if divisible:
                break
        
        if not divisible:
            list.append(i)
        i += 2

    end = time.time()
    print(list)
    return f'Finished in {str(end - start)[:4]} secondes'


def new_main(t: int):
    #  This function searches for all the prime numbers it can for t second
    start = time.time()
    i = 2
    first_number = [2]
    first_number_jumeaux = []

    while (time.time() - start) <= t:
        divisible = False
        for number in first_number:
            if i % number == 0:
                divisible = True
                break

        if not divisible:
            first_number.append(i)
            if first_number[-1] - first_number[-2] == 2:
                first_number_jumeaux.append(f'[{first_number[-1]} | {first_number[-2]}]')

        i += 1
    return first_number_jumeaux

for item in new_main(10):
    print(item)
input()
