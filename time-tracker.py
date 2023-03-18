import datetime

# create an empty list to hold time entries
time_entries = []

# loop to prompt for time entries
while True:
    # prompt for client, project, and description of work
    client = input("Client: ")
    project = input("Project: ")
    description = input("Description of work: ")

    # get the start time
    start_time = datetime.datetime.now()

    # prompt for end time
    while True:
        end_time_str = input("End time (HH:MM) or 'now' for current time: ")
        if end_time_str.lower() == "now":
            end_time = datetime.datetime.now()
            break
        try:
            end_time = datetime.datetime.strptime(end_time_str, "%H:%M")
            end_time = datetime.datetime.combine(start_time.date(), end_time.time())
            break
        except ValueError:
            print("Invalid time format. Please enter in HH:MM format or 'now' for current time.")

    # add the time entry to the list
    time_entries.append([start_time, end_time, client, project, description])

    # prompt for completion
    done = input("Type 'done' to exit or press enter to continue: ")
    if done == "done":
        break

# create CSV file with time entries for the day
filename = f"time_entries_{start_time.date()}.csv"
with open(filename, "w") as file:
    file.write("Date,Start Time,End Time,Client,Project,Description\n")
    for entry in time_entries:
        file.write(f"{entry[0].date()},{entry[0].time()},{entry[1].time()},{entry[2]},{entry[3]},{entry[4]}\n")
