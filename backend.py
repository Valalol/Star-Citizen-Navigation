#Made by Valalol#1790
#First release 16/04/2021

#Imports
import math
from math import sqrt, degrees, radians, cos, acos, sin, asin, atan2
import pyperclip
import time
import datetime
import tkinter as tk
import tkinter.ttk as ttk
import json
import os
import csv
import sys

os.system("")

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

Program_mode_list = ["Planetary Navigation", "Space Navigation", "Companion", "Racing Tool"]

with open('Database.json') as f:
    Database = json.load(f)


Container_list = []
for i in Database["Containers"]:
    Container_list.append(Database["Containers"][i]["Name"])

Space_POI_list = []
for poi in Database["Space_POI"]:
    Space_POI_list.append(poi)

Planetary_POI_list = {}
for container_name in Database["Containers"]:
    Planetary_POI_list[container_name] = []
    for poi in Database["Containers"][container_name]["POI"]:
        Planetary_POI_list[container_name].append(poi)



Target = ""
Mode = ""



#-------------------------------------------------------------GUI-----------------------------------------------------------------------
#------------------------------------------------------------Start----------------------------------------------------------------------

def Program_mode_selected(event):

    if Program_mode_selection_Combobox.get() == "Planetary Navigation" :
        Planetary_Navigation_Frame.grid(column='1', row='0')
        Space_Navigation_Frame.grid_forget()
        Companion_Tool_Frame.grid_forget()
        Racing_Tool_Frame.grid_forget()



    elif Program_mode_selection_Combobox.get() == "Space Navigation" :
        Planetary_Navigation_Frame.grid_forget()
        Space_Navigation_Frame.grid(column='1', row='0')
        Companion_Tool_Frame.grid_forget()
        Racing_Tool_Frame.grid_forget()



    elif Program_mode_selection_Combobox.get() == "Companion" :
        Planetary_Navigation_Frame.grid_forget()
        Space_Navigation_Frame.grid_forget()
        Companion_Tool_Frame.grid(column='1', row='0')
        Racing_Tool_Frame.grid_forget()



    elif Program_mode_selection_Combobox.get() == "Racing Tool" :
        Planetary_Navigation_Frame.grid_forget()
        Space_Navigation_Frame.grid_forget()
        Companion_Tool_Frame.grid_forget()
        Racing_Tool_Frame.grid(column='1', row='0')




def Container_Selected(event):
    Planetary_POI_Selection_Combobox["values"] = Planetary_POI_list[Container_Selection_Combobox.get()]



def Planetary_Known_or_custom_selected(event):
    if Planetary_Known_or_custom_POI_Combobox.get() == "Known POI" :
        Planetary_Known_POI_Frame.grid(column='2', row='0')
        Planetary_Custom_POI_Frame.grid_forget()


    elif Planetary_Known_or_custom_POI_Combobox.get() == "Custom POI" :
        Planetary_Known_POI_Frame.grid_forget()
        Planetary_Custom_POI_Frame.grid(column='2', row='0')



def Planetary_Known_Target_Selected(event):
    Planetary_Known_POI_Frame_Start_Navigation_Button.grid(column='1', padx='8', pady='8', row='0')



def Start_Planetary_Navigation_Known_POI():
    global Target, Mode
    Mode = Program_mode_selection_Combobox.get()
    Target = Database["Containers"][Container_Selection_Combobox.get()]["POI"][f'{Planetary_POI_Selection_Combobox.get()}']

    root.destroy()



def Start_Planetary_Navigation_Custom_POI():
    global Target, Mode
    Mode = Program_mode_selection_Combobox.get()
    Target = {'Name': 'Custom POI', 'Container': f'{Container_Selection_Combobox.get()}', 'X': float(Planetary_X_Custom_POI_Entry.get()), 'Y': float(Planetary_Y_Custom_POI_Entry.get()), 'Z': float(Planetary_Z_Custom_POI_Entry.get()), "QTMarker": "FALSE"}

    root.destroy()


def Space_Known_or_custom_selected(event):
    if Space_Known_or_custom_POI_Combobox.get() == "Known POI" :
        Space_Known_POI_Frame.grid(column='2', row='0')
        Space_Custom_POI_Frame.grid_forget()


    elif Space_Known_or_custom_POI_Combobox.get() == "Custom POI" :
        Space_Known_POI_Frame.grid_forget()
        Space_Custom_POI_Frame.grid(column='2', row='0')


def Space_Known_Target_Selected(event):
    Space_Known_POI_Frame_Start_Navigation_Button.grid(column='1', padx='8', pady='8', row='0')


def Start_Space_Navigation_Known_POI():
    global Target, Mode
    Mode = Program_mode_selection_Combobox.get()
    Target = Database["Space_POI"][f'{Space_POI_Selection_Combobox.get()}']

    root.destroy()


def Start_Space_Navigation_Custom_POI():
    global Target, Mode
    Mode = Program_mode_selection_Combobox.get()
    Target = {'Name': 'Custom POI', 'Container': 0, 'X': float(Space_X_Custom_POI_Entry.get()), 'Y': float(Space_Y_Custom_POI_Entry.get()), 'Z': float(Space_Z_Custom_POI_Entry.get()), 'QTMarker': "FALSE"}

    root.destroy()


def Start_Companion():
    global Mode
    Mode = Program_mode_selection_Combobox.get()

    root.destroy()




#root
root = tk.Tk()

root.title("Navigation Tool")
root.iconbitmap(r'Images/Icon.ico')


#Man Frame
MainWindow = ttk.Frame(root)
MainWindow.configure(borderwidth='0', height='200', relief='flat', width='200')
MainWindow.pack(expand='true', fill='both', side='left')

#Program mode selection combobox always here
Program_mode_selection_Combobox = ttk.Combobox(MainWindow, state='readonly', values = Program_mode_list)
Program_mode_selection_Combobox.bind("<<ComboboxSelected>>", Program_mode_selected)
Program_mode_selection_Combobox.grid(column='0', padx='8', pady='8', row='0')



#Planetary Navigation Frame
Planetary_Navigation_Frame = ttk.Frame(MainWindow)
Planetary_Navigation_Frame.configure(borderwidth='0', height='200', relief='flat', width='200')


Container_Selection_Combobox = ttk.Combobox(Planetary_Navigation_Frame, state='readonly', values = Container_list)
Container_Selection_Combobox.bind("<<ComboboxSelected>>", Container_Selected)
Container_Selection_Combobox.grid(column='0', padx='8', pady='8', row='0')


Planetary_Known_or_custom_POI_Combobox = ttk.Combobox(Planetary_Navigation_Frame, state='readonly', values = ["Known POI", "Custom POI"])
Planetary_Known_or_custom_POI_Combobox.bind("<<ComboboxSelected>>", Planetary_Known_or_custom_selected)
Planetary_Known_or_custom_POI_Combobox.grid(column='1', padx='8', pady='8', row='0')



#Known Poi Selection
Planetary_Known_POI_Frame = ttk.Frame(Planetary_Navigation_Frame)
Planetary_Known_POI_Frame.configure(borderwidth='0', height='200', relief='flat', width='200')


Planetary_POI_Selection_Combobox = ttk.Combobox(Planetary_Known_POI_Frame, state='readonly', values = "")
Planetary_POI_Selection_Combobox.bind("<<ComboboxSelected>>", Planetary_Known_Target_Selected)
Planetary_POI_Selection_Combobox.grid(column='0', padx='8', pady='8', row='0')


Planetary_Known_POI_Frame_Start_Navigation_Button = tk.Button(Planetary_Known_POI_Frame, text="Start Navigation", command=Start_Planetary_Navigation_Known_POI)



#Custom Poi Selection
Planetary_Custom_POI_Frame = ttk.Frame(Planetary_Navigation_Frame)
Planetary_Custom_POI_Frame.configure(borderwidth='0', height='200', relief='flat', width='200')


Planetary_X_Custom_POI_Small_X = tk.Label(Planetary_Custom_POI_Frame, text="X =")
Planetary_X_Custom_POI_Small_Y = tk.Label(Planetary_Custom_POI_Frame, text="Y =")
Planetary_X_Custom_POI_Small_Z = tk.Label(Planetary_Custom_POI_Frame, text="Z =")

Planetary_X_Custom_POI_Small_X.grid(column='0', padx='1', pady='3', row='0')
Planetary_X_Custom_POI_Small_Y.grid(column='0', padx='1', pady='3', row='1')
Planetary_X_Custom_POI_Small_Z.grid(column='0', padx='1', pady='3', row='2')


Planetary_X_Custom_POI_Entry = tk.Entry(Planetary_Custom_POI_Frame)
Planetary_Y_Custom_POI_Entry = tk.Entry(Planetary_Custom_POI_Frame)
Planetary_Z_Custom_POI_Entry = tk.Entry(Planetary_Custom_POI_Frame)

Planetary_X_Custom_POI_Entry.grid(column='1', padx='1', pady='3', row='0')
Planetary_Y_Custom_POI_Entry.grid(column='1', padx='1', pady='3', row='1')
Planetary_Z_Custom_POI_Entry.grid(column='1', padx='1', pady='3', row='2')


Planetary_Custom_POI_Frame_Start_Navigation_Button = tk.Button(Planetary_Custom_POI_Frame, text="Start Navigation", command=Start_Planetary_Navigation_Custom_POI)
Planetary_Custom_POI_Frame_Start_Navigation_Button.grid(column='2', padx='8', pady='2', row='1')





#Space Navigation frame
Space_Navigation_Frame = ttk.Frame(MainWindow)
Space_Navigation_Frame.configure(borderwidth='0', height='200', relief='flat', width='200')


Space_Known_or_custom_POI_Combobox = ttk.Combobox(Space_Navigation_Frame, state='readonly', values = ["Known POI", "Custom POI"])
Space_Known_or_custom_POI_Combobox.bind("<<ComboboxSelected>>", Space_Known_or_custom_selected)
Space_Known_or_custom_POI_Combobox.grid(column='1', padx='8', pady='8', row='0')



#Known Poi Selection
Space_Known_POI_Frame = ttk.Frame(Space_Navigation_Frame)
Space_Known_POI_Frame.configure(borderwidth='0', height='200', relief='flat', width='200')


Space_POI_Selection_Combobox = ttk.Combobox(Space_Known_POI_Frame, state='readonly', values = Space_POI_list)
Space_POI_Selection_Combobox.bind("<<ComboboxSelected>>", Space_Known_Target_Selected)
Space_POI_Selection_Combobox.grid(column='0', padx='8', pady='8', row='0')


Space_Known_POI_Frame_Start_Navigation_Button = tk.Button(Space_Known_POI_Frame, text="Start Navigation", command=Start_Space_Navigation_Known_POI)



#Custom Poi Selection
Space_Custom_POI_Frame = ttk.Frame(Space_Navigation_Frame)
Space_Custom_POI_Frame.configure(borderwidth='0', height='200', relief='flat', width='200')


Space_X_Custom_POI_Small_X = tk.Label(Space_Custom_POI_Frame, text="X =")
Space_X_Custom_POI_Small_Y = tk.Label(Space_Custom_POI_Frame, text="Y =")
Space_X_Custom_POI_Small_Z = tk.Label(Space_Custom_POI_Frame, text="Z =")

Space_X_Custom_POI_Small_X.grid(column='0', padx='1', pady='3', row='0')
Space_X_Custom_POI_Small_Y.grid(column='0', padx='1', pady='3', row='1')
Space_X_Custom_POI_Small_Z.grid(column='0', padx='1', pady='3', row='2')


Space_X_Custom_POI_Entry = tk.Entry(Space_Custom_POI_Frame)
Space_Y_Custom_POI_Entry = tk.Entry(Space_Custom_POI_Frame)
Space_Z_Custom_POI_Entry = tk.Entry(Space_Custom_POI_Frame)

Space_X_Custom_POI_Entry.grid(column='1', padx='1', pady='3', row='0')
Space_Y_Custom_POI_Entry.grid(column='1', padx='1', pady='3', row='1')
Space_Z_Custom_POI_Entry.grid(column='1', padx='1', pady='3', row='2')


Space_Custom_POI_Frame_Start_Navigation_Button = tk.Button(Space_Custom_POI_Frame, text="Start Navigation", command=Start_Space_Navigation_Custom_POI)
Space_Custom_POI_Frame_Start_Navigation_Button.grid(column='2', padx='8', pady='2', row='1')











#Companion Tool Frame
Companion_Tool_Frame = ttk.Frame(MainWindow)
Companion_Tool_Frame.configure(borderwidth='0', height='200', relief='flat', width='200')

Start_Companion_Button = tk.Button(Companion_Tool_Frame, text="Start Companion", command=Start_Companion)
Start_Companion_Button.grid(column='0', padx='8', pady='8', row='0')



#Racing Tool Frame
Racing_Tool_Frame = ttk.Frame(MainWindow)
Racing_Tool_Frame.configure(borderwidth='0', height='200', relief='flat', width='200')

Racing_Tool_WIP_Label = tk.Label(Racing_Tool_Frame, text="Work in progress")
Racing_Tool_WIP_Label.grid(column='0', padx='8', pady='8', row='0')


root.mainloop()

Log_Mode = True

#-------------------------------------------------------------GUI-----------------------------------------------------------------------
#-------------------------------------------------------------END-----------------------------------------------------------------------


if Mode == '':
    raise Exception("Program mode not selected")
    time.sleep(1)
    exit()

if Mode == "Planetary Navigation" : 
    setup = {
        "updated" : f"Updated : {time.strftime('%H:%M:%S', time.localtime(time.time()))}",
        "target" : Target['Name'],
        "player_actual_container" : "None",
        "target_container" : Target['Container'],
        "player_x" : "0.0",
        "player_y" : "0.0",
        "player_z" : "0.0",
        "player_long" : "0.0°",
        "player_lat" : "0.0°",
        "player_height" : "0 m",
        "player_OM1" : "OM-1 : 0.000 km",
        "player_OM2" : "OM-3 : 0.000 km",
        "player_OM3" : "OM-5 : 0.000 km",
        "player_closest_poi" : "None : 0.000 km",
        "target_x" : "0.0",
        "target_y" : "0.0",
        "target_z" : "0.0",
        "target_long" : "0.0°",
        "target_lat" : "0.0°",
        "target_height" : "0 m",
        "target_OM1" : "OM-1 : 0.000 km",
        "target_OM2" : "OM-3 : 0.000 km",
        "target_OM3" : "OM-5 : 0.000 km",
        "target_closest_QT_beacon" : "None : 0.000 km",
        "distance_to_poi" : "0.000 km",
        "distance_to_poi_color" : "#00ff00",
        "delta_distance_to_poi" : "0.000 km",
        "delta_distance_to_poi_color" : "#00ff00",
        "total_deviation" : "0°",
        "total_deviation_color" : "#00ff00",
        "horizontal_deviation" : "0°",
        "horizontal_deviation_color" : "#00ff00",
        "heading" : "0°",
        "ETA" : "00:00:00"
    }

elif Mode == "Space Navigation":
    setup = {
        "updated" : f"Updated : {time.strftime('%H:%M:%S', time.localtime(time.time()))}",
        "target" : Target['Name'],
        "player_x" : "0.0",
        "player_y" : "0.0",
        "player_z" : "0.0",
        "target_x" : "0.0",
        "target_y" : "0.0",
        "target_z" : "0.0",
        "distance_to_poi" : "0.000 km",
        "distance_to_poi_color" : "#00ff00",
        "delta_distance_to_poi" : "0.000 km",
        "delta_distance_to_poi_color" : "#00ff00",
        "total_deviation" : "0°",
        "total_deviation_color" : "#00ff00",
        "ETA" : "00:00:00"
    }

elif Mode == "Companion":
    setup = {
        "updated" : f"Updated : {time.strftime('%H:%M:%S', time.localtime(time.time()))}",
        "player_global_x" : "Global X : 0.0",
        "player_global_y" : "Global Y : 0.0",
        "player_global_z" : "Global Z : 0.0",
        "distance_change" : "Distance since last update : 0.000 km",
        "actual_container" : "Actual Container : None",
        "player_local_x" : "Local X : 0.0",
        "player_local_y" : "Local Y : 0.0",
        "player_local_z" : "Local Z : 0.0",
        "player_long" : "Longitude : 0.0°",
        "player_lat" : "Latitude : 0.0°",
        "player_height" : "Height : 0 m",
        "player_OM1" : "OM-1 : 0.000 km",
        "player_OM2" : "OM-3 : 0.000 km",
        "player_OM3" : "OM-5 : 0.000 km",
        "closest_poi" : f"Closest POI : \nNone (0.000 km) \nNone (0.000 km)",
    }


print(f"Mode : {Mode}")
sys.stdout.flush()
time.sleep(0.2)
print("New data :", json.dumps(setup))
sys.stdout.flush()



def vector_norm(a):
    """Returns the norm of a vector"""
    return sqrt(a["X"]**2 + a["Y"]**2 + a["Z"]**2)

def vector_product(a, b):
    """Returns the dot product of two vectors"""
    return a["X"]*b["X"] + a["Y"]*b["Y"] + a["Z"]*b["Z"]

def angle_between_vectors(a, b):
    """Function that returns an angle in degrees between 2 vectors"""
    try :
        angle = degrees(acos(vector_product(a, b) / (vector_norm(a) * vector_norm(b))))
    except ZeroDivisionError:
        angle = 0.0
    return angle

def rotate_point_2D(Unrotated_coordinates, angle):
    Rotated_coordinates = {}
    Rotated_coordinates["X"] = Unrotated_coordinates["X"] * cos(angle) - Unrotated_coordinates["Y"]*sin(angle)
    Rotated_coordinates["Y"] = Unrotated_coordinates["X"] * sin(angle) + Unrotated_coordinates["Y"]*cos(angle)
    Rotated_coordinates["Z"] = Unrotated_coordinates["Z"]
    return (Rotated_coordinates)


#Sets some variables
Reference_time_UTC = datetime.datetime(2020, 1, 1)
Epoch = datetime.datetime(1970, 1, 1)
Reference_time = (Reference_time_UTC - Epoch).total_seconds()


if Log_Mode == True:
    if not os.path.isdir('Logs'):
        os.mkdir('Logs')

    if not os.path.isfile('Logs/Logs.csv'):
        field = ['Key', 'X', 'Y', 'Z', 'Container', 'Longitude', 'Latitude', 'Height']
        with open("Logs/Logs.csv","w+", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(field)
    
    New_run_field = ['New_Run']
    with open(r'Logs/Logs.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(New_run_field)




Old_clipboard = ""

Old_player_Global_coordinates = {}
for i in ["X", "Y", "Z"]:
    Old_player_Global_coordinates[i] = 0.0

Old_player_local_rotated_coordinates = {}
for i in ["X", "Y", "Z"]:
    Old_player_local_rotated_coordinates[i] = 0.0

Old_Distance_to_POI = {}
for i in ["X", "Y", "Z"]:
    Old_Distance_to_POI[i] = 0.0

Old_container = {
    "Name": "None",
    "X": 0,
    "Y": 0,
    "Z": 0,
    "Rotation Speed": 0,
    "Rotation Adjust": 0,
    "OM Radius": 0,
    "Body Radius": 0,
    "POI": {}
}


Old_time = time.time()


#Reset the clipboard content
pyperclip.copy("")


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

        #If it contains some coordinates
        if new_clipboard.startswith("Coordinates:"):


            #split the clipboard in sections
            new_clipboard_splitted = new_clipboard.replace(":", " ").split(" ")


            #get the 3 new XYZ coordinates
            New_Player_Global_coordinates = {}
            New_Player_Global_coordinates['X'] = float(new_clipboard_splitted[3])/1000
            New_Player_Global_coordinates['Y'] = float(new_clipboard_splitted[5])/1000
            New_Player_Global_coordinates['Z'] = float(new_clipboard_splitted[7])/1000



            #-----------------------------------------------------Planetary Navigation--------------------------------------------------------------
            # If the target is within the attraction of a planet
            if Mode == "Planetary Navigation":



                #---------------------------------------------------Actual Container----------------------------------------------------------------
                #search in the Databse to see if the player is ina Container
                Actual_Container = {
                    "Name": "None",
                    "X": 0,
                    "Y": 0,
                    "Z": 0,
                    "Rotation Speed": 0,
                    "Rotation Adjust": 0,
                    "OM Radius": 0,
                    "Body Radius": 0,
                    "POI": {}
                }
                for i in Database["Containers"] :
                    Player_Container_vector = {"X" : Database["Containers"][i]["X"] - New_Player_Global_coordinates["X"], "Y" : Database["Containers"][i]["Y"] - New_Player_Global_coordinates["Y"], "Z" : Database["Containers"][i]["Z"] - New_Player_Global_coordinates["Z"]}
                    if vector_norm(Player_Container_vector) <= 1.5 * Database["Containers"][i]["OM Radius"]:
                        Actual_Container = Database["Containers"][i]



                #---------------------------------------------------New player local coordinates----------------------------------------------------
                #Time passed since the start of game simulation
                Time_passed_since_reference_in_seconds = New_time - Reference_time

                #Grab the rotation speed of the container in the Database and convert it in degrees/s
                player_Rotation_speed_in_hours_per_rotation = Actual_Container["Rotation Speed"]
                try:
                    player_Rotation_speed_in_degrees_per_second = 0.1 * (1/player_Rotation_speed_in_hours_per_rotation)
                except ZeroDivisionError:
                    player_Rotation_speed_in_degrees_per_second = 0
                    continue
                
                
                #Get the actual rotation state in degrees using the rotation speed of the container, the actual time and a rotational adjustment value
                player_Rotation_state_in_degrees = ((player_Rotation_speed_in_degrees_per_second * Time_passed_since_reference_in_seconds) + Actual_Container["Rotation Adjust"]) % 360

                #get the new player unrotated coordinates
                New_player_local_unrotated_coordinates = {}
                for i in ['X', 'Y', 'Z']:
                    New_player_local_unrotated_coordinates[i] = New_Player_Global_coordinates[i] - Actual_Container[i]

                #get the new player rotated coordinates
                New_player_local_rotated_coordinates = rotate_point_2D(New_player_local_unrotated_coordinates, radians(-1*player_Rotation_state_in_degrees))




                #---------------------------------------------------New player local coordinates----------------------------------------------------

                #Grab the rotation speed of the container in the Database and convert it in degrees/s
                target_Rotation_speed_in_hours_per_rotation = Database["Containers"][Target["Container"]]["Rotation Speed"]
                try:
                    target_Rotation_speed_in_degrees_per_second = 0.1 * (1/target_Rotation_speed_in_hours_per_rotation)
                except ZeroDivisionError:
                    target_Rotation_speed_in_degrees_per_second = 0
                    continue
                
                
                #Get the actual rotation state in degrees using the rotation speed of the container, the actual time and a rotational adjustment value
                target_Rotation_state_in_degrees = ((target_Rotation_speed_in_degrees_per_second * Time_passed_since_reference_in_seconds) + Database["Containers"][Target["Container"]]["Rotation Adjust"]) % 360

                #get the new player rotated coordinates
                target_rotated_coordinates = rotate_point_2D(Target, radians(target_Rotation_state_in_degrees))




                #-------------------------------------------------player local Long Lat Height--------------------------------------------------
                
                if Actual_Container['Name'] != "None":
                    
                    #Cartesian Coordinates
                    x = New_player_local_rotated_coordinates["X"]
                    y = New_player_local_rotated_coordinates["Y"]
                    z = New_player_local_rotated_coordinates["Z"]

                    #Radius of the container
                    player_Radius = Actual_Container["Body Radius"]

                    #Radial_Distance
                    player_Radial_Distance = sqrt(x**2 + y**2 + z**2)

                    #Height
                    player_Height = player_Radial_Distance - player_Radius
                    
                    #Longitude
                    try :
                        player_Longitude = -1*degrees(atan2(x, y))
                    except Exception as err:
                        print(f'Error in Longitude : {err} \nx = {x}, y = {y} \nPlease report this to Valalol#1790 for me to try to solve this issue')
                        sys.stdout.flush()
                        player_Longitude = 0

                    #Latitude
                    try :
                        player_Latitude = degrees(asin(z/player_Radial_Distance))
                    except Exception as err:
                        print(f'Error in Latitude : {err} \nz = {z}, radius = {player_Radial_Distance} \nPlease report this at Valalol#1790 for me to try to solve this issue')
                        sys.stdout.flush()
                        player_Latitude = 0

                
                
                #-------------------------------------------------target local Long Lat Height--------------------------------------------------

                #Cartesian Coordinates
                x = Target["X"]
                y = Target["Y"]
                z = Target["Z"]

                #Radius of the container
                target_Radius = Database["Containers"][Target["Container"]]["Body Radius"]

                #Radial_Distance
                target_Radial_Distance = sqrt(x**2 + y**2 + z**2)

                #Height
                target_Height = target_Radial_Distance - target_Radius
                
                #Longitude
                try :
                    target_Longitude = -1*degrees(atan2(x, y))
                except Exception as err:
                    print(f'Error in Longitude : {err} \nx = {x}, y = {y} \nPlease report this to Valalol#1790 for me to try to solve this issue')
                    sys.stdout.flush()
                    target_Longitude = 0

                #Latitude
                try :
                    target_Latitude = degrees(asin(z/target_Radial_Distance))
                except Exception as err:
                    print(f'Error in Latitude : {err} \nz = {z}, radius = {target_Radial_Distance} \nPlease report this at Valalol#1790 for me to try to solve this issue')
                    sys.stdout.flush()
                    target_Latitude = 0





                #---------------------------------------------------Distance to POI-----------------------------------------------------------------
                New_Distance_to_POI = {}
                
                if Actual_Container == Target["Container"]:
                    for i in ["X", "Y", "Z"]:
                        New_Distance_to_POI[i] = abs(Target[i] - New_player_local_rotated_coordinates[i])
                
                
                else:
                    for i in ["X", "Y", "Z"]:
                        New_Distance_to_POI[i] = abs((target_rotated_coordinates[i] + Database["Containers"][Target["Container"]][i]) - New_Player_Global_coordinates[i])

                #get the real new distance between the player and the target
                New_Distance_to_POI_Total = vector_norm(New_Distance_to_POI)

                if New_Distance_to_POI_Total <= 100:
                    New_Distance_to_POI_Total_color = "#00ff00"
                elif New_Distance_to_POI_Total <= 1000:
                    New_Distance_to_POI_Total_color = "#ffd000"
                else :
                    New_Distance_to_POI_Total_color = "#ff3700"


                #---------------------------------------------------Delta Distance to POI-----------------------------------------------------------
                #get the real old distance between the player and the target
                Old_Distance_to_POI_Total = vector_norm(Old_Distance_to_POI)




                #get the 3 XYZ distance travelled since last update
                Delta_Distance_to_POI = {}
                for i in ["X", "Y", "Z"]:
                    Delta_Distance_to_POI[i] = New_Distance_to_POI[i] - Old_Distance_to_POI[i]

                #get the real distance travelled since last update
                Delta_Distance_to_POI_Total = New_Distance_to_POI_Total - Old_Distance_to_POI_Total

                if Delta_Distance_to_POI_Total <= 0:
                    Delta_distance_to_poi_color = "#00ff00"
                else:
                    Delta_distance_to_poi_color = "#ff3700"



                #---------------------------------------------------Estimated time of arrival to POI------------------------------------------------
                #get the time between the last update and this update
                Delta_time = New_time - Old_time


                #get the time it would take to reach destination using the same speed
                try :
                    Estimated_time_of_arrival = (Delta_time*New_Distance_to_POI_Total)/abs(Delta_Distance_to_POI_Total)
                except ZeroDivisionError:
                    Estimated_time_of_arrival = 0.00



                #----------------------------------------------------Closest Quantumable POI--------------------------------------------------------
                Target_to_POIs_Distances = []
                if Target["QTMarker"] == "FALSE":
                    for POI in Database["Containers"][Target["Container"]]["POI"]:
                        if Database["Containers"][Target["Container"]]["POI"][POI]["QTMarker"] == "TRUE":

                            Vector_POI_Target = {}
                            for i in ["X", "Y", "Z"]:
                                Vector_POI_Target[i] = abs(Target[i] - Database["Containers"][Target["Container"]]["POI"][POI][i])

                            Distance_POI_Target = vector_norm(Vector_POI_Target)

                            Target_to_POIs_Distances.append({"Name" : POI, "Distance" : Distance_POI_Target})

                    Target_to_POIs_Distances_Sorted = sorted(Target_to_POIs_Distances, key=lambda k: k['Distance'])
                
                else :
                    Target_to_POIs_Distances_Sorted = [{
                        "Name" : "POI itself",
                        "Distance" : 0
                    }]




                #----------------------------------------------------Player Closest POI--------------------------------------------------------
                Player_to_POIs_Distances = []
                for POI in Actual_Container["POI"]:
                
                    Vector_POI_Player = {}
                    for i in ["X", "Y", "Z"]:
                        Vector_POI_Player[i] = abs(New_player_local_rotated_coordinates[i] - Actual_Container["POI"][POI][i])

                    Distance_POI_Player = vector_norm(Vector_POI_Player)

                    Player_to_POIs_Distances.append({"Name" : POI, "Distance" : Distance_POI_Player})

                Player_to_POIs_Distances_Sorted = sorted(Player_to_POIs_Distances, key=lambda k: k['Distance'])





                #-------------------------------------------------------3 Closest OMs to player---------------------------------------------------------------
                player_Closest_OM = {}
                
                if New_player_local_rotated_coordinates["X"] >= 0:
                    player_Closest_OM["X"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-5"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-5"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-5"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-5"]["Z"]})}
                else:
                    player_Closest_OM["X"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-6"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-6"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-6"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-6"]["Z"]})}
                if New_player_local_rotated_coordinates["Y"] >= 0:
                    player_Closest_OM["Y"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-3"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-3"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-3"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-3"]["Z"]})}
                else:
                    player_Closest_OM["Y"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-4"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-4"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-4"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-4"]["Z"]})}
                if New_player_local_rotated_coordinates["Z"] >= 0:
                    player_Closest_OM["Z"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-1"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-1"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-1"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-1"]["Z"]})}
                else:
                    player_Closest_OM["Z"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-2"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-2"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-2"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-2"]["Z"]})}




                #-------------------------------------------------------3 Closest OMs to target---------------------------------------------------------------
                target_Closest_OM = {}
                
                if Target["X"] >= 0:
                    target_Closest_OM["X"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-5"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-5"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-5"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-5"]["Z"]})}
                else:
                    target_Closest_OM["X"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-6"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-6"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-6"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-6"]["Z"]})}
                if Target["Y"] >= 0:
                    target_Closest_OM["Y"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-3"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-3"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-3"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-3"]["Z"]})}
                else:
                    target_Closest_OM["Y"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-4"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-4"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-4"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-4"]["Z"]})}
                if Target["Z"] >= 0:
                    target_Closest_OM["Z"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-1"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-1"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-1"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-1"]["Z"]})}
                else:
                    target_Closest_OM["Z"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-2"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-2"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-2"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-2"]["Z"]})}




                #----------------------------------------------------Course Deviation to POI--------------------------------------------------------
                #get the vector between current_pos and previous_pos
                Previous_current_pos_vector = {}
                for i in ['X', 'Y', 'Z']:
                    Previous_current_pos_vector[i] = New_player_local_rotated_coordinates[i] - Old_player_local_rotated_coordinates[i]


                #get the vector between current_pos and target_pos
                Current_target_pos_vector = {}
                for i in ['X', 'Y', 'Z']:
                    Current_target_pos_vector[i] = Target[i] - New_player_local_rotated_coordinates[i]


                #get the angle between the current-target_pos vector and the previous-current_pos vector
                Total_deviation_from_target = angle_between_vectors(Previous_current_pos_vector, Current_target_pos_vector)


                if Total_deviation_from_target <= 10:
                    Total_deviation_from_target_color = "#00ff00"
                elif Total_deviation_from_target <= 20:
                    Total_deviation_from_target_color = "#ffd000"
                else:
                    Total_deviation_from_target_color = "#ff3700"


                #----------------------------------------------------------Flat_angle--------------------------------------------------------------
                previous = Old_player_local_rotated_coordinates
                current = New_player_local_rotated_coordinates


                #Vector AB (Previous -> Current)
                previous_to_current = {}
                for i in ["X", "Y", "Z"]:
                    previous_to_current[i] = current[i] - previous[i]

                #Vector AC (C = center of the planet, Previous -> Center)
                previous_to_center = {}
                for i in ["X", "Y", "Z"]:
                    previous_to_center[i] = 0 - previous[i]

                #Vector BD (Current -> Target)
                current_to_target = {}
                for i in ["X", "Y", "Z"]:
                    current_to_target[i] = Target[i] - current[i]

                    #Vector BC (C = center of the planet, Current -> Center)
                current_to_center = {}
                for i in ["X", "Y", "Z"]:
                    current_to_center[i] = 0 - current[i]



                #Normal vector of a plane:
                #abc : Previous/Current/Center
                n1 = {}
                n1["X"] = previous_to_current["Y"] * previous_to_center["Z"] - previous_to_current["Z"] * previous_to_center["Y"]
                n1["Y"] = previous_to_current["Z"] * previous_to_center["X"] - previous_to_current["X"] * previous_to_center["Z"]
                n1["Z"] = previous_to_current["X"] * previous_to_center["Y"] - previous_to_current["Y"] * previous_to_center["X"]

                #acd : Previous/Center/Target
                n2 = {}
                n2["X"] = current_to_target["Y"] * current_to_center["Z"] - current_to_target["Z"] * current_to_center["Y"]
                n2["Y"] = current_to_target["Z"] * current_to_center["X"] - current_to_target["X"] * current_to_center["Z"]
                n2["Z"] = current_to_target["X"] * current_to_center["Y"] - current_to_target["Y"] * current_to_center["X"]

                Flat_angle = angle_between_vectors(n1, n2)


                if Flat_angle <= 10:
                    Flat_angle_color = "#00ff00"
                elif Flat_angle <= 20:
                    Flat_angle_color = "#ffd000"
                else:
                    Flat_angle_color = "#ff3700"
                
                
                
                
                #----------------------------------------------------------Heading--------------------------------------------------------------
                
                bearingX = cos(radians(target_Latitude)) * sin(radians(target_Longitude) - radians(player_Longitude))
                bearingY = cos(radians(player_Latitude)) * sin(radians(target_Latitude)) - sin(radians(player_Latitude)) * cos(radians(target_Latitude)) * cos(radians(target_Longitude) - radians(player_Longitude))

                Bearing = (degrees(atan2(bearingX, bearingY)) + 360) % 360





                #------------------------------------------------------------Backend to Frontend------------------------------------------------------------
                new_data = {
                    "updated" : f"{time.strftime('%H:%M:%S', time.localtime(time.time()))}",
                    "target" : Target['Name'],
                    "player_actual_container" : Actual_Container['Name'],
                    "target_container" : Target['Container'],
                    "player_x" : round(New_player_local_rotated_coordinates['X'], 3),
                    "player_y" : round(New_player_local_rotated_coordinates['Y'], 3),
                    "player_z" : round(New_player_local_rotated_coordinates['Z'], 3),
                    "player_long" : f"{round(player_Longitude, 2)}°",
                    "player_lat" : f"{round(player_Latitude, 2)}°",
                    "player_height" : f"{round(player_Height, 1)} m",
                    "player_OM1" : f"{player_Closest_OM['Z']['OM']['Name']} : {round(player_Closest_OM['Z']['Distance'], 3)} km",
                    "player_OM2" : f"{player_Closest_OM['Y']['OM']['Name']} : {round(player_Closest_OM['Y']['Distance'], 3)} km",
                    "player_OM3" : f"{player_Closest_OM['X']['OM']['Name']} : {round(player_Closest_OM['X']['Distance'], 3)} km",
                    "player_closest_poi" : f"{Player_to_POIs_Distances_Sorted[0]['Name']} : {round(Player_to_POIs_Distances_Sorted[0]['Distance'], 3)} km",
                    "target_x" : Target["X"],
                    "target_y" : Target["Y"],
                    "target_z" : Target["Z"],
                    "target_long" : f"{round(target_Longitude, 2)}°",
                    "target_lat" : f"{round(target_Latitude, 2)}°",
                    "target_height" : f"{round(target_Height, 1)} m",
                    "target_OM1" : f"{target_Closest_OM['Z']['OM']['Name']} : {round(target_Closest_OM['Z']['Distance'], 3)} km",
                    "target_OM2" : f"{target_Closest_OM['Y']['OM']['Name']} : {round(target_Closest_OM['Y']['Distance'], 3)} km",
                    "target_OM3" : f"{target_Closest_OM['X']['OM']['Name']} : {round(target_Closest_OM['X']['Distance'], 3)} km",
                    "target_closest_QT_beacon" : f"{Target_to_POIs_Distances_Sorted[0]['Name']} : {round(Target_to_POIs_Distances_Sorted[0]['Distance'], 3)} km",
                    "distance_to_poi" : f"{round(New_Distance_to_POI_Total, 3)} km",
                    "distance_to_poi_color" : New_Distance_to_POI_Total_color,
                    "delta_distance_to_poi" : f"{round(abs(Delta_Distance_to_POI_Total), 3)} km",
                    "delta_distance_to_poi_color" : Delta_distance_to_poi_color,
                    "total_deviation" : f"{round(Total_deviation_from_target, 1)}°",
                    "total_deviation_color" : Total_deviation_from_target_color,
                    "horizontal_deviation" : f"{round(Flat_angle, 1)}°",
                    "horizontal_deviation_color" : Flat_angle_color,
                    "heading" : f"{round(Bearing, 1)}°",
                    "ETA" : f"{str(datetime.timedelta(seconds=round(Estimated_time_of_arrival, 0)))}"
                }
                print("New data :", json.dumps(new_data))
                sys.stdout.flush()
                



                #------------------------------------------------------------Logs update------------------------------------------------------------
                if Log_Mode == True:
                    if Actual_Container['Name'] != "None":
                        fields = ['None', str(New_player_local_rotated_coordinates['X']), str(New_player_local_rotated_coordinates['Y']), str(New_player_local_rotated_coordinates['Z']), str(Actual_Container['Name']), str(player_Longitude), str(player_Latitude), str(player_Height)]

                        with open(r'Logs/Logs.csv', 'a', newline='') as csv_file:
                            writer = csv.writer(csv_file)
                            writer.writerow(fields)



                #---------------------------------------------------Update coordinates for the next update------------------------------------------
                for i in ["X", "Y", "Z"]:
                    Old_player_Global_coordinates[i] = New_Player_Global_coordinates[i]

                for i in ["X", "Y", "Z"]:
                    Old_player_local_rotated_coordinates[i] = New_player_local_rotated_coordinates[i]

                for i in ["X", "Y", "Z"]:
                    Old_Distance_to_POI[i] = New_Distance_to_POI[i]

                Old_time = New_time

                #-------------------------------------------------------------------------------------------------------------------------------------------








            #-----------------------------------------------------Space Navigation------------------------------------------------------------------
            #If the target is within the attraction of a planet
            if Mode == "Space Navigation":

                #-----------------------------------------------------Distance to POI---------------------------------------------------------------
                New_Distance_to_POI = {}
                for i in ["X", "Y", "Z"]:
                    New_Distance_to_POI[i] = abs(Target[i] - New_Player_Global_coordinates[i])

                #get the real new distance between the player and the target
                New_Distance_to_POI_Total = vector_norm(New_Distance_to_POI)

                if New_Distance_to_POI_Total <= 100:
                    New_Distance_to_POI_Total_color = "#00ff00"
                elif New_Distance_to_POI_Total <= 1000:
                    New_Distance_to_POI_Total_color = "#ffd000"
                else :
                    New_Distance_to_POI_Total_color = "#ff3700"



                #---------------------------------------------------Delta Distance to POI-----------------------------------------------------------
                Old_Distance_to_POI_Total = vector_norm(Old_Distance_to_POI)


                #get the real distance travelled since last update
                Delta_Distance_to_POI_Total = New_Distance_to_POI_Total - Old_Distance_to_POI_Total


                if Delta_Distance_to_POI_Total <= 0:
                    Delta_distance_to_poi_color = "#00ff00"
                else:
                    Delta_distance_to_poi_color = "#ff3700"



                #-----------------------------------------------Estimated time of arrival-----------------------------------------------------------
                #get the time between the last update and this update
                Delta_time = New_time - Old_time


                #get the time it would take to reach destination using the same speed
                try :
                    Estimated_time_of_arrival = (Delta_time*New_Distance_to_POI_Total)/abs(Delta_Distance_to_POI_Total)
                except ZeroDivisionError:
                    Estimated_time_of_arrival = 0.00



                #----------------------------------------------------Course Deviation---------------------------------------------------------------
                #get the vector between current_pos and previous_pos
                Previous_current_pos_vector = {}
                for i in ['X', 'Y', 'Z']:
                    Previous_current_pos_vector[i] = New_Player_Global_coordinates[i] - Old_player_Global_coordinates[i]


                #get the vector between current_pos and target_pos
                Current_target_pos_vector = {}
                for i in ['X', 'Y', 'Z']:
                    Current_target_pos_vector[i] = Target[i] - New_Player_Global_coordinates[i]


                #get the angle between the current-target_pos vector and the previous-current_pos vector
                Course_Deviation = angle_between_vectors(Previous_current_pos_vector, Current_target_pos_vector)
                
                
                if Course_Deviation <= 10:
                    Total_deviation_from_target_color = "#00ff00"
                elif Course_Deviation <= 20:
                    Total_deviation_from_target_color = "#ffd000"
                else:
                    Total_deviation_from_target_color = "#ff3700"




                #------------------------------------------------------------Backend to Frontend------------------------------------------------------------
                new_data = {
                    "updated" : f"Updated : {time.strftime('%H:%M:%S', time.localtime(time.time()))}",
                    "target" : Target['Name'],
                    "player_x" : round(New_Player_Global_coordinates['X'], 3),
                    "player_y" : round(New_Player_Global_coordinates['Y'], 3),
                    "player_z" : round(New_Player_Global_coordinates['Z'], 3),
                    "target_x" : round(Target["X"], 3),
                    "target_y" : round(Target["Y"], 3),
                    "target_z" : round(Target["Z"], 3),
                    "distance_to_poi" : f"{round(New_Distance_to_POI_Total, 3)} km",
                    "distance_to_poi_color" : New_Distance_to_POI_Total_color,
                    "delta_distance_to_poi" : f"{round(abs(Delta_Distance_to_POI_Total), 3)} km",
                    "delta_distance_to_poi_color" : Delta_distance_to_poi_color,
                    "total_deviation" : f"{round(Course_Deviation, 1)}°",
                    "total_deviation_color" : Total_deviation_from_target_color,
                    "ETA" : f"{str(datetime.timedelta(seconds=round(Estimated_time_of_arrival, 0)))}"
                }
                
                print("New data :", json.dumps(new_data))
                sys.stdout.flush()




                #-------------------------------------------Update coordinates for the next update--------------------------------------------------
                for i in ["X", "Y", "Z"]:
                    Old_player_Global_coordinates[i] = New_Player_Global_coordinates[i]
                
                for i in ["X", "Y", "Z"]:
                    Old_Distance_to_POI[i] = New_Distance_to_POI[i]

                Old_time = New_time



            #---------------------------------------------------------------------------------------------------------------------------------------
            
            if Mode == "Companion":
                
                # Actual container
                # Search in the Database to see if the player is in a Container
                Actual_Container = {
                    "Name": "None",
                    "X": 0,
                    "Y": 0,
                    "Z": 0,
                    "Rotation Speed": 0,
                    "Rotation Adjust": 0,
                    "OM Radius": 0,
                    "Body Radius": 0,
                    "POI": {}
                }
                for i in Database["Containers"] :
                    Player_Container_vector = {"X" : Database["Containers"][i]["X"] - New_Player_Global_coordinates["X"], "Y" : Database["Containers"][i]["Y"] - New_Player_Global_coordinates["Y"], "Z" : Database["Containers"][i]["Z"] - New_Player_Global_coordinates["Z"]}
                    if vector_norm(Player_Container_vector) <= 1.5 * Database["Containers"][i]["OM Radius"]:
                        Actual_Container = Database["Containers"][i]
                
                
                
                
                # If around a container :
                if Actual_Container['Name'] != "None" :
                    
                    
                    
                    # Local coordinates
                    
                    #Time passed since the start of game simulation
                    Time_passed_since_reference_in_seconds = New_time - Reference_time
                    #Grab the rotation speed of the container in the Database and convert it in degrees/s
                    Rotation_speed_in_hours_per_rotation = Actual_Container["Rotation Speed"]
                    try:
                        Rotation_speed_in_degrees_per_second = 0.1 * (1/Rotation_speed_in_hours_per_rotation)
                    except ZeroDivisionError:
                        Rotation_speed_in_degrees_per_second = 0
                        continue
                    
                    #Get the actual rotation state in degrees using the rotation speed of the container, the actual time and a rotational adjustment value
                    Rotation_state_in_degrees = ((Rotation_speed_in_degrees_per_second * Time_passed_since_reference_in_seconds) + Actual_Container["Rotation Adjust"]) % 360
                    
                    #get the new player unrotated coordinates
                    New_player_local_unrotated_coordinates = {}
                    for i in ['X', 'Y', 'Z']:
                        New_player_local_unrotated_coordinates[i] = New_Player_Global_coordinates[i] - Actual_Container[i]
                    
                    #get the new player rotated coordinates
                    New_player_local_rotated_coordinates = rotate_point_2D(New_player_local_unrotated_coordinates, radians(-1*Rotation_state_in_degrees))
                    
                    
                    
                    Distance_since_last_update = {}
                    if Actual_Container["Name"] == Old_container["Name"]:
                        for i in ["X", "Y", "Z"]:
                            Distance_since_last_update[i] = abs(Old_player_local_rotated_coordinates[i] - New_player_local_rotated_coordinates[i])
                    
                    else :
                        for i in ["X", "Y", "Z"]:
                            Distance_since_last_update[i] = abs(Old_player_Global_coordinates[i] - New_Player_Global_coordinates[i])
                    Distance_since_last_update_Total = vector_norm(Distance_since_last_update)
                    
                    
                    
                    
                    # Lattitude, Longitude, Height
                    
                    #Radius of the container
                    Radius = Actual_Container["Body Radius"]
                    
                    #Radial_Distance
                    Radial_Distance = sqrt(New_player_local_rotated_coordinates["X"]**2 + New_player_local_rotated_coordinates["Y"]**2 + New_player_local_rotated_coordinates["Z"]**2)
                    
                    #Height
                    Height = Radial_Distance - Radius
                    
                    #Longitude
                    try :
                        Longitude = -1*degrees(atan2(New_player_local_rotated_coordinates["X"], New_player_local_rotated_coordinates["Y"]))
                    except Exception as err:
                        print(f'Error in Longitude : {err} \nx = {New_player_local_rotated_coordinates["X"]}, y = {New_player_local_rotated_coordinates["Y"]} \nPlease report this to Valalol#1790 for me to try to solve this issue')
                        sys.stdout.flush()
                        Longitude = 0
                    
                    #Latitude
                    try :
                        Latitude = degrees(asin(New_player_local_rotated_coordinates["Z"]/Radial_Distance))
                    except Exception as err:
                        print(f'Error in Latitude : {err} \nz = {New_player_local_rotated_coordinates["Z"]}, radius = {Radial_Distance} \nPlease report this at Valalol#1790 for me to try to solve this issue')
                        sys.stdout.flush()
                        Latitude = 0
                    
                    
                    
                    
                    
                    
                    
                    
                    # 3 closest OMs
                    
                    Closest_OM = {}
                    
                    if New_player_local_rotated_coordinates["X"] >= 0:
                        Closest_OM["X"] = {"OM" : Actual_Container["POI"]["OM-5"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Actual_Container["POI"]["OM-5"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Actual_Container["POI"]["OM-5"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Actual_Container["POI"]["OM-5"]["Z"]})}
                    else:
                        Closest_OM["X"] = {"OM" : Actual_Container["POI"]["OM-6"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Actual_Container["POI"]["OM-6"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Actual_Container["POI"]["OM-6"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Actual_Container["POI"]["OM-6"]["Z"]})}
                    if New_player_local_rotated_coordinates["Y"] >= 0:
                        Closest_OM["Y"] = {"OM" : Actual_Container["POI"]["OM-3"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Actual_Container["POI"]["OM-3"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Actual_Container["POI"]["OM-3"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Actual_Container["POI"]["OM-3"]["Z"]})}
                    else:
                        Closest_OM["Y"] = {"OM" : Actual_Container["POI"]["OM-4"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Actual_Container["POI"]["OM-4"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Actual_Container["POI"]["OM-4"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Actual_Container["POI"]["OM-4"]["Z"]})}
                    if New_player_local_rotated_coordinates["Z"] >= 0:
                        Closest_OM["Z"] = {"OM" : Actual_Container["POI"]["OM-1"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Actual_Container["POI"]["OM-1"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Actual_Container["POI"]["OM-1"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Actual_Container["POI"]["OM-1"]["Z"]})}
                    else:
                        Closest_OM["Z"] = {"OM" : Actual_Container["POI"]["OM-2"], "Distance" : vector_norm({"X" : New_player_local_rotated_coordinates["X"] - Actual_Container["POI"]["OM-2"]["X"], "Y" : New_player_local_rotated_coordinates["Y"] - Actual_Container["POI"]["OM-2"]["Y"], "Z" : New_player_local_rotated_coordinates["Z"] - Actual_Container["POI"]["OM-2"]["Z"]})}
                
                
                
                
                
                
                
                    # 2 Closest POIs
                    Player_to_POIs_Distances = []
                    for POI in Database['Containers'][Actual_Container['Name']]["POI"]:
                        Vector_POI_Player = {}
                        for i in ["X", "Y", "Z"]:
                            Vector_POI_Player[i] = abs(New_player_local_rotated_coordinates[i] - Database["Containers"][Actual_Container['Name']]["POI"][POI][i])
                        Distance_POI_Player = vector_norm(Vector_POI_Player)
                        Player_to_POIs_Distances.append({"Name" : POI, "Distance" : Distance_POI_Player})
                
                # for POI in Database['Space_POI']:
                #     Vector_POI_Player = {}
                #     for i in ["X", "Y", "Z"]:
                #         Vector_POI_Player[i] = abs(New_Player_Global_coordinates[i] - Database["Space_POI"][POI][i])
                #     Distance_POI_Player = vector_norm(Vector_POI_Player)
                #     Player_to_POIs_Distances.append({"Name" : POI, "Distance" : Distance_POI_Player})
                
                
                    Player_to_POIs_Distances_Sorted = sorted(Player_to_POIs_Distances, key=lambda k: k['Distance'])






                #------------------------------------------------------------Backend to Frontend------------------------------------------------------------
                if Actual_Container["Name"] == "None":
                    new_data = {
                        "updated" : f"Updated : {time.strftime('%H:%M:%S', time.localtime(time.time()))}",
                        "player_global_x" : f"Global X : {round(New_Player_Global_coordinates['X'], 3)}",
                        "player_global_y" : f"Global Y : {round(New_Player_Global_coordinates['Y'], 3)}",
                        "player_global_z" : f"Global Z : {round(New_Player_Global_coordinates['Z'], 3)}",
                        "distance_change" : f"Distance since last update : {round(Distance_since_last_update_Total, 3)} km",
                        "actual_container" : "None",
                        "player_local_x" : "",
                        "player_local_y" : "",
                        "player_local_z" : "",
                        "player_long" : "",
                        "player_lat" : "",
                        "player_height" : "",
                        "player_OM1" : "",
                        "player_OM2" : "",
                        "player_OM3" : "",
                        "closest_poi" : ""
                    }
                else :
                    new_data = {
                        "updated" : f"Updated : {time.strftime('%H:%M:%S', time.localtime(time.time()))}",
                        "player_global_x" : f"Global X : {round(New_Player_Global_coordinates['X'], 3)}",
                        "player_global_y" : f"Global Y : {round(New_Player_Global_coordinates['Y'], 3)}",
                        "player_global_z" : f"Global Z : {round(New_Player_Global_coordinates['Z'], 3)}",
                        "distance_change" : f"Distance since last update : {round(Distance_since_last_update_Total, 3)} km",
                        "actual_container" : f"Actual Container : {Actual_Container['Name']}",
                        "player_local_x" : f"Local X : {round(New_player_local_rotated_coordinates['X'], 3)}",
                        "player_local_y" : f"Local Y : {round(New_player_local_rotated_coordinates['Y'], 3)}",
                        "player_local_z" : f"Local Z : {round(New_player_local_rotated_coordinates['Z'], 3)}",
                        "player_long" : f"Longitude : {round(Longitude, 2)}°",
                        "player_lat" : f"Latitude : {round(Latitude, 2)}°",
                        "player_height" : f"Height : {round(Height, 1)} m",
                        "player_OM1" : f"{Closest_OM['Z']['OM']['Name']} : {round(Closest_OM['Z']['Distance'], 3)} km",
                        "player_OM2" : f"{Closest_OM['Y']['OM']['Name']} : {round(Closest_OM['Y']['Distance'], 3)} km",
                        "player_OM3" : f"{Closest_OM['X']['OM']['Name']} : {round(Closest_OM['X']['Distance'], 3)} km",
                        "closest_poi" : f"Closest POI : \n{Player_to_POIs_Distances_Sorted[0]['Name']} ({round(Player_to_POIs_Distances_Sorted[0]['Distance'], 3)} km) \n{Player_to_POIs_Distances_Sorted[1]['Name']} ({round(Player_to_POIs_Distances_Sorted[1]['Distance'], 3)} km)",
                        }
                
                print("New data :", json.dumps(new_data))
                sys.stdout.flush()




                #---------------------------------------------------Update coordinates for the next update------------------------------------------
                for i in ["X", "Y", "Z"]:
                    Old_player_Global_coordinates[i] = New_Player_Global_coordinates[i]
                if Actual_Container["Name"] != "None":
                    for i in ["X", "Y", "Z"]:
                        Old_player_local_rotated_coordinates[i] = New_player_local_rotated_coordinates[i]
                
                Old_container = Actual_Container
                
                Old_time = New_time
                
                #-------------------------------------------------------------------------------------------------------------------------------------------


        if new_clipboard == "1rst hotkey":
            print("1rst hotkey")
            sys.stdout.flush()



        if new_clipboard == "2nd hotkey":
            print("2nd hotkey")
            sys.stdout.flush()


# Jericho_Station
# Hurston : Coordinates: x:12850457093 y:0 z:0
# Microtech : Coordinates: x:22462016306.0103 y:37185625645.8346 z:0
# Daymar : Coordinates: x:-18930439540 y:-2610058765 z:0

# Coordinates: x:-16930439540 y:-2610058765 z:0