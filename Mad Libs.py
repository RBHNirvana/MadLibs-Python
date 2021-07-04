from tkinter import * #Use pip install tk to install tkinter and this line imports all its functions for use.
root = Tk() #This is our GUI window
root.geometry("300x300") #Specification on the size of the window
root.title("Nirvana's-Mad Libs Generator") #Name given to the window
Label(root, text= "Mad Libs Generator \n Have Fun!" , font = "arial 20 bold").pack() #Text on the GUI with pack grouping the text together
Label(root, text = "Click Any One :", font = "arial 15 bold").place(x=40, y=80) #More text but with specification of placement of the text


def madlib1():

    animals= input("Enter an animal name : ")
    profession = input("Enter a profession name: ")
    cloth = input("Enter a piece of cloth name: ")
    things = input("Enter an object's name: ")
    name= input("Enter a name: ")
    place = input("Enter a place name: ")
    verb = input("Enter a verb in ing form: ")
    food = input("Enter a food name: ")
    print("Say " + food + ", the photographer said as the camera flashed! " + name + " and I had gone to " + place +" to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as " + animals + " pretending to be a " + profession + ". when we saw the second photo, it was exactly what I wanted. We both looked like " + things + " wearing " + cloth + " and " + verb + " --exactly what I had in mind")

def madlib2():
   
    adjactive = input("Enter adjective : ")
    color = input("Enter a color name : ")
    thing = input("Enter an object name :")
    place = input("Enter a place name : ")
    person= input("Enter a person name : ")
    adjactive1 = input("Enter an adjactive : ")
    insect= input("Enter a insect name : ")
    food = input("Enter a food name : ")
    verb = input("Enter a verb name : ")

    print("Last night I dreamed I was a " +adjactive+ " butterfly with " + color+ " splocthes that looked like "+thing+ " .I flew to " + place+ " with my bestfriend and "+person+ " who was a "+adjactive1+ " " +insect +" .We ate some " +food+ " when we got there and then decided to "+verb+ " and the dream ended when I said-- lets " +verb+ ".")


def madlib3():

    person = input("Enter person name: ")
    color = input("Enter color : ")
    foods = input("Enter food name : ")
    adjective = input("Enter an adjective name: ")
    thing = input("Enter a thing name : ")
    place = input("Enter place : ")
    verb = input("Enter verb : ")
    adverb = input("Enter adverb : ")
    food = input("Enter food name: ")
    things = input("Enter a thing name : ")
   
    print("Today we picked apple from " +person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ " apples straight off the tree that tested like "+foods+ ". Then there was a "+adjective+ " apple that looked like a " + thing + ".When our bag were full, we went on a free hay ride to "+place+ " and back. It ended at a hay pile where we got to " +verb+ " " +adverb+ ". I can hardly wait to get home and cook with the apples. We are going to make appple "+food+ " and "+things+" pies!.")  

Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120) #Creating interactive buttons with specific positions
Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()
