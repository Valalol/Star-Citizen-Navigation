#Imports
import math
from math import sqrt, degrees, radians, cos, acos, sin
import pyperclip
import time
from datetime import datetime

class colors:
    Black = "\u001b[30m"
    Red = "\u001b[31m"
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Magenta = "\u001b[35m"
    Cyan = "\u001b[36m"
    White = "\u001b[37m"
    Reset = "\u001b[0m"


Database = {
    "Containers": {
        "Hurston": {
            "Name": "Hurston",
            "X" : 12850457093,
            "Y" : 0,
            "Z" : 0
        },
        "Crusader" : {
            "Name": "Crusader",
            "X" : -18962176000,
            "Y" : -2664959999.99999,
            "Z" : 0
        },
        "ArcCorp": {
            "Name": "ArcCorp",
            "X" : 18587664739.856,
            "Y" : -22151916920.3125,
            "Z" : 0
        },
        "Microtech": {
            "Name": "Microtech",
            "X" : 22462016306.0103,
            "Y" : 37185625645.8346,
            "Z" : 0
        },
        "Delamar": {
            "Name": "Delamar",
            "X" : -10531703478.4293,
            "Y" : 18241438663.8409,
            "Z" : 0
        },
        "Daymar": {
            "Name": "Daymar",
            "X": -18930439.540,
            "Y": -2610058.765,
            "Z": 0,
            "Rotation Speed": 2.4800000,
            "Rotation Adjustment": 29.86531,
            "OM Radius": 430.028,
            "Body Radius": 295.000
        }
    },
    "POI": {
        "Javelin_Wreck": {
            "Name": "Javelin_Wreck",
            "Container": "Daymar",
            "X": 102.055,
            "Y": 267.619,
            "Z": 70.856
        },
        "Jericho_Station": {
            "Name": "Jericho_Station",
            "Container": None,
            "X": 20196776410.415634,
            "Y": 33456387485.680557,
            "Z": 2896115.502795
        },
    }
}


def angle_between_vectors(a, b):
    return degrees(acos((a["X"]*b["X"] + a["Y"]*b["Y"] + a["Z"]*b["Z"]) / (vector_norm(a) * vector_norm(b))))

def vector_norm(a):
    return sqrt(a["X"]**2 + a["Y"]**2 + a["Z"]**2)

def rotate_point_2D(Unrotated_coordinates, angle):
    Rotated_coordinates = {}
    Rotated_coordinates["X"] = Unrotated_coordinates["X"] * cos(angle) - Unrotated_coordinates["Y"]*sin(angle)
    Rotated_coordinates["Y"] = Unrotated_coordinates["X"] * sin(angle) + Unrotated_coordinates["Y"]*cos(angle)
    Rotated_coordinates["Z"] = Unrotated_coordinates["Z"]
    return (Rotated_coordinates)


#Sets the target
Planetary_navigation = input("Planetary Navigation ?")

if Planetary_navigation == 'no':
    Target = Database["Containers"][f'{input("What is your target ?")}']
elif Planetary_navigation == 'yes':
    Target = Database["POI"][f'{input("What is your target ?")}']



#Sets some variables
Old_clipboard = ""

Old_player_coordinates = {}

for i in ["X", "Y", "Z"]:
    Old_player_coordinates[i] = 0.0

Old_time = time.time()



#Reset the clipboard content
pyperclip.copy("")


print("Program has started")


while True:

    #Get the new clipboard content
    new_clipboard = pyperclip.paste()


    #If clipboard content hasn't changed
    if new_clipboard == Old_clipboard:

        #Wait some time
        time.sleep(1/5)
    

    #If clipboard content has changed
    else :

        #update the memory with the new content
        Old_clipboard = new_clipboard

        New_time = time.time()

        #print the new content
        print(f"New clipboard content -> {new_clipboard}")



        #If it contains some coordinates
        if new_clipboard.startswith("Coordinates:"):


            #split the clipboard in sections
            new_clipboard_splitted = new_clipboard.replace(":", " ").split(" ")


            #get the 3 new XYZ coordinates
            New_player_coordinates = {}
            New_player_coordinates['X'] = float(new_clipboard_splitted[3])
            New_player_coordinates['Y'] = float(new_clipboard_splitted[5])
            New_player_coordinates['Z'] = float(new_clipboard_splitted[7])



            #get the 3 new XYZ distances between the player and the target
            New_Distance_to_POI = {}
            for i in ["X", "Y", "Z"]:
                New_Distance_to_POI[i] = abs(Target[i] - New_player_coordinates[i])

            #get the real new distance between the player and the target
            New_Distance_Total = vector_norm(New_Distance_to_POI)



            #get the 3 old XYZ distances between the player and the target
            Old_Distance_to_POI = {}
            for i in ["X", "Y", "Z"]:
                Old_Distance_to_POI[i] = abs(Target[i] - Old_player_coordinates[i])

            #get the real old distance between the player and the target
            Old_Distance_Total = vector_norm(Old_Distance_to_POI)



            #get the 3 XYZ distance travelled since last update
            Delta_Distance_to_POI = {}
            for i in ["X", "Y", "Z"]:
                Delta_Distance_to_POI[i] = New_Distance_to_POI[i] - Old_Distance_to_POI[i]

            #get the real distance travelled since last update
            Delta_Distance_Total = New_Distance_Total - Old_Distance_Total



            #get the time between the last update and this update
            Delta_time = New_time - Old_time


            #get the time it would take to reach destination using the same speed
            Estimated_time_of_arrival = (Delta_time*New_Distance_Total)/abs(Delta_Distance_Total)


            #get the vector between current_pos and previous_pos
            Previous_current_pos_vector = [New_player_coordinates['X'] - Old_player_coordinates['X'], New_player_coordinates['Y'] - Old_player_coordinates['Y'], New_player_coordinates['Z'] - Old_player_coordinates['Z']]

            #get the vector between current_pos and target_pos
            Current_target_pos_vector = [Target['X'] - New_player_coordinates['X'], Target['Y'] - New_player_coordinates['Y'], Target['Z'] - New_player_coordinates['Z']]

            #get the angle between the current-target_pos vector and the previous-current_pos vector
            Course_Deviation = degrees(acos((Previous_current_pos_vector[0] * Current_target_pos_vector[0] + Previous_current_pos_vector[1] * Current_target_pos_vector[1] + Previous_current_pos_vector[2] * Current_target_pos_vector[2]) / (sqrt(Previous_current_pos_vector[0]**2 + Previous_current_pos_vector[1]**2 + Previous_current_pos_vector[2]**2) * sqrt(Current_target_pos_vector[0]**2 + Current_target_pos_vector[1]**2 + Current_target_pos_vector[2]**2))))

            if Planetary_navigation == 1:
                Reference_time_UTC = datetime(2020, 1, 1)
                Epoch = datetime(1970, 1, 1)
                Reference_time = (Reference_time_UTC - Epoch).total_seconds()

                Time_passed_since_reference_in_seconds = New_time - Reference_time

                Rotation_speed_in_hours_per_rotation = Database["Containers"][Target["Container"]]["Rotation Speed"]
                Rotation_speed_in_degrees_per_second = 0.1 * (1/Rotation_speed_in_hours_per_rotation)
                
                Rotation_state_in_degrees = ((Rotation_speed_in_degrees_per_second * Time_passed_since_reference_in_seconds) + Database["Containers"][Target["Container"]]["Rotation Adjustment"]) % 360


                Player_local_unrotated_coordinates = {}
                for i in ['X', 'Y', 'Z']:
                    Player_local_unrotated_coordinates[i] = New_player_coordinates[i] - Database["Containers"][Target["Container"]][i]


                Player_local_rotated_coordinates = rotate_point_2D(Player_local_unrotated_coordinates, radians(Rotation_state_in_degrees))





            #update coordinates for the next update
            for i in ["X", "Y", "Z"]:
                Old_player_coordinates[i] = New_player_coordinates[i]


            Old_time = New_time



            #display data
            print(f"X = {New_player_coordinates['X']}")
            print(f"Y = {New_player_coordinates['Y']}")
            print(f"Z = {New_player_coordinates['Z']}")
            print(f"")

            print(f"Distance X = {New_Distance_to_POI['X']}")
            print(f"Distance Y = {New_Distance_to_POI['Y']}")
            print(f"Distance Z = {New_Distance_to_POI['Z']}")
            print(f"Distance to target = {New_Distance_Total}")
            print(f"")

            if Delta_Distance_to_POI['X'] <= 0 :
                print(f"Delta Distance X = {colors.Green}{abs(Delta_Distance_to_POI['X'])}{colors.Reset}")
            else :
                print(f"Delta Distance X = {colors.Red}{abs(Delta_Distance_to_POI['X'])}{colors.Reset}")

            if Delta_Distance_to_POI['Y'] <= 0 :
                print(f"Delta Distance Y = {colors.Green}{abs(Delta_Distance_to_POI['Y'])}{colors.Reset}")
            else :
                print(f"Delta Distance Y = {colors.Red}{abs(Delta_Distance_to_POI['Y'])}{colors.Reset}")

            if Delta_Distance_to_POI['Z'] <= 0 :
                print(f"Delta Distance Z = {colors.Green}{abs(Delta_Distance_to_POI['Z'])}{colors.Reset}")
            else :
                print(f"Delta Distance Z = {colors.Red}{abs(Delta_Distance_to_POI['Z'])}{colors.Reset}")

            if Delta_Distance_Total <= 0 :
                print(f"Delta Distance to target = {colors.Green}{abs(Delta_Distance_Total)}{colors.Reset}")
            else :
                print(f"Delta Distance to target = {colors.Red}{abs(Delta_Distance_Total)}{colors.Reset}")

            print(f"")

            print(f"Estimated time of arrival = {Estimated_time_of_arrival} secondes")
            print(f"")

            print(f"Course deviation = {Course_Deviation}\N{DEGREE SIGN}")

#
# Hurston : Coordinates: x:12850457093 y:0 z:0
# Microtech : Coordinates: x:22462016306.0103 y:37185625645.8346 z:0
#
#
#
#
