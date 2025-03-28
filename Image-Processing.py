import cv2
import numpy as np
from google.colab import files


uploaded = files.upload()


filename = "gans_gfg-(1).jpg"  


img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE) 


if img is None:
    print("Error: Unable to load image. Check the filename or file format.")
else:
   
    img_arr = np.array(img)
    
   
    print("Shape:", img_arr.shape)
    print("NumPy Array:\n", img_arr)


image.save("grayscale_output.jpg")
files.download("grayscale_output.jpg") 