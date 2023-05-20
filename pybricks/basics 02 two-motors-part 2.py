#runs 2 motors at the same time
#shows how stopping works

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

print("\r\n\r\n\r\n\r\n")

hub = InventorHub()

left_wheel = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B)    # default positive direction is clockwise

wait(1000)
print()

print(f"right_wheel.run(speed = 1000)")
right_wheel.run(speed = 1000)
print(f"left_wheel.run(speed = 1000)")
left_wheel.run(speed = 1000)
wait(1000)
print()

print(f"right_wheel.run(speed = 0)")
right_wheel.run(speed = 0) # controlled deceleration to 0 speed
print(f"left_wheel.run(speed = 0)")
left_wheel.run(speed = 0) # controlled deceleration to 0 speed
wait(1000)
print()

print(f"right_wheel.run(speed = 500)")
right_wheel.run(speed = 500)
print(f"left_wheel.run(speed = 500)")
left_wheel.run(speed = 500)
wait(1000)
print()

print("right_wheel.stop()")
right_wheel.stop() #The motor gradually stops due to friction.
print("left_wheel.stop()")
left_wheel.stop() #The motor gradually stops due to friction.
wait(1000)
print()

print(f"right_wheel.run(speed = 750)")
right_wheel.run(speed = 750)
print(f"left_wheel.run(speed = 750)")
left_wheel.run(speed = 750)
wait(1000)
print()

print("right_wheel.brake()")
right_wheel.brake() #The motor stops due to friction, plus the voltage 
                    #that is generated while the motor is still moving.
print("left_wheel.brake()")
left_wheel.brake() #The motor stops due to friction, plus the voltage 
                    #that is generated while the motor is still moving.
wait(1000)
print()

print(f"right_wheel.run(speed = -800)")
right_wheel.run(speed = -800)
print(f"left_wheel.run(speed = -800)")
left_wheel.run(speed = -800)
wait(1000)
print()

print("right_wheel.hold()")
right_wheel.hold() #Stops the motor and actively holds it at its current angle.
print("left_wheel.hold()")
left_wheel.hold() #Stops the motor and actively holds it at its current angle.
wait(1000)
print()
