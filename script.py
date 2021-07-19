import os
import subprocess
import gspread

# Location of the service account json file
path = '/home/swastik/Git/vbb/PS-Station-Work/key.json' # Add Path to your service account JSON file
gc = gspread.service_account(filename=path)

spreadsheet_id = '1NoEbHNGSc20Ne9ngELvTNdfaVGaVXsOwZEW8ZDANbrkl2' # Add the Spreadsheet Id
spreadsheet = gc.open_by_key(spreadsheet_id)
worksheet = spreadsheet.sheet1
values = worksheet.get_all_values()

no_of_events = 20 # No of events in the GSheet

time = []
# To Store Time of the events
# Not included End-time, as GMeetRecorder exits at less number of people

links = []
# To Store links of the events

name = []
# To Store the name and location of the script

for event in values[1:]:
    time.append(event[1])
    links.append(event[3])

# Schedule the script with cron-job using the Time
    # Time Format is --> Example :
    # '2021-07-05T08:00:00+05:30'
    # '0123456789012345678901234' <--

# Make the file with the extension of.sh
# Each event is stored as a script
for x in range(0, no_of_events):
    # Time for 'at' command
    minutes = (time[x][14:16])
    hour = (time[x][11:13])
    day = (time[x][8:10])
    month = (time[x][5:7])
    year = (time[x][0:4])

    # Name and Location of the file you want to store it as
    name = "/home/swastik/Git/vbb/GMeetRecorder/" + links[x][24:] + day + month + ".sh" # Edit it as the "path where you want to store the recording" + "name of the file(s)"

    # Checking if the script exists if so, the event is already taken into account
    if os.path.isfile(name):
        continue

    # Making the script
    make = "echo \"#!/bin/bash\" > " + name
    create = subprocess.run(make, shell=True)

    # Command
    # Credentials of the Gmail ID for the GMeetRecorder to use to access the bot
    gmail = "randomjohnrecording@gmail.com" # Add the gmail account and password [ Need to work on the code of bot to facilitate better authentication ]
    password = "'JohnDoe123'" # password needs to be within "''"

    # Time in minutes for minimum and maximum duration
    minimum_minutes = 2
    maximum_minutes = 3

    # Time Conversion as GMeetRecorder takes time only in seconds
    min_duration = minimum_minutes * 60
    max_duration = maximum_minutes * 60

    #Storage
    directory = "/home/swastik/Git/vbb/gcalender/videos" # Directory to store the meet recordings
    video_name = hour + ":" + minutes + "_" + day + "-" + month + "-" + year + "_" + links[x][24:]
    command = "echo  \" sudo BACKEND=gmail EMAIL=" + gmail + " PASSWORD=" + password + " MEET_URL=" + links[x] \
              + " MIN_DURATION=" + str(min_duration) + " MAX_DURATION=" + str(max_duration) + \
              " OUTPUT_DIR=" + directory + " VIDEO_NAME=" + video_name + " FRAC_TO_EXIT=0.83 docker-compose up\" >> " + name
    create2 = subprocess.run(command, shell=True)

    # Permission to Execute the script
    permission = "sudo chmod +x " + name
    create3 = subprocess.run(permission, shell=True)

    # Return Error
    if create.returncode != 0 or create2.returncode != 0 or create3.returncode != 0:
        print(create.stderr, create2.stderr, create3.stderr)

    # Execute Script using 'at'
    exec_time = str(year) + month + day + hour + minutes
    execution = 'sudo echo  "' + name + '" | at -t ' + exec_time
    # print(create.stdout, create2.stdout, create3.stdout, execution.stdout)
    # echo "/home/swas...../xxx-yyyy-zzz.sh" | at YYYYMMDDHHMM

    execute = subprocess.run(execution, shell=True)
    if execute.returncode != 0:
        print(execute.stderr)
