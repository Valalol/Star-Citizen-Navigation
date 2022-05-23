let { PythonShell } = require('python-shell')

window.resizeTo(350,119)

var Mode = ""

let pyshell = new PythonShell('backend.py')

error_message = "Something Wrong Happened. \nPlease see the error below \nIf anything shows up please report the issue to Valalol#1790 on Discord"

pyshell.on('stderr', function (stderr) {
    console.log(stderr)
    window.resizeTo(350,850)

    document.getElementById("loading_status_icon").src = 'Images/red_dot.png';
    document.getElementById("loading_status_message").innerText = error_message
    document.getElementById("loading_error_message").innerText = stderr
    document.getElementById("planetary_status_icon").src = 'Images/red_dot.png';
    document.getElementById("planetary_status_message").innerText = error_message
    document.getElementById("planetary_error_message").innerText = stderr
    document.getElementById("space_status_icon").src = 'Images/red_dot.png';
    document.getElementById("space_status_message").innerText = error_message
    document.getElementById("space_error_message").innerText = stderr
    document.getElementById("companion_status_icon").src = 'Images/red_dot.png';
    document.getElementById("companion_status_message").innerText = error_message
    document.getElementById("companion_error_message").innerText = stderr
})

pyshell.on('error', function (err) {
    console.log(err)
    window.resizeTo(350,850)

    document.getElementById("loading_status_icon").src = 'Images/red_dot.png';
    document.getElementById("loading_status_message").innerText = error_message
    document.getElementById("loading_error_message").innerText = err
    document.getElementById("planetary_status_icon").src = 'Images/red_dot.png';
    document.getElementById("planetary_status_message").innerText = error_message
    document.getElementById("planetary_error_message").innerText = err
    document.getElementById("space_status_icon").src = 'Images/red_dot.png';
    document.getElementById("space_status_message").innerText = error_message
    document.getElementById("space_error_message").innerText = err
    document.getElementById("companion_status_icon").src = 'Images/red_dot.png';
    document.getElementById("companion_status_message").innerText = error_message
    document.getElementById("companion_error_message").innerText = err
})





pyshell.on('message', (message) => {
    console.log(message)
    if (message.startsWith('Mode : ')) {
        Mode = message.slice(7)
        console.log("Mode selected :", Mode)

        if (Mode === "Planetary Navigation") {
            window.resizeTo(350,750)
            // hide all mode divs except planetary navigation
            document.getElementById("Loading").style.display = "none";
            document.getElementById("planetary_Navigation").style.display = "block";
            document.getElementById("Space_Navigation").style.display = "none";
            document.getElementById("companion").style.display = "none";
        }
        if (Mode === "Space Navigation") {
            window.resizeTo(350,367)
            // hide all mode divs except space navigation
            document.getElementById("Loading").style.display = "none";
            document.getElementById("planetary_Navigation").style.display = "none";
            document.getElementById("Space_Navigation").style.display = "block";
            document.getElementById("companion").style.display = "none";
            
        }
        if (Mode === "Companion") {
            window.resizeTo(350,450)
            // hide all mode divs except companion
            document.getElementById("Loading").style.display = "none";
            document.getElementById("planetary_Navigation").style.display = "none";
            document.getElementById("Space_Navigation").style.display = "none";
            document.getElementById("companion").style.display = "block";
            
        }
    }
    if (message.startsWith("New data : ")) {
        var new_data = JSON.parse(message.slice(11));

        if (Mode === "Planetary Navigation") {
            document.getElementById("planetary_updated_value").innerText = new_data["updated"]
            document.getElementById("planetary_target_selected_value").innerText = new_data["target"]
            document.getElementById("planetary_player_container_value").innerText = new_data["player_actual_container"]
            document.getElementById("player_X_local_coordinate_value").innerText = new_data["player_x"]
            document.getElementById("player_Y_local_coordinate_value").innerText = new_data["player_y"]
            document.getElementById("player_Z_local_coordinate_value").innerText = new_data["player_z"]
            document.getElementById("player_longitude_value").innerText = new_data["player_long"]
            document.getElementById("player_latitude_value").innerText = new_data["player_lat"]
            document.getElementById("player_height_value").innerText = new_data["player_height"]
            document.getElementById("player_OM1_value").innerText = new_data["player_OM1"]
            document.getElementById("player_OM2_value").innerText = new_data["player_OM2"]
            document.getElementById("player_OM3_value").innerText = new_data["player_OM3"]
            document.getElementById("player_closest_poi_value").innerText = new_data["player_closest_poi"]
            document.getElementById("player_state_of_the_day_value").innerText = new_data["player_state_of_the_day"]
            document.getElementById("player_next_event_value").innerText = new_data["player_next_event"]
            document.getElementById("player_next_event_time_value").innerText = new_data["player_next_event_time"]
            document.getElementById("target_container_value").innerText = new_data["target_container"]
            document.getElementById("target_X_local_coordinate_value").innerText = new_data["target_x"]
            document.getElementById("target_Y_local_coordinate_value").innerText = new_data["target_y"]
            document.getElementById("target_Z_local_coordinate_value").innerText = new_data["target_z"]
            document.getElementById("target_longitude_value").innerText = new_data["target_long"]
            document.getElementById("target_latitude_value").innerText = new_data["target_lat"]
            document.getElementById("target_height_value").innerText = new_data["target_height"]
            document.getElementById("target_OM1_value").innerText = new_data["target_OM1"]
            document.getElementById("target_OM2_value").innerText = new_data["target_OM2"]
            document.getElementById("target_OM3_value").innerText = new_data["target_OM3"]
            document.getElementById("target_closest_QT_beacon_value").innerText = new_data["target_closest_QT_beacon"]
            document.getElementById("target_state_of_the_day_value").innerText = new_data["target_state_of_the_day"]
            document.getElementById("target_next_event_value").innerText = new_data["target_next_event"]
            document.getElementById("target_next_event_time_value").innerText = new_data["target_next_event_time"]
            document.getElementById("planetary_distance_to_poi_value").innerText = new_data["distance_to_poi"]
            document.getElementById("planetary_distance_to_poi_value").style.color = new_data["distance_to_poi_color"]
            document.getElementById("planetary_distance_to_poi_value_delta").innerText = new_data["delta_distance_to_poi"]
            document.getElementById("planetary_distance_to_poi_value_delta").style.color = new_data["delta_distance_to_poi_color"]
            document.getElementById("planetary_course_deviation_value").innerText = new_data["total_deviation"]
            document.getElementById("planetary_course_deviation_value").style.color = new_data["total_deviation_color"]
            document.getElementById("planetary_flat_angle_value").innerText = new_data["horizontal_deviation"]
            document.getElementById("planetary_flat_angle_value").style.color = new_data["horizontal_deviation_color"]
            document.getElementById("planetary_heading_value").innerText = new_data["heading"]
            document.getElementById("planetary_ETA_value").innerText = new_data["ETA"]
            console.log("Succefully updated the GUI")
        }

        if (Mode === "Space Navigation") {
            document.getElementById("space_updated_value").innerText = new_data["updated"]
            document.getElementById("space_target_selected_value").innerText = new_data["target"]
            document.getElementById("player_X_global_coordinate_value").innerText = new_data["player_x"]
            document.getElementById("player_Y_global_coordinate_value").innerText = new_data["player_y"]
            document.getElementById("player_Z_global_coordinate_value").innerText = new_data["player_z"]
            document.getElementById("target_X_global_coordinate_value").innerText = new_data["target_x"]
            document.getElementById("target_Y_global_coordinate_value").innerText = new_data["target_y"]
            document.getElementById("target_Z_global_coordinate_value").innerText = new_data["target_z"]
            document.getElementById("space_distance_to_poi_value").innerText = new_data["distance_to_poi"]
            document.getElementById("space_distance_to_poi_value").style.color = new_data["distance_to_poi_color"]
            document.getElementById("space_distance_to_poi_value_delta").innerText = new_data["delta_distance_to_poi"]
            document.getElementById("space_distance_to_poi_value_delta").style.color = new_data["delta_distance_to_poi_color"]
            document.getElementById("space_course_deviation_value").innerText = new_data["total_deviation"]
            document.getElementById("space_course_deviation_value").style.color = new_data["total_deviation_color"]
            document.getElementById("space_ETA_value").innerText = new_data["ETA"]
            console.log("Succefully updated the GUI")
        }

        if (Mode === "Companion") {
            document.getElementById("companion_updated").innerText = new_data["updated"]
            document.getElementById("companion_player_X_global_coordinate").innerText = new_data["player_global_x"]
            document.getElementById("companion_player_Y_global_coordinate").innerText = new_data["player_global_y"]
            document.getElementById("companion_player_Z_global_coordinate").innerText = new_data["player_global_z"]
            document.getElementById("distance_changed").innerText = new_data["distance_change"]
            document.getElementById("companion_player_container").innerText = new_data["actual_container"]
            document.getElementById("companion_player_X_local_coordinate").innerText = new_data["player_local_x"]
            document.getElementById("companion_player_Y_local_coordinate").innerText = new_data["player_local_y"]
            document.getElementById("companion_player_Z_local_coordinate").innerText = new_data["player_local_z"]
            document.getElementById("companion_player_longitude").innerText = new_data["player_long"]
            document.getElementById("companion_player_latitude").innerText = new_data["player_lat"]
            document.getElementById("companion_player_height").innerText = new_data["player_height"]
            document.getElementById("companion_OM1").innerText = new_data["player_OM1"]
            document.getElementById("companion_OM2").innerText = new_data["player_OM2"]
            document.getElementById("companion_OM3").innerText = new_data["player_OM3"]
            document.getElementById("companion_closest_poi").innerText = new_data["closest_poi"]
        }
    }
})


