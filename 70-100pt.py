#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="green")
direction = 5
# Create your "enemies" here, before the class
circle = drawpad.create_oval(350, 250, 550, 450, fill='red')
oval = drawpad.create_oval(100, 300, 350, 350, fill='purple')
square = drawpad.create_rectangle(100, 10, 50, 50, fill='yellow')

#Animation Functions
def animateCircle():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle)
    if x2 > 850: 
        direction = - 1000
    elif x1 < 0:
        direction = 3
    #Move our oval object by the value of direction
    drawpad.move(circle,direction,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(10, animateCircle)
    
animateCircle()

def animateOval():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(oval)
    if x2 > 850: 
        direction = - 1000
    elif x1 < 0:
        direction = 7
    #Move our oval object by the value of direction
    drawpad.move(oval,direction,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(10, animateOval)
    
animateOval()
    
def animateSquare():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(square)
    if x2 > 850: 
        direction = - 1000
    elif x1 < 0:
        direction = 4
    #Move our oval object by the value of direction
    drawpad.move(square,direction,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(10, animateSquare)
    
animateSquare()

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    
       	    #up button
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    #down button
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "pink")
       	    self.down.grid(row=3,column=1)
       	    # Bind an event to the first button
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    #left button
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "blue")
       	    self.left.grid(row=2,column=0)
       	    # Bind an event to the first button
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    #right button
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "red")
       	    self.right.grid(row=2,column=3)
       	    # Bind an event to the first button
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    #drawpad.after(10,self.animate)
		
	#Up	
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	#down  
        def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	   
	#left   
        def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	   
	#right   
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
		

app = MyApp(root)
root.mainloop()