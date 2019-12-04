import math

def calucate_fuel(n):
    return (n // 3) - 2
    
def main():
    with open('../input.txt') as f:
        data = f.read()
    
    lines = data.split('\n')
    result = sum(calucate_fuel(int(n)) for n in lines)
    
    return result

if __name__ == '__main__':
    print(main())
