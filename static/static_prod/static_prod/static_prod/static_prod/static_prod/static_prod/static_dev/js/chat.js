navigator.getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia;
var permissions = { audio: true, video: true };

navigator.getUserMedia(permissions, gotStream, streamError);

function gotStream(stream) {
   var videoElement = document.querySelector('video');
   videoElement.src = URL.createObjectURL(stream);
}

function streamError(error) {
   console.log(error);
}