from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from fileloader import open_file
from graph import graph
from graph_visualization import *
from prim import prim
from kruskal import kruskal

# Initialization
win = Tk()
win.title('MST Generator App')
win.tk.call('wm', 'iconphoto', win._w, PhotoImage(file='./assets/Graph.png'))
width = int(1920*0.6)
height = int(1080*0.6)
win.geometry(f"{width}x{height}")
win.resizable(False,False)

# Frame
frame = Frame(win, width=width, height=height)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Background
img = ImageTk.PhotoImage(Image.open("./assets/Background.png"))
bg = Label(frame, image = img)
bg.pack()

# Initializing variables
filename = ""
on = True
main_graph: graph
pos = ""

# Placing widgets
    
mst_label = Label(
    frame,
    text="✓",
    bg="#ffffff",
    font=("Arial", 25)
)
mst_label.place(
    x=880, y=42
)

mst_img = PhotoImage(file="./assets/MST Clustering.png")
mst_button = Button(
    frame,
    image=mst_img,
    bg="#ffffff",
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: check()
)
mst_button.place(
    x=930, y=45
)

text_img = PhotoImage(file="./assets/Text.png")
text_img_label = Label(frame, image=text_img, bg="#ffffff")
text_label = Label(frame, text="File Path", font=("Inter", 10))
text_img_label.place(
    x=85, y=215
)
text_label.place(
    x=100, y=236
)

insert_img = PhotoImage(file="./assets/Insert Button.png")
insert_button = Button(
    frame,
    image=insert_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: insert(),
    bg="#ffffff"
)
insert_button.place(
    x=87, y=304 
)

vis_img = PhotoImage(file="./assets/Visualize Button.png")
visualize_btn = Button(
    frame,
    image=vis_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: vis(),
    bg="#ffffff"
)
visualize_btn.place(
    x=325, y=304    
)

#Load an image in the script
graph_img = (Image.open("./assets/Photo.png"))
#Resize the Image using resize method
resized_image= graph_img.resize((400,350), Image.ANTIALIAS)
resized_graph_image = ImageTk.PhotoImage(resized_image)
graph_img_label = Label(frame, image=resized_graph_image, bg="#ffffff")
graph_img_label.place(
    x=629, y=210
)

prim_img = PhotoImage(file='./assets/Prim Button.png')
prim_btn = Button(
    frame,
    image=prim_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: prim_vis(),
    bg="#ffffff"
)
prim_btn.place(
    x=88, y=393
)

kruskal_img = PhotoImage(file='./assets/Kruskal Button.png')
kruskal_btn = Button(
    frame,
    image=kruskal_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: kruskal_vis(),
    bg="#ffffff"
)
kruskal_btn.place(
    x=325, y=393
)

node_img = PhotoImage(file='./assets/Node Button.png')
node_btn = Button(
    frame,
    image=node_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: print("Hi"),
    bg="#ffffff"
)
node_btn.place(
    x=88, y=393+90
)

edge_img = PhotoImage(file='./assets/Edge Button.png')
edge_btn = Button(
    frame,
    image=edge_img,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    command=lambda: print("Hi"),
    bg="#ffffff"
)
edge_btn.place(
    x=325, y=393+90
)

# Functionalities

def check():
    global mst_label
    global on

    on = not on
    # print(on)
    if on:
        mst_label['text'] = "✓"
    else:
        mst_label['text'] = "✕"
    mst_label.update()

def insert():
    global text_label
    global filename
    global main_graph
    global pos
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
    )
    text_label['text'] = filename
    text_label.update()
    main_graph = open_file(filename)
    pos = visualize(main_graph)

def vis():
    graph_img = (Image.open("./img/plotgraph.png"))
    resized_image= graph_img.resize((400,350), Image.ANTIALIAS)
    resized_graph_image = ImageTk.PhotoImage(resized_image)
    change_image(resized_graph_image)

def change_image(image):
    global graph_img_label
    
    graph_img_label.configure(image=image)
    graph_img_label.image = image

def prim_vis():
    global pos
    global main_graph
    out = prim(main_graph)
    visualize_with_MST(main_graph, out, pos)

    graph_img = (Image.open("./img/MST.png"))
    resized_image= graph_img.resize((400,350), Image.ANTIALIAS)
    resized_graph_image = ImageTk.PhotoImage(resized_image)
    change_image(resized_graph_image)

def kruskal_vis():
    global pos
    global main_graph
    out = kruskal(main_graph)
    visualize_with_MST(main_graph, out, pos)

    graph_img = (Image.open("./img/MST.png"))
    resized_image= graph_img.resize((400,350), Image.ANTIALIAS)
    resized_graph_image = ImageTk.PhotoImage(resized_image)
    change_image(resized_graph_image)


win.mainloop()