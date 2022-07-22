# 4 Custom Dockerfile
This folder contains:
 - A `webots.yaml` file that is mandatory for the simulation to be published on webots.cloud.
 - A `Dockerfile` file that will install an additional library need by the controller: `ikpy`.
 - A `worlds` folder containing the thumbnail (optional) and the world.
 - A `controllers` folder containing the controller.

Another solution would be to build another docker (with the needed libraries inside), push it on https://hub.docker.com and then use it for your simulation (by changing the `FROM` of the Dockerfile).
The first time you will load the simulation on a server, it will be slower, because the server need to get the new docker, but it will be faster the next times.

You can see this simulation on webots.cloud [here](https://webots.cloud/run?version=R2022b&url=https://github.com/cyberbotics/webots-cloud-simulation-demos/blob/main/4_custom_dockerfile/worlds/inverse_kinematics.wbt)
