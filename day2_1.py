data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,6,23,1,23,6,27,1,13,27,31,2,13,31,35,1,5,35,39,2,39,13,43,1,10,43,47,2,13,47,51,1,6,51,55,2,55,13,59,1,59,10,63,1,63,10,67,2,10,67,71,1,6,71,75,1,10,75,79,1,79,9,83,2,83,6,87,2,87,9,91,1,5,91,95,1,6,95,99,1,99,9,103,2,10,103,107,1,107,6,111,2,9,111,115,1,5,115,119,1,10,119,123,1,2,123,127,1,127,6,0,99,2,14,0,0]

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]

def main():
    for x1 in range(100):
        for x2 in range(100):
            data[1] = x1
            data[2] = x2
            for i in range(0, len(data), 4):
                opcode = data[i]
                i1, i2, i3 = data[i+1], data[i+2], data[i+3] 
                if opcode == 1:
                    data[i3] = data[i1] + data[i2]
                if opcode == 2:
                    data[i3] = data[i1] * data[i2]
                if opcode == 99:
                    break
            if data[0] == 19690720:
                    print(data[i1], data[i2])
    print(data)


if __name__ == '__main__':
    main()