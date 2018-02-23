
(function () {

	window.myCoolThing = {aa: 44.3, bb: 'hi there'};

	// Manually construct the WebSocket URL relative to the current page's URL:
	var new_uri;
	if (window.location.protocol === 'https:') {
		new_uri = 'wss:';
	} else {
		new_uri = 'ws:';
	}
	new_uri += '//' + window.location.host + '/ws';


	window.ws = new WebSocket(new_uri);

	window.ws.onmessage = function (msgEvent) {
		console.log('new msg from websocket');
		console.log(msgEvent);

		window.myCoolThing.lastMessage = msgEvent;
	};

}());

