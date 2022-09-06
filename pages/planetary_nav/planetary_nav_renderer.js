window.resizeTo(350, 750)

let { PythonShell } = require('python-shell')

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

// known : ../planetary_nav/planetary_nav.html?container=Aberdeen&known=true&target=Klescher Rehabilitation Facility
// custom oms : ../planetary_nav/planetary_nav.html?container=Aberdeen&known=false&entry_type=oms&OM1_name=om1&OM1_value=242&OM2_name=om4&OM2_value=258.38&OM3_name=om6&OM3_value=8988.36&height=85.3
// custom xyz : ../planetary_nav/planetary_nav.html?container=Aberdeen&known=false&entry_type=xyz&x=424.3&y=42.456&z=147.6
// custom llh : ../planetary_nav/planetary_nav.html?container=Aberdeen&known=false&entry_type=longlatheight&lat=25.5325&long=42.52&height=52.4412

var container = urlParams.get('container');
var known = urlParams.get('known');

if (known == "true") {
    var target = urlParams.get('target');
    var options = {
        mode: 'text',
        args: ["planetary_nav", "--container", container, "--known", "true", "--target", target]
    };
} else {
    var entry_type = urlParams.get('entry_type');
    if (entry_type == "xyz") {
        var x = urlParams.get('x');
        var y = urlParams.get('y');
        var z = urlParams.get('z');
        var options = {
            mode: 'text',
            args: ["planetary_nav", "--container", container, "--known", "false", "--entry_type", "xyz", "--x", x, "--y", y, "--z", z]
        };
    } else if (entry_type == "oms") {
        var OM1_name = urlParams.get('OM1_name');
        var OM1_value = urlParams.get('OM1_value');
        var OM2_name = urlParams.get('OM2_name');
        var OM2_value = urlParams.get('OM2_value');
        var OM3_name = urlParams.get('OM3_name');
        var OM3_value = urlParams.get('OM3_value');
        var height = urlParams.get('height');
        var options = {
            mode: 'text',
            args: ["planetary_nav", "--container", container, "--known", "false", "--entry_type", "oms", "--OM1_name", OM1_name, "--OM1_value", OM1_value, "--OM2_name", OM2_name, "--OM2_value", OM2_value, "--OM3_name", OM3_name, "--OM3_value", OM3_value, "--height", height]
        };
    } else if (entry_type == "longlatheight") {
        var lat = urlParams.get('lat');
        var long = urlParams.get('long');
        var height = urlParams.get('height');
        var options = {
            mode: 'text',
            args: ["planetary_nav", "--container", container, "--known", "false", "--entry_type", "longlatheight", "--lat", lat, "--long", long, "--height", height]
        };
    }
}

let pyshell = new PythonShell('backend.py', options);


error_message = "Something Wrong Happened. \nPlease see the error below \nIf anything shows up please report the issue to Valalol#1790 on Discord"

pyshell.on('stderr', function (stderr) {
    console.log(stderr)
    window.resizeTo(350, 850)

    document.getElementById("planetary_status_icon").src = '../../Images/red_dot.png';
    document.getElementById("planetary_status_message").innerText = error_message
    document.getElementById("planetary_error_message").innerText = stderr
})

pyshell.on('error', function (err) {
    console.log(err)
    window.resizeTo(350, 850)

    document.getElementById("planetary_status_icon").src = '../../Images/red_dot.png';
    document.getElementById("planetary_status_message").innerText = error_message
    document.getElementById("planetary_error_message").innerText = err
})



pyshell.on('message', (message) => {
    console.log(message)
    if (message.startsWith("New data : ")) {
        var new_data = JSON.parse(message.slice(11));

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
})



home_img = document.getElementById("home_img");

home_img.addEventListener('click', function () {
    link = "../menu/menu.html?ignore_choices=true";
    console.log(link)
    window.location.href = link;
} , false);
