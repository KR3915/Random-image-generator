import numpy as np
import matplotlib.pyplot as plt
#define Height and wdith
W = None
H = None
#error handlers
while W is None:
    try:
        W = int(input("Enter width: "))
    except ValueError:
        print("Invalid input. Please enter a whole number for width.")

while H is None:
    try:
        H = int(input("Enter height: "))
    except ValueError:
        print("Invalid input. Please enter a whole number for height.")
#create random array
def make_img(width=W, height= H):
    return np.random.rand(width, height, 3) 
#declare variables
image_list = [] #list of images
image_list.append(make_img()) #make first image
current_image_index = 0 #global holding value of current image
fig, ax = plt.subplots() #conf axis and figure
image_display = ax.imshow(image_list[current_image_index]) #image displaying

ax.set_title(f"(use enter to cycle through images, backspace for coming back)") #title for figure

def on_key_press(event): 
    global saved_image_count
    global current_image_index 
    # cycle thru imgs
    if event.key == "enter":
        image_list.append(make_img())
        current_image_index = (current_image_index + 1) % len(image_list)
    if event.key == "backspace":
        current_image_index = (current_image_index - 1) % len(image_list)
    image_display.set_data(image_list[current_image_index])
    #set title
    ax.set_title(f"Image {current_image_index + 1}")
    
    fig.canvas.draw_idle() #redraw fig

fig.canvas.mpl_connect('key_press_event', on_key_press)#set events to canvas

plt.show()

print("Image browser closed.")
