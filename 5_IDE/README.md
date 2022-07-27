# 5 IDE
This folder contains:
 - A [webots.yaml](webots.yaml) file that allows to enable the IDE in the web simulation.
 - A [worlds](worlds) folder containing the [thumbnail](worlds/.robotino_example.jpg) (optional, displayed during the simulation load) and the [world](worlds/robotino_example.wbt).
 - A [controllers](controllers) folder containing the [controller](controllers/robotino3/robotino3.py).

More information about the online IDE is available [here](https://www.cyberbotics.com/doc/guide/setup-a-webots-project-repository#running-a-simulation)

You can run this simulation in webots.cloud and modify its controller with the IDE [here](https://webots.cloud/run?version=R2022b&url=https://github.com/cyberbotics/webots-cloud-simulation-examples/blob/main/5_IDE/worlds/robotino_example.wbt).

Once the simulation is launched, you can open the IDE by pressing the following button:

<img src="https://user-images.githubusercontent.com/25938827/181250602-78d74c8b-2b13-45d0-892d-40a04c7b0e98.svg" width=100/>

To open the controller in the IDE, click on ```File -> Open... -> webots-projects -> robotino3 -> robotino3.py ```.

To apply the modifications, save the controller file and reset the simulation.
