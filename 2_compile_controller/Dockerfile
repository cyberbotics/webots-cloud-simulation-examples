FROM benjamindeleze/webots-test:R2022b14LGA
ARG PROJECT_PATH
RUN mkdir -p $PROJECT_PATH
COPY . $PROJECT_PATH
FROM cyberbotics/webots.cloud:R2022b
ARG PROJECT_PATH
RUN mkdir -p $PROJECT_PATH
COPY . $PROJECT_PATH
cd $PROJECT_PATH/controllers/spot_moving_demo && make
