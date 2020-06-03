def naiveAlgorithm(base, power):
    if power < 0:
        return naiveAlgorithm(1/base, (power*-1))
    if power == 0:
        return 1
    result = 1
    for i in range(1, power + 1):
        result *= base
    return result


def fastPowering(base, power):
    if power < 0: return fastPowering((1/base), (power*-1))
    elif power == 0: return 1
    elif power == 1: return base
    elif (power % 2) == 0: return fastPowering((base * base), (power / 2))  # Even power
    else: return base * fastPowering((base * base), ((power - 1) / 2))  # Odd power
