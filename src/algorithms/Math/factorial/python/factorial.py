def factorial(number):
    if int(number) < 0:
        return "Erro, number cannot be less than 0"
    elif int(number) == 0:
        return 1
    else:
        result = 1
        for i in range(1, int(number)+1):
            result *= i
        return result
