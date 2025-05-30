try:
    print("Reading file content:")
    with open("sample.txt", "r") as file:
        line1 = file.readlines()
    line2 = 1
    for line in line1:
        print("Line", line2, ":", line.strip())
        line2 += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
