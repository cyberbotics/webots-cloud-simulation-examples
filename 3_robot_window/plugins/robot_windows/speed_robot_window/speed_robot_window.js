import RobotWindow from 'https://cyberbotics.com/wwi/R2022b/RobotWindow.js';

function sendSpeed() {
    const slider = document.getElementById('speedSlider')
    if (slider)
      window.robotWindow.send('speed:' + slider.value);
}

// Initialize the RobotWindow class in order to communicate with the robot.
window.onload = function() {
  window.robotWindow = new RobotWindow();
  window.robotWindow.setTitle('Custom HTML robot window');
  const slider = document.getElementById('speedSlider')
  if (slider)
    slider.oninput = sendSpeed
};
