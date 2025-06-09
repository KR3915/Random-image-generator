import numpy as np
import matplotlib.pyplot as plt

def make_img():
    return np.random.rand(35, 35, 3) 

image_list = []
image_list.append(make_img())

current_image_index = 0
fig, ax = plt.subplots() 

image_display = ax.imshow(image_list[current_image_index])

ax.set_title(f"Image {current_image_index + 1}/{len(image_list)} (Use Left/Right Arrows)")

def on_key_press(event):

    global current_image_index 

    if event.key == "enter":
        image_list.append(make_img())
        current_image_index = (current_image_index + 1) % len(image_list)
    if event.key == "backspace":
        current_image_index = (current_image_index - 1) % len(image_list)
    image_display.set_data(image_list[current_image_index])
    
    ax.set_title(f"Image {current_image_index + 1}\n (use enter to cycle through images, backslash for coming back)")
    
    fig.canvas.draw_idle() 

fig.canvas.mpl_connect('key_press_event', on_key_press)

plt.show()

print("Image browser closed.")