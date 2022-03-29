from tkinter import *
root =Tk()
root.geometry('400x800')
root.title("Mad Libs Generator")
root.configure(bg="black")
Label(root, text='Mad Libs Generator \n  Have fun! ', font='arial 20 bold').pack()
Label(root, text = 'Click Any One : ', font='arial 20 bold').place(x=40, y=80)

def madlib1():

    animals= input('enter a animal name : ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name= input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')


def madlib2():
   
    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')

    print('Last night I dreamed I was a ' +adjactive+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')


def madlib3():

    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')
   
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')  

def madlib4():
    person=input('Enter a person name: ')
    cloth_article=input('An article of clothing: ')
    creature=input('A creature: ')
    adjective=input('enter a adjective name: ')
    place=input('enter a village name: ')
    exclamation=input('enter a exclamation: ')
    things=input('favorite thing for yours: ')

    print('On one dark, stormy night,' +person + ' came along. He was wearing nothing but a' +cloth_article+'. He went into the woods and there he found a '+creature+'! It was '+adjective+'. In fright he ran into a nearby village called ' + place + ' screaming, ' +exclamation +'! The footsteps of the '+creature+ 'behind him became louder and louder. The villagers screamed, Its a' +adjective+ '! Taking no prisoners the '+creature+ ' demolished the entire village leaving only the trace of someones' +things+'.  Then it went back into the woods and waited for its next victim to emerge.')

def madlib5():
    animal=input('enter a animal name: ')
    parent=input('choose a parent: ')
    month=input('Choose a month: ')
    path=input('Choose a Path: ')
    movement=input('Choose a movement type: ')
    number=input('Enter a number: ')

    print('There was once a '+animal+'. He was always getting told off. One day while his '+parent+' was sitting in the garden in' +month+', he sneaked out. He did not mean to go far but he saw a glittery thing on the '+path+' and '+movement+' over to it. He found out it was gold and became rich because he had' +number+' pieces of gold.')

def madlib6():
    boy=input("enter a boy's name: ")
    anboy=input("Another boy: ")
    girl=input("enter girl name: ")
    angirl=input("enter another girl name: ")
    animal=input("enter a animal name: ")
    excla=input("Enter a exclamation: ")
    print('Once upon a time, two people,' +girl+' and '+boy+' were walking in the park. They were talking about his '+animal+'. Then' +boy+ 'exclaimed, '+excla+'! What is it, '+boy+'? cried '+girl+'. I just remembered something, I have this ring in my pocket. said' +boy+'. Why would you have that? asked '+girl+'. Will you marry me?' +boy+' asked. '+girl+' replied, "Ummmmmmm... Yes, I Love You, '+boy+'! So they left on '+boy+'s '+animal+' to their kingdom and had 2 children named '+angirl+' and '+anboy+' and they lived happily ever after as every story should end!')

Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'aliceblue').place(x=60, y=120)
Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=60, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=60, y=240)
Button(root, text= 'One Dark, Stromy night', font ='arial 15', command = madlib4, bg = 'ghost white').place(x=60, y=300)
Button(root, text= 'The Gold!', font ='arial 15', command = madlib5, bg = 'ghost white').place(x=60, y=360)
Button(root, text= 'The Ring', font ='arial 15', command = madlib6, bg = 'ghost white').place(x=60, y=420)



root.mainloop()    
    
