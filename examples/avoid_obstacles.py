import picar_4wd as fc
from picar_4wd.servo import Servo
from picar_4wd.ultrasonic import Ultrasonic
import time
import random

'''
This is my naive mapping algorithm for the Picar that I built for CS 437 IoT. The task 
is to write a program that uses the ultrasonic sensor to detect obstacles that come 
within several centimeters of your car's front bumper. When your car gets within that 
obstacle, it should stop, choose another random direction, back up and turn, and then 
move forward in the new direction.
'''

speed = 20

def main():

    while True:
        
        # Assume the car is in an idle position when scanning environment
        scan_list = fc.scan_step(30)
        ''''
        scan_step(int) returns a a list of 0s, 1s, or 2s.
        input int the upper range of how far out the ultrasonic sensor 
        Default is 10 different steps, one for every 18 degress. 
        
        Records ultrsonic distances and gives a value of 0, 1, or 2
        for each 18 degree step the servo turns:
        0 = Something right in front of car
        1 = Something was detected in between lower and upper range, 10 (default) and 30 (input)
        2 = Nothing in front of the car or too far away / out of bounds
        '''       
        
        # If you do not have any measurements, the scan_list is empty.
        if not scan_list:

            # Sends you at the beginning of the while loop until scan_list is true
            continue

        # One items are in scan list with obstacle information, do:
        # Check middle values only because you are only going forward
        tmp = scan_list[3:7] # only look at what is in front of car
        print(f'tmp= {tmp}')
       
        '''
        From idle position, scan a full reading of environment. 
        When obstacles are detected, Choose random direction to turn.
        Reverse. Take baby steps to gain the momentum to 
        transition into a smooth turn.Turn in the randomly chosen direction. 
        Stop after turn. Iterate the while loop and repeat process at new position.
        '''
        
        if (tmp != [2,2,2,2]) and (tmp != [2,2]):
    
            print("STOP! Obstacle Found!")

            # Choose random direction
            directions = ["left", "right" ]
            random_direction = random.choice(directions)

            # Turn in the randomly chosen direction
            if random_direction=="left":
                #reverse()
                #baby_steps()
                #fc.turn_left(speed) 
                time.sleep(0.5)
                # Stop the Picar so that it can be idle for when the
                # while loop repeats from start
                fc.stop() 

            elif random_direction=="right":
                #reverse()
                #baby_steps()
                #fc.turn_right(speed) # function runs until it sleeps
                time.sleep(0.5)
                # Stop the Picar so that it can be idle for when the
                # while loop repeats from start
                fc.stop() 
        
        else:
            print("No Obstacle Found. PROCEED!")
            #forward() 
            time.sleep(0.25) 
            fc.stop()

# Move car forward                 
def forward():
    speed2 = fc.Speed(25)
    speed2.start()
    time.sleep(0.25)
    fc.forward(100)
    x = 0
    for i in range(3):
        time.sleep(0.1)
        speed = speed2()
        x += speed * 0.1
    speed2.deinit()
    fc.stop()

# Move car in reverse
def reverse():
    speed2 = fc.Speed(25)
    speed2.start()
    time.sleep(0.25)
    fc.backward(100)
    x = 0
    for i in range(2):
        time.sleep(0.05)
        speed = speed2()
        x += speed * 0.1
    speed2.deinit()
    fc.stop()

'''
Moves car in baby steps. When driving, you 
don't immediately swerve to a new direction 
when you want to turn to avoid an obstacle. You 
take small baby steps ahead so you can gain 
momentum to transition into a smooth turn,
and then you turn. 
'''
def baby_steps():
    print("Take a few Baby Steps Forward!")
    speed3 = fc.Speed(10)
    speed3.start()
    time.sleep(1)
    fc.forward(100)
    x = 0
    for i in range(1):
        time.sleep(0.1)
        speed = speed3()
        x += speed * 0.1
    speed3.deinit()
    fc.stop()

if __name__ == "__main__":
   try:
       main()
   finally:
       fc.stop()


