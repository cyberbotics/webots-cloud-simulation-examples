# 1: simple simulation
This folder contains:
 - A `webots.yaml` file that is mandatory for the simulation to be published on webots.cloud.
 - A `Makefile` such that the default ([Dockerfile](https://github.com/cyberbotics/webots/blob/master/resources/web/server/config/simulation/docker/Dockerfile.default)) will compile the controller.
 - A `worlds` folder containing the world and the thumbnail (optional).
 - A `controllers` folder containing the controller and the necessary Makefiles.

You can see the simulation on webots.cloud ([here](https://webots.cloud/run?version=R2022b&url=https://github.com/cyberbotics/webots-cloud-simulation-demos/blob/main/1_simple_simulation/worlds/panda.wbt))
