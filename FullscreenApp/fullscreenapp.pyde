focus_controller = 0
wantmenuloaded = 1
wanttasksloaded = 0
timeractive = 0
starttime = (millis()/1000) + 60
timeleft = 0
task1completed = 0

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
    global timeractive
    global timeleft
    global task1completed
    shakemodifier = 0
    
    if timeractive == 1:
        shakemodifier = 1.1 ** (60-timeleft)
        fill(69,69,69)
        noStroke()
        rect(width/2-50, height/2-300, 100, 50, 7)
        
        fill(169,89,89)
        textSize(32)
        textAlign(CENTER)
        text(str(timeleft), width/2-150, height/2-300, 300, 50)
        
        for i in range(int(1.15**(60-timeleft))):
            fill(random(0,255),random(0,100),random(0,100))
            noStroke()
            rect(random(0,width), random(0,height), random(4,10), random(4,10))
    
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
    rect(width/2-150 + random(-shakemodifier, shakemodifier), height/2+100 + random(-shakemodifier, shakemodifier), 300, 50, 7)
    
    Task1 = "Task 1"
    if task1completed == 1 and timeractive == 0:
        Task1 = "COMPLETED"
    fill(69,69,69)
    textSize(32)
    textAlign(CENTER)
    text(Task1, width/2-150 + random(-shakemodifier, shakemodifier), height/2+100 + random(-shakemodifier, shakemodifier), 300, 50)    
    
    fill(255,255,255)
    noStroke()
    rect(width/2-150 + random(-shakemodifier, shakemodifier), height/2 + random(-shakemodifier, shakemodifier), 300, 50, 7)
    
    Task2 = "Task 2"
    fill(69,69,69)
    textSize(32)
    textAlign(CENTER)
    text(Task2, width/2-150 + random(-shakemodifier, shakemodifier), height/2 + random(-shakemodifier, shakemodifier), 300, 50)
    
    fill(255,255,255)
    noStroke()
    rect(width/2-150 + random(-shakemodifier, shakemodifier), height/2-100 + random(-shakemodifier, shakemodifier), 300, 50, 7)
    
    Task3 = "Task 3"
    fill(69,69,69)
    textSize(32)
    textAlign(CENTER)
    text(Task3, width/2-150 + random(-shakemodifier, shakemodifier), height/2-100 + random(-shakemodifier, shakemodifier), 300, 50)
    
def task_1():
    word = loadImage("cheese screenshot.png")
    image(word, width/2-75, height/2-200, 150, 150)
    
    question = "Fill in the Blank" 
    fill(255, 255, 255) 
    textSize(25)
    textAlign(CENTER)
    text(question, width/2-150, height/2, 300, 150)
    
    letter1 = loadImage("letterE.png")
    image(letter1, width/2-175, height/2 + 150, 50, 50)
    
    letter2 = loadImage("r.png") 
    image(letter2, width/2-25, height/2 + 150, 50, 50)
    
    letter3 = loadImage("a.png") 
    image(letter3, width/2+125, height/2 + 150, 50, 50)
    
def setup():
    fullScreen()
    #loadmenu()
    #loadTasks()
    
def draw():
    global timeractive
    global starttime
    global timeleft
    if timeractive == 1:
        timeleft = max(0, starttime - millis()/1000)
        background(200,200-(120-timeleft*2),180-(120-timeleft*2))
    else:
        background(200,200,180)
    
    global focus_controller
    global task1completed
    if (focus_controller == 0):#menu
        loadmenu()
        if mousePressed:
            if ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 + 350)) and (mouseY > (height/2))):
                focus_controller = 1
    elif (focus_controller == 1):#tasks selector
        loadTasks()
        if mousePressed:
            if ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 + 150)) and (mouseY > (height/2 + 100))):
                if task1completed == 0:
                    focus_controller = 2
            elif ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 + 50)) and (mouseY > (height/2))):
                focus_controller = 3
            elif ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 -50)) and (mouseY > (height/2 - 100))):
                focus_controller = 4
    elif (focus_controller == 2):#tasks:
        task_1()
        if mousePressed:
            if ((mouseX > (width/2-175)) and (mouseX < (width/2-125)) and (mouseY < (height/2 + 200)) and (mouseY > (height/2 + 150))):
                focus_controller = 1
                task1completed = 1
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
        
    
