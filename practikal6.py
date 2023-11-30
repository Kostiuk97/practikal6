import math

def data(file_path='0.txt'):
    with open(file_path ,'r') as file:
        numbers = file.readline().split() 
        x = float(numbers[0])
        n = float(numbers[1])
        w = abs(1 - math.sin(2*x) + n)  
        t = 2*w + 1/7**3
    return x, n, w, t

result = data()

result_str = f"x: {result[0]}\n n: {result[1]}\n w: {result[2]}\n t: {result[3]}"
print(result_str)
with open("output.txt", 'w') as f:
    f.write(result_str)