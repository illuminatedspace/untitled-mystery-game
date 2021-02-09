init python:
    def pad_single_digit(num):
        output = str(num)

        if len(output) == 1:
            output = "0" + output

        return output

    def format_time(hour, minute):
        string_hour = str(hour)
        string_minute = str(minute)

        return pad_single_digit(hour) + ":" + pad_single_digit(minute)

screen time_management():
    $ date = "20XX-09-" + str(day + 21) + " " + format_time(hour, minute)
    
    vbox:

        xpos 240
        ypos 5

        text date

init python:
    config.overlay_screens.append("time_management")