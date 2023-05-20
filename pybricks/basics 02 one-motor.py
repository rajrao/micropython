#connect a motor to port E
#this code shows some of the basic commands one can apply to a motor

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#clear the screen to make it easier to read
print("\r\n\r\n\r\n\r\n")

hub = InventorHub()

motor = Motor(Port.E)

# Make some variables to use in the examples
speed = 500     # (deg/s) up to about 1000 for a MINDSTORMS motor
power = 75      # (percent) -100 (reverse) to 100 (forward)
time = 1000     # (ms) (milliseconds)
angle = 180     # (deg)
pos = 270       # (deg) accumulated and relative to 0 position

#run_time
print(f"motor.run_time(speed = {speed}, time = {time})")
motor.run_time(speed = speed, time = time)      
print(f"motor.run_time(speed = {-speed}, time = {time})")
motor.run_time(-speed, time)

wait(1000)
print()
#run_angle
print(f"motor.run_angle(speed = {speed}, rotation_angle = {angle})")
motor.run_angle(speed = speed, rotation_angle = angle)    # rotate by angle
print(f"motor.run_angle(speed = {-speed}, rotation_angle = {angle})")
motor.run_angle(speed = -speed, rotation_angle = angle)    # rotate by angle

wait(1000)
print()
#run_angle angle > 360 and speed = 100
angle = 390
speed = 250
print(f"motor.run_angle(speed = {speed}, rotation_angle = {angle})")
motor.run_angle(speed = speed, rotation_angle = angle)    # rotate by angle
print(f"motor.run_angle(speed = {-speed}, rotation_angle = {angle})")
motor.run_angle(speed = -speed, rotation_angle = angle)    # rotate by angle

print(f"motor.run_target(speed = {speed}, target_angle = 0)")
motor.run_target(speed = speed, target_angle = 0)       # move to 0 position (absolute 0 if not reset)

wait(1000)
print()
angle = 270
print(f"testing different speeds, turn {angle} degrees....")
expected_angle = motor.angle()
print(f"starting angle: {expected_angle}")

#test different speeds
for current_speed in range(-1000, 1000, 100): 
    print(f"motor.run_angle(speed = {current_speed}, rotation_angle = {angle})")
    motor.run_angle(speed = current_speed, rotation_angle = angle)    # rotate by angle
    if (current_speed < 0):
        expected_angle = expected_angle - angle
    elif (current_speed > 0):
        expected_angle = expected_angle + angle
    print(f"current angle: {motor.angle()} expected angle: {expected_angle}")
    wait(1000)
print(f"ending angle: {motor.angle()}. expected angle: {expected_angle}")
wait(1000)
print()

print(f"motor.run_target(speed = {speed}, 0)")
motor.run_target(speed = speed,target_angle = 0)       # move to 0 position (absolute 0 if not reset)
print(f"motor.run_target(speed = {speed},target_angle = {pos})")
motor.run_target(speed = speed,target_angle = pos)     # rotate to target position

print(f"current angle: {motor.angle()}")

wait(1000)
print()
print(f"motor.track_target(target_angle = {pos})")
motor.track_target(target_angle = pos)          # update to new target position
print(f"current angle: {motor.angle()}")

wait(1000)
print()
print("motor.reset_angle(0)")
motor.reset_angle(0) # resets the current angle position to be 0
print(f"current angle: {motor.angle()}")

wait(1000)
print()
print("motor.reset_angle()")
motor.reset_angle() # resets the motor so 0 is where the markers line up
print(f"current angle: {motor.angle()}")
