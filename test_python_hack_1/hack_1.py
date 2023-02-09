"""
text: "fooziman" output => "FOOZIMAN"
"""
def upper_change(result):
    def contenedor():
        r = result()
        return r.upper()
    return contenedor

@upper_change
def fn_hack_1():
    result = "fooziman"
    
    return result  
