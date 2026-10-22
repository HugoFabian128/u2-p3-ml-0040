import numpy as np
# Hugo Fabian NC 0040

n0040 = np.array([10,20,30,40,50])
print(n0040)
print(n0040[0])
print(n0040[3])
print(n0040[-1])
print(n0040[-2])
print("-----------------------")

n0040 = np.array([
    [10,20,30],
    [40,50,60]
])
print(n0040)
print(n0040[0,0])
print(n0040[1,2])
print(n0040[-1,-1])
print(n0040[-2,-2])

print("-----------------------")
n0040 = np.array([
    # 0 -2
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    # 1 -1
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])

print(n0040)
print(n0040[0, 0, 0])
print(n0040[1, 1, 2])
print(n0040[-1, -1, -2])
print("Hugo Fabian NC 0040")
