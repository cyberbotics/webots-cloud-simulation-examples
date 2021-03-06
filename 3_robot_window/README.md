# 3 Robot Window
This example includes a custom robot window that allows the user to change the speed of the robot during runtime.

This folder contains:
 - A [webots.yaml](webots.yaml) file that is mandatory for the simulation to be published on webots.cloud.
 - A [Dockerfile](Dockerfile) file that will compile the robot window of the example.
 - A [worlds](worlds) folder containing the [thumbnail](worlds/.thymio_obstacle_avoidance.jpg) (optional) and the [world](worlds/thymio_obstacle_avoidance.wbt).
 - A [controllers](controllers) folder containing the [controller](controllers/thymo_braitenberg/thymo_braitenberg.py).
 - A [plugins](plugins) folder containing the element of the robot window.
   - The [HTML file](plugins/robot_windows/speed_robot_window/speed_robot_window.html) contains the page content.
   - The [CSS file](plugins/robot_windows/speed_robot_window/speed_robot_window.css) contains the page style.
   - The [JavaScript](plugins/robot_windows/speed_robot_window/speed_robot_window.js) and [C](plugins/robot_windows/speed_robot_window/speed_robot_window.c) files deal with the interactions between the page and the robot, using the WWI API to exchange string messages.

You can run this simulation in webots.cloud [here](https://webots.cloud/run?version=R2022b&url=https://github.com/cyberbotics/webots-cloud-simulation-examples/blob/main/3_robot_window/worlds/thymio_obstacle_avoidance.wbt).

In the simulation, you can view the robot window by click on the following button:

<img src=https://user-images.githubusercontent.com/25938827/181248790-fca0787a-3aed-4f3b-a42c-5fe5a286fe0b.svg width=100 />
