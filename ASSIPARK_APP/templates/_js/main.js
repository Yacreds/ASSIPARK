let time = document.getElementById("current-time");

setInterval (() => {
    let dt = new Date();
    time.innerHTML = dt.toLocaleTimeString();
},1000)

