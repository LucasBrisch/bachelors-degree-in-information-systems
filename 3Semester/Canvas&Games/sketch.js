let circles = [];

function setup () {
    createCanvas(600, 500);

    for (let j = 0; j < 200; j++) {
        let x = random(width);
        let y = random(height);
        circles.push({x: x, y: y}); 
    }
}

function draw () {
    background(0);

    fill (255)

    for (let i = 0; i < circles.length; i++) {
        let circlePos = circles[i];
        circle(circlePos.x, circlePos.y, 5);
    }


    fill(255)
    circle (300, 180, 200);

    fill(200)
    circle (250, 125, 30);
    circle (320, 167, 22);
    circle (350, 120, 27);
    circle (350, 220, 27);
    circle (230, 200, 27);
    
    fill (6,57,112)
    square(0, 240, 800);

    fill (0)
    triangle(250, 175, 200, 240, 300, 240);
    triangle(335, 190, 300, 240, 375, 240);
    triangle(300, 150, 250, 240, 350, 240);



    fill (40)
    triangle(250, 290, 200, 240, 300, 240);
    triangle(335, 280, 300, 240, 375, 240);
    triangle(300, 300, 250, 240, 350, 240);


    fill(139, 69, 19);
    vertex(330, 440);
    vertex(490, 440);
    vertex(470, 460);
    vertex(350, 460);
    endShape(CLOSE);

    fill(255);
    triangle(410, 440, 410, 380, 430, 440);

    
    
    
        
}