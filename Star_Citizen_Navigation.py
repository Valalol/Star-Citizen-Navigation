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
    POI_Selection_Combobox["values"] = Planetary_POI_list[Container_Selection_Combobox.get()]



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
    Target = Database["Containers"][Container_Selection_Combobox.get()]["POI"][f'{POI_Selection_Combobox.get()}']
    
    root.destroy()



def Start_Planetary_Navigation_Custom_POI():
    global Target, Mode
    Mode = Program_mode_selection_Combobox.get()
    Target = {'Name': 'Custom POI', 'Container': f'{Container_Selection_Combobox.get()}', 'X': float(Planetary_X_Custom_POI_Entry.get()), 'Y': float(Planetary_Y_Custom_POI_Entry.get()), 'Z': float(Planetary_Z_Custom_POI_Entry.get())}
    
    root.destroy()



#root
root = tk.Tk()

root.title("Navigation Tool")
root.iconbitmap('Icon.ico')


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


POI_Selection_Combobox = ttk.Combobox(Planetary_Known_POI_Frame, state='readonly', values = "")
POI_Selection_Combobox.bind("<<ComboboxSelected>>", Planetary_Known_Target_Selected)
POI_Selection_Combobox.grid(column='0', padx='8', pady='8', row='0')


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

Space_Navigation_WIP_Label = tk.Label(Space_Navigation_Frame, text="Work in progress")
Space_Navigation_WIP_Label.grid(column='0', padx='8', pady='8', row='0')



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


#-------------------------------------------------------------GUI-----------------------------------------------------------------------
#-------------------------------------------------------------END-----------------------------------------------------------------------



def angle_between_vectors(a, b):
    """Function that return an angle in degrees between 2 vectors"""

    try :
        angle = degrees(acos((a["X"]*b["X"] + a["Y"]*b["Y"] + a["Z"]*b["Z"]) / (vector_norm(a) * vector_norm(b))))
    except :
        angle = 0.0
    return angle


def vector_norm(a):
    """Return the norm of a vector """
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

Old_player_Global_coordinates = {}
for i in ["X", "Y", "Z"]:
    Old_player_Global_coordinates[i] = 0.0

Old_player_local_rotated_coordinates = {}
for i in ["X", "Y", "Z"]:
    Old_player_local_rotated_coordinates[i] = 0.0


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
        #print(f"New clipboard content -> {new_clipboard}")



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
                Actual_Container = 0
                for i in Database["Containers"] :
                    Player_Container_vector = {"X" : Database["Containers"][i]["X"] - New_Player_Global_coordinates["X"], "Y" : Database["Containers"][i]["Y"] - New_Player_Global_coordinates["Y"], "Z" : Database["Containers"][i]["Z"] - New_Player_Global_coordinates["Z"]}
                    if vector_norm(Player_Container_vector) <= 1.5 * Database["Containers"][i]["OM Radius"]:
                        Actual_Container = Database["Containers"][i]



        #-------------------------------------------------New player local Long Lat Height--------------------------------------------------
                if Actual_Container != 0:
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
                        Longitude = degrees(atan2(x, y))
                        
                        #Latitude
                        Latitude = degrees(asin(z/Radius))
                        
                        




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
                except :
                    Estimated_time_of_arrival = 0.00



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
                Course_Deviation = angle_between_vectors(Previous_current_pos_vector, Current_target_pos_vector)



        #---------------------------------------------------Display cool data---------------------------------------------------------------

                print(f"-------------------------------------------------------------------------")
                print(f"Updated                   : {colors.Cyan}{time.strftime('%H:%M:%S', time.localtime(New_time))}{colors.Reset},  Destination : {colors.Cyan}{Target['Name']}{colors.Reset}")
                
                print(f"Global coordinates        : {colors.Cyan}{round(New_Player_Global_coordinates['X'], 3)}{colors.Reset}; {colors.Cyan}{round(New_Player_Global_coordinates['Y'], 3)}{colors.Reset}; {colors.Cyan}{round(New_Player_Global_coordinates['Z'], 3)}{colors.Reset}")
                
                if Actual_Container == 0:
                    print(f"Actual Container          : {colors.Yellow}None{colors.Reset}")
                elif Actual_Container['Name'] == Target['Container']:
                    print(f"Actual Container          : {colors.Green}{Actual_Container['Name']}{colors.Reset}")
                else :
                    print(f"Actual Container          : {colors.Red}{Actual_Container['Name']}{colors.Reset}")
                
                if Actual_Container != 0:
                    if Actual_Container['Name'] == Target['Container']:
                        print(f"Local coordinates         : {colors.Cyan}{round(New_player_local_rotated_coordinates['X'], 3)}{colors.Reset}; {colors.Cyan}{round(New_player_local_rotated_coordinates['Y'], 3)}{colors.Reset}; {colors.Cyan}{round(New_player_local_rotated_coordinates['Z'], 3)}{colors.Reset}")
                        
                        if Delta_Distance_to_POI_Total <= 0 :
                            print(f"Distance to POI           : {colors.Cyan}{round(New_Distance_to_POI_Total, 3)} km{colors.Reset} (Delta : {colors.Green}{round(abs(Delta_Distance_to_POI_Total), 3)} km{colors.Reset})")
                        else :
                            print(f"Distance to POI           : {colors.Cyan}{round(New_Distance_to_POI_Total, 3)} km{colors.Reset} (Delta : {colors.Red}{round(abs(Delta_Distance_to_POI_Total), 3)} km{colors.Reset})")
                
                if Course_Deviation <= 5:
                    print(f"Course Deviation          : {colors.Green}{round(Course_Deviation, 1)}°{colors.Reset}")
                elif Course_Deviation > 5 and Course_Deviation <= 15:
                    print(f"Course Deviation          : {colors.Yellow}{round(Course_Deviation, 1)}°{colors.Reset}")
                else:
                    print(f"Course Deviation          : {colors.Red}{round(Course_Deviation, 1)}°{colors.Reset}")
                
                
                print(f"Estimated time of arrival : {colors.Cyan}{int(Estimated_time_of_arrival)//60} Min {int(Estimated_time_of_arrival)%60} Sec{colors.Reset}")
                
                
                



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
                    Estimated_time_of_arrival = (Delta_time*New_Distance_to_POI)/abs(Delta_Distance_to_POI_Total)
                except :
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


                print(f"-------------------------------------------------------------------------------------------")
                print(f"Destination : {Target['Name']}   Updated : {time.strftime('%H:%M:%S', time.localtime(New_time))}")
                print(f"")
                print(f"         Player Global Coordinates       Distance to the POI       Delta distance to the POI ")
                
                if Delta_Distance_to_POI['X'] <= 0 :
                    print(f"    X :  {New_Player_Global_coordinates['X']}{(31-len(str(New_Player_Global_coordinates['X'])))*' '} {New_Distance_to_POI['X']}{(25-len(str(New_Distance_to_POI['X'])))*' '} {colors.Green}{abs(Delta_Distance_to_POI['X'])}{colors.Reset}")
                else :
                    print(f"    X :  {New_Player_Global_coordinates['X']}{(31-len(str(New_Player_Global_coordinates['X'])))*' '} {New_Distance_to_POI['X']}{(25-len(str(New_Distance_to_POI['X'])))*' '} {colors.Red}{abs(Delta_Distance_to_POI['X'])}{colors.Reset}")

                if Delta_Distance_to_POI['Y'] <= 0 :
                    print(f"    Y :  {New_Player_Global_coordinates['Y']}{(31-len(str(New_Player_Global_coordinates['Y'])))*' '} {New_Distance_to_POI['Y']}{(25-len(str(New_Distance_to_POI['Y'])))*' '} {colors.Green}{abs(Delta_Distance_to_POI['Y'])}{colors.Reset}")
                else :
                    print(f"    Y :  {New_Player_Global_coordinates['Y']}{(31-len(str(New_Player_Global_coordinates['Y'])))*' '} {New_Distance_to_POI['Y']}{(25-len(str(New_Distance_to_POI['Y'])))*' '} {colors.Red}{abs(Delta_Distance_to_POI['Y'])}{colors.Reset}")
                
                if Delta_Distance_to_POI['Z'] <= 0 :
                    print(f"    Z :  {New_Player_Global_coordinates['Z']}{(31-len(str(New_Player_Global_coordinates['Z'])))*' '} {New_Distance_to_POI['Z']}{(25-len(str(New_Distance_to_POI['Z'])))*' '} {colors.Green}{abs(Delta_Distance_to_POI['Z'])}{colors.Reset}")
                else :
                    print(f"    Z :  {New_Player_Global_coordinates['Z']}{(31-len(str(New_Player_Global_coordinates['Z'])))*' '} {New_Distance_to_POI['Z']}{(25-len(str(New_Distance_to_POI['Z'])))*' '} {colors.Red}{abs(Delta_Distance_to_POI['Z'])}{colors.Reset}")
                
                if Delta_Distance_to_POI_Total <= 0 :
                    print(f"Total :                                  {New_Distance_to_POI_Total}{(25-len(str(New_Distance_to_POI_Total)))*' '} {colors.Green}{abs(Delta_Distance_to_POI_Total)}{colors.Reset}")
                else :
                    print(f"Total :                                  {New_Distance_to_POI_Total}{(25-len(str(New_Distance_to_POI_Total)))*' '} {colors.Red}{abs(Delta_Distance_to_POI_Total)}{colors.Reset}")
                
                print(f"")


                print(f"Estimated time of arrival = {Estimated_time_of_arrival} secondes")
                print(f"")

                print(f"Course deviation = {Course_Deviation}\N{DEGREE SIGN}")

                print(f"-------------------------------------------------------------------------------------------")



        #-------------------------------------------Update coordinates for the next update--------------------------------------------------
                for i in ["X", "Y", "Z"]:
                    Old_player_Global_coordinates[i] = New_Player_Global_coordinates[i]

                Old_time = New_time

    #---------------------------------------------------------------------------------------------------------------------------------------


# Jericho_Station
# Hurston : Coordinates: x:12850457093 y:0 z:0
# Microtech : Coordinates: x:22462016306.0103 y:37185625645.8346 z:0
# Daymar : Coordinates: x:-18930439540 y:-2610058765 z:0
