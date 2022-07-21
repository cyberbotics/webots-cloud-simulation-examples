# demo1: simple simulation
This folder contains:
 - A `webots.yaml` file that is mandatory for the simulation to be published on webots.cloud
 - A `Makefile` such that the default ([Dockerfile](https://github.com/cyberbotics/webots/blob/master/resources/web/server/config/simulation/docker/Dockerfile.default)) will compile the controller.
 - A `worlds` folder containing the thumbnail (optional) and the world.
 - A `controllers` folder containing the controller and the necessary Makefiles

 You can see the simulation displayed on webots.cloud ([here](https://webots.cloud/run?version=R2022b&url=https://github.com/cyberbotics/webots-cloud-simulation-demos/blob/main/demo1_simple_simulation/worlds/panda.wbt))