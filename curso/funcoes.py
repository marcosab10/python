def multiplica(*args):
    if(len(args) > 0):
        total = 1;
        for i in args:
            total *= i
        return total
    return 0

print(multiplica(1,2,3,4,5,6))
print(1*2*3*4*5*6)

def primo(numero):
    if numero == 1 or numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    divisor = numero
    while divisor > 2:
        divisor -= 1
        if numero % divisor == 0:
            return False
    return True

for i in range(100):
    if primo(i):
        print(f'{i} é primo.')    
    

