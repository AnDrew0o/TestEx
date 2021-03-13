line_count = 0

with open("acme_worksheet.csv", "r") as file:
    for line in file:
        line_count += 1

arr_sheet1 = [0] * line_count
for i in range(line_count):
    arr_sheet1[i] = [0] * 3

with open("acme_worksheet.csv", "r") as file:
    for i in range(line_count):
        for j in range(3):
            print(arr_sheet1[i][j], end="")
        print()