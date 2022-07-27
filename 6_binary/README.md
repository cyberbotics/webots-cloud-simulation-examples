# 6 Binary
When the compilation of the controller takes too much time (because it is complex, rely on external dependencies,...), it is possible to commit the binary in the repository.
By doing so, we can skip the compilation step when loading the simulation.

However this is a bad practice, should be done cautiously, and is not guarantee to work depending on the version of the compiler.

This folder contains:
 - A [webots.yaml](webots.yaml) file that is mandatory for the simulation to be published on webots.cloud.
 - A [worlds](worlds) folder containing the [thumbnail](worlds/.ned.jpg) (optional, displayed during the simulation load) and the [world](worlds/ned.wbt).
 - A [controllers](controllers) folder containing the already compiled binary.

You can run this simulation in webots.cloud [here](https://webots.cloud/run?version=R2022b&url=https://github.com/cyberbotics/webots-cloud-simulation-examples/blob/main/6_binary/worlds/ned.wbt).
