arr = list(map(int, input("Enter array elements: ").split()))
D = int(input("Enter number of rotations: "))

rotated_arr = arr[-D:] + arr[:-D]
print(f"Array after rotation: {rotated_arr}")
