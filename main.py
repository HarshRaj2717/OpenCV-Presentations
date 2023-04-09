import os
import customtkinter
import presenter


# Variables
filename = ""


def choose_ppt_file() -> None:
    global filename
    global file_selection_label

    filetypes = (
        ('temp', '*.*'),
        ('ppt', '*.ppt'),
        ('pptx', '*.pptx')
        # TODO try this out for libreoffice's default ppt format
        # TODO remove the temp entry
    )

    filename = customtkinter.filedialog.askopenfilename(
        title='Open a file',
        initialdir=os.curdir,
        filetypes=filetypes
    )

    if len(filename) == 0:
        filename = ""
    else:
        file_selection_label.configure(
            text="✅ PPT file selected.", text_color="green")


def ppt_to_images() -> None:
    # TODO Convert the PPT file into images into a ./temp folder so that it can be later used in presenter.py
    ...


def presentation_starter() -> None:
    global file_selection_label

    if filename == "":
        file_selection_label.configure(
            text="❌ PPT file not selected!", text_color="red")
    else:
        ppt_to_images()
        presenter.start_presenting()


def main():
    # Packing all UI elements to the frame
    file_open_button.pack(padx=20, pady=20)
    file_selection_label.pack(padx=20, pady=20)
    presentation_start_button.pack(padx=20, pady=20)

    # Running the mainloop for root
    root.mainloop()


# Setting the theme and colour scheme of UI
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Making the root for CTk
root = customtkinter.CTk()
root.title("OpenCV-Presentation")
root.geometry("500x250")

# Building a frame to work in
frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Adding button to choose the ppt file
file_open_button = customtkinter.CTkButton(
    master=frame, text="Choose ppt file", command=choose_ppt_file)

# Adding a file selection label
file_selection_label = customtkinter.CTkLabel(
    master=frame, text="", font=("Roboto", 20))

# Adding button to start the presentation
presentation_start_button = customtkinter.CTkButton(
    master=frame, text="Start Presenting", command=presentation_starter)

if __name__ == "__main__":
    main()
