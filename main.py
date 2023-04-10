import os
import customtkinter
import presenter

# Variables
Slide_directory_name = ""


def choose_ppt_file() -> None:
    global Slide_directory_name
    global file_selection_label

    Slide_directory_name = customtkinter.filedialog.askdirectory(
        title='Open a file',
        initialdir=os.curdir
    )

    if len(Slide_directory_name) == 0:
        Slide_directory_name = ""
    else:
        file_selection_label.configure(
            text="✅ Directory of slides selected.", text_color="green")


def presentation_starter() -> None:
    global file_selection_label

    if Slide_directory_name == "":
        file_selection_label.configure(
            text="❌ Directory of slides not selected!", text_color="red")
    else:
        presenter.start_presenting(Slide_directory_name)


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
    master=frame, text="Choose slides directory", command=choose_ppt_file)

# Adding a file selection label
file_selection_label = customtkinter.CTkLabel(
    master=frame, text="", font=("Roboto", 20))

# Adding button to start the presentation
presentation_start_button = customtkinter.CTkButton(
    master=frame, text="Start Presenting", command=presentation_starter)

if __name__ == "__main__":
    main()
