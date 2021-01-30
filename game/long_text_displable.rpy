init python:

    class LongText(renpy.Displayable):

        def __init__(self, **kwargs):
            super(LongText, self, **kwargs).__init__(**kwargs)

            self.width = 200
            self.height = 200

            # self.child = renpy.displayable(child)

        def render(self, width, height, st, at):

            input_child = renpy.input("Editing Notes", default=store.notes)

            child_render = renpy.render(input_child, width, height, st, at)

            render = renpy.Render(self.width, self.height)

            render.blit(child_render, (0,0))

            return render