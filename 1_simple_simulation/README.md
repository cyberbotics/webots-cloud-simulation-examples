# 1 Simple Simulation
This basic example does not have a Dockerfile. Thus, the default one will be used.

This folder contains:
 - A [webots.yaml](webots.yaml) file that is mandatory for the simulation to be published on webots.cloud.
 - A [Makefile](Makefile) such that the default [Dockerfile](https://github.com/cyberbotics/webots/blob/master/resources/web/server/config/simulation/docker/Dockerfile.default) will compile the controller.
 - A [worlds](worlds) folder containing the [thumbnail](worlds/.moose_demo.jpg) (optional, displayed during the simulation load) and the [world](worlds/moose_demo.wbt) file.
 - A [controllers](controllers) folder containing the [controller](controllers/moose_path_following/moose_path_following.c) and the necessary Makefiles.

You can run this simulation in webots.cloud [here](https://webots.cloud/run?version=R2022b&url=https://github.com/cyberbotics/webots-cloud-simulation-examples/blob/main/1_simple_simulation/worlds/moose_demo.wbt).

See [here](https://cyberbotics.com/doc/guide/webots-cloud#publish-cloud-based-simulations) for more information about running your simulation in [webots.cloud](https://webots.cloud/).
