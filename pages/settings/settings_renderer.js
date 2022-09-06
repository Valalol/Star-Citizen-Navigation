var fs = require('fs');


path = require('path');
if (fs.existsSync(path.resolve(__dirname + '../../../Database.json'))) {
    packaged = false;
} else if (fs.existsSync(path.resolve(__dirname + '../../../../../Database.json'))) {
    packaged = true;
}

if (packaged == false) {
    var settings_json = require('../../settings.json');
} else {
    var settings_json = require('../../../../settings.json');
}


save_settings = function() {
    fs.writeFile('settings.json', JSON.stringify(settings_json, null, 4), function(err) {
        if(err) {
            console.log(err);
        }}
    );
}


update_checker_checkbox = document.getElementById('update_checker_checkbox');
if (settings_json.update_checker == true) {
    update_checker_checkbox.checked = true;
}

logs_checkbox = document.getElementById('logs_checkbox');
if (settings_json.logs_enabled == true) {
    logs_checkbox.checked = true;
}

save_screenshots_checkbox = document.getElementById('save_screenshots_checkbox');
if (settings_json.save_screenshots == true) {
    save_screenshots_checkbox.checked = true;
}

remember_choices_checkbox = document.getElementById('remember_choices_checkbox');
if (settings_json.remember_choices == true) {
    remember_choices_checkbox.checked = true;
}



update_checker_checkbox.addEventListener('change', function() {
    settings_json.update_checker = update_checker_checkbox.checked;
    console.log("New_value for update checker: " + update_checker_checkbox.checked);
    save_settings();
});

logs_checkbox.addEventListener('change', function() {
    settings_json.logs_enabled = logs_checkbox.checked;
    console.log("New_value for logs: " + logs_checkbox.checked);
    save_settings();
});

save_screenshots_checkbox.addEventListener('change', function() {
    settings_json.save_screenshots = save_screenshots_checkbox.checked;
    console.log("New_value for save_screenshots: " + save_screenshots_checkbox.checked);
    save_settings();
});

remember_choices_checkbox.addEventListener('change', function() {
    settings_json.remember_choices = remember_choices_checkbox.checked;
    console.log("New_value for remember_choices: " + remember_choices_checkbox.checked);
    save_settings();
});




home_img = document.getElementById("home_img");

home_img.addEventListener('click', function () {
    link = "../menu/menu.html?ignore_choices=true";
    console.log(link)
    window.location.href = link;
} , false);