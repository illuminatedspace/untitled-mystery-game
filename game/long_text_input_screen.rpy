#### Long Form Text Input Read
screen long_text_input_read:

    frame:
        xalign 0.5
        ypos 50
        vbox:
            text "[store.notes]"
            textbutton "Edit" action Show('long_text_input_write')

#### Long Form Text Input Edit
screen long_text_input_write:

    frame:
        xalign 0.5
        ypos 50
        xsize 800
        ysize 600
        has vbox
        label "Notes"
        $ notes_key = len(notes_dict)
        $ current_note = notes_dict[0]
        text "[notes_key]"
        text "[current_note]"
        input:
            default current_note
            value DictInputValue(notes_dict, 0)
            length 300

        textbutton "done" action Return()

screen edit_notes_button:
    textbutton "Edit Notes":
        action ShowMenu('long_text_input_write')
        xalign 0.5
        ypos 50
