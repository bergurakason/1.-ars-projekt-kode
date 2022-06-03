from numpy import True_
import smbus
import time
import led

bus = smbus.SMBus(1)
i2c_address = 0x49


god_luft = 50

Dårlig_luft = 25

max_val = 1023


def get_data():

    rd = bus.read_word_data(i2c_address, 0)

    data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)

    adc_val = data >> 2
    air_quality = 100- ((adc_val/max_val) * 100.0)
    percentage = format(air_quality, '.2f')
    
    print("luftkvalitet procent: ", percentage)
    print(adc_val)
    return air_quality

def air_quality():
    current_qual = get_data()

    if current_qual > god_luft:
        print("Luften er god")
        led.green_on()
        return current_qual

    elif Dårlig_luft < current_qual <= god_luft:
        print("Luften er ikke super")
        led.yellow_on()
        return current_qual

    elif current_qual <= Dårlig_luft:
        print("Luften er meget dårlig")
        led.red_on()
        return current_qual