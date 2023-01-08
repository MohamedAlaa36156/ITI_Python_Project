from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image,ImageTk

# def reset():
	
	# global small.counter
	# global medium.counter
	# global large.counter


# def order():
   
    # Toplevel object which will
    # be treated as a new window
	# order = Toplevel(root)
    # sets the title of the
    # Toplevel widget
	# order.title("Order Taking Window")
	# sets the geometry of toplevel
	# order.geometry("600x470")
	# A Label widget to show in toplevel
	# Show image using label
	# label1 = Label( order, image = bg)
	# label1.place(x = 0,y = 0)
	# order.iconbitmap("icon1.ico")	
	# small1 =Label(order, fg="dark green")
	# small1.place(x = 100,y =400)

	
	
	# photo_1 = PhotoImage(file="small.png")
	# photo_1=photo_1.subsample(10,10)
	# photo_2=PhotoImage(file="medium.png")
	# photo_2=photo_2.subsample(15,15)
	# photo_3=PhotoImage(file="large.png")
	# photo_3=photo_3.subsample(15,15)
	# b1=Button(order , text="Small",background="green",fg="yellow",command= small)
	# b1.place(x = 100,y =300)
	# b2=Button(order , text="Medium",background="green",fg="yellow",command = medium)
	# b2.place(x = 300,y = 300)
	# b3=Button(order , text="Large",background="green",fg="yellow",command = large)
	# b3.place(x = 480,y = 300)
	# b1=Button(order , text="Small",background="green",fg="yellow",image=photo_1)
	# b1.pack(side=LEFT)
	# b2=Button(order , text="Medium",background="green",fg="yellow",image=photo_2)
	# b2.pack(side=LEFT)
	# b3=Button(order , text="Large",background="green",fg="yellow",image=photo_3)
	# b3.pack(side=LEFT)
def root(): 
	window.destroy()
	
	def total():
		global total
		total1=Label(root, fg="dark green")
		total1.place(x=300,y=200)
		total=(10*small.counter)+(20*medium.counter)+(25*large.counter)
		total1.config(text=str(total))
		
	
	def small():
		global x1
		small1 =Label(root, fg="dark green")
		small1.place(x = 100,y =400)
		small.counter +=1
		x1=5*(small.counter)
		small1.config(text=str(x1))
		
		
		
	
	def medium():
	
		global x2
		medium1 =Label(root, fg="dark green")
		medium1.place(x = 300,y =400)
		medium.counter +=1
		x2=10*medium.counter
		medium1.config(text=str(x2))
	
		
	def large():
		global x3
		large1 =Label(root, fg="dark green")
		large1.place(x = 480,y =400)
		large.counter +=1
		x3=20*large.counter
		large1.config(text=str(x3))
	
	def reset():
		small.counter=0
		medium.counter=0
		large.counter=0
		x1=0
		x2=0
		x3=0
		total1=0
		small1 =Label(root, fg="dark green",background="olivedrab4")
		small1.place(x = 100,y =400)
		small1.config(text=str("	"))
		large1 =Label(root, fg="dark green",background="olivedrab4")
		large1.place(x = 480,y =400)
		large1.config(text=str("	"))
		total1=Label(root, fg="dark green",background="yellow3")
		total1.place(x=300,y=200)
		total1.config(text=str("	"))
		medium1 =Label(root, fg="dark green",background="yellow3")
		medium1.place(x = 300,y =400)
		medium1.config(text=str("	"))
		
	
	
	small.counter=0
	medium.counter=0
	large.counter=0		
		
	root = Tk()
	
	# Adjust size 
	root.geometry("600x470")
	root.title("Main Menu")
	
	# Add image file
	bg2= PhotoImage( file = "medium.png")
	root.iconbitmap("icon.ico")
	
	# Show image using label
	label1=Label(root,image=bg2)
	label1.place(x = 0,y = 0)
	
	# Add text
	label2 = Label( root, text = "Alaa 2asab Shop", bg = "yellow",font =('ravie', 14))
	label2.place(x=200,y=50)
	# label2.pack(pady = 100)
	
	# Create Frame
	frame1 = Frame( root, bg = "#B3E820")
	frame1.pack(pady = 0)
	
	
	b1=Button(root , text="Small",background="green",fg="yellow",command= small)
	b1.place(x = 100,y =300)
	b2=Button(root , text="Medium",background="green",fg="yellow",command = medium)
	b2.place(x = 300,y = 300)
	b3=Button(root , text="Large",background="green",fg="yellow",command = large)
	b3.place(x = 480,y = 300)
	
	
	b4=Button(root , text="Reset",background="green",fg="yellow",command= reset)
	b4.place(x = 250,y =430)
	b5=Button(root , text="Total",background="green",fg="yellow",command= total)
	b5.place(x = 350,y =430)
	# Add buttons
	# button2 = Button( frame1, text = "Start",font=('calibre',10,'normal'), command = order )
	# button2.pack(pady = 20)
	# button1 = Button( frame1, text = "Exit",font=('calibre',10,'normal'),command=root.destroy)
	# button1.pack(pady = 20)
	x1=0
	x2=0
	x3=0
	total1=0
	# Execute tkinter
	root.mainloop()	
window = Tk()
window.geometry('600x470')
bg = PhotoImage( file = "medium.png")
window.iconbitmap("icon.ico")
label = Label(window , image = bg)
window.title('Alaa 2asab Shop')
label.place(x = 0, y = 0)
label_1 = Label(window , text = "Welcome To Alaa's Shop", fg = 'green',bg = 'yellow', font =('ravie', 24))
label_1.pack(side = TOP)
B1=Button(window , text = "Taking Orders" ,background="yellow", font =('ravie', 14) , fg="green" , bd = '0',command= root ,width='12',height='1')
B1.place(x = 220,y =400)
# photo = PhotoImage(file = "sugar-cane_cup.png")
# res = photo.subsample(2,2)
# bt = Button(window ,text = 'SMALL', image = res,bg = 'white', compound= TOP)
# bt.pack()
window.mainloop()