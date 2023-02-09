"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""
def cbm(char: str):
    change = {"o": "0",
              "i": "1",  
              "a": "@"}
    for b, a in change.items():
        char = char.replace(b, a)
    return char.upper()


def fn_hack_10():
    result = "fooziman"
    result = list(map(cbm, result))
    return result  