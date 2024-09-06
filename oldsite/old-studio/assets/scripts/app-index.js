var fSpeed = false;
var tFast = (Math.random() * 10000) + 1000;
var tSlow = (Math.random() * 600000) + 100000;
var r = "http://www.unknowablesymbols.com"
var t;

if(fSpeed === true){
	t =+ tFast;
} else {
	t =+ tSlow;
}

window.onkeyup = function(e) {
   var key = e.keyCode ? e.keyCode : e.which;
   if (key == 13) {
       window.location = r;
   }
}

// setInterval(function(){
// 	window.location = r;
// }, t);

