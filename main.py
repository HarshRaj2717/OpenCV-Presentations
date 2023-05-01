import os
import customtkinter
import presenter
from resize_and_save_slides import resize_and_save_slides

# Variables
slide_directory_name = ""


def choose_ppt_file() -> None:
    global slide_directory_name
    global file_selection_label

    slide_directory_name = customtkinter.filedialog.askdirectory(
        title='Open a file',
        initialdir=os.curdir
    )

    if len(slide_directory_name) == 0:
        slide_directory_name = ""
    else:
        file_selection_label.configure(
            text="✅ Directory of slides selected.", text_color="green")


def prepare_temp_slides() -> bool:
    # Gathering path to all slides in slide_directory_name directory
    slides = os.listdir(slide_directory_name)
    # Saving all slides with thier names and paths
    slides = list(
        map(os.path.join, [slide_directory_name] * len(slides), slides))
    # Keeping only files with a known image extension
    slides = [_ for _ in slides if _.split(
        '.')[-1] in ['jpeg', 'png', 'jpg', 'svg', 'webp']]
    if len(slides) == 0:
        # Return false (no success) if there are no slide images in the provided slide_directory_name
        return False

    # Creating a temp directory in root folder
    try:
        os.mkdir(os.path.join(os.curdir, "temp"))
    except Exception as error:
        print(error)

    # Resize all slides to 1280x720 pixels
    # and save into the temp directory
    resize_and_save_slides(slides)

    # Returning True to specify success
    return True


def delete_temp_slides() -> None:
    # Delete temp directory in root folder
    try:
        # Gathering path to all slides in slide_directory_name directory
        slides = os.listdir(os.path.join(os.curdir, "temp"))
        # Saving all slides with thier names and paths
        slides = list(
            map(os.path.join, [os.path.join(os.curdir, "temp")] * len(slides), slides))
        # Deleting each slide inside temp directory
        for slide in slides:
            os.remove(slide)
        # Deleting temp directory
        os.rmdir(os.path.join(os.curdir, "temp"))
    except Exception as error:
        print(error)


def presentation_starter() -> None:
    global file_selection_label

    if slide_directory_name == "":
        file_selection_label.configure(
            text="❌ Directory of slides not selected!", text_color="red")
    else:
        success = prepare_temp_slides()
        if success:
            presenter.start_presenting("temp")
        delete_temp_slides()


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
