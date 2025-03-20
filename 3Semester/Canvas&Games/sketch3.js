let circleX = 100;
let circleY = 100;

function setup() {
    createCanvas(windowWidth, windowHeight);
  }

function draw () {
    background(220);

    circle (circleX, circleY, 50)

    
}

function mousePressed () {
    circleX = mouseX;
    circleY = mouseY;
}