cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)
    
print(f"The first three items in the list are:")
print(cubes[0:2])
print(f"The three middle items in the list are:")
print(cubes[3:6])
print(f"The last three items in the list are:")
print(cubes[7:10])
