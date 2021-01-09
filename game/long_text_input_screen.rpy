#### Long Form Text Input Read
screen long_text_input_read:
    tag case

    frame:
        xalign 0.5
        ypos 50
        vbox:
            text "[store.notes]"
            textbutton "Edit" action Show('long_text_input_write')

#### Long Form Text Input Edit
screen long_text_input_write:
    tag case

    frame:
        xalign 0.5
        ypos 50
        vbox:
            text "[store.notes]"