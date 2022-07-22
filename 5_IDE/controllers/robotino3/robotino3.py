"""robotino3 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Supervisor, Motor, DistanceSensor

# create the Robot instance.
robot = Supervisor()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
motor1 = robot.getDevice('wheel0_joint')
motor2 = robot.getDevice('wheel1_joint')
motor3 = robot.getDevice('wheel2_joint')

#Control the robot in velocity
motor1.setPosition(float('inf'))
motor2.setPosition(float('inf'))
motor3.setPosition(float('inf'))

motor1.setVelocity(0)
motor2.setVelocity(-5)
motor3.setVelocity(5)

distance_sensor = robot.getDevice('ds')
distance_sensor.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    val = distance_sensor.getValue()
    robot.setLabel(0, "distance sensor value: " + str(val), 0, 0, 0.1, 0x000000, 0, "Arial")

    # Process sensor data here.$

    #Uncomment thos lines to make the robot stop before a collision
    # if val > 850:
    #     motor2.setVelocity(0)
    #     motor3.setVelocity(0)



# Enter here exit cleanup code.
