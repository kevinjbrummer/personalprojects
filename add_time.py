def add_time(start, duration, day=None):
    colon = 0
    space = 0
    for i in range(len(start)):
      if start[i] == ":":
        colon = i
      if start[i] == " ":
        space = i
    hour = int(start[0:colon])
    minute = int(start[colon + 1 :space])
    apm = start[space + 1:]
    for i in range(len(duration)):
        if duration[i] == ":":
            colon = i
    change_hour = int(duration[0:colon])
    change_minute = int(duration[colon +1:])

    if (minute + change_minute) < 60:
        new_minute = minute + change_minute
    else:
        new_minute = (minute + change_minute) - 60
        change_hour = change_hour + 1
    if new_minute < 10:
        new_minute = "0" + str(new_minute)
    else:
        new_minute = str(new_minute)
        
    days = 0
    if change_hour >= 24:
        days = int(change_hour / 24)
        change_hour = change_hour - (days * 24)

    if change_hour >=12:
        if apm == "AM":
            apm = "PM"
        else:
            apm = "AM"
            days = days + 1
        change_hour = change_hour - 12
    if (hour + change_hour) > 12:
        if apm == "AM":
            apm = "PM"
        else:
            apm = "AM"
            days = days + 1
        new_hour = (hour + change_hour) - 12
    elif (hour + change_hour) == 12:
        if apm == "AM":
            apm = "PM"
        else:
            apm = "AM"
            days = days + 1
        new_hour = hour + change_hour
    else:
        new_hour = hour + change_hour


    if day != None:
            day = day.lower()
            date = {0:"monday", 1:"tuesday", 2:"wednesday",
            3:"thursday", 4:"friday", 5:"saturday",
            6:"sunday"}
            date_keys = list(date.keys())
            date_values = list(date.values())
            index = 0
            for i in range(len(date_values)):
                if date_values[i] == day:
                    index = i
            change_days = 0
            if days%7 !=0:
                change_days = days - 7 * int((days/7))
              

            
            if days == 0:
                day = day[0].upper() + day[1:]
                return "%i:%s %s, %s" % (new_hour, new_minute, apm, day)
            elif days == 1:
                return "%i:%s %s, %s (next day)" % (new_hour, new_minute, apm,
                                                    (date[index+1][0].upper() +
                                                     date[index+1][1:]))
            elif days == 7:
                return "%i:%s %s, %s (%i days later)" % (new_hour, new_minute,
                                             apm,(date[index][0].upper() +
                                                 date[index][1:]), days)
            else:
                if index + change_days < 7:
                    return "%i:%s %s, %s (%i days later)" % (new_hour, new_minute,
                                             apm,(date[index+change_days][0].upper() +
                                                 date[index + change_days][1:]), days)
                else:
                    index = (index + change_days) - 7
                    return "%i:%s %s, %s (%i days later)" % (new_hour, new_minute,
                                             apm,(date[index][0].upper() +
                                                 date[index][1:]), days)

    else:
        if days == 0:
            return "%i:%s %s" % (new_hour, new_minute, apm)
        elif days == 1:
            return "%i:%s %s (next day)" % (new_hour, new_minute, apm)
        else:
            return "%i:%s %s (%i days later)" % (new_hour, new_minute,
                                             apm, days)


print(add_time("2:03 PM", "543:47", "Monday"))
