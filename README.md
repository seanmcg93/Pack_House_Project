# Sensor Monitoring Dashboard

This project aims to create a system for monitoring sensors using Raspberry Pi. 
The goal is to have multiple meters for different types of sensors and to display the sensor data on a web app dashboard.

## Dependencies
- ttkbootstrap
- PIL
- tkinter
- RPi.GPIO

## Installation
1. Install dependencies:
   ```bash
   pip install ttkbootstrap pillow
   pip install RPi.GPIO



1.Connect the sensors to the Raspberry Pi GPIO pins.
2.Clone this repository:
git clone https://github.com/seanmcg93/Pack_House_Project


Usage
1.Run the script sensor_monitor.py.
2.The script will create a GUI window displaying the sensor data.
3.Each sensor's data will be shown on a separate meter.
4.To restart the counter, click on the "Restart" button.

Configuration
1.Modify BEAM_PIN variable to match the GPIO pin connected to the sensor.
2.Adjust the GUI settings such as window title, size, and theme in the script as needed.

Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

