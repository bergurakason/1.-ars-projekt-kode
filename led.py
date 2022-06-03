from gpiozero import LED

green = LED(26)
yellow = LED(19)
red = LED(13)

def green_on():
    green.on()
    yellow.off()
    red.off()

def red_on():
    red.on()
    yellow.off()
    green.off()

def yellow_on():
    yellow.on()
    red.off()
    green.off()

def off():
    yellow.off()
    red.off()
    green.off()