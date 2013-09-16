import pyfirmata
#http://learn.adafruit.com/downloads/pdf/adafruit-arduino-lesson-3-rgb-leds.pdf
#DO NOT USE....Will be hooked up later to POMODORO
#Used common ANODE LED
#LOTS OF CLEAN UP...But, works with 
PORT = '/dev/ttyACM0'
DELAY = 5 # A 2 seconds delay

BOARD = pyfirmata.Arduino(PORT)
RED = BOARD.get_pin('d:11:p') #11
GREEN = BOARD.get_pin('d:10:p') #10
BLUE = BOARD.get_pin('d:9:p') #9

def fade_in(in_secs, from_red, from_green, from_blue, to_red, to_green, to_blue):
    interval = float(in_secs) / 255
    r_inc = float(to_red - from_red) / 255
    g_inc = float(to_green - from_green) / 255
    b_inc = float(to_blue - from_blue) / 255
    set_color(from_red, from_green, from_blue)
    for i in xrange(255):
        set_color(from_red + i * r_inc, from_green + i * g_inc, from_blue + i * b_inc)
        BOARD.pass_time(interval)
    set_color(to_red, to_green, to_blue)
    
def set_color(red,green,blue):
    RED.write(to_analog(255 - red))
    GREEN.write(to_analog(255 - green))
    BLUE.write(to_analog(255 - blue))
    
def to_analog(in_byte):
    return float(in_byte) / 255
    
def main():
    while True:
        set_color(0,255,0) #GREEN
        #fade_in(5, 0,0,0, 0,255,0)
        BOARD.pass_time(15)
        fade_in(5, 0,255,0, 255,255,0)
        BOARD.pass_time(5)
        fade_in(5, 255,255,0, 255,0,0)
        BOARD.pass_time(5)
        fade_in(5, 255,0,0, 0,0,0)
        BOARD.pass_time(DELAY)
        #set_color(128,128,0) #BRONZE
        #board.pass_time(DELAY)
        #set_color(0,0,0) #BLACK
        #board.pass_time(DELAY)
    BOARD.exit()
main()