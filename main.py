#importer les librerie 

from random import randrange
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
from PIL import Image
import matplotlib.pyplot as plt
# import os

#create l'interface
root = Tk()

#le titre au haut application
root.title("Mini Photoshop")
haut = Frame(root, borderwidth=2, relief=GROOVE)
haut.grid(column=0,row=0)
Label(haut, text="Mini Photoshop Avec Python",font=("ariel 10 bold"),fg='blue').grid(column=0,row=0)

#le cadre de image  Cette méthode modifie l'image pour qu'elle contienne 
# une version miniature d'elle-même, pas plus grande que la taille donnée
cadr = (330, 330)
#le longeur et largeur des image
imagewidth = 190
imageheight = 190



##method pour selectioner l'image
def selected():
    global img_path, img
    # img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    #importer l image dans une fichier
    img_path = filedialog.askopenfilename()
    #ovrier l'image
    img = Image.open(img_path)
    img.thumbnail(cadr)
    # Convert the image to a PhotoImage object
    img1 = ImageTk.PhotoImage(img)
    canvas1.create_image(imagewidth,imageheight, image=img1)
    canvas1.image = img1
    canvas2.create_image(imagewidth,imageheight, image=img1)
    canvas2.image = img1

#inisialiser les image par le premier image uplaoder
def clear():
    global  img
    img.thumbnail(cadr)
    img1 = ImageTk.PhotoImage(img)
    canvas1.create_image(imagewidth,imageheight, image=img1)
    canvas1.image = img1
    canvas2.create_image(imagewidth,imageheight, image=img1)
    canvas2.image = img1 

#images avant utiliser
img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None

def blur():
    win1 = Toplevel(root)
    win1.title("BLUR")
    v1 = IntVar()
    blurr = Label(win1, text="Blur:", font=("ariel 17 bold"), width=4, anchor='e').grid(row=0,column=0)
    def blur1(event):
        global img_path, img1, imgg
        for m in range(0, v1.get()+1):
            img = Image.open(img_path)
            img.thumbnail(cadr)
            #Blur
            imgg = img.filter(ImageFilter.BoxBlur(m))
            img1 = ImageTk.PhotoImage(imgg)
            canvas2.create_image(imagewidth,imageheight, image=img1)
            canvas2.image = img1
    scale1 = ttk.Scale(win1, from_=0, to=10, variable=v1,orient=HORIZONTAL, command=blur1).grid(row=0,column=1)
def brightness():
    win1 = Toplevel(root)
    win1.title("Brightness")
    v2 = IntVar()
    bright = Label(win1, text="Brightness:", font=("ariel 10 bold")).grid(row=0,column=0)
    def brightness1(event):
        global img_path, img2, img3
        for m in range(0, v2.get()+1):
            img = Image.open(img_path)
            img.thumbnail(cadr)
            #brightness
            imgg = ImageEnhance.Brightness(img)
            img2 = imgg.enhance(m)
            img3 = ImageTk.PhotoImage(img2)
            canvas2.create_image(imagewidth,imageheight, image=img3)
            canvas2.image = img3
    scale2 = ttk.Scale(win1, from_=0, to=10, variable=v2,orient=HORIZONTAL, command=brightness1).grid(row=0,column=1)

def contrast():
    win1 = Toplevel(root)
    win1.title("contaste")
    v3 = IntVar()
    bright = Label(win1, text="contrast:", font=("ariel 10 bold")).grid(row=0,column=0)
    def contrast1(event):
        global img_path, img4, img5
        for m in range(0, v3.get()+1):
            img = Image.open(img_path)
            img.thumbnail(cadr)
            #contrast image
            imgg = ImageEnhance.Contrast(img)
            #valeur de contrast
            img4 = imgg.enhance(m)
            img5 = ImageTk.PhotoImage(img4)
            canvas2.create_image(imagewidth,imageheight, image=img5)
        canvas2.image = img5
    scale2 = ttk.Scale(win1, from_=0, to=10, variable=v3,orient=HORIZONTAL, command=contrast1).grid(row=0,column=1)    
def rotate_image():
    win1 = Toplevel(root)
    win1.title("rotate")
    def rotate_image1():
        global img_path, img6, img7
        img = Image.open(img_path)
        img.thumbnail(cadr)
        #rotate image 
        img6 = img.rotate(int(var.get()))
        img7 = ImageTk.PhotoImage(img6)
        canvas2.create_image(imagewidth,imageheight, image=img7)
        canvas2.image = img7

    var = IntVar()
    R1 = Radiobutton(win1, text="O", variable=var, value=0, command=rotate_image1).pack( anchor = W )
    R2 = Radiobutton(win1, text="90", variable=var, value=90,command=rotate_image1).pack( anchor = W )
    R5 = Radiobutton(win1, text="180", variable=var, value=180,command=rotate_image1).pack( anchor = W)
    R3 = Radiobutton(win1, text="270", variable=var, value=270,command=rotate_image1).pack( anchor = W)    
    R4 = Radiobutton(win1, text="360", variable=var, value=360,command=rotate_image1).pack( anchor = W)

def flip():
    win1 = Toplevel(root)
    win1.title("flip")
    def flip_image():
        global img_path, img8, img9
        img = Image.open(img_path)
        img.thumbnail(cadr)
        v =randrange(1,3)
        if v ==1:
            #filp LEFT_RIGHT
            img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif v ==2:
            #filp TOP_BOTTOM
            img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
        img9 = ImageTk.PhotoImage(img8)
        canvas2.create_image(imagewidth,imageheight, image=img9)
        canvas2.image = img9
    flip = Label(win1, text="Flip:").grid(row=0,column=0)
    b1 = Button(win1,text='FLIP',command=flip_image).grid(row=1,column=0)



def border_image():
    win1 = Toplevel(root)
    win1.title("Border")
    border = Label(win1, text="Border", font=("ariel 17 bold")).grid(row=0,column=0)
    def image_border():
        global img_path, img10, img11
        v =randrange(10, 45, 5)
        img = Image.open(img_path)
        img.thumbnail(cadr)
        #border 
        img10 = ImageOps.expand(img, border=int(v))
        img11 = ImageTk.PhotoImage(img10)
        canvas2.create_image(imagewidth,imageheight, image=img11)
        canvas2.image = img11
    R1 = Button(win1, text="Border", command=image_border).grid(row=0,column=0)



# les fonction des filtres
def filres():
    win1 = Toplevel(root)
    win1.title("Filres")

    def negative():    
        global img_path, img10, img11
        img = Image.open(img_path)
        img.thumbnail(cadr)
        #la medthod qui invert l image
        img = ImageOps.invert(img)
        img11 = ImageTk.PhotoImage(img)
        canvas2.create_image(imagewidth,imageheight, image=img11)
        canvas2.image = img11
    R1 = Button(win1, text="Negative", command=negative).grid(row=0,column=0)
    def blackandwhite():    
        global img_path
        img = Image.open(img_path)
        img.thumbnail(cadr)
        #la fomction qui fait l'image Noire et Blanc
        img= img.convert('1')
        img11 = ImageTk.PhotoImage(img)
        canvas2.create_image(imagewidth,imageheight, image=img11)
        canvas2.image = img11
    R1 = Button(win1, text="blackandwhite", command=blackandwhite).grid(row=1,column=0)
    def GaussianBlur():    
        global img_path
        img = Image.open(img_path)
        img.thumbnail(cadr)
        #le filte Gaussien
        img= img.filter(ImageFilter.GaussianBlur(radius = 5))
        img11 = ImageTk.PhotoImage(img)
        canvas2.create_image(imagewidth,imageheight, image=img11)
        canvas2.image = img11
    R1 = Button(win1, text="Filtre Gaussian", command=GaussianBlur).grid(row=2,column=0)

    def median_blur():    
        global img_path
        img = Image.open(img_path)
        img.thumbnail(cadr)
        #le filtre Median
        img = img.filter(ImageFilter.MedianFilter(size = 3)) 
        img11 = ImageTk.PhotoImage(img)
        canvas2.create_image(imagewidth,imageheight, image=img11)
        canvas2.image = img11
    R1 = Button(win1, text="Filtre Median", command=median_blur).grid(row=3,column=0)

#Enregester l'image
def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}", filetypes=[(
        "All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    if file:
        if canvas2.image == img1:
            imgg.save(file)
        elif canvas2.image == img3:
            img2.save(file)
        elif canvas2.image == img5:
            img4.save(file)
        elif canvas2.image == img7:
            img6.save(file)
        elif canvas2.image == img9:
            img8.save(file)
        elif canvas2.image == img11:
            img10.save(file)

# create canvas to display image
frame = Canvas(root,width=800,height=900)

#image 1 before
canvas1 = Canvas(frame,width=400,height=325, relief=RIDGE, bd=2)
canvas1.create_text(160, 25, text="AVANT", fill="black", font=('Helvetica 15 bold'))
canvas1.grid(row=0,column=0)

#image 2 After
canvas2 = Canvas(frame,width=400,height=325,relief=RIDGE, bd=2)
canvas2.create_text(160, 25, text="APRES", fill="black", font=('Helvetica 15 bold'))
canvas2.grid(row=0,column=1)

frame.grid(row=2,column=0)

#frame 2 pour les Buttons
frame2 = Canvas(root,width=800,height=900)
frame2.grid(row=3,column=0)



# create buttons
btn1 = Button(frame2, text="clear", bg='silver', fg='black',font=('ariel 15 bold'),  command=clear)
btn1.grid(row=100,column=0)
btn1 = Button(frame2, text="Select Image", bg='silver', fg='black',font=('ariel 15 bold'),  command=selected)
btn1.grid(row=100,column=1)
btn2 = Button(frame2, text="Save",  bg='silver', fg='black',font=('ariel 15 bold'),  command=save)
btn2.grid(row=100,column=2)
btn3 = Button(frame2, text="Exit",  bg='silver', fg='black',font=('ariel 15 bold'),  command=root.destroy)
btn3.grid(row=100,column=3)

#Histograme
def histo():
    global img_path
    image = Image.open(img_path)
    def getRed(redVal):
        return '#%02x%02x%02x' % (redVal, 0, 0)
    def getGreen(greenVal):
        return '#%02x%02x%02x' % (0, greenVal, 0)
    def getBlue(blueVal):
        return '#%02x%02x%02x' % (0, 0, blueVal)
    image.putpixel((0,1), (1,1,5))
    image.putpixel((0,2), (2,1,5))
    histogram = image.histogram()
    l1 = histogram[0:256]
    l2 = histogram[256:512]
    l3 = histogram[512:768]
    plt.figure(0)
    for i in range(0, 256):
        plt.bar(i, l1[i], color = getRed(i), edgecolor=getRed(i), alpha=0.3)
    plt.figure(1)
    for i in range(0, 256):
        plt.bar(i, l2[i], color = getGreen(i), edgecolor=getGreen(i),alpha=0.3)
    plt.figure(2)
    for i in range(0, 256):
        plt.bar(i, l3[i], color = getBlue(i), edgecolor=getBlue(i),alpha=0.3)
    plt.show()

# Creating Menubar
menubar = Menu(root)

#menu Files
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Open...', command = selected)
file.add_command(label ='Save', command = save)
file.add_command(label ='clear', command = clear)
file.add_separator()
file.add_command(label ='Exit', command = root.quit)
#menu Outiles
outils = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Outils', menu = outils)
outils.add_command(label ='Blur', command = blur)
outils.add_command(label ='brightness', command = brightness)
outils.add_command(label ='contrast', command = contrast)
outils.add_command(label ='rotate', command = rotate_image)
outils.add_command(label ='flip', command = flip)
outils.add_command(label ='border', command = border_image)
#menu Filtres
filtree = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Filtres', menu = filtree)
filtree.add_command(label ='Filtres', command = filres)

edition = Menu(menubar, tearoff = 0)
historgrame = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Histograme', menu = historgrame)
menubar.add_cascade(label ='edition', menu = edition)

def show_about():
    about_window = Toplevel(root)
    about_window.title("Edition")
    Label(about_window, text="Mini Photoshop Avec Python.  \n Made By Mohamed Gzl \n Copyright © 2022–2023 ESTM ").pack()
    Button(about_window, text="Close", command=about_window.destroy).pack()

edition.add_command(label ='Edition', command =show_about)
historgrame.add_command(label ='historgrame', command =histo)

  


# display Menu
root.config(menu = menubar)
root.mainloop()