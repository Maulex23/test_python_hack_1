"""
text: "FOOZIMAN" output => "fooziman"
"""
def lower_change(result):
    def contenedor():
        r = result()
        return r.lower()
    return contenedor


@lower_change
def fn_hack_2():
    result = "FOOZIMAN"
    
    return result