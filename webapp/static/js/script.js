function vibrateDevice() {
    if("vibrate" in navigator) {
	    navigator.vibrate(200);
    }
}
function sendSignal(button) {
	    fetch('/click-button', {
	        method: 'POST',
	        headers: { 'Content-Type': 'application/json' },
	        body: JSON.stringify({ signal: button})  // Send parameter
	    })
	    .then(response => response.json())
	    .then(data => setStatus(data.response))  // Show response in status
	    .catch(error => console.error('Error:', error));
	}
function buttonClicked(button) {
    vibrateDevice();
    sendSignal(button);
}
function setStatus(text) {
    document.getElementById('status').innerHTML = text;

}
