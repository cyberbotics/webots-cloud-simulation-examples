FROM cyberbotics/webots.cloud:R2022b
ARG PROJECT_PATH
RUN mkdir -p $PROJECT_PATH
COPY . $PROJECT_PATH
RUN cd $PROJECT_PATH/controllers/spot_moving_demo && make
