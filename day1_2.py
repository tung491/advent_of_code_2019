import math

def calucate_fuel(n):
    result = (n // 3) - 2
    if result > 0:
        return result
    else:
        return 0

def calucate_module(n):
    fuel = 1
    fuels = [calucate_fuel(n)]
    while fuel != 0:
        fuel = calucate_fuel(fuels[-1])
        fuels.append(fuel)
    return sum(fuels) 
    
def main():
    with open('../input.txt') as f:
        data = f.read()
    
    lines = data.split('\n')
    result = sum(calucate_module(int(n)) for n in lines)
    
    return result

if __name__ == '__main__':
    print(main())
