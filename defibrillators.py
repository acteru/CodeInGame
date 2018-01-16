import sys
import math

lon = input()
lat = input()
n = int(input())
defi = [ input() for i in range(n)]

def get_distance(lonA, lonB, latA, latB):
    lonA = float(lonA.replace(",", "."))
    lonB = float(lonB.replace(",", "."))
    latA = float(latA.replace(",", "."))
    latB = float(latB.replace(",", "."))
    x = (lonB - lonA) * (math.cos((latA + latB) / 2))
    y = (latB - latA)
    #d = math.sqrt(((x**2 + y**2) * 6371))
    d = math.sqrt(x**2 + y**2) * 6371
    return d

defi_new = []
for i in range(len(defi)):
    defi_new.append(defi[i].split(";"))

positions = []
for i in range(n):
    positions.append(defi_new[i][1])
    positions.append(defi_new[i][4])
    positions.append(defi_new[i][5])

count = 1
count_1 = 0
d = {}
for i in range(n):
    x = get_distance(lon, positions[count], lat, positions[count +1])
    d[x] = positions[count_1]
    count += 3
    count_1 += 3

print(d[min(d)])
