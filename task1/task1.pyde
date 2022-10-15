def task_1():
    word = loadImage("cheese screenshot.png")
    image(word, 490, 200)
    
    question = "Fill in the Blank" 
    fill(255, 255, 255) 
    textSize(25)
    textAlign(CENTER)
    text(question, width/2-150, height/2, 300, 150)
    
    letter1 = loadImage("a.png")
    image(letter1, 400, 500)
    
    letter2 = loadImage("r.png") 
    image(letter2, 620, 500)
    
    letter3 = loadImage("a.png") 
    image(letter3, 830, 500)
    
# REMOVE 
def setup():
    fullScreen()
    background(200,200,180)
    task_1()
    
