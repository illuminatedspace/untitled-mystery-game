﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define nvl_notes = Character("IO Jones", kind=nvl)

default form_fields = {
    "subject_name": "default"
}

default notes = "Enter your case notes here."
default notes_list = ["A note", "another note"]
default notes_dict = {0: "pikachu", 1: "bulbasaur"}

default subject_name = "default"
default edit_field_name = None
default edit_notes = False
default note = ""

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene glass_main

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    nvl show

    nvl_notes "You've created a new Ren'Py game."

    nvl_notes "This is the first text This is the first text This is the first text This is the first text This is the first text This is the first text This is the first text This is the first text This is the first text This is the first text"
    nvl_notes "This is the second text"
    nvl_notes "This is the third text"
    nvl_notes "This is the fourth text"
    nvl_notes "This is the fifth text"
    nvl_notes "This is the sixth text"
    nvl_notes "This is the seventh text"
    nvl_notes "This is the eighth text"
    nvl_notes "This is the ninth text"
    nvl_notes "This is the tenth text"
    nvl_notes "This is the eleventh text"
    nvl_notes "This is the twelvth text"
    nvl_notes "This is the thirteenth text"
    nvl_notes "This is the fourteenth text"
    nvl_notes "This is the fifteenth text"

    # This ends the game.

    menu:
        e "do you want to go to case?"

        "Yes":
            jump case

        "No":
            pass

    return

label case:
    show screen case_form

    menu:
        "edit":
            hide screen case_form
            jump case_edit_option
        "close":
            hide screen case_form
            jump start

    e "This is the case form"

label case_edit_option:
    menu:
        e "What entry would you like to edit?"

        "Subject Name":
            $ edit_field_name = 'subject_name'
            jump case_edit

        "Cancel":
            jump case

label case_edit:
    python:
        form_fields[edit_field_name] = renpy.input("enter new value")
        form_fields[edit_field_name] = form_fields[edit_field_name].strip()
        edit_field_name = None

    jump case

label notes:
    nvl show
    show screen edit_notes_button
    $ pointer = 0

    while pointer < len(notes_dict):
        $ current_note = notes_dict[pointer]
        nvl_notes "[pointer] [current_note]"
        $ pointer = pointer + 1

    nvl_notes "end of notes"

    return