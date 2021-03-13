'''import csv


skip_count = 0
name_count = 0

with open("acme_worksheet.csv","r") as old_file:
    file_reader = csv.DictReader(old_file)
    for row in file_reader:
        if row["Employee Name"] in name_list:
            skip_count += 1
        else:
            name_list.append(row["Employee Name"])
            name_count += 1

date_list = []

with open("acme_worksheet.csv", "r") as old_file:
    file_reader = csv.DictReader(old_file)
    for row in file_reader:
        if row["Date"] in date_list:
            skip_count += 1
        else:
            date_list.append(row["Date"])
            name_count += 1

with open("acme_worksheet_new.csv", "w") as new_file:
    file_writer = csv.writer(new_file)
    file_writer.writerow(date_list)
    file_writer.writerow(name_list)'''

import csv

date_list = []
skip_count = 0

with open("acme_worksheet.csv", "r") as old_file:
    file_reader = csv.DictReader(old_file)
    for row in file_reader:
        if row["Date"] in date_list:
            skip_count += 1
        else:
            date_list.append(row["Date"])

with open("acme_worksheet_new.csv", "w", newline="") as new_file:
    file_write = new_file.write("Name/Date, ")
    file_writer = csv.writer(new_file)
    file_writer.writerow(date_list)

############
name_list = []

with open("acme_worksheet.csv","r") as old_file:
    file_reader = csv.DictReader(old_file)
    for row in file_reader:
        if row["Employee Name"] in name_list:
            skip_count += 1
        else:
            name_list.append(row["Employee Name"])

time_dict = {}
count = 0
'''
#while count < len(name_list):
with open("acme_worksheet.csv", "r") as old_file:
    file_reader = csv.DictReader(old_file)
    for row in file_reader:
        if row["Employee Name"] == name_list[count]:
            time_dict[row["Date"]] = row["Work Hours"]
with open("acme_worksheet_new.csv", "a", newline="") as new_file:
    new_file.write(row["Employee Name"] + ",")
    file_writer = csv.DictWriter(new_file, fieldnames=date_list)
    file_writer.writerow(time_dict)
count +=1'''

while count < len(name_list):
    with open("acme_worksheet.csv", "r") as old_file:
        file_reader = csv.DictReader(old_file)
        for row in file_reader:
            if row["Employee Name"] == name_list[count]:
                time_dict["Name/Date"] = row["Employee Name"]
                time_dict[row["Date"]] = row["Work Hours"]
        print(time_dict, count)
    with open("acme_worksheet_new.csv", "a", newline="") as new_file:
        file_writer = csv.DictWriter(new_file, fieldnames=time_dict)
        file_writer.writerow(time_dict)
    count += 1