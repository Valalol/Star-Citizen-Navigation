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

The `Database.json` file contains all the data the program needs to operate (rotational speed of the planets, their location, coordinates of points of interest, etc.)

### Glossary 
- POI = Point Of Interest
- Container = The planets and moons on which the points of interest can be

### Screenshot
![Screenshot of the main window](Images/Screenshot_1.png)
![Screenshot of the app running with Javelin Wreck](Images/Screenshot_2.png)



## Installation

This program requires [Python](https://www.python.org/downloads/) to run and it **must be added to the PATH** during installation.

Open a command prompt by clicking on the adress bar on top of this folder and by typing cmd then pressing Enter
Then type pip install -r requirements.txt to install the library required

If everything worked you should be able to launch the program called "star-citizen-navigation-tool.exe" without problems



## Contribute:
### How to contribute :

Either send me a pm at Valalol#1790 on Discord or go to the github repository (https://github.com/Valalol/Star-Citizen-Navigation) fork the project, do your changements and submit a pull request for me to review it and maybe merge it with the main branch. 


## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).

