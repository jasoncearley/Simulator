import os, fileinput, csv, string
from os.path import join

number = 1

with open('APP_TRG_files_numbered.csv', 'wb') as csvfile:

    fieldnames = ['Name', 'Number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for root, dirs, files in os.walk('SEGs/12-10-15/3A/TRG'):

        for file in files:

            if file == "Thumbs.db":
                break

            short_file_path = os.path.join(root, file)

            short_file_path= string.split(short_file_path, "SystemActions/", 1)

            short_file_path = short_file_path[1]

            writer.writerow({'Name': short_file_path, 'Number': number},)

            number += 1

    writer.writerow({'Name': "APP Files"},)

    for root, dirs, files in os.walk('SEGs/12-10-15/3A/APP/ScenarioDev/SystemActions'):

        for file in files:

            if file == "Thumbs.db":
                break

            short_file_path = os.path.join(root, file)

            short_file_path= string.split(short_file_path, "SystemActions/", 1)

            short_file_path = short_file_path[1]

            writer.writerow({'Name': short_file_path, 'Number': number},)

            number += 1
