def add_time(start_time, duration_time, *optional):
    hours = 0
    minutes = 0
    format = ""
    days = 0
    formula_days = ""
    formula_later = ""

    #adding start_time minutes and duratio_time minutes
    start_minutes_positoner = start_time.find(":") + 1
    start_minutes = int(start_time[start_minutes_positoner: start_minutes_positoner + 2])

    duration_minutes_positioner = duration_time.find(":") + 1
    duration_minutes = int(duration_time[duration_minutes_positioner: duration_minutes_positioner + 2])
    
    minutes_combined = start_minutes + duration_minutes

    added_hours = 0
    while minutes_combined > 59:
        added_hours += 1
        minutes_combined -= 60
    minutes = minutes_combined
    if minutes < 10:
        minutes = "0" + str(minutes)


    #conting start_time hours and duration_time hours
    start_hours = int(start_time[:start_time.find(':')])
    if start_time[-2:] == "PM":                                                #format to 24h
        start_hours += 12
    
    duration_hours = int(duration_time[:duration_time.find(':')])

    hours_combined = start_hours + duration_hours + added_hours
    days = hours_combined // 24

    while hours_combined > 24:
        hours_combined -= 24
    if hours_combined > 12:                                                    #format back to AM/PM
        hours = hours_combined - 12
        format = "PM"
    else:                                                                      #format back to AM/PM
        hours = hours_combined
        format = "AM"
    if hours == 12:                                                            # 24:12 = 12:12AM, 12:32 = 12:32PM
        if format == "PM":
            format = "AM"
        else:
            format = "PM"

    helper_days = False                                                             #used to return result with ","!!!!
    days_list = ["Monday", "tuesday", "Wednesday", "Thursday", "Friday", "saturDay", "Sunday"]
    try:
        optional = optional[0]

    except:
        pass
    if optional in days_list:
        day = days_list.index(optional)
        skip = days

        combined = day + skip
        while combined > 6:
            combined -= 7
        
        formula_days = days_list[combined]
        helper_days = True
    
    helper_later = False
    if days > 0:
        if days == 1:
            formula_later += "(next day)"
        else:
            formula_later += f"({days} days later)"
        helper_later = True

    return str(f"{hours}:{minutes} {format}" + (", " + formula_days) * helper_days + (" " + formula_later) * helper_later)









