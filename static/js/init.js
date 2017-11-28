function init() {

    var conn = new WebSocket(window.location.protocol == "https:" ? 'wss' : 'ws' + '://' + window.location.host);

    var number = document.getElementById('number')
    conn.addEventListener('open', function(event){
        console.log('sys:CONNECTED');
    });

    conn.addEventListener('message', function(event){
        update(event.data);
    });

    conn.addEventListener('close', function(event){
        console.log('sys:DISCONNECTED');
    });


    function update(data){
        number.innerHTML = data;
    }

}


