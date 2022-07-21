"""Braitenberg-based obstacle-avoiding robot controller."""
#################### IMPORTS AND INITIALIZATION ###########################

from controller import Robot

# Get reference to the robot.
robot = Robot()

# Get simulation step length.
TIME_STEP = int(robot.getBasicTimeStep())

# Constants of the Thymio II motors and distance sensors.
maxMotorVelocity = 9.53
distanceSensorCalibrationConstant = 360

# Get left and right wheel motors.
leftMotor = robot.getDevice('motor.left')
rightMotor = robot.getDevice('motor.right')

# Get frontal distance sensors.
outerLeftSensor = robot.getDevice('prox.horizontal.0')
centralLeftSensor = robot.getDevice('prox.horizontal.1')
centralSensor = robot.getDevice('prox.horizontal.2')
centralRightSensor = robot.getDevice('prox.horizontal.3')
outerRightSensor = robot.getDevice('prox.horizontal.4')

# Enable distance sensors.
outerLeftSensor.enable(TIME_STEP)
centralLeftSensor.enable(TIME_STEP)
centralSensor.enable(TIME_STEP)
centralRightSensor.enable(TIME_STEP)
outerRightSensor.enable(TIME_STEP)

receiver = robot.getDevice("receiver")
receiver.enable(TIME_STEP)

# Disable motor PID control mode.
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# Set ideal motor velocity.
initialVelocity = 1

# Set the initial velocity of the left and right wheel motors.
leftMotor.setVelocity(initialVelocity)
rightMotor.setVelocity(initialVelocity)

while robot.step(TIME_STEP) != -1:
    while receiver.getQueueLength() > 0:
      message = receiver.getData();
      message = message.decode("utf-8")
      initialVelocity = float(message[0])
      receiver.nextPacket();

    # Read values from four distance sensors and calibrate.
    outerLeftSensorValue = outerLeftSensor.getValue() / distanceSensorCalibrationConstant
    centralLeftSensorValue = centralLeftSensor.getValue() / distanceSensorCalibrationConstant
    centralSensorValue = centralSensor.getValue() / distanceSensorCalibrationConstant
    centralRightSensorValue = centralRightSensor.getValue() / distanceSensorCalibrationConstant
    outerRightSensorValue = outerRightSensor.getValue() / distanceSensorCalibrationConstant

    # Set wheel velocities based on sensor values, prefer right turns if the central sensor is triggered.
    leftMotor.setVelocity(initialVelocity - (centralRightSensorValue + outerRightSensorValue) / 2)
    rightMotor.setVelocity(initialVelocity - (centralLeftSensorValue + outerLeftSensorValue) / 2 - centralSensorValue)
