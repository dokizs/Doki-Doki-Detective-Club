init python:
    def destroy_persistent():
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswith("_"):
                setattr(persistent, attr, None)
        renpy.reload_script()
return