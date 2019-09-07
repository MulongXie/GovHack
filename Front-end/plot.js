function plot_population(data) {
    let board = document.getElementById('plot');

    var population = {'year':[], 'population':[]};
    for(let i=0; i < data.length; i++){
        var existing = false;
        for(let y=0; y < population.year.length; y++){
            if(data[i].Year == population.year[y]){
                population.population[y] += data[i].Population;
                existing = true;
                break;
            }
        }

        if(!existing){
            population.year.push(data[i].Year);
            population.population.push(0);
        }
    }

    var plot_data = [{x: population.year, y: population.population}];
    var plot_layout = {
        width: 359,
        height: 360,
        title: "Population in Australian Capital Territory",
        font:{
            size:10
        },
        xaxis:{
            title: "Year",
            showgrid: false,
            zeroline: false
        },
        yaxis:{
            title: "Population"
        }
    };

    Plotly.newPlot(board, plot_data, plot_layout);
}

function plot_crash(data) {
    console.log(data);

    let board = document.getElementById('plot');

    var crash = {'year':[], 'crash':[]};
    for(let i=0; i < data.length; i++){
        var existing = false;
        for(let c=0; c < crash.year.length; c++){
            if(data[i].Year == crash.year[c]){
                crash.crash[c] += 1;
                existing = true;
                break;
            }
        }

        if(!existing){
            crash.year.push(data[i].Year);
            crash.crash.push(0);
        }
    }

    var plot_data = [{x: crash.year, y: crash.crash}];
    var plot_layout = {
        width: 359,
        height: 360,
        title: "Traffic Crash in Australian Capital Territory",
        font:{
            size:10
        },
        xaxis:{
            title: "Year",
            showgrid: false,
            zeroline: false
        },
        yaxis:{
            title: "Crash Number"
        }
    };

    Plotly.newPlot(board, plot_data, plot_layout);
}

function plot(data, flag) {
    if (flag == 'population'){
        plot_population(data)
    }
    else if (flag == 'crash'){
        plot_crash(data)
    }
}