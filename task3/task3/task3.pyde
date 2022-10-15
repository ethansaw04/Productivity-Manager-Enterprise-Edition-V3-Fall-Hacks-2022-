def task3():
    walter = loadImage("wlt.png")
    image(walter, width/2, height/2, 490, 200)

    question = "Who is this?" 
    fill(255, 255, 255) 
    textSize(25)
    textAlign(CENTER)
    text(question, width/2-150, height/2, 300, 150)
    
    
    letter1 = loadImage("walter1.png")
    image(letter1, 400, 500)
    
    letter2 = loadImage("walter2.png") 
    image(letter2, 620, 500)
    
    letter3 = loadImage("walter3.png") 
    image(letter3, 830, 500)
    
    
def setup():
    fullScreen()
    background(200,200,180)
    task3()
