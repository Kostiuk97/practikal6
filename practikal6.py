import math

def data(file_path='input.txt'):
    with open(file_path, 'r') as file:
        x = float(file.read())
        import math
x = 0.9
n = 1.6
w = abs(1 - math.sin(2*x) + n)
t = 2*w + 1/7**3
print(f'n = {n}, x = {x}, w = {w}, t = {t}')