# 3: robot window
This folder contains:
 - A `webots.yaml` file that is mandatory for the simulation to be published on webots.cloud
 - A `Dockerfile` file that will compile the robot window of the demo.
 - A `worlds` folder containing the thumbnail (optional) and the world.
 - A `controllers` folder containing the controller
 - A `plugins`folder containing the element of the roboto window
   - The HTML file contains the page content.
   - The CSS file contains the page style.
   - The JavaScript and C files deal with the interactions between the page and the robot, using the WWI API to
     exchange string messages.

 You can see the simulation on webots.cloud ([here](https://github.com/cyberbotics/webots-cloud-simulation-demos/blob/main/3_robot_window/worlds/thymio_obstacle_avoidance.wbt))
