from rembg import remove
import easygui
from PIL import Image
import os

def main():
    # Prompt user to select an input file
    input_path = easygui.fileopenbox(
        title='Select Image File',
        filetypes=["*.png", "*.jpg", "*.jpeg"]
    )
    
    if input_path is None:
        print("No file selected. Exiting.")
        return
    
    # Prompt user to specify output file path
    output_path = easygui.filesavebox(
        title='Save File To',
        default=os.path.splitext(input_path)[0] + "_no_bg.png",
        filetypes=["*.png", "*.jpg"]
    )
    
    if output_path is None:
        print("No save location selected. Exiting.")
        return

    try:
        # Open the input image
        input_image = Image.open(input_path)
        
        # Remove the background
        output_image = remove(input_image)
        
        # Save the output image
        output_image.save(output_path)
        print(f"Background removed and saved to {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

