#impotring libraries
import machine
import utime
#making variables
sensor = machine.ADC(28)

while True:
    value=sensor.read_u16()
    print(value)
    utime.sleep_ms(200)