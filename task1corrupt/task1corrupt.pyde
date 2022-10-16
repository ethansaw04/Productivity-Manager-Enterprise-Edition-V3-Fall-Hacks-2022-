def task_1corrupt():
    word = loadImage("cheesepic.png")
    image(word, 490, 150)
    
    question = "Fill in the Blank" 
    fill(255, 255, 255) 
    textSize(25)
    textAlign(CENTER)
    text(question, width/2-150, height/2, 300, 150)
    
    letter1 = loadImage("cheese1.png")
    image(letter1, 370, 500)
    
    letter2 = loadImage("cheese2.png") 
    image(letter2, 575, 500)
    
    letter3 = loadImage("cheese3.png") 
    image(letter3, 830, 500)
