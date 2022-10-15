def setup():
    fullScreen()
    background(200,200,180)
    
    TopLeft = "Productivity Manager Enterprise V3"
    fill(69,69,69)
    textSize(20)
    text(TopLeft, 0, 0, width/3, height/15)
    
    BottomRight = "Copyright 2003: Boolatov Industries LLC"
    fill(69,69,69)
    textSize(20)
    textAlign(RIGHT, BOTTOM)
    text(BottomRight, width/3*2, height/15*14, width/3, height/15)
    
    Logo = loadImage("blogo.png")
    image(Logo, width/2-75, height/2-150, 150, 150)
    LogoText = "Boolatov Industries LLC"
    fill(255,255,255)
    textSize(32)
    textAlign(CENTER)
    text(LogoText, width/2-150, height/2, 300, 150)
