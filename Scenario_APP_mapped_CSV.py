import os, fileinput, csv, string
from os.path import join

with open('Scenario_APP_mapped.csv', 'wb') as csvfile:
    fieldnames = ['Scenario', 'trg', 'app']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for root, dirs, files in os.walk('SEGs/12-10-15/3A/APP/V34_Sim_Guides/SDFRG'):
         for file in files:
            with open(os.path.join(root, file), "r") as auto:
                #file_name = os.path.join(root, file)
                writer.writerow({'Scenario': file},)

                #Scan all lines in open file to search for a trigger file call
                for line in auto:
                    if 'trg ' in line:
                        #Split the line on SystemActions so only needed part of line is used
                        line_list = string.split(line, "SystemActions\\", 1)

                        #Only use second half of line after SystemActions\
                        line = line_list[1]

                        #Split line again to get rid of anything at the end
                        line_list = string.split(line, '"', 1)

                        #Only use folder path part of line
                        line = line_list[0]

                        #Write the trigger file used to trg column in csv file
                        writer.writerow({'trg': line})

                    if 'trg= ' in line:
                        #Split the line on SystemActions so only needed part of line is used
                        line_list = string.split(line, "SystemActions\\", 1)

                        #Account for times when no app file is used with trg=
                        if len(line_list) == 1:
                            break
                        else:
                            #Only use second half of line after SystemActions\
                            line = line_list[1]

                        #Split line again to get rid of anything at the end
                        line_list = string.split(line, '"', 1)

                        #Only use folder path part of line
                        line = line_list[0]

                        #Write the APP file used to app column in csv file
                        writer.writerow({'app': line})
