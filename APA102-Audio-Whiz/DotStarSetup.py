import board
import adafruit_dotstar as dotstar
import math
import random
import time

# // TODO:
# // To add MOAR dots! Ahkhem... I mean more comments
# // Create a base line values (Config.py module?)
# // To convert the base code into "def"-s a.la. to OOB'ify it
# // Create a sine wave module for the LED WAVE
# // Rainbow?
# // Audio reactive
# // Fourier series wave??


# CONFIG!
# The amount of LED on the strip
StripLength = 300
# The amperage of the power supply
PowerCurrent = 10

dividing_point = StripLength//3 #At what index the colours will be shifted



# TODO: Refresh rate?


# Return the maximum brightness value if the power supply used is under the value of the recommended amount
# to prevent bugs and other sorts of bad things happening with the LED strip
def CurrentCompensationF(StripLength, PowerCurrent):
    # SI unit from base to the milli(m)
    BaseToMilli = 1000
    # Maximum recommended amount in the LED (From Adafruit documentation it is 60mA per LED)
    MilliMaxPowerLED = 90
    # Total current draw of the LEDs
    CurrentDraw = StripLength * MilliMaxPowerLED / BaseToMilli
    # The current compensation is applied when the PSU amperage would not cut it!
    if CurrentDraw > PowerCurrent:
        print("Warning: The PSU is weak! Apply STR (Amperage) attributes to your PSU current!")
        return PowerCurrent / CurrentDraw
    elif CurrentDraw <= PowerCurrent:
        return 1


# LED STRIP SETUP
led_strip = dotstar.DotStar(board.SCK, board.MOSI, (StripLength + dividing_point),
                            brightness=CurrentCompensationF(StripLength, PowerCurrent))


# while True:
#    while StripLength = led_strip_SMT
#        for led_strip_SMT in range(StripLength):
#            led_strip[led_strip_SMT] = (Red_Value, Green_Value, Blue_Value)

x_rgb_base_conversion = 0
point_value_rgb = 0
def sine_wave_rgb():
    global x_rgb_base_conversion
    global point_value_rgb
    while 312 == 312:
    #while True:
    # RGB Base Number 255 is divisor of amplitude of sine wave to get the maximum possible points of the x axis
    # Maybe could be increased to make more smooth wave in the LEDs?
        RGB_Units_Max = 255
        x_rgb_base_unit = float(1 / RGB_Units_Max)
        x_rgb_base_conversion = x_rgb_base_conversion + x_rgb_base_unit
    # 0 point value should be 0 in the RGB
    # 1 point value should be 255 in the RGB

    # The sine wave amplitudes are -1 and 1, so the prevent the value errors... lets offset by 1!
        sine_wave = math.sin(x_rgb_base_conversion)
        point_value_rgb = 1 + sine_wave
    # As we shifted the values the units have to be shifted by dividing by 2.
    # Returns one unit less than 255 to prevent the Overflow of the 255 value.
    # Make a loop that does not overflow to software, full sine wave is 2*pi!
        return int(point_value_rgb * ((255 - 3) / 2))


# To write randomization module
# To write randomizer module?

# Could be replaced with random choices/shuffle?


def random_function_picker():
    rgb_random_decider = random.randint(0, 1)
    if rgb_random_decider == 0:
        list = [0, 1, 0]
        random.shuffle(list)
        return list
    elif rgb_random_decider == 1:
        list = [0, 1, 1]
        random.shuffle(list)
        return list



# Touples the colour values together
def RGB_touple(Red_Value, Green_Value, Blue_Value):
    return (Red_Value, Green_Value, Blue_Value)


# Applied value to the colour
def RGB_sine_wave_mono():
    sine_wave_rgb()


# One random waves of colour
def LED_Strip_sine_wave_mono(  # to add
):
    led_strip_SMT = len(led_strip)
    while True:
        # To write and x^2/radial function which randomises the smooth hue in the wave form.
        while StripLength == led_strip_SMT:
            set_colour = random.shuffle([0, 1, 1-sine_wave])
            for led_strip_SMT in range(StripLength):
                rgb = [j * sine_wave_rgb() for j in set_colour]
                led_strip[led_strip_SMT] = (tuple(rgb))
            time.sleep(0.25)



# Random random waves of colour
def LED_sine_wave_duo(  # to add
):
    led_strip_SMT = led_strip
    while True:
        # To write and x^2/radial function which randomises the smooth hue in the wave form.
        while StripLength == led_strip_SMT:
            set_colour = random.shuffle([0, 1, 1 - float(point_value_rgb)])
            for led_strip_SMT in range(StripLength):
                rgb = [j * sine_wave_rgb() for j in set_colour]
                led_strip[led_strip_SMT] = (tuple(rgb))


def LED_mayhem(  # to add all the defined functions picked by random colours at the same time and random functions,
        # Maybe be cancerous to look at... <.<
):
    led_strip_SMT1 = len(led_strip)
    led_strip_SMT2 = len(led_strip)
    while True:
        # To write and x^2/radial function which randomises the smooth hue in the wave form.
        while (StripLength + dividing_point) == led_strip_SMT1:
            set_colour  = random_function_picker()
            set_colour2 = random_function_picker()
            for led_strip_SMT1 in range(StripLength):
                rgb1 = ([int(j * sine_wave_rgb()) for j in set_colour])
                rgb2 = ([int(j * sine_wave_rgb()) for j in set_colour2])
                led_strip[led_strip_SMT1] = (tuple(rgb1))
                led_strip[led_strip_SMT1-(dividing_point)] = (tuple(rgb2))
        LED_mayhem()
        
def LED_mayhem1(  # to add all the defined functions picked by random colours at the same time and random functions,
        # Maybe be cancerous to look at... <.<
):
    led_strip_SMT1 = len(led_strip)
    led_strip_SMT2 = len(led_strip)
    while True:
        # To write and x^2/radial function which randomises the smooth hue in the wave form.
        while (StripLength + dividing_point) == led_strip_SMT1:
            set_colour  = [0.1, 0, 1]
            set_colour1 = [1, 0, 1]
            set_colour2 = [1, 1, 1]
            for led_strip_SMT1 in range(StripLength):
                rgb0 = ([int(j * 255) for j in set_colour])
                rgb1 = ([int(j * 255) for j in set_colour1])
                rgb2 = ([int(j * 255) for j in set_colour2])
                led_strip[led_strip_SMT1] = (tuple(rgb1))
                led_strip[led_strip_SMT1-(dividing_point)] = (tuple(rgb2))
                led_strip[led_strip_SMT1-((dividing_point)*3)] = (tuple(rgb2))
        LED_mayhem1()
                