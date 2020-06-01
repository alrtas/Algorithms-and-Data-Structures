def getBit(number, bitPosition):
    return (number >> bitPosition) #& 1
#https://wiki.python.org.br/BitwiseOperators

print getBit(1110, 1001)
