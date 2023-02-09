"""
text: "fooziman" output => "Fooziman"
"""
def capitalize_change(result):
    def contenedor():
        r = result()
        return r.capitalize()
    return contenedor


@capitalize_change
def fn_hack_3():
    result = "fooziman"
    
    return result