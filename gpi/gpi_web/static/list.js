window.onload = function() {
    request = new XMLHttpRequest();
    request.onload = processList;
    request.open('GET', '/api/packages');
    request.send();
}

function processList() {
    var list = JSON.parse(this.responseText);
    var item;
    var plugin_list = document.getElementById('plugin_list');
    for(var i=0; i < list.length; i++) {
        item = document.createElement("div");
        item.id = list[i].package_name;
        item.innerHTML = listElement(list[i].name, list[i].releases[0].version);
        plugin_list.appendChild(item);
    }
}

function listElement(name, version) {
    return '<span class="packagename">' + name + '</span>: <span class="packageversion">' + version + '</span>';
}
