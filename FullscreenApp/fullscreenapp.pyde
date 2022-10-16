focus_controller = 0
wantmenuloaded = 1
wanttasksloaded = 0
timeractive = 0
starttime = (millis()/1000) + 60
timeleft = 0
task1completed = 0
task2completed = 0
task3completed = 0

can_type = False
typed_text = ""

def draw_text_box_reset():
    global can_type
    global typed_text
    can_type = False
    typed_text = ""
    
def task_2():
    global can_type
    global typed_text
    global keydown
    line(mouseX, mouseY, mouseX+80, mouseY+80)
    if mousePressed:
        if (mouseX>width/2-300 and mouseY>height/2+150 and mouseX<(width/2)+300 and mouseY<(height/2)+230):
            fill(0,255,0)
        print(mouseX," ",mouseY)
    else:
        fill(255)
    rect(width/2-300,height/2+150,600,80,7)
    textSize(32)
    fill(0)
    text(typed_text, (width/2 - 300), (height/2)+50, 600, 50)
    
    question = "Write ln 9000 = x in exponential form." 
    fill(255, 255, 255) 
    textSize(25)
    textAlign(CENTER)
    text(question, width/2-150, height/2-150, 300, 150)

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
    global task2completed
    global task3completed
    shakemodifier = 0
    
    if timeractive == 1:
        shakemodifier = 1.1 ** (60-timeleft)
    
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
    if task2completed == 1 and timeractive == 0:
        Task2 = "COMPLETED"
    fill(69,69,69)
    textSize(32)
    textAlign(CENTER)
    text(Task2, width/2-150 + random(-shakemodifier, shakemodifier), height/2 + random(-shakemodifier, shakemodifier), 300, 50)
    
    fill(255,255,255)
    noStroke()
    rect(width/2-150 + random(-shakemodifier, shakemodifier), height/2-100 + random(-shakemodifier, shakemodifier), 300, 50, 7)
    
    Task3 = "Task 3"
    if task3completed == 1 and timeractive == 0:
        Task3 = "COMPLETED"
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
    image(letter1, width/2-175, height/2 + 150, 50, 80)
    
    letter2 = loadImage("r.png") 
    image(letter2, width/2-25, height/2 + 150, 50, 30)
    
    letter3 = loadImage("a.png") 
    image(letter3, width/2+125, height/2 + 150, 90, 50)
    
def task_3():
    word = loadImage("wlt.png")
    image(word, width/2-75, height/2-200, 150, 150)
    
    question = "Who is this?" 
    fill(255, 255, 255) 
    textSize(25)
    textAlign(CENTER)
    text(question, width/2-150, height/2, 300, 150)
    
    letter1 = loadImage("walter1.png")
    image(letter1, width/2-175, height/2 + 150, 50, 80)
    
    letter2 = loadImage("walter2.png") 
    image(letter2, width/2-25, height/2 + 150, 50, 30)
    
    letter3 = loadImage("walter3.png") 
    image(letter3, width/2+125, height/2 + 150, 90, 50)
    
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
    else:
        background(200,200,180)
    
    global focus_controller
    global task1completed
    global task2completed
    global task3completed
    global can_type
    
    if task1completed == 1 and task2completed == 1 and task3completed == 1 and timeractive == 0:
        starttime = (millis()/1000) + 60
        timeractive = 1
        
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
                if task2completed == 0:
                    focus_controller = 3
            elif ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 -50)) and (mouseY > (height/2 - 100))):
                if task3completed == 0:
                    focus_controller = 4
    elif (focus_controller == 2):#tasks:
        task_1()
        if mousePressed:
            if ((mouseX > (width/2-175)) and (mouseX < (width/2-125)) and (mouseY < (height/2 + 230)) and (mouseY > (height/2 + 150))):
                focus_controller = 1
                task1completed = 1
    elif (focus_controller == 3):
        task_2()
    elif (focus_controller == 4):
        task_3()
        if mousePressed:
            if ((mouseX > (width/2-175)) and (mouseX < (width/2-125)) and (mouseY < (height/2 + 230)) and (mouseY > (height/2 + 150))):
                focus_controller = 1
                task3completed = 1
    elif (focus_controller == 5):
        task_1()
    elif (focus_controller == 6):
        task_1()
    else:
        print("Error")
        
def mouseClicked():
    global can_type
    global focus_controller
    if (focus_controller == 3):
        if (mouseX>width/2-300 and mouseY>height/2+150 and mouseX<(width/2)+300 and mouseY<(height/2)+230):
            can_type = not can_type
            print("clicked ",can_type)
        
def keyTyped():
    global can_type
    global typed_text
    global task2completed
    global focus_controller
    if (can_type==True):
        if (key==BACKSPACE):
            typed_text = typed_text[:-1]
        elif (key==ENTER):
            typed_text = typed_text
        else:
            if len(typed_text)<24:
                typed_text = typed_text + key
                if typed_text == "e^x = 9000":
                    task2completed = 1
                    focus_controller = 1
                    draw_text_box_reset
            print(typed_text)
        
    
