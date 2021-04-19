#Imports
import math
from math import sqrt, degrees, radians, cos, acos, sin
import pyperclip
import time
from datetime import datetime
import json

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


with open('Database.json') as f:
    Database = json.load(f) 


def angle_between_vectors(a, b):
    """Function that return an angle in degrees between 2 vectors

    Args:
        a (dict): Dictionnory representing a vector with X, Y and Z keys
        b (dict): Dictionnory representing a vector with X, Y and Z keys

    Returns:
        float: Angle in degrees between the 2 vectors
    """
    
    
    try :
        angle = degrees(acos((a["X"]*b["X"] + a["Y"]*b["Y"] + a["Z"]*b["Z"]) / (vector_norm(a) * vector_norm(b))))
    except :
        angle = 0.0
    return angle


def vector_norm(a):
    return sqrt(a["X"]**2 + a["Y"]**2 + a["Z"]**2)


def rotate_point_2D(Unrotated_coordinates, angle):
    Rotated_coordinates = {}
    Rotated_coordinates["X"] = Unrotated_coordinates["X"] * cos(angle) - Unrotated_coordinates["Y"]*sin(angle)
    Rotated_coordinates["Y"] = Unrotated_coordinates["X"] * sin(angle) + Unrotated_coordinates["Y"]*cos(angle)
    Rotated_coordinates["Z"] = Unrotated_coordinates["Z"]
    return (Rotated_coordinates)


#Sets some variables
Reference_time_UTC = datetime(2020, 1, 1)
Epoch = datetime(1970, 1, 1)
Reference_time = (Reference_time_UTC - Epoch).total_seconds()


Old_clipboard = ""

Old_player_coordinates = {}

for i in ["X", "Y", "Z"]:
    Old_player_coordinates[i] = 0.0

Old_time = time.time()



#Sets the target
Target = Database["POI"][f'{input("What is your target ?")}']



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



            #If the target is within the attraction of a planet
            if Target["Container"] != 0:
                
                #Time passed since the start of game simulation
                Time_passed_since_reference_in_seconds = New_time - Reference_time
                
                #Grab the rotation speed of the container in the Database and convert it in degrees/s
                Rotation_speed_in_hours_per_rotation = Database["Containers"][Target["Container"]]["Rotation Speed"]
                Rotation_speed_in_degrees_per_second = 0.1 * (1/Rotation_speed_in_hours_per_rotation)
                
                #Get the actual rotation state in degrees using the rotation speed of the container, the actual time and a rotational adjustment value
                Rotation_state_in_degrees = ((Rotation_speed_in_degrees_per_second * Time_passed_since_reference_in_seconds) + Database["Containers"][Target["Container"]]["Rotation Adjustment"]) % 360

                #get the 
                New_player_local_unrotated_coordinates = {}
                for i in ['X', 'Y', 'Z']:
                    New_player_local_unrotated_coordinates[i] = New_player_coordinates[i] - Database["Containers"][Target["Container"]][i]

                New_player_coordinates = rotate_point_2D(New_player_local_unrotated_coordinates, radians(-1*Rotation_state_in_degrees))





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
            try :
                Estimated_time_of_arrival = (Delta_time*New_Distance_Total)/abs(Delta_Distance_Total)
            except :
                Estimated_time_of_arrival = 0.00



            #get the vector between current_pos and previous_pos
            Previous_current_pos_vector = {}
            for i in ['X', 'Y', 'Z']:
                Previous_current_pos_vector[i] = New_player_coordinates[i] - Old_player_coordinates[i]


            #get the vector between current_pos and target_pos
            Current_target_pos_vector = {}
            for i in ['X', 'Y', 'Z']:
                Current_target_pos_vector[i] = Target[i] - New_player_coordinates[i]


            #get the angle between the current-target_pos vector and the previous-current_pos vector
            Course_Deviation = angle_between_vectors(Previous_current_pos_vector, Current_target_pos_vector)






            #update coordinates for the next update
            for i in ["X", "Y", "Z"]:
                Old_player_coordinates[i] = New_player_coordinates[i]

            Old_time = New_time



            #display data
            print(f"---------------------------------------------------------------------------")
            print(f"Destination : {Target['Name']}   Updated : {time.strftime('%H:%M:%S', time.localtime(New_time))} ")
            print(f"")
            print(f"         Player Coordinates        Distance to the POI       Delta distance to the POI ")
            
            if Delta_Distance_to_POI['X'] <= 0 :
                print(f"    X :  {New_player_coordinates['X']}{(25-len(str(New_player_coordinates['X'])))*' '} {New_Distance_to_POI['X']}{(25-len(str(New_Distance_to_POI['X'])))*' '} {colors.Green}{abs(Delta_Distance_to_POI['X'])}{colors.Reset}")
            else :
                print(f"    X :  {New_player_coordinates['X']}{(25-len(str(New_player_coordinates['X'])))*' '} {New_Distance_to_POI['X']}{(25-len(str(New_Distance_to_POI['X'])))*' '} {colors.Red}{abs(Delta_Distance_to_POI['X'])}{colors.Reset}")

            if Delta_Distance_to_POI['Y'] <= 0 :
                print(f"    Y :  {New_player_coordinates['Y']}{(25-len(str(New_player_coordinates['Y'])))*' '} {New_Distance_to_POI['Y']}{(25-len(str(New_Distance_to_POI['Y'])))*' '} {colors.Green}{abs(Delta_Distance_to_POI['Y'])}{colors.Reset}")
            else :
                print(f"    Y :  {New_player_coordinates['Y']}{(25-len(str(New_player_coordinates['Y'])))*' '} {New_Distance_to_POI['Y']}{(25-len(str(New_Distance_to_POI['Y'])))*' '} {colors.Red}{abs(Delta_Distance_to_POI['Y'])}{colors.Reset}")
            
            if Delta_Distance_to_POI['Z'] <= 0 :
                print(f"    Z :  {New_player_coordinates['Z']}{(25-len(str(New_player_coordinates['Z'])))*' '} {New_Distance_to_POI['Z']}{(25-len(str(New_Distance_to_POI['Z'])))*' '} {colors.Green}{abs(Delta_Distance_to_POI['Z'])}{colors.Reset}")
            else :
                print(f"    Z :  {New_player_coordinates['Z']}{(25-len(str(New_player_coordinates['Z'])))*' '} {New_Distance_to_POI['Z']}{(25-len(str(New_Distance_to_POI['Z'])))*' '} {colors.Red}{abs(Delta_Distance_to_POI['Z'])}{colors.Reset}")
            
            if Delta_Distance_Total <= 0 :
                print(f"Total :                            {New_Distance_Total}{(25-len(str(New_Distance_Total)))*' '} {colors.Green}{abs(Delta_Distance_Total)}{colors.Reset}")
            else :
                print(f"Total :                            {New_Distance_Total}{(25-len(str(New_Distance_Total)))*' '} {colors.Red}{abs(Delta_Distance_Total)}{colors.Reset}")
            
            print(f"")


            print(f"Estimated time of arrival = {Estimated_time_of_arrival} secondes")
            print(f"")

            print(f"Course deviation = {Course_Deviation}\N{DEGREE SIGN}")

            print(f"---------------------------------------------------------------------------")



# Jericho_Station
# Hurston : Coordinates: x:12850457093 y:0 z:0
# Microtech : Coordinates: x:22462016306.0103 y:37185625645.8346 z:0
# Daymar : Coordinates: x:-18930439540 y:-2610058765 z:0
# 
