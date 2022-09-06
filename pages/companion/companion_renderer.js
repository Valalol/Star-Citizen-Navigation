window.resizeTo(350,450)

let { PythonShell } = require('python-shell')


var options = {
    mode: 'text',
    args: ["companion"]
};

let pyshell = new PythonShell('backend.py', options);


error_message = "Something Wrong Happened. \nPlease see the error below \nIf anything shows up please report the issue to Valalol#1790 on Discord"

pyshell.on('stderr', function (stderr) {
    console.log(stderr)
    window.resizeTo(350, 850)

    document.getElementById("companion_status_icon").src = '../../Images/red_dot.png';
    document.getElementById("companion_status_message").innerText = error_message
    document.getElementById("companion_error_message").innerText = err
})

pyshell.on('error', function (err) {
    console.log(err)
    window.resizeTo(350, 850)

    document.getElementById("companion_status_icon").src = '../../Images/red_dot.png';
    document.getElementById("companion_status_message").innerText = error_message
    document.getElementById("companion_error_message").innerText = err
})



pyshell.on('message', (message) => {
    console.log(message)
    if (message.startsWith("New data : ")) {
        var new_data = JSON.parse(message.slice(11));

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
        console.log("Succefully updated the GUI")
    }
})



home_img = document.getElementById("home_img");

home_img.addEventListener('click', function () {
    link = "../menu/menu.html?ignore_choices=true";
    console.log(link)
    window.location.href = link;
}, false);
