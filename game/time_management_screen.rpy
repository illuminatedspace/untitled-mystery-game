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

style datetime_textbutton:
    color "#B3DCD9"

screen time_management():
    $ date = "20XX-09-" + str(day + 21) + " " + format_time(hour, minute)
    
    vbox:

        xpos 240
        ypos 5

        textbutton date:
            text_style "datetime_textbutton"
            action NullAction()

init python:
    config.overlay_screens.append("time_management")