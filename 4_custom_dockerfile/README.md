# 4 Custom Dockerfile
This simulation demonstrates how to load additional dependencies needed by the simulation.

This folder contains:
 - A [webots.yaml](webots.yaml) file that is mandatory for the simulation to be published on webots.cloud.
 - A [Dockerfile](Dockerfile) file that will install an additional library needed by the controller: [ikpy](https://pypi.org/project/ikpy/).
 - A [worlds](worlds) folder containing the [thumbnail](worlds/.inverse_kinematics.jpg) (optional, displayed during the simulation load) and the [world](worlds/inverse_kinematics.wbt).
 - A [controllers](controllers) folder containing the [controller](controllers/inverse_kinematics/inverse_kinematics.py).

Another solution would be to build another docker (with the needed libraries inside), push it on https://hub.docker.com and then use it for your simulation (by changing the `FROM` of the Dockerfile).
The first time you will load the simulation on a server, it will be slower, because the server need to get the new docker, but it will be faster the next times.

You can run this simulation in webots.cloud [here](https://webots.cloud/run?version=R2022b&url=https://github.com/cyberbotics/webots-cloud-simulation-examples/blob/main/4_custom_dockerfile/worlds/inverse_kinematics.wbt).
