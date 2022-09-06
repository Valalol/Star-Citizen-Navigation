window.resizeTo(350,367)

let { PythonShell } = require('python-shell')

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

// space known : ../space_nav/space_nav.html?mode=space_nav&known=true&target=hey
// space custom xyz : ../space_nav/space_nav.html?mode=space_nav&known=false&entry_type=xyz&x=142275&y=257829&z=83583.638

var known = urlParams.get('known');

if (known == "true") {
    var target = urlParams.get('target');
    var options = {
        mode: 'text',
        args: ["space_nav", "--known", "true", "--target", target]
    };
} else {
    var x = urlParams.get('x');
    var y = urlParams.get('y');
    var z = urlParams.get('z');
    var options = {
        mode: 'text',
        args: ["space_nav", "--known", "false", "--x", x, "--y", y, "--z", z]
    };
}


let pyshell = new PythonShell('backend.py', options);


error_message = "Something Wrong Happened. \nPlease see the error below \nIf anything shows up please report the issue to Valalol#1790 on Discord"

pyshell.on('stderr', function (stderr) {
    console.log(stderr)
    window.resizeTo(350, 850)

    document.getElementById("space_status_icon").src = '../../Images/red_dot.png';
    document.getElementById("space_status_message").innerText = error_message
    document.getElementById("space_error_message").innerText = stderr
})

pyshell.on('error', function (err) {
    console.log(err)
    window.resizeTo(350, 850)

    document.getElementById("space_status_icon").src = '../../Images/red_dot.png';
    document.getElementById("space_status_message").innerText = error_message
    document.getElementById("space_error_message").innerText = err
})



pyshell.on('message', (message) => {
    console.log(message)
    if (message.startsWith("New data : ")) {
        var new_data = JSON.parse(message.slice(11));

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
})



home_img = document.getElementById("home_img");

home_img.addEventListener('click', function () {
    link = "../menu/menu.html?ignore_choices=true";
    console.log(link)
    window.location.href = link;
} , false);
