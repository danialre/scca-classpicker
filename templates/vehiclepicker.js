// this implies that jquery has already been imported
// list of Vehicle objects: vehiclelist
/* vehicles format: {
    make: {
        model: {
            trim: {
                'yearmin-yearmax': {
                    street: 'street class'
                    etc.
} } } } }
*/
var vehicles = {};
function clear_class() {
    $('#carclass').text(null);
    $.each(["make", "model", "years", "trim"], function(idx, selector) {
        $("#cls-" + selector).find('option').remove()
        $("#cls-" + selector).append($("<option/>", {value: null, text: "Select", disabled: true, selected: true}));
    });
    // update Make selector
    $.each(Object.keys(vehicles), function(idx, val) {
        $("#cls-make").append($("<option/>", {value: val, text: val}));
    });
}
function get_makes_and_models() {
    // (re)generate a list of makes
    vehicles = {};
    $.each(vehiclelist, function(idx) {
        var v = vehiclelist[idx];
        var yearstring = String(v.yearmin) + '-' + String(v.yearmax);
        if(yearstring == "None-None") yearstring = "Any"
        if(!(v.make in vehicles)) {
            vehicles[v.make] = {}
        }
        if(!(v.model in vehicles[v.make])) {
            vehicles[v.make][v.model] = {}
        }
        if(!(v.trim in vehicles[v.make][v.model])) {
            vehicles[v.make][v.model][v.trim] = {}
        }
        if(!(yearstring in vehicles[v.make][v.model][v.trim])) {
            vehicles[v.make][v.model][v.trim][yearstring] = {}
        }
        vehicles[vehiclelist[idx].make][vehiclelist[idx].model][vehiclelist[idx].trim][yearstring] = {
            STREET: vehiclelist[idx].class_street, STR_TOURING: vehiclelist[idx].class_str_touring, STR_PREP: vehiclelist[idx].class_str_prep, STR_MOD: vehiclelist[idx].class_str_mod, PREP: vehiclelist[idx].class_prep, MOD: vehiclelist[idx].class_mod
        }
    });
    if(!$("#cls-make").val()) clear_class();
}

function search_vehicle(make=null, model=null, trim=null, yearrange=null) {
    if(!make) {
        return Object.keys(vehicles); // return a list of makes
    }
    if(!model && !vehicles[make][null]) {
        return Object.keys(vehicles[make]); // return a list of models   
    }
    if(!trim && !vehicles[make][model][null]) {
        return Object.keys(vehicles[make][model]); // return a list of trims
    }
    if(!yearrange && !vehicles[make][model][trim][null]) {
        return Object.keys(vehicles[make][model][trim]); // return a list of year ranges
    }
    return vehicles[make][model][trim][yearrange];
}

function get_model() {
    console.log('model');
    result = search_vehicle(make=$("#cls-make").val());
    $("#cls-model").find('option').remove();
    $("#cls-model").append($("<option/>", {value: null, text: "Select", disabled: true}));
    $.each(result, function(idx, val) {
        $("#cls-model").append($("<option/>", {value: val, text: val}));
    });
    if(result.length <= 1) {
        $("#cls-model option:last-child").attr('selected', true);
        get_trim();
    } else {
        $("#cls-model option:first-child").attr('selected', true);
    }
}
function get_trim() {
    console.log('trim');
    result = search_vehicle(make=$("#cls-make").val(), model=$("#cls-model").val());
    $("#cls-trim").find('option').remove();
    $("#cls-trim").append($("<option/>", {value: null, text: "Select", disabled: true}));
    $.each(result, function(idx, val) {
        $("#cls-trim").append($("<option/>", {value: val, text: val}));
    });
    if(result.length <= 1) {
        $("#cls-trim option:last-child").attr('selected', true);
        get_years();
    } else {
        $("#cls-trim option:first-child").attr('selected', true);
    }
}
function get_years() {
    console.log('years');
    result = search_vehicle(make=$("#cls-make").val(), model=$("#cls-model").val(), trim=$("#cls-trim").val());
    console.log(result);
    $("#cls-years").find('option').remove();
    $("#cls-years").append($("<option/>", {value: null, text: "Select", disabled: true}));
    $.each(result, function(idx, val) {
        $("#cls-years").append($("<option/>", {value: val, text: val}));
    });
    if(result.length <= 1) {
        $("#cls-years option:last-child").attr('selected', true);
        get_vehicleclass();
    } else {
        $("#cls-years option:first-child").attr('selected', true);
    }
}
function get_vehicleclass() {
    var make = $("#cls-make").val();
    var model = $("#cls-model").val();
    var trim = $("#cls-trim").val();
    var years = $("#cls-years").val();
    if(!make || !model || !years || !trim) return; // quit right away
    result = search_vehicle(make, model, trim, years);
    if(result.constructor === Array) return;

    // lookup based on mods and update #carclass
    switch(best_modclass) { // update the UI
        case VCl.STR_TOURING: result = result.STR_TOURING; break;
        case VCl.STR_PREP:    result = result.STR_PREP; break;
        case VCl.STR_MOD:     result = result.STR_MOD; break;
        case VCl.PREP:        result = result.PREP; break;
        case VCl.MOD:         result = result.MOD; break;
        case VCl.XP:          result = "XP"; break;
        default:              result = result.STREET;
    }
    if(result == 'None') result = 'Class not found - check the rulebook';
    $('#carclass').text(result);
}
