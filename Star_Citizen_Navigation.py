#Made by Valalol#4360
#First release 16/04/2021

#Imports
import math
from math import sqrt, degrees, radians, cos, acos, sin, asin, atan2
import pyperclip
import time
from datetime import datetime
import tkinter as tk
import tkinter.ttk as ttk
import json
import os
import csv

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

Companion_Tool_WIP_Label = tk.Label(Companion_Tool_Frame, text="Work in progress")
Companion_Tool_WIP_Label.grid(column='0', padx='8', pady='8', row='0')



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
    print(f'Program Mode not selected')
    time.sleep(1/3)
    print(f'Closing program ...')
    time.sleep(1)
    exit()


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
Reference_time_UTC = datetime(2020, 1, 1)
Epoch = datetime(1970, 1, 1)
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


Old_time = time.time()


#Reset the clipboard content
pyperclip.copy("")


print("Program is ready \nType the command '/showlocation' in the chat to start the navigation")


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



                #---------------------------------------------------New player local coordinates----------------------------------------------------
                #Time passed since the start of game simulation
                Time_passed_since_reference_in_seconds = New_time - Reference_time

                #Grab the rotation speed of the container in the Database and convert it in degrees/s
                Rotation_speed_in_hours_per_rotation = Database["Containers"][Target["Container"]]["Rotation Speed"]
                Rotation_speed_in_degrees_per_second = 0.1 * (1/Rotation_speed_in_hours_per_rotation)

                #Get the actual rotation state in degrees using the rotation speed of the container, the actual time and a rotational adjustment value
                Rotation_state_in_degrees = ((Rotation_speed_in_degrees_per_second * Time_passed_since_reference_in_seconds) + Database["Containers"][Target["Container"]]["Rotation Adjust"]) % 360

                #get the new player unrotated coordinates
                New_player_local_unrotated_coordinates = {}
                for i in ['X', 'Y', 'Z']:
                    New_player_local_unrotated_coordinates[i] = New_Player_Global_coordinates[i] - Database["Containers"][Target["Container"]][i]

                #get the new player rotated coordinates
                New_player_local_rotated_coordinates = rotate_point_2D(New_player_local_unrotated_coordinates, radians(-1*Rotation_state_in_degrees))



                #---------------------------------------------------Actual Container----------------------------------------------------------------
                #search in the Databse to see if the player is ina Container
                Actual_Container = {
                    "Name": None,
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



                #-------------------------------------------------New player local Long Lat Height--------------------------------------------------
                
                if Actual_Container['Name'] == Target['Container']:
                    
                    #Cartesian Coordinates
                    x = New_player_local_rotated_coordinates["X"]
                    y = New_player_local_rotated_coordinates["Y"]
                    z = New_player_local_rotated_coordinates["Z"]

                    #Radius of the container
                    Radius = Actual_Container["Body Radius"]

                    #Radial_Distance
                    Radial_Distance = sqrt(x**2 + y**2 + z**2)

                    #Height
                    Height = Radial_Distance - Radius
                    
                    #Longitude
                    try :
                        Longitude = -1*degrees(atan2(x, y))
                    except Exception as err:
                        print(f'Error in Longitude : {err}')
                        Longitude = 0
                        continue

                    #Latitude
                    try :
                        Latitude = degrees(asin(z/Radius))
                    except Exception as err:
                        print(f'Error in Latitude : {err}')
                        Latitude = 0
                        continue





                #---------------------------------------------------Distance to POI-----------------------------------------------------------------
                New_Distance_to_POI = {}
                for i in ["X", "Y", "Z"]:
                    New_Distance_to_POI[i] = abs(Target[i] - New_player_local_rotated_coordinates[i])

                #get the real new distance between the player and the target
                New_Distance_to_POI_Total = vector_norm(New_Distance_to_POI)



                #---------------------------------------------------Delta Distance to POI-----------------------------------------------------------
                #get the 3 old XYZ distances between the player and the target
                Old_Distance_to_POI = {}
                for i in ["X", "Y", "Z"]:
                    Old_Distance_to_POI[i] = abs(Target[i] - Old_player_local_rotated_coordinates[i])

                #get the real old distance between the player and the target
                Old_Distance_to_POI_Total = vector_norm(Old_Distance_to_POI)



                #get the 3 XYZ distance travelled since last update
                Delta_Distance_to_POI = {}
                for i in ["X", "Y", "Z"]:
                    Delta_Distance_to_POI[i] = New_Distance_to_POI[i] - Old_Distance_to_POI[i]

                #get the real distance travelled since last update
                Delta_Distance_to_POI_Total = New_Distance_to_POI_Total - Old_Distance_to_POI_Total



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
                
                
                
                #-------------------------------------------------------3 Closest OMs---------------------------------------------------------------
                Closest_OM = {}
                
                if Target["X"] >= 0:
                    Closest_OM["X"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-5"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-5"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-5"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-5"]["Z"]})}
                else:
                    Closest_OM["X"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-6"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-6"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-6"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-6"]["Z"]})}
                if Target["Y"] >= 0:
                    Closest_OM["Y"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-3"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-3"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-3"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-3"]["Z"]})}
                else:
                    Closest_OM["Y"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-4"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-4"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-4"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-4"]["Z"]})}
                if Target["Z"] >= 0:
                    Closest_OM["Z"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-1"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-1"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-1"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-1"]["Z"]})}
                else:
                    Closest_OM["Z"] = {"OM" : Database["Containers"][Target["Container"]]["POI"]["OM-2"], "Distance" : vector_norm({"X" : Target["X"] - Database["Containers"][Target["Container"]]["POI"]["OM-2"]["X"], "Y" : Target["Y"] - Database["Containers"][Target["Container"]]["POI"]["OM-2"]["Y"], "Z" : Target["Z"] - Database["Containers"][Target["Container"]]["POI"]["OM-2"]["Z"]})}




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
                Total_deviation_from_target= angle_between_vectors(Previous_current_pos_vector, Current_target_pos_vector)



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




                #---------------------------------------------------Display cool data---------------------------------------------------------------)))))))))

                print(f"---------------------------------------------------------------------------------------")
                print(f"Updated                           : {colors.Cyan}{time.strftime('%H:%M:%S', time.localtime(New_time))}{colors.Reset}")
                
                print(f"Target                            : {colors.Cyan}{Target['Name']}{colors.Reset}   ({colors.Cyan}{Target['X']}{colors.Reset}; {colors.Cyan}{Target['Y']}{colors.Reset}; {colors.Cyan}{Target['Z']}{colors.Reset})")
                
                print(f"Closest Orbital Markers           : {colors.Cyan}{Closest_OM['Z']['OM']['Name']} ({round(Closest_OM['Z']['Distance'], 3)} km){colors.Reset}, {colors.Cyan}{Closest_OM['Y']['OM']['Name']} ({round(Closest_OM['Y']['Distance'], 3)} km){colors.Reset}, {colors.Cyan}{Closest_OM['X']['OM']['Name']} ({round(Closest_OM['X']['Distance'], 3)} km){colors.Reset}")
                
                if Target["QTMarker"] == "FALSE":
                    print(f"Closest Quantum Beacon to target  : {colors.Cyan}{Target_to_POIs_Distances_Sorted[0]['Name']}{colors.Reset} ({colors.Cyan}{round(Target_to_POIs_Distances_Sorted[0]['Distance'], 3)} km{colors.Reset})")

                print(f"Global coordinates                : {colors.Cyan}{round(New_Player_Global_coordinates['X'], 3)}{colors.Reset}; {colors.Cyan}{round(New_Player_Global_coordinates['Y'], 3)}{colors.Reset}; {colors.Cyan}{round(New_Player_Global_coordinates['Z'], 3)}{colors.Reset}")

                if Actual_Container['Name'] == None:
                    print(f"Actual Container                  : {colors.Yellow}None{colors.Reset}")
                elif Actual_Container['Name'] == Target['Container']:
                    print(f"Actual Container                  : {colors.Green}{Actual_Container['Name']}{colors.Reset}")
                else :
                    print(f"Actual Container                  : {colors.Red}{Actual_Container['Name']}{colors.Reset}")

                if Actual_Container['Name'] == Target['Container']:
                    print(f"Local coordinates                 : {colors.Cyan}{round(New_player_local_rotated_coordinates['X'], 3)}{colors.Reset}; {colors.Cyan}{round(New_player_local_rotated_coordinates['Y'], 3)}{colors.Reset}; {colors.Cyan}{round(New_player_local_rotated_coordinates['Z'], 3)}{colors.Reset}")

                    if Delta_Distance_to_POI_Total <= 0 :
                        print(f"Distance to POI                   : {colors.Cyan}{round(New_Distance_to_POI_Total, 3)} km{colors.Reset} (Delta : {colors.Green}{round(abs(Delta_Distance_to_POI_Total), 3)} km{colors.Reset})")
                    else :
                        print(f"Distance to POI                   : {colors.Cyan}{round(New_Distance_to_POI_Total, 3)} km{colors.Reset} (Delta : {colors.Red}{round(abs(Delta_Distance_to_POI_Total), 3)} km{colors.Reset})")

                if Total_deviation_from_target <= 10:
                    print(f"Total deviation from target       : {colors.Green}{round(Total_deviation_from_target, 1)}°{colors.Reset}")
                elif 10 < Total_deviation_from_target <= 20:
                    print(f"Total deviation from target       : {colors.Yellow}{round(Total_deviation_from_target, 1)}°{colors.Reset}")
                else:
                    print(f"Total deviation from target       : {colors.Red}{round(Total_deviation_from_target, 1)}°{colors.Reset}")


                if Actual_Container['Name'] == Target['Container']:
                    if Flat_angle <= 10:
                        print(f"Horizontal deviation from target  : {colors.Green}{round(Flat_angle, 1)}°{colors.Reset}")
                    elif 10 < Flat_angle <= 20:
                        print(f"Horizontal deviation from target  : {colors.Yellow}{round(Flat_angle, 1)}°{colors.Reset}")
                    else:
                        print(f"Horizontal deviation from target  : {colors.Red}{round(Flat_angle, 1)}°{colors.Reset}")


                print(f"Estimated time of arrival         : {colors.Cyan}{int(Estimated_time_of_arrival)//60} Min {int(Estimated_time_of_arrival)%60} Sec{colors.Reset}")



                #------------------------------------------------------------Logs update------------------------------------------------------------
                if Log_Mode == True:
                    fields = ['None', str(New_player_local_rotated_coordinates['X']), str(New_player_local_rotated_coordinates['Y']), str(New_player_local_rotated_coordinates['Z']), str(Actual_Container['Name']), str(Longitude), str(Latitude), str(Height)]

                    with open(r'Logs/Logs.csv', 'a', newline='') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow(fields)



                #---------------------------------------------------Update coordinates for the next update------------------------------------------
                for i in ["X", "Y", "Z"]:
                    Old_player_Global_coordinates[i] = New_Player_Global_coordinates[i]

                for i in ["X", "Y", "Z"]:
                    Old_player_local_rotated_coordinates[i] = New_player_local_rotated_coordinates[i]

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



                #---------------------------------------------------Delta Distance to POI-----------------------------------------------------------
                #get the 3 old XYZ distances between the player and the target
                Old_Distance_to_POI = {}
                for i in ["X", "Y", "Z"]:
                    Old_Distance_to_POI[i] = abs(Target[i] - Old_player_Global_coordinates[i])

                #get the real old distance between the player and the target
                Old_Distance_to_POI_Total = vector_norm(Old_Distance_to_POI)



                #get the 3 XYZ distance travelled since last update
                Delta_Distance_to_POI = {}
                for i in ["X", "Y", "Z"]:
                    Delta_Distance_to_POI[i] = New_Distance_to_POI[i] - Old_Distance_to_POI[i]

                #get the real distance travelled since last update
                Delta_Distance_to_POI_Total = New_Distance_to_POI_Total - Old_Distance_to_POI_Total



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



                #----------------------------------------------------Display cool data--------------------------------------------------------------


                print(f"-------------------------------------------------------------------------")
                print(f"Updated                   : {colors.Cyan}{time.strftime('%H:%M:%S', time.localtime(New_time))}{colors.Reset},  Destination : {colors.Cyan}{Target['Name']}{colors.Reset}")

                print(f"Global coordinates        : {colors.Cyan}{round(New_Player_Global_coordinates['X'], 3)}{colors.Reset}; {colors.Cyan}{round(New_Player_Global_coordinates['Y'], 3)}{colors.Reset}; {colors.Cyan}{round(New_Player_Global_coordinates['Z'], 3)}{colors.Reset}")

                if Delta_Distance_to_POI_Total <= 0 :
                    print(f"Distance to POI           : {colors.Cyan}{round(New_Distance_to_POI_Total, 3)} km{colors.Reset} (Delta : {colors.Green}{round(abs(Delta_Distance_to_POI_Total), 3)} km{colors.Reset})")
                else :
                    print(f"Distance to POI           : {colors.Cyan}{round(New_Distance_to_POI_Total, 3)} km{colors.Reset} (Delta : {colors.Red}{round(abs(Delta_Distance_to_POI_Total), 3)} km{colors.Reset})")

                if Course_Deviation <= 10:
                    print(f"Course Deviation          : {colors.Green}{round(Course_Deviation, 1)}°{colors.Reset}")
                elif 10 < Course_Deviation <= 20:
                    print(f"Course Deviation          : {colors.Yellow}{round(Course_Deviation, 1)}°{colors.Reset}")
                else:
                    print(f"Course Deviation          : {colors.Red}{round(Course_Deviation, 1)}°{colors.Reset}")


                print(f"Estimated time of arrival : {colors.Cyan}{int(Estimated_time_of_arrival)//60} Min {int(Estimated_time_of_arrival)%60} Sec{colors.Reset}")



                #-------------------------------------------Update coordinates for the next update--------------------------------------------------
                for i in ["X", "Y", "Z"]:
                    Old_player_Global_coordinates[i] = New_Player_Global_coordinates[i]

                Old_time = New_time


        #---------------------------------------------------------------------------------------------------------------------------------------


        if new_clipboard == "1rst hotkey":
            print("1rst hotkey")



        if new_clipboard == "2nd hotkey":
            print("2nd hotkey")


# Jericho_Station
# Hurston : Coordinates: x:12850457093 y:0 z:0
# Microtech : Coordinates: x:22462016306.0103 y:37185625645.8346 z:0
# Daymar : Coordinates: x:-18930439540 y:-2610058765 z:0
