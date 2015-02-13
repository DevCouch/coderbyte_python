def convert_time_to_min(time):
    if time == "12:00am":
        return 0
    time_split = time.split(":")
    time_min = int(time_split[0]) * 60
    if int(time_split[0]) >= 1 and int(time_split[0]) <= 11 and time_split[1].endswith("pm"):
        time_min += (12 * 60)
    time_min += int(time_split[1][0:-2])
    return time_min    

def CountingMinutesI(str): 

    # code goes here
    times = str.split("-")
    from_time = convert_time_to_min(times[0])
    to_time = convert_time_to_min(times[1])
    if to_time < from_time:
        to_time += (24 * 60)
  
    return to_time - from_time
    
print CountingMinutesI("1:23am-1:08am")
print CountingMinutesI("12:30pm-12:00am")
