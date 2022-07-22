# webots-cloud-simulation-demos

## Disclaimer
Some of the simulations in this repository would have been more adapted to [animation](https://cyberbotics.com/doc/guide/web-animation) or even [scene](https://cyberbotics.com/doc/guide/web-scene)
than simulations.

However they are here to explain some mechanisms in a simple way.

As animations and scenes are faster to load, we advise you to prefer them to web simulation whenever possible.

A simulation cannot be replaced by an animation in the following cases:
 - You have an interesting/interactive robot window.
 - You want the user to be able to see/modify the controller.
 - The behavior of a robot is not always the same.
 - You spawn objects during the simulation. It is not recommended.
   You should prefer to have all objects in the world at the loading, very far away, and move them closer when you want to "spawn" them.

## List of simulations

Repository hosting simulations samples for [webots.cloud](https://webots.cloud):
 - [1_simple_simulation](1_simple_simulation): a simple simulation that has no Dockerfile and thus will use the default one.
 - [2_compile_controller](2_compile_controller): a simulation with a Dockerfile that will compile a specific controller.
 - [3_robot_window](3_robot_window): a simulation with a custom robot window.
 - [4_custom_dockerfile](4_custom_dockerfile): a simulation with a Dockerfile to install an additional library.
 - [5_IDE](5_IDE): a simulation that will expose an IDE to modify the controller online.
 - [6_binary](6_binary): a simulation that uses a dirty trick to reduce the loading time.
 - [7_local_assets](7_local_assets): a simulation that uses a local proto and a local texture.

More information is available [here](https://cyberbotics.com/doc/guide/webots-cloud).

A template repository is available [here](https://github.com/cyberbotics/webots-cloud-simulation-template)
