# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default form_fields = {
    "subject_name": "default"
}

default notes = "Enter your case notes here."

default subject_name = "default"
default edit_field_name = None

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

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