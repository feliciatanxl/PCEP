hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

mins += duration
hour += mins // 60
mins = mins % 60
hour = hour % 24
print("End time: ", hour, ":", mins, sep="")