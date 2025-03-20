function setup() {
    createCanvas(windowWidth, windowHeight);
  }
  
  let angle = 0;

function setup() {
  createCanvas(windowWidth, windowHeight);
}

function draw() {
  background(220);
  
  
  circle(mouseX, mouseY, 50);
  
  
  let orbitRadius = 100;
  let orbitX = mouseX + orbitRadius * cos(angle);
  let orbitY = mouseY + orbitRadius * sin(angle);
  
 
  circle(orbitX, orbitY, 30);
  
  angle += 0.05;
}