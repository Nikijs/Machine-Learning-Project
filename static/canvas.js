$(document).ready(function(e) {
  
  // Add a click handler to the submit button.
  $("#submitButton").click(function(e) {
    
    // Prevent the form actually submitting.
    e.preventDefault();
    canvas = document.getElementById('myCanvas');
    console.log(canvas.toDataURL());
    
    // Send AJAX request to generate image to base64
    $.post("/predict", {"theimage": canvas.toDataURL()}, function(data){
      
      // Update the text area with base64.
      $("#randomNumbers").text(data.message);
    
    });
  
  });

});
//code adapted from https://www.html5canvastutorials.com/labs/html5-canvas-paint-application/
var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');
 
var painting = document.getElementById('paint');
var paint_style = getComputedStyle(painting);
canvas.width = parseInt(255);
canvas.height = parseInt(255);

var mouse = {x: 0, y: 0};
 
canvas.addEventListener('mousemove', function(e) {
  mouse.x = e.pageX - this.offsetLeft;
  mouse.y = e.pageY - this.offsetTop;
}, false);

ctx.lineWidth = 10;
ctx.lineJoin = 'round';
ctx.lineCap = 'round';
ctx.strokeStyle = '##000000';
 
canvas.addEventListener('mousedown', function(e) {
    ctx.beginPath();
    ctx.moveTo(mouse.x, mouse.y);
 
    canvas.addEventListener('mousemove', onPaint, false);
}, false);
 
canvas.addEventListener('mouseup', function() {
    canvas.removeEventListener('mousemove', onPaint, false);
}, false);
 
var onPaint = function() {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
};