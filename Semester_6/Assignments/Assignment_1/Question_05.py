import re

class Time:
    def __init__(self, time_str):
        self.time_str = time_str
        self.hours, self.minutes, self.seconds = 0, 0, 0
        if self.is_valid_time():
            self.hours, self.minutes, self.seconds = map(int, self.time_str.split(":"))
        else:
            self.hours, self.minutes, self.seconds = None, None, None

    def is_valid_time(self):
        time_pattern = r'^[0-2][0-9]:[0-5][0-9]:[0-5][0-9]$'
        if re.match(time_pattern, self.time_str):
            hours, minutes, seconds = map(int, self.time_str.split(":"))
            if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
                return True
        return False

    def convert_to_12_hour_format(self):
        if self.hours is None:
            return "Invalid time format"

        period = "AM"
        if self.hours >= 12:
            period = "PM"
            if self.hours > 12:
                self.hours -= 12
        elif self.hours == 0:
            self.hours = 12

        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} {period}"


time_input = input("Enter time in HH:MM:SS format (24-hour): ")
time_obj = Time(time_input)

if time_obj.is_valid_time():
    print("Converted time in 12-hour format:", time_obj.convert_to_12_hour_format())
else:
    print("Invalid time format. Please enter time in the correct HH:MM:SS format.")