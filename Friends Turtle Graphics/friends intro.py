# All Commands To Download The Turtle package In The Description
# No Need to download winsound and time as it is inbuilt
# directly import winsound and time also the source code is in the description with the images and the sound file
import turtle
import winsound
import time

win = turtle.Screen()
win.setup(width=840,height=500)
win.bgcolor('black')

win.addshape('images/ross.gif')
win.addshape('images/joey.gif')
win.addshape('images/chandler.gif')
win.addshape('images/monica.gif')
win.addshape('images/rachel.gif')
win.addshape('images/phoebe.gif')
win.addshape('images/friends1.gif')
win.addshape('images/friends2.gif')
win.addshape('images/coffee.gif')
win.addshape('images/sofa.gif')
win.addshape('images/song.gif')
win.addshape('images/end.gif')

winsound.PlaySound('friends.wav',winsound.SND_ASYNC)

text = turtle.Turtle()
text.color('white')
text.speed(0)
text.penup()
text.hideturtle()
style = ('Courier',20,'italic')

def create(pic,pos):
    x,y = pos

    t = turtle.Turtle()
    t.penup()
    t.shape(pic)
    t.goto(x,y)

    return t

def sleep(t):
    time.sleep(t)

def show(t):
    t.showturtle()
    sleep(1)
    t.hideturtle()

def write(message,pos):
    text.showturtle()
    x,y = pos
    text.goto(x,y)
    text.write(message,font=style,move=True)
    text.hideturtle()

coffee = create('images/coffee.gif',(0,0))
sleep(3)
coffee.hideturtle()

friends1 = create('images/friends1.gif',(0,0))
sleep(3)
friends1.hideturtle()

joey = create('images/joey.gif',(-350,0))
write("How You Doing  !",(-60,0))
sleep(2)
text.clear()
joey.hideturtle()
show(friends1)

chandler = create('images/chandler.gif',(-210,0))
write("Oh! I don't care",(-60,0))
sleep(2)
text.clear()
chandler.hideturtle()
show(friends1)

ross = create('images/ross.gif',(-70,0))
write("We were on a break",(40,0))
sleep(2)
text.clear()
ross.hideturtle()
show(friends1)

monica = create('images/monica.gif',(70,0))
write("I Know",(-210,0))
sleep(2)
text.clear()
monica.hideturtle()
show(friends1)

rachel = create('images/rachel.gif',(210,0))
write("No Friends, no opinion",(-280,0))
sleep(2)
text.clear()
rachel.hideturtle()
show(friends1)

phoebe = create('images/phoebe.gif',(350,0))
write("oh, I wish i could",(-230,0))
write("but I don't want to",(-230,-40))
sleep(2)
text.clear()
phoebe.hideturtle()
show(friends1)

friends1.showturtle()
sleep(2)
friends1.hideturtle()

friends2 = create('images/friends2.gif',(0,0))

sleep(3)

friends2.hideturtle()

sofa = create('images/sofa.gif',(0,0))
sleep(5)
sofa.hideturtle()

song = create('images/song.gif',(0,0))
sleep(13)
song.hideturtle()

end = create('images/end.gif',(0,0))

turtle.done()