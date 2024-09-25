# Assign coordinates for each restaurant to a file

try:
    with open('Points.txt', 'w') as coords_file:
        coords_file.write('35.0800, -106.6460, Whataburger\n')
        coords_file.write('35.0831, -106.5700, Chick-fil-A\n')
        coords_file.write('35.0538, -106.6744, Sonic Drive-In\n')
        coords_file.write('35.1034, -106.5208, Subway\n')
        coords_file.write('35.1082, -106.5783, Panda Express')
except:
    print("Error: File not found.")
    exit()
print("Coordinates have been assigned to the file.")