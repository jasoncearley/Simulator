import os, fileinput, string
from os.path import join

app_files = dict()
trg_files = dict()
scenario_files = dict()

number = 1

for root, dirs, files in os.walk('SEGs/3_2_2017/TRG/ScenarioDev'):

    for file in files:

        if file == "Thumbs.db":
            break

        short_file_path = os.path.join(root, file)

        short_file_path= string.split(short_file_path, "SystemActions/", 1)

        short_file_path = short_file_path[1]

        #key:value
        trg_files[short_file_path] = number

        number += 1

for root, dirs, files in os.walk('SEGs/3_2_2017/APP/ScenarioDev/SystemActions'):

    for file in files:

        if file == "Thumbs.db":
            break

        short_file_path = os.path.join(root, file)

        short_file_path= string.split(short_file_path, "SystemActions/", 1)

        short_file_path = short_file_path[1]

        app_files[short_file_path] = number

        number += 1

for root, dirs, files in os.walk('SEGs/3_2_2017/APP/V34_Sim_Guides'):

    for file in files:

        if file == "Thumbs.db":
            break

        short_file_path = os.path.join(root, file)

        scenario_files[short_file_path] = number

        number += 1

with open('Scenario_APP_mapped_gml.txt', 'w') as textfile:

    textfile.write('graph\n')
    textfile.write('[')

    keys = trg_files.viewkeys()

    for key in keys:
        textfile.write('\n  node')
        textfile.write('\n  [')
        textfile.write(('\n   id %s') % trg_files[key])
        textfile.write(('\n   label "%s"') % key)
        textfile.write('\n  ]')

    keys = app_files.viewkeys()

    for key in keys:
        textfile.write('\n  node')
        textfile.write('\n  [')
        textfile.write(('\n   id %s') % app_files[key])
        textfile.write(('\n   label "%s"') % key)
        textfile.write('\n  ]')

    keys = scenario_files.viewkeys()

    for key in keys:
        textfile.write('\n  node')
        textfile.write('\n  [')
        textfile.write(('\n   id %s') % scenario_files[key])
        textfile.write(('\n   label "%s"') % key)
        textfile.write('\n  ]')

    for root, dirs, files in os.walk('SEGs/3_2_2017/APP/V34_Sim_Guides'):

         for file in files:

            with open(os.path.join(root, file), "r") as auto:

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

                        line = line.replace('\\', '/')

                        short_file_path = os.path.join(root, file)

                        #Write the trigger file used
                        textfile.write('\n  edge')
                        textfile.write('\n  [')
                        textfile.write(('\n   source %s') % scenario_files[short_file_path])
                        textfile.write(('\n   target %s') % trg_files[line])
                        textfile.write('\n  ]')

                    if 'trg= ' in line:
                        #Split the line on SystemActions so only needed part of line is used
                        line_list = string.split(line, "SystemActions\\", 1)

                        #Account for times when no app file is used with trg=
                        if len(line_list) == 1:
                            break

                        #Only use second half of line after SystemActions\
                        line = line_list[1]

                        #Split line again to get rid of anything at the end
                        line_list = string.split(line, '"', 1)

                        #Only use folder path part of line
                        line = line_list[0]

                        line = line.replace('\\', '/')

                        short_file_path = os.path.join(root, file)

                        #Write the trigger file used
                        textfile.write('\n  edge')
                        textfile.write('\n  [')
                        textfile.write(('\n   source %s') % scenario_files[short_file_path])
                        textfile.write(('\n   target %s') % app_files[line])
                        textfile.write('\n  ]')

    textfile.write('\n]')
