def setup():
    size(1920, 1080)

can_type = False
typed_text = ""

def draw_text_box_reset():
    global can_type
    global typed_text
    can_type = False
    typed_text = ""

def draw_text_box():
    global can_type
    global typed_text
    global keydown
    line(mouseX, mouseY, mouseX+80, mouseY+80)
    if mousePressed:
        if (mouseX>width/3 and mouseY>height/2 and mouseX<(width/3)+600 and mouseY<(height/2)+80):
            fill(0,255,0)
        print(mouseX," ",mouseY)
    else:
        fill(255)
    rect(width/3,height/2,600,80,7)
    textSize(32)
    fill(0)
    text(typed_text, (width/3), (height/2)+40)

def draw():
    background(255)
    draw_text_box()
            
    
def mouseClicked():
    global can_type
    if (mouseX>width/3 and mouseY>height/2 and mouseX<(width/3)+600 and mouseY<(height/2)+80):
        can_type = not can_type
        print("clicked ",can_type)
def keyTyped():
    global can_type
    global typed_text
    if (can_type==True):
        if (key==BACKSPACE):
            typed_text = typed_text[:-1]
        elif (key==ENTER):
            typed_text = typed_text
        else:
            if len(typed_text)<24:
                typed_text = typed_text + key
            print(typed_text)
