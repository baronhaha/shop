var getUserMedia;
var browserUserMedia =	navigator.webkitGetUserMedia	||	// WebKit
						navigator.mozGetUserMedia	||	// Mozilla FireFox
						navigator.getUserMedia;			// 2013...
if ( !browserUserMedia ) throw 'Your browser doesn\'t support WebRTC';

getUserMedia = browserUserMedia.bind( navigator );

getUserMedia(
	{
		audio: true,
		video: true
	},
	function( stream ) {
		console.log( stream );
	},
	function( err ) {
		console.log( err );
	}
);