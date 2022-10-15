global startTime

def setup():
    global startTime
    size(200, 100) 
    fill(0) 
    textSize(50) 
    
    #            millis() / 1000 + NUMBER OF SECONDS 
    startTime = (millis()/1000) + 10 

def draw():
    global startTime
    background(255)
    
    seconds = startTime - millis()/1000
    
    if (seconds < 0):
        startTime = millis()/1000 + 10
    elif seconds == 0: 
        text("you're bad")
    else: 
        text(seconds, 80, 80)
    
