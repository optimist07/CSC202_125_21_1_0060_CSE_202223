from tkinter import *

BACKGROUND_COLOR = "#D3D3D3"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=750, height=520)
card_front_img = PhotoImage(file="Image/cardFront.jpg")  #Make_sure_to_provide_the_correct_path
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 35, "italic"))  # Correct_the_font_name_type_("Ariel" to "Arial")
canvas.create_text(400, 263, text="word", font=("Arial", 65, "bold"))  # Correct the font name typo ("Ariel" to "Arial")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # Fix the config argument to set the background color
canvas.grid(row=0, column=0)

window.mainloop()
