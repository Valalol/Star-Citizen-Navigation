import math
from math import sqrt, degrees, radians, cos, sin, acos
import time
from datetime import datetime

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
        "Javelin-Wreck": {
            "Name": "Javelin-Wreck",
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
    return degrees(acos((a[0]*b[0] + a[1]*b[1] + a[2]*b[2]) / (vector_norm(a) * vector_norm(b))))


def vector_norm(a):
    return sqrt(a[0]**2 + a[1]**2 + a[2]**2)


def rotate_point_2D(Unrotated_coordinates, angle):
    Rotated_coordinates = {}
    Rotated_coordinates["X"] = Unrotated_coordinates["X"] * cos(angle) - Unrotated_coordinates["Y"]*sin(angle)
    Rotated_coordinates["Y"] = Unrotated_coordinates["X"] * sin(angle) + Unrotated_coordinates["Y"]*cos(angle)
    Rotated_coordinates["Z"] = Unrotated_coordinates["Z"]
    return (Rotated_coordinates)


New_time = time.time()

Reference_time_UTC = datetime(2020, 1, 1)
Epoch = datetime(1970, 1, 1)
Reference_time = (Reference_time_UTC - Epoch).total_seconds()


Time_passed_since_reference_in_seconds = New_time - Reference_time


Rotation_speed_in_hours_per_rotation = Database["Containers"]["Daymar"]["Rotation Speed"]
Rotation_speed_in_degrees_per_second = 0.1 * \
    (1/Rotation_speed_in_hours_per_rotation)


Rotation_state_in_degrees = ((Rotation_speed_in_degrees_per_second * Time_passed_since_reference_in_seconds) + Database["Containers"]["Daymar"]["Rotation Adjustment"]) % 360
print(f"Time_passed_since_reference : {Time_passed_since_reference_in_seconds}")

print("Rotation_speed_in_hours_per_rotation :", Rotation_speed_in_hours_per_rotation)
print("Rotation_speed_in_degrees_per_second :", Rotation_speed_in_degrees_per_second)

print(f"Rotation_state_in_degrees : {round(Rotation_state_in_degrees, 2)}°")

Player_global_coordinates = {
    "X": -18930339.540,
    "Y": -2610158.765,
    "Z": 0,
}

Player_local_unrotated_coordinates = {
    "X": Player_global_coordinates["X"] - Database["Containers"]["Daymar"]["X"],
    "Y": Player_global_coordinates["Y"] - Database["Containers"]["Daymar"]["Y"],
    "Z": Player_global_coordinates["Z"] - Database["Containers"]["Daymar"]["Z"]
}

Player_local_rotated_coordinates = rotate_point_2D(Player_local_unrotated_coordinates, radians(Rotation_state_in_degrees))

print(f"Player global coordinates : {Player_global_coordinates}")
print(f"Player local unrotated coordinates : {Player_local_unrotated_coordinates}")
print(f"Player local rotated coordinates : {Player_local_rotated_coordinates}")
