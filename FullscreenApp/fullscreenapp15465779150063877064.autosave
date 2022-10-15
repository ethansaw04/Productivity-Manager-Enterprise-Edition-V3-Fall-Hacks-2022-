focus_controller = 0
wantmenuloaded = 1
wanttasksloaded = 0

def loadmenu():
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
    
    fill(255,255,255)
    noStroke()
    rect(width/2-150, height/2+300, 300, 50)
    
    LogoText = "Click to get started!"
    fill(69,69,69)
    textSize(32)
    textAlign(CENTER)
    text(LogoText, width/2-150, height/2+300, 300, 50)
    
def loadTasks():
    TopLeft = "Productivity Manager Enterprise V3"
    fill(69,69,69)
    textSize(20)
    text(TopLeft, 0, 0, width/3, height/15)
    
    BottomRight = "Copyright 2003: Boolatov Industries LLC"
    fill(69,69,69)
    textSize(20)
    textAlign(RIGHT, BOTTOM)
    text(BottomRight, width/3*2, height/15*14, width/3, height/15)
    
    fill(255,255,255)
    noStroke()
    rect(width/2-150, height/2+100, 300, 50, 7)
    
    Task1 = "Task 1"
    fill(69,69,69)
    textSize(32)
    textAlign(CENTER)
    text(Task1, width/2-150, height/2+100, 300, 50)    
    
    fill(255,255,255)
    noStroke()
    rect(width/2-150, height/2, 300, 50, 7)
    
    Task2 = "Task 2"
    fill(69,69,69)
    textSize(32)
    textAlign(CENTER)
    text(Task2, width/2-150, height/2, 300, 50)
    
    fill(255,255,255)
    noStroke()
    rect(width/2-150, height/2-100, 300, 50, 7)
    
    Task3 = "Task 3"
    fill(69,69,69)
    textSize(32)
    textAlign(CENTER)
    text(Task3, width/2-150, height/2-100, 300, 50)
    
def task_1():
    print("task1")
    
def setup():
    fullScreen()
    #loadmenu()
    #loadTasks()
    
def draw():
    global focus_controller
    background(200,200,180)
    if (focus_controller == 0):#menu
        loadmenu()
        if mousePressed:
            if ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 + 350)) and (mouseY > (height/2))):
                focus_controller = 1
    elif (focus_controller == 1):#tasks selector
        loadTasks()
        if mousePressed:
            if ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 + 150)) and (mouseY > (height/2 + 100))):
                focus_controller = 2
            elif ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 + 50)) and (mouseY > (height/2))):
                focus_controller = 3
            elif ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 -50)) and (mouseY > (height/2 - 100))):
                focus_controller = 4
    elif (focus_controller == 2):#tasks:
        task_1()
    elif (focus_controller == 3):
        task_1()
    elif (focus_controller == 4):
        task_1()
    elif (focus_controller == 5):
        task_1()
    elif (focus_controller == 6):
        task_1()
    else:
        print("Error")
        
    
