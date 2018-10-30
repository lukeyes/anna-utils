import I2C_LCD_driver
import socket
import fcntl
import struct
import time

mylcd = I2C_LCD_driver.lcd()

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be connected
        s.connect(('10.255.255.255',1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

while True:
    mylcd.lcd_clear()
    mylcd.lcd_display_string("IP ADDRESS:",1)
    ip_address = get_ip_address()
    print ip_address
    mylcd.lcd_display_string(ip_address, 2)    
    time.sleep(5)
