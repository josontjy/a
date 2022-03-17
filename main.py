a = 0

def on_forever():
    global a
    a += 1
basic.forever(on_forever)
