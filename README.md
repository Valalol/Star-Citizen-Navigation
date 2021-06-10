# Star Citizen Navigation

This project is a tool designed to help the navigation in Star Citizen.

This project was greatly inspired by the **"Murphy Exploration Group"** and more particularly by **Graupunkt#4414** who carried out a very similar program.


## Table of Contents
1. [General Info](#general-info)
2. [Installation](#installation)
3. [Contribute](#contribute)
4. [LICENSE](#license)


## General Info
This program relies almost entirely on the in-game `/showlocation` command. This command copies the global coordinates (relative to the center of the system) to the clipboard. This program continuously retrieves the contents of this clipboard and, if coordinates are found, interprets them in order to guide the user to his target.

The program itself is called [Star_Citizen_Navigation.py](Star_Citizen_Navigation.py). When launched, a terminal and another window should open. The window allows you to select the navigation mode and the desired target. Once the target is selected, the window should close and a `Program has started` should appear in the terminal.

From this moment the program is in working order.

The `Database.json` file contains all the data the program needs to operate (rotational speed of the planets, their location, coordinates of points of interest, etc.)

### Glossary 
- POI = Point Of Interest
- Container = The planets and moons on which the points of interest can be

### Displayed Informations
During navigation, various information are displayed:
- `Updated` : The time of the last command
- `Target` : Your target
- `Closest Orbital Markers` : The 3 closest Orbital Markers from the target
- `Closest Quantum Beacon to target` : The closest Quantum Beacon from the target to start the navigation
- `Global coordinates` : The global coordinates of your character
- `Actual Container` : The planet/moon you are around
       (red: bad star, yellow: in the middle of nowhere, green: around the star of your target)
- `Total Deviation from target` : The angle between your previous position, your current position and your target

  (red : Angle > 20°, Yellow : 20° > Angle > 10°, green: 10° > Angle)
- `Horizontal Deviation from target` : The flat angle between your previous position, your current position and your target. It allows to ignore the vertical deviation and to get an heading to the target.

  (red : Angle > 20°, Yellow : 20° > Angle > 10°, green: 10° > Angle)
- `Estimated time of arrival` : Approximate time of arrival at your target if the speed is kept constant

If you are around your target's container, two other pieces of information are displayed:
- `Local coordinates` : The local coordinates of your character (in relation to the star)
- `Distance to POI` : The distance between you and your target and the distance traveled to your target
       (green if you get closer, red if you move away)

### Screenshot
![Screenshot of the main window](Images/Screenshot_1.png)
![Screenshot of the app running with Javelin Wreck](Images/Screenshot_2.png)



## Installation

This program requires [Python](https://www.python.org/downloads/) to run.

```
git clone https://github.com/Valalol/Star-Citizen-Navigation.git
cd Star-Citizen-Navigation
pip install -r requirements.txt 
python "Star_Citizen_Navigation.py"
```


## Contribute:
### How to contribute :

Either send me a pm at Valalol#0001 or go to the github repository (https://github.com/Valalol/Star-Citizen-Navigation) fork the project, do your changements and submit a pull request for me to review it and maybe merge it with the main branch. 


## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).

