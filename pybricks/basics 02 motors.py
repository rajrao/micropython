from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

print("\r\n\r\n\r\n\r\n")

hub = InventorHub()

left_wheel = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B)    # default positive direction is clockwise

# Make some variables to use in the examples
speed = 500     # (deg/s) up to about 1000 for a MINDSTORMS motor
power = 75      # (percent) -100 (reverse) to 100 (forward)
time = 1000     # (ms) (milliseconds)
angle = 180     # (deg)
pos = 270       # (deg) accumulated and relative to 0 position

print(f"left_wheel.dc(duty = {power})")
left_wheel.dc(duty = power) # run at % power (duty cycle), until next command
wait(1000)

left_wheel.stop()
wait(1000)

print(f"left_wheel.dc(duty = {-power})")
left_wheel.dc(duty = -power) # negative power goes backwards, until next command
wait(1000)

print(f"right_wheel.run(speed = {speed})")
right_wheel.run(speed = speed)     # accelerate to speed, maintain until told different 
wait(1000)

print("right_wheel.stop()")
right_wheel.stop()
wait(1000)

print(f"right_wheel.run(speed = {-speed})")
right_wheel.run(speed = -speed)    # negative speed goes backwards
wait(1000)

print("right_wheel.stop()")
right_wheel.stop()
print(left_wheel.stop())
left_wheel.stop()
wait(1000)

print(f"right_wheel.run(speed = 1000)")
right_wheel.run(speed = 1000)
wait(1000)

print(f"right_wheel.run(speed = 0)")
right_wheel.run(speed = 0) # controlled deceleration to 0 speed
wait(1000)

print(f"right_wheel.run(speed = 1000)")
right_wheel.run(speed = 1000)
wait(1000)

print("right_wheel.stop()")
right_wheel.stop() #The motor gradually stops due to friction.
wait(1000)

print(f"right_wheel.run(speed = 1000)")
right_wheel.run(speed = 1000)
wait(1000)

print("right_wheel.brake()")
right_wheel.brake() #The motor stops due to friction, plus the voltage 
                    #that is generated while the motor is still moving.
wait(1000)

print(f"right_wheel.run(speed = 1000)")
right_wheel.run(speed = 1000)
wait(1000)

print("right_wheel.hold()")
right_wheel.hold() #Stops the motor and actively holds it at its current angle.
wait(1000)

print(f"right_wheel.run(speed = 1000)")
right_wheel.run(speed = 1000)
wait(1000)

print(f"right_wheel.run(speed = 0)")
right_wheel.run(speed = 0)         # controlled deceleration to 0 speed
wait(1000)
