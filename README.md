# Internet Cat Feeder
Raspberry Pi internet-enabled cat feeder using the PicoBorg Reverse.    

I wanted to have a way to feed my cats while I am out of town, so I started this project. A Raspberry Pi is connected to a PicoBorg Reverse which is then connected to a battery pack and a 125oz. stepper motor. The stepper will be connected to a dry food dispenser to turn the handle the specified amount (currently 1080 deg for normal and 2160 for "large") or attempt to unjam the feeder. Please note that I do not recommend opening this up to the internet quite yet unless you want to have the whole world feed your cats (or worse).

**Links to things I've used in this project:**  
Raspberry Pi Model B - http://www.raspberrypi.org/products/model-b/  
PicoBorg Reverse - https://www.piborg.org/picoborgrev  
Sparkfun NEMA 23 125oz. stepper motor - https://www.sparkfun.com/products/10847  
Zevro WM100 dry food dispenser - http://www.amazon.com/WM100-Indispensable-SmartSpace-Wall-Mounted-Dispenser/dp/B0009MGQUC
Sparkfun 4xAA battery pack - https://www.sparkfun.com/products/12083  
Sparkfun 1/4" x 4" D-shaft - https://www.sparkfun.com/products/12165  
Sparkfun 1/4" to 1/4" shaft coupler - https://www.sparkfun.com/products/12251  
Topcoat - http://topcoat.io/topcoat/

To Do:
[ ] - Add a live(ish) stream to monitor hopper, bowls, and cats
[ ] - Fix logging to write to a location readable by the web server
[ ] - Make the web interface not as ugly
[ ] - Write up mounting instructions (still designing)
