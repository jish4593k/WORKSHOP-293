import torch
from torchvision import transforms
from PIL import Image
from tkinter import Tk, Label, Button, filedialog

class ImageResizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Resizer")

        self.label = Label(master, text="Select an image to resize:")
        self.label.pack()

        self.select_button = Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.resize_image(file_path)

    def resize_image(self, original_path):
        input_image = Image.open(original_path)

        
        transform = transforms.Compose([
            transforms.Resize((256, 256)),  # Adjust the size as needed
            transforms.ToTensor()
        ])

        resized_image = transform(input_image)
        
   
        result_path = "resized_image.jpg"  # You can customize the result path
        resized_image_pil = transforms.ToPILImage()(resized_image)
        resized_image_pil.save(result_path)

      
        resized_image_pil.show()

        print(f"Image resized and saved to {result_path}")

if __name__ == '__main__':
    root = Tk()
    app = ImageResizerGUI(root)
    root.mainloop()
