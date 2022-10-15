def setup():
    size(1920, 1080)

def draw():
    background(200,200,180)
    noCursor()
    if  mousePressed:
        fill(0)
    else:
        fill(255)
    rect (100,100,width/2,height/2)
    line(mouseX, mouseY, mouseX+80, mouseY+80)
    
def update():
    line(100,200,300,400)
