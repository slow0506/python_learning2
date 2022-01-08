import math
edge = int(input())
eight_faces = 2 * math.sqrt(3) * edge *edge
volume = math.sqrt(2) * (edge ** 3) / 3
print(round(eight_faces, 2), round(volume, 2))