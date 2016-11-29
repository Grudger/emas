var createLoad = function() {
    for (var i in volt1Val) {
        load1Val.push(volt1Val[i] * cur1Val[i]);
    }
    for (var i in volt2Val) {
        load2Val.push(volt2Val[i] * cur2Val[i]);
    }
    for (var i in volt3Val) {
        load3Val.push(volt3Val[i] * cur3Val[i]);
    }
    drawChart();
}

var setCur1 = function(myJson) {
    cur1 = jQuery.parseJSON(JSON.stringify(myJson));
    for (var i in cur1) {
        var json2 = cur1[i];
        for (var j in json2) {
            cur1Val.push(json2[j]);
        }
    }
    app.cur2(setCur2);
};

var setCur2 = function(myJson) {
    cur2 = jQuery.parseJSON(JSON.stringify(myJson));
    for (var i in cur2) {
        var json2 = cur2[i];
        for (var j in json2) {
            cur2Val.push(json2[j]);
        }
    }
    app.cur3(setCur3);
};

var setCur3 = function(myJson) {
    cur3 = jQuery.parseJSON(JSON.stringify(myJson));
    for (var i in cur3) {
        var json2 = cur3[i];
        for (var j in json2) {
            cur3Val.push(json2[j]);
        }
    }
    app.volt1(setVolt1);
};

var setVolt1 = function(myJson) {
    volt1 = jQuery.parseJSON(JSON.stringify(myJson));
    for (var i in volt1) {
        var json2 = volt1[i];
        for (var j in json2) {
            volt1Val.push(json2[j]);
        }
    }
    app.volt2(setVolt2);
};

var setVolt2 = function(myJson) {
    volt2 = jQuery.parseJSON(JSON.stringify(myJson));
    for (var i in volt2) {
        var json2 = volt2[i];
        for (var j in json2) {
            volt2Val.push(json2[j]);
        }
    }
    app.volt3(setVolt3);
};

var setVolt3 = function(myJson) {
    volt3 = jQuery.parseJSON(JSON.stringify(myJson));
    for (var i in volt3) {
        var json2 = volt3[i];
        for (var j in json2) {
            volt3Val.push(json2[j]);
        }
    }
    app.time(setTime);
};

var setTime = function(myJson) {
    time = jQuery.parseJSON(JSON.stringify(myJson));
    for (var i in time) {
        var json2 = time[i];
        for (var j in json2) {
            timeVal.push(json2[j]);
        }
    }
    createLoad();
}