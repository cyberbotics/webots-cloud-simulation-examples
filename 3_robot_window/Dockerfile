FROM cyberbotics/webots.cloud:R2022b-ubuntu20.04
ARG PROJECT_PATH
RUN mkdir -p $PROJECT_PATH
COPY . $PROJECT_PATH
RUN cd $PROJECT_PATH/plugins/robot_windows/speed_robot_window && make
