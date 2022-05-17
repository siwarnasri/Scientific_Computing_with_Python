def add_time(start, duration, starting_day=""):
    #
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    # Separte the start into time and format, then separate the time into hours and minutes
    arguments = start.split()
    start_time = arguments[0].split(":")
    start_hour = start_time[0]
    start_min = start_time[1]
    # AM, PM ending format
    start_ending = arguments[1]
    # Separate the duration into hours and minutes
    duration_time = duration.split(":")
    duration_hour = duration_time[0]
    duration_min = duration_time[1]
 
    if int(start_min) not in [*range(60)] or int(duration_min) not in [*range(60)]:
      return print("Error: minutes should be less then 60")
    elif not int(start_hour) in [*range(12)] :
      return print("Error : start hour should be in the 12-hour clock format")
    elif starting_day.lower().capitalize() not in week_days and starting_day != "":
      return print("Error: the start day's name should be a valid day:")
    elif start_ending not in ["AM", "PM"]:
      return print("Error: the start time ending should be an 'AM' or a 'PM')")

    else:

      # Calculate 24-hour clock format
      if start_ending == "PM" :
        start_hour = int(start_hour) + 12 

      # Add hours and minutes
      new_min = int(start_min) + int(duration_min)
      new_hour = int(start_hour) + int(duration_hour)
      if new_min >= 60:
        new_min -= 60
        new_hour += 1
      new_day = 0
      if new_hour >=24:
        new_day = new_hour // 24
        new_hour -= new_day * 24
      
      # Find AM and PM
      # Return to 12-hour clock format
      new_ending = ""
      if new_hour < 12 :
          new_ending = "AM"
      elif new_hour >= 12 :
          new_ending = "PM"
          new_hour -= 12
      

      if new_day == 1 :
        days_later = " (next day)"
      elif new_day > 1 :
        days_later = " (" + str(new_day) + " days later)"
      else :
        days_later = ""

      if starting_day != "":
          weeks = new_day // 7
          i = week_days.index(starting_day.lower().capitalize()) + (new_day - 7 * weeks)
          if i > 6 :
              i -= 7
          day = ", " + week_days[i]
      else :
          day = ""    
      new_time= str(new_hour) + ":" + \
          (str(new_min) if new_min > 9 else ("0" + str(new_min))) + \
          " " + new_ending + day + days_later
      return new_time