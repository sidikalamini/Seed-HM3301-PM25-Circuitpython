import board
from seeed_hm3301 import HM3301_I2C
import time


i2c = board.I2C()

hm3301 = HM3301_I2C(i2c, address=0x40)


while True:
    PM25 = hm3301.PM_2_5_conctrt_std
    PM1 = hm3301.PM_1_0_conctrt_std
    PM10 = hm3301.PM_10_conctrt_std

    print("PM2.5 : "+str(PM25))
    print("PM1.0 : "+str(PM1))
    print("PM10 : "+str(PM10))
    time.sleep(5)



