import board
import neopixel
import time
 
pixel_pin = board.D2   #the ring data is connected to this pin
num_pixels = 12        #number of leds pixels on the ring
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
 
RED = (255, 0, 0) #RGB
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0,0,0)

 
while True:
    pixels[1] = RED
    pixels.show()     #required to update pixels
    time.sleep(1)
    
    pixels[2] = YELLOW
    pixels.show()
    time.sleep(1)
    
    pixels[0] = GREEN
    pixels.show()
    time.sleep(1)
    
    pixels[5] = CYAN
    pixels.show()
    time.sleep(1)
    
    pixels[4] = BLUE
    pixels.show()
    time.sleep(1)
    
    pixels[3] = PURPLE
    pixels.show()
    time.sleep(1)
    
    pixels[6] = PURPLE
    pixels.show()
    time.sleep(1)
