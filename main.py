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

name_list = []

with open("acme_worksheet.csv","r") as old_file:
    file_reader = csv.DictReader(old_file)
    for row in file_reader:
        if row["Employee Name"] in name_list:
            skip_count += 1
        else:
            name_list.append(row["Employee Name"])

time_dict = {
        'Name/Date':0,'Jun 29 2020':0, 'Jun 30 2020':0, 'Jul 01 2020':0, 'Jul 02 2020':0, 'Jul 03 2020':0, 'Jul 04 2020':0, 'Jul 05 2020':0
    }
count = 0


for count in range(len(name_list)):
    with open("acme_worksheet.csv", "r") as old_file:
        file_reader = csv.DictReader(old_file)
        for row in file_reader:
            # if count == 0:
            #     time_dict["Name/Date"] = 0
            #     time_dict[row["Date"]] = 0
            if row["Employee Name"] == name_list[count]:
                time_dict["Name/Date"] = row["Employee Name"]
                time_dict[row["Date"]] = row["Work Hours"]
        print(time_dict, count)
    with open("acme_worksheet_new.csv", "a", newline="") as new_file:
        file_writer = csv.DictWriter(new_file, fieldnames=time_dict)
        file_writer.writerow(time_dict)
    time_dict = {
        'Name/Date':0,'Jun 29 2020':0, 'Jun 30 2020':0, 'Jul 01 2020':0, 'Jul 02 2020':0, 'Jul 03 2020':0, 'Jul 04 2020':0, 'Jul 05 2020':0
    }

print(date_list)