focus_controller = 0
wantmenuloaded = 1
wanttasksloaded = 0
timeractive = 0
starttime = (millis()/1000) + 60
timeleft = 0
task1completed = 0
task2completed = 0
task3completed = 0
cursed1completed = 0
cursed2completed = 0
cursed3completed = 0

can_type = False
typed_text = ""

def draw_text_box_reset():
    global can_type
    global typed_text
    can_type = False
    typed_text = ""

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
    global cursed1completed
    global cursed2completed
    global cursed3completed
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
    elif cursed1completed == 1 and timeractive == 1:
        Task1 = "C0MPL3T3D"
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
    elif cursed2completed == 1 and timeractive == 1:
        Task2 = "C0MPL3T3D"
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
    elif cursed3completed == 1 and timeractive == 1:
        Task3 = "C0MPL3T3D"
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
    
def cursed_1():
    global timeleft
    shakemodifier = 0
    
    if timeractive == 1:
        shakemodifier = 1.1 ** (60-timeleft)
        
    word = loadImage("cheesepic.png")
    image(word, width/2-75 + random(-shakemodifier, shakemodifier), height/2-200 + random(-shakemodifier, shakemodifier), 150, 150)
    
    question = "Fill in the Blank" 
    fill(255, 255, 255) 
    textSize(25)
    textAlign(CENTER)
    text(question, width/2-150 + random(-shakemodifier, shakemodifier), height/2 + random(-shakemodifier, shakemodifier), 300, 150)
    
    letter1 = loadImage("cheese3.png")
    image(letter1, width/2-175 + random(-shakemodifier, shakemodifier), height/2 + 150 + random(-shakemodifier, shakemodifier), 50, 80)
    
    letter2 = loadImage("cheese2.png") 
    image(letter2, width/2-25 + random(-shakemodifier, shakemodifier), height/2 + 150 + random(-shakemodifier, shakemodifier), 50, 30)
    
    letter3 = loadImage("cheese1.png") 
    image(letter3, width/2+125 + random(-shakemodifier, shakemodifier), height/2 + 150 + random(-shakemodifier, shakemodifier), 90, 50)

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
    
def cursed_2():
    global can_type
    global typed_text
    global keydown
    
    global timeleft
    shakemodifier = 0
    
    if timeractive == 1:
        shakemodifier = 1.1 ** (60-timeleft)
    
    line(mouseX, mouseY, mouseX+80, mouseY+80)
    if mousePressed:
        if (mouseX>width/2-300 and mouseY>height/2+150 and mouseX<(width/2)+300 and mouseY<(height/2)+230):
            fill(0,255,0)
        print(mouseX," ",mouseY)
    else:
        fill(255)
    rect(width/2-300 + random(-shakemodifier, shakemodifier),height/2+150 + random(-shakemodifier, shakemodifier),600,80,7)
    textSize(32)
    fill(0)
    text(typed_text, (width/2 - 300), (height/2)+50, 600, 50)
    
    question = "What is the square root of -5?" 
    fill(255, 255, 255) 
    textSize(25)
    textAlign(CENTER)
    text(question, width/2-150 + random(-shakemodifier, shakemodifier), height/2-150 + random(-shakemodifier, shakemodifier), 300, 150)
    
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
    
def cursed_3():
    global timeleft
    shakemodifier = 0
    
    if timeractive == 1:
        shakemodifier = 1.1 ** (60-timeleft)

    word = loadImage("cursedwalter.png")
    image(word, width/2-75 + random(-shakemodifier, shakemodifier), height/2-200 + random(-shakemodifier, shakemodifier), 150, 150)
    
    question = "Who is this?" 
    fill(255, 255, 255) 
    textSize(25)
    textAlign(CENTER)
    text(question, width/2-150 + random(-shakemodifier, shakemodifier), height/2 + random(-shakemodifier, shakemodifier), 300, 150)
    
    letter1 = loadImage("walgreens.png")
    image(letter1, width/2-175 + random(-shakemodifier, shakemodifier), height/2 + 150 + random(-shakemodifier, shakemodifier), 50, 80)
    
    letter2 = loadImage("waltuh.png") 
    image(letter2, width/2-25 + random(-shakemodifier, shakemodifier), height/2 + 150 + random(-shakemodifier, shakemodifier), 50, 30)
    
    letter3 = loadImage("walmarrt.png") 
    image(letter3, width/2+125 + random(-shakemodifier, shakemodifier), height/2 + 150 + random(-shakemodifier, shakemodifier), 90, 50)
    
def setup():
    fullScreen()
    #loadmenu()
    #loadTasks()
    
def draw():
    global timeractive
    global starttime
    global timeleft
    shakemodifier = 0
    
    if timeractive == 1:
        timeleft = max(0, starttime - millis()/1000)
        background(200,200-(120-timeleft*2),180-(120-timeleft*2))
        
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
            rect(random(0,width), random(0,height), random(4,60-timeleft+4), random(4,60-timeleft+4))
    else:
        background(200,200,180)
    
    global focus_controller
    global task1completed
    global task2completed
    global task3completed
    global cursed1completed
    global cursed2completed
    global cursed3completed
    global can_type
    
    if task1completed == 1 and task2completed == 1 and task3completed == 1 and timeractive == 0:
        starttime = (millis()/1000) + 60
        timeleft = starttime
        timeractive = 1
    
    if timeleft == 0 and timeractive == 1:
        background(0,0,0)
        word = loadImage("cursedwalter.png")
        image(word, random(-shakemodifier, shakemodifier), random(-shakemodifier, shakemodifier), width, height)
    elif (focus_controller == 0):#menu
        loadmenu()
        if mousePressed:
            if ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 + 350)) and (mouseY > (height/2))):
                focus_controller = 1
    elif (focus_controller == 1):#tasks selector
        loadTasks()
        if mousePressed:
            if ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 + 150)) and (mouseY > (height/2 + 100))):
                if task1completed == 0 and timeractive == 0:
                    focus_controller = 2
                elif cursed1completed == 0 and timeractive == 1:
                    focus_controller = 5
            elif ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 + 50)) and (mouseY > (height/2))):
                if task2completed == 0 and timeractive == 0:
                    focus_controller = 3
                elif cursed2completed == 0 and timeractive == 1:
                    focus_controller = 6
            elif ((mouseX > (width/2 - 150)) and (mouseX < (width/2 + 150)) and (mouseY < (height/2 -50)) and (mouseY > (height/2 - 100))):
                if task3completed == 0 and timeractive == 0:
                    focus_controller = 4
                elif cursed3completed == 0 and timeractive == 1:
                    focus_controller = 7
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
        cursed_1()
        if mousePressed:
            if ((mouseX > (width/2+125)) and (mouseX < (width/2+210)) and (mouseY < (height/2 + 200)) and (mouseY > (height/2 + 150))):
                focus_controller = 1
                cursed1completed = 1
    elif (focus_controller == 6):
        cursed_2()
    elif(focus_controller == 7):
        cursed_3()
        #image(letter2, width/2-25 + random(-shakemodifier, shakemodifier), height/2 + 150 + random(-shakemodifier, shakemodifier), 50, 30)
        if mousePressed:
            if ((mouseX > (width/2-25)) and (mouseX < (width/2+25)) and (mouseY < (height/2 + 180)) and (mouseY > (height/2 + 150))):
                    focus_controller = 1
                    cursed3completed = 1
    else:
        print("Error")
        
def mouseClicked():
    global can_type
    global focus_controller
    if (focus_controller == 3 or focus_controller == 6):
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
                if typed_text == "e^x = 9000" and timeractive == 0:
                    task2completed = 1
                    focus_controller = 1
                    draw_text_box_reset
                    typed_text = ""
                elif typed_text == "2.2360679775i" and timeractive == 1:
                    cursed2completed = 1
                    focus_controller = 1
                    draw_text_box_reset
                    typed_text = ""
            print(typed_text)
        
    
