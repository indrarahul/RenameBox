import tkinter as tk
import os
from PIL import ImageTk, Image
dire = input()
a = os.listdir(dire + '/.')
os.system('mkdir ' + dire + '_new')
class tkwindow:
	is_over = False

	def __init__(self,file):
		self.filename = file
		self.root = tk.Tk()
		self.root.title("Editing Box")
		self.root.geometry("300x250")
		name = tk.Label(self.root, text='Current Name: '+ self.filename)
		img = ImageTk.PhotoImage(Image.open(os.path.join(dire + "/" + self.filename)).resize((150, 50), Image.ANTIALIAS))
		editbut = tk.Button(self.root, text='Edit',command= self.naam)
		nextb = tk.Button(self.root, text='Next',command= self.nextbb)
		exitb = tk.Button(self.root, text = 'Exit', command= self.on_exit)
		self.rename = tk.Entry(self.root)
		panel = tk.Label(self.root, image=img)
		name.grid(column=0, row=0, columnspan=6)
		panel.grid(column=0, row=1)
		editbut.grid(column=0, row=6)
		nextb.grid(column=1, row=6)
		self.rename.grid(column=0,row=2)
		exitb.grid(column=2, row=6)
		self.root.mainloop()

	def on_exit(self):
		self.is_over = True
		self.root.destroy()

	def naam(self):
		# try:
		os.system('mv ' + dire + "/" + self.filename + " " + dire + "_new/" + self.rename.get() + "." + self.filename.split('.')[-1])
		print("Done")
		self.nextbb()
		# except(e):
		# 	print(e)

	def nextbb(self):
		self.root.destroy()


for i in a:
	window = tkwindow(i)
	if window.is_over:
		exit()
