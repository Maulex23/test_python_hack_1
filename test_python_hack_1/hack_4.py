"""
text: "fooziman" output => "foozimaN"
"""
def replace_change(result):
    def contenedor():
        r = result()
        return r.replace("n", "N")
    return contenedor

@replace_change
def fn_hack_4():
    result = "fooziman"
    
    return result