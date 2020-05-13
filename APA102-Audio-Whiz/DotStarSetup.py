import board
import adafruit_dotstar as dotstar
import math
import random

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


# TODO: Refresh rate?


# Return the maximum brightness value if the power supply used is under the value of the recommended amount
# to prevent bugs and other sorts of bad things happening with the LED strip
def CurrentCompensationF():
    # SI unit from base to the milli(m)
    BaseToMilli = 1000
    # Maximum recommended amount in the LED (From Adafruit documentation it is 60mA per LED)
    MilliMaxPowerLED = 60
    # Total current draw of the LEDs
    CurrentDraw = StripLength * MilliMaxPowerLED / BaseToMilli
    # The current compensation is applied when the PSU amperage would not cut it!
    if CurrentDraw > PowerCurrent:
        print("Warning: The PSU is weak! Apply STR (Amperage) attributes to your PSU current!")
        return PowerCurrent / CurrentDraw
    elif CurrentDraw <= PowerCurrent:
        return 1


# LED STRIP SETUP
led_strip = dotstar.DotStar(board.SCK, board.MOSI, StripLength,
                            brightness=CurrentCompensationF(StripLength, PowerCurrent))


# while True:
#    while StripLength = led_strip_SMT
#        for led_strip_SMT in range(StripLength):
#            led_strip[led_strip_SMT] = (Red_Value, Green_Value, Blue_Value)


def sine_wave_rgb():
    # RGB Base Number 255 is divisor of amplitude of sine wave to get the maximum possible points of the x axis
    # Maybe could be increased to make more smooth wave in the LEDs?
    RGB_Units_Max = 255
    x_rgb_base_unit = float(1 / RGB_Units_Max)
    x_rgb_base_conversion = + x_rgb_base_unit
    # 0 point value should be 0 in the RGB
    # 1 point value should be 255 in the RGB

    # The sine wave amplitudes are -1 and 1, so the prevent the value errors... lets offset by 1!
    sine_wave = math.sin(x_rgb_base_conversion)
    point_value_rgb = 1 + sine_wave
    # As we shifted the values the units have to be shifted by dividing by 2.
    # Returns one unit less than 255 to prevent the Overflow of the 255 value.
    # Make a loop that does not overflow to software, full sine wave is 2*pi!
    while sine_wave >= 2 * math.pi:
        return int(point_value_rgb * ((255 - 1) / 2))
    else:
        #    #Hacky maybe, will it work? I do not know for the life of me...
        #        sine_wave_rgb()
        sine_wave = 0


# To write randomization module
# To write randomizer module?

# Could be replaced with random choices/shuffle?


def random_function_picker():
    rgb_random_decider = random.randint(0, 1)
    if rgb_random_decider == 0:
        return random.shuffle([0, 1, 0], k=3)
    elif rgb_random_decider == 1:
        return random.shuffle([0, 1, 1], k=3)


# Touples the colour values together
def RGB_touple(Red_Value, Green_Value, Blue_Value):
    return (Red_Value, Green_Value, Blue_Value)


# Applied value to the colour
def RGB_sine_wave_mono():
    sine_wave_rgb()


# One random waves of colour
def LED_Strip_sine_wave_mono(  # to add
):
    global led_strip_SMT
    while True:
        # To write and x^2/radial function which randomises the smooth hue in the wave form.
        while StripLength == led_strip_SMT:
            set_colour = random.shuffle([0, 1, 0], k=3)
            for led_strip_SMT in range(StripLength):
                rgb = [j * sine_wave_rgb() for j in set_colour]
                led_strip[led_strip_SMT] = (tuple(rgb))


# Random random waves of colour
def LED_sine_wave_duo(  # to add
):
    global led_strip_SMT
    while True:
        # To write and x^2/radial function which randomises the smooth hue in the wave form.
        while StripLength == led_strip_SMT:
            set_colour = random.shuffle([0, 1, 1], k=3)
            for led_strip_SMT in range(StripLength):
                rgb = [j * sine_wave_rgb() for j in set_colour]
                led_strip[led_strip_SMT] = (tuple(rgb))


def LED_mayhem(  # to add all the defined functions picked by random colours at the same time and random functions,
        # Maybe be cancerous to look at... <.<
):
    global led_strip_SMT
    while True:
        # To write and x^2/radial function which randomises the smooth hue in the wave form.
        while StripLength == led_strip_SMT:

            set_colour = random.shuffle([0, 1, 1], k=3)
            for led_strip_SMT in range(StripLength):
                rgb = [j * sine_wave_rgb() for j in set_colour]
                led_strip[led_strip_SMT] = (tuple(rgb))

