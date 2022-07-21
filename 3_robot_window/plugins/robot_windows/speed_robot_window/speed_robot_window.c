/*
 * Copyright 1996-2022 Cyberbotics Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <webots/emitter.h>
#include <webots/plugins/robot_window/robot_wwi.h>
#include <webots/robot.h>

#include <math.h>
#include <stdio.h>

static WbDeviceTag emitter;

// Window initialization: get some robot devices.
void wb_robot_window_init() {
  emitter = wb_robot_get_device("emitter");
}

// A simulation step occurred.
void wb_robot_window_step(int time_step) {
  // Window initialization: get some robot devices.
  const char *message;
  while ((message = wb_robot_wwi_receive_text())) {
    if (strncmp(message, "speed:", 6) == 0) {
      char speed = message[6];
      wb_emitter_send(emitter, &speed, 2);
    }
  }
}
