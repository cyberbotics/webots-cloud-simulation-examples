# 6 : binaries
This folder contains:
 - A `webots.yaml` file that is mandatory for the simulation to be published on webots.cloud.
 - A `worlds` folder containing the thumbnail (optional) and the world.
 - A `controllers` folder containing the already compiled binaries.
 - A `libraries` folder that is needed to build the controllers binaries.

When the compilation of the controllers takes too much time (because they are complex, rely on external dependencies,...), it is possible to commit the binaries in the repository.
By doing so, we can skip the compilation step when loading the simulation.

However this is a bad practice, should be done cautiously, and is not guarantee to work depending on the version of the compiler.

You can see the simulation on webots.cloud [here](https://webots.cloud/run?version=R2022b&url=https://github.com/cyberbotics/webots-cloud-simulation-demos/blob/main/4_custom_dockerfile/worlds/inverse_kinematics.wbt)
