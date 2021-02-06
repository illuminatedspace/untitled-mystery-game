default day = 0
init python:
    def advance_day():
        day = day + 1

screen time_management():
    $ date = "20XX-09-" + str(day + 21)
    
    vbox:

        xpos 240
        ypos 5

        text date
        textbutton "advance day" action Function(advance_day) 

init python:
    config.overlay_screens.append("time_management")