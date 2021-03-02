init python:
    import datetime

    starting_year = 2091
    starting_month = 9
    starting_day = 21
    staring_hour = 10
    starting_minute = 0

    default.day2 = (starting_day + 1, 8, 11)

    # Initialize the starting date time
    starting_date_time = datetime.datetime(starting_year, starting_month, starting_day, staring_hour, starting_minute)
    default.current_time = starting_date_time

    def advance_time(hour_to_advance, minutes_to_advance):
        default.current_time = default.current_time + datetime.timedelta(hours=hour_to_advance, minutes=minutes_to_advance)

    def set_time(day, hour, minute):
        default.current_time = default.current_time.replace(day=day, hour=hour, minute=minute)

style datetime_textbutton:
    color "#B3DCD9"

screen time_management():
    $ date = default.current_time.strftime("%Y-%m-%d %H:%M")
    
    vbox:

        xpos 240
        ypos 5

        textbutton date:
            text_style "datetime_textbutton"
            action NullAction()

init python:
    config.overlay_screens.append("time_management")