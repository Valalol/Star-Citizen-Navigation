window.resizeTo(550, 350)

var fs = require('fs');


path = require('path');
if (fs.existsSync(path.resolve(__dirname + '../../../Database.json'))) {
    packaged = false;
} else if (fs.existsSync(path.resolve(__dirname + '../../../../../Database.json'))) {
    packaged = true;
}

if (packaged == false) {
    var Database = require('../../Database.json');
    var settings_json = require('../../settings.json');
} else {
    var Database = require('../../../../Database.json');
    var settings_json = require('../../../../settings.json');
}


const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

if (settings_json.remember_choices == true && urlParams.has('ignore_choices') == false) {
    window.location.href = settings_json.last_choice_link;
}

save_settings = function () {
    fs.writeFile('settings.json', JSON.stringify(settings_json, null, 4), function (err) {
        if (err) {
            console.log(err);
        }
    });
}

Container_list = Object.keys(Database["Containers"]);
console.log(Container_list);

Space_POI_list = Object.keys(Database["Space_POI"]);
console.log(Space_POI_list);

Planetary_POI_list = {};
Container_list.forEach(function (container_name) {
    Planetary_POI_list[container_name] = Object.keys(Database["Containers"][container_name]["POI"]);
});
console.log(Planetary_POI_list);



mode_select = document.getElementById("mode_select");


mode_select.addEventListener('change', function () {
    console.log(mode_select.value + ' has been selected as tool mode');

    var mode_divs = document.getElementsByClassName("mode_div");

    Array.from(mode_divs).forEach(function (mode_div) {
        mode_div.style.display = "none";
    });

    document.getElementById(mode_select.value + "_div").style.display = "block";

}, false);



planetary_container_select = document.getElementById("planetary_container_select");
Container_list.forEach(function (Container_list) {
    planetary_container_select.appendChild(
        new Option(Container_list, Container_list)
    );
});

planetary_target_select = document.getElementById("planetary_target_select");

planetary_container_select.addEventListener('change', function () {
    console.log(planetary_container_select.value + ' has been selected as planetary container');

    planetary_target_select.options.length = 0;
    Planetary_POI_list[planetary_container_select.value].forEach(function (Planetary_POI) {
        planetary_target_select.appendChild(
            new Option(Planetary_POI, Planetary_POI)
        );
    });
}, false);


planetary_known_or_custom_POI_select = document.getElementById("planetary_known_or_custom_POI_select");
planetary_known_poi_div = document.getElementById("planetary_known_poi_div");
planetary_custom_poi_div = document.getElementById("planetary_custom_poi_div");

planetary_known_or_custom_POI_select.addEventListener('change', function () {
    console.log(planetary_known_or_custom_POI_select.value + ' has been selected');

    if (planetary_known_or_custom_POI_select.value == "known_POI") {
        planetary_known_poi_div.style.display = "block";
        planetary_custom_poi_div.style.display = "none";
    } else {
        planetary_known_poi_div.style.display = "none";
        planetary_custom_poi_div.style.display = "block";
    }
}, false);



planetary_known_poi_button = document.getElementById("planetary_known_poi_button");

planetary_target_select.addEventListener('change', function () {
    console.log(planetary_target_select.value + ' has been selected as target');

    planetary_known_poi_button.disabled = false;
}, false);


planetary_known_poi_button.addEventListener('click', function () {
    if (planetary_container_select.value == "" || planetary_target_select.value == "") {
        console.log("Please select a container and a target");
    } else {
        link = "../planetary_nav/planetary_nav.html?container=" + planetary_container_select.value +
            "&known=true" +
            "&target=" + planetary_target_select.value;
        console.log(link)
        if (settings_json.remember_choices == true) {
            settings_json.last_choice_link = link;
            save_settings();
        }
        window.location.href = link;
    }
}, false);


custom_entry_type_select = document.getElementById("custom_entry_type_select");

custom_entry_type_select.addEventListener('change', function () {
    var custom_entries_divs = document.getElementsByClassName("custom_entries_div");

    Array.from(custom_entries_divs).forEach(function (custom_entries_div) {
        custom_entries_div.style.display = "none";
    });

    console.log("planetary_custom_poi_" + custom_entry_type_select.value + "_div");
    document.getElementById("planetary_custom_poi_" + custom_entry_type_select.value + "_div").style.display = "flex";
}, false);


planetary_custom_poi_xyz_button = document.getElementById("planetary_custom_poi_xyz_button");
planetary_custom_poi_entry_x = document.getElementById("planetary_custom_poi_entry_x");
planetary_custom_poi_entry_y = document.getElementById("planetary_custom_poi_entry_y");
planetary_custom_poi_entry_z = document.getElementById("planetary_custom_poi_entry_z");

planetary_custom_poi_xyz_button.addEventListener('click', function () {
    if (planetary_container_select.value == "" || planetary_custom_poi_entry_x.value == "" || planetary_custom_poi_entry_y.value == "" || planetary_custom_poi_entry_z.value == "") {
        console.log("one of the fields is empty");
    } else {
        link = "../planetary_nav/planetary_nav.html?container=" + planetary_container_select.value +
            "&known=false" +
            "&entry_type=xyz" +
            "&x=" + planetary_custom_poi_entry_x.value +
            "&y=" + planetary_custom_poi_entry_y.value +
            "&z=" + planetary_custom_poi_entry_z.value;
        console.log(link)
        if (settings_json.remember_choices == true) {
            settings_json.last_choice_link = link;
            save_settings();
        }
        window.location.href = link;
    }
}, false);


planetary_custom_poi_oms_button = document.getElementById("planetary_custom_poi_oms_button");
planetary_custom_poi_entry_OM1 = document.getElementById("planetary_custom_poi_entry_OM1");
planetary_custom_poi_entry_OM2 = document.getElementById("planetary_custom_poi_entry_OM2");
planetary_custom_poi_entry_OM3 = document.getElementById("planetary_custom_poi_entry_OM3");
om_select_1 = document.getElementById("om_select_1");
om_select_2 = document.getElementById("om_select_2");
om_select_3 = document.getElementById("om_select_3");
planetary_custom_poi_entry_omheight = document.getElementById("planetary_custom_poi_entry_omheight");

planetary_custom_poi_oms_button.addEventListener('click', function () {
    if (planetary_container_select.value == "" || planetary_custom_poi_entry_OM1.value == "" || planetary_custom_poi_entry_OM2.value == "" || planetary_custom_poi_entry_OM3.value == "" || om_select_1.value == "" || om_select_2.value == "" || om_select_3.value == "" || planetary_custom_poi_entry_omheight.value == "") {
        console.log("one of the fields is empty");
    } else {
        link = "../planetary_nav/planetary_nav.html?container=" + planetary_container_select.value +
            "&known=false" +
            "&entry_type=oms" +
            "&OM1_name=" + om_select_1.value +
            "&OM1_value=" + planetary_custom_poi_entry_OM1.value +
            "&OM2_name=" + om_select_2.value +
            "&OM2_value=" + planetary_custom_poi_entry_OM2.value +
            "&OM3_name=" + om_select_3.value +
            "&OM3_value=" + planetary_custom_poi_entry_OM3.value +
            "&height=" + planetary_custom_poi_entry_omheight.value;
        console.log(link)
        if (settings_json.remember_choices == true) {
            settings_json.last_choice_link = link;
            save_settings();
        }
        window.location.href = link;
    }
}, false);


planetary_custom_poi_longlatheight_button = document.getElementById("planetary_custom_poi_longlatheight_button");
planetary_custom_poi_entry_lat = document.getElementById("planetary_custom_poi_entry_lat");
planetary_custom_poi_entry_long = document.getElementById("planetary_custom_poi_entry_long");
planetary_custom_poi_entry_llheight = document.getElementById("planetary_custom_poi_entry_llheight");

planetary_custom_poi_longlatheight_button.addEventListener('click', function () {
    if (planetary_container_select.value == "" || planetary_custom_poi_entry_lat.value == "" || planetary_custom_poi_entry_long.value == "" || planetary_custom_poi_entry_llheight.value == "") {
        console.log("one of the fields is empty");
    } else {
        link = "../planetary_nav/planetary_nav.html?container=" + planetary_container_select.value +
            "&known=false" +
            "&entry_type=longlatheight" +
            "&lat=" + planetary_custom_poi_entry_lat.value +
            "&long=" + planetary_custom_poi_entry_long.value +
            "&height=" + planetary_custom_poi_entry_llheight.value;
        console.log(link)
        if (settings_json.remember_choices == true) {
            settings_json.last_choice_link = link;
            save_settings();
        }
        window.location.href = link;
    }
}, false);


space_known_or_custom_POI_select = document.getElementById("space_known_or_custom_POI_select");
space_known_poi_div = document.getElementById("space_known_poi_div");
space_custom_poi_div = document.getElementById("space_custom_poi_div");

space_known_or_custom_POI_select.addEventListener('change', function () {
    console.log(space_known_or_custom_POI_select.value + ' has been selected');

    if (space_known_or_custom_POI_select.value == "known_POI") {
        space_known_poi_div.style.display = "block";
        space_custom_poi_div.style.display = "none";
    } else {
        space_known_poi_div.style.display = "none";
        space_custom_poi_div.style.display = "flex";
    }
}, false);


space_target_select = document.getElementById("space_target_select");

Space_POI_list.forEach(function (Space_POI) {
    space_target_select.appendChild(
        new Option(Space_POI, Space_POI)
    );
});


space_known_poi_button = document.getElementById("space_known_poi_button");

space_target_select.addEventListener('change', function () {
    console.log(space_target_select.value + ' has been selected as target');

    space_known_poi_button.disabled = false;
}, false);


space_known_poi_button = document.getElementById("space_known_poi_button");

space_known_poi_button.addEventListener('click', function () {
    if (space_target_select.value == "") {
        console.log("no target has been selected");
    } else {
        link = "../space_nav/space_nav.html?mode=space_nav" +
            "&known=true" +
            "&target=" + space_target_select.value;
        console.log(link)
        if (settings_json.remember_choices == true) {
            settings_json.last_choice_link = link;
            save_settings();
        }
        window.location.href = link;
    }
}, false);


space_custom_poi_xyz_button = document.getElementById("space_custom_poi_xyz_button");
space_custom_poi_entry_x = document.getElementById("space_custom_poi_entry_x");
space_custom_poi_entry_y = document.getElementById("space_custom_poi_entry_y");
space_custom_poi_entry_z = document.getElementById("space_custom_poi_entry_z");

space_custom_poi_xyz_button.addEventListener('click', function () {
    if (space_custom_poi_entry_x.value == "" || space_custom_poi_entry_y.value == "" || space_custom_poi_entry_z.value == "") {
        console.log("one of the fields is empty");
    } else {
        link = "../space_nav/space_nav.html?mode=space_nav" +
            "&known=false" +
            "&entry_type=xyz" +
            "&x=" + space_custom_poi_entry_x.value +
            "&y=" + space_custom_poi_entry_y.value +
            "&z=" + space_custom_poi_entry_z.value;
        console.log(link)
        if (settings_json.remember_choices == true) {
            settings_json.last_choice_link = link;
            save_settings();
        }
        window.location.href = link;
    }
}, false);


companion_button = document.getElementById("companion_button");

companion_button.addEventListener('click', function () {
    link = "../companion/companion.html";
    console.log(link)
    if (settings_json.remember_choices == true) {
        settings_json.last_choice_link = link;
        save_settings();
    }
    window.location.href = link;
}, false);


home_img = document.getElementById("home_img");

home_img.addEventListener('click', function () {
    link = "menu.html";
    console.log(link)
    window.location.href = link;
}, false);


settings_img = document.getElementById("settings_img");

settings_img.addEventListener('click', function () {
    link = "../settings/settings.html";
    console.log(link)
    window.location.href = link;
}, false);