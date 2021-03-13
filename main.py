import csv

date_list = []
skip_count = 0

old_file_name = "acme_worksheet.csv"
new_file_name = "acme_worksheet_new.csv"

with open(old_file_name, "r") as old_file:
    file_reader = csv.DictReader(old_file)
    for row in file_reader:
        if row["Date"] in date_list:
            skip_count += 1
        else:
            date_list.append(row["Date"])

with open(new_file_name, "w", newline="") as new_file:
    file_write = new_file.write("Name/Date, ")
    file_writer = csv.writer(new_file)
    file_writer.writerow(date_list)

name_list = []

with open(old_file_name,"r") as old_file:
    file_reader = csv.DictReader(old_file)
    for row in file_reader:
        if row["Employee Name"] in name_list:
            skip_count += 1
        else:
            name_list.append(row["Employee Name"])

time_dict = {}
count = 0

time_dict["Name/Date"] = 0
for i in range(len(date_list)):
    time_dict[date_list[i]] = 0

for count in range(len(name_list)):
    with open(old_file_name, "r") as old_file:
        file_reader = csv.DictReader(old_file)
        for row in file_reader:
            if row["Employee Name"] == name_list[count]:
                time_dict["Name/Date"] = row["Employee Name"]
                time_dict[row["Date"]] = row["Work Hours"]
    with open(new_file_name, "a", newline="") as new_file:
        file_writer = csv.DictWriter(new_file, fieldnames=time_dict)
        file_writer.writerow(time_dict)
    for i in range(len(date_list)):
        time_dict[date_list[i]] = 0