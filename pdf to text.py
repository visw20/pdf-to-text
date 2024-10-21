#pdf to text


# import fitz  # PyMuPDF

# def pymupdf_pdf_to_text(pdf_path):
#     """
#     Extract text from a PDF using PyMuPDF (Fitz).
    
#     :param pdf_path: Path to the PDF file
#     :return: Extracted text from the PDF
#     """
#     # Open the PDF
#     pdf_document = fitz.open(pdf_path)
    
#     full_text = ""
    
#     # Iterate through all the pages and extract text
#     for page_num in range(len(pdf_document)):
#         page = pdf_document.load_page(page_num)
#         text = page.get_text()
#         full_text += f"\n--- Page {page_num + 1} ---\n{text}\n"
    
#     return full_text

# # Example usage
# pdf_path = r'C:/Users/Viswajith/Downloads/Screenshot 2024-10-21 114041.pdf'
# extracted_text = pymupdf_pdf_to_text(pdf_path)

# print("Extracted Text:\n", extracted_text)






#pdf to text using tkinter

# import fitz  # PyMuPDF
# import tkinter as tk
# from tkinter import filedialog, Text, Scrollbar

# # Function to extract text from a PDF using PyMuPDF (Fitz)
# def pymupdf_pdf_to_text(pdf_path):
#     """
#     Extract text from a PDF using PyMuPDF (Fitz).
    
#     :param pdf_path: Path to the PDF file
#     :return: Extracted text from the PDF
#     """
#     # Open the PDF
#     pdf_document = fitz.open(pdf_path)
    
#     full_text = ""
    
#     # Iterate through all the pages and extract text
#     for page_num in range(len(pdf_document)):
#         page = pdf_document.load_page(page_num)
#         text = page.get_text()
#         full_text += f"\n--- Page {page_num + 1} ---\n{text}\n"
    
#     return full_text

# # Function to open a file dialog and extract text from the selected PDF
# def open_pdf():
#     # Open file dialog to select a PDF file
#     pdf_path = filedialog.askopenfilename(
#         title="Select PDF",
#         filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
#     )
    
#     if pdf_path:
#         # Extract text from the PDF
#         extracted_text = pymupdf_pdf_to_text(pdf_path)
        
#         # Clear the text box and insert the extracted text
#         text_box.delete(1.0, tk.END)
#         text_box.insert(tk.END, extracted_text)

# # Setting up the main window
# root = tk.Tk()
# root.title("PDF Text Extractor")

# # Create a Text widget with Scrollbar for displaying extracted text
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# text_box = Text(root, wrap=tk.WORD, yscrollcommand=scrollbar.set)
# text_box.pack(expand=True, fill='both')

# scrollbar.config(command=text_box.yview)

# # Create a button to open and extract text from a PDF
# open_button = tk.Button(root, text="Open PDF", command=open_pdf)
# open_button.pack(pady=10)

# # Start the GUI main loop
# root.geometry("600x600")  # Set default window size
# root.mainloop()






#--------------------

# # extract text from images in a PDF using PyMuPDF and tesseract

# import fitz  # PyMuPDF
# import pytesseract
# from PIL import Image
# import io

# # Specify the correct path to tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Viswajith\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# def extract_image_text_from_pdf(pdf_path):
#     """
#     Extract text from images inside a PDF using PyMuPDF and Tesseract OCR.
    
#     :param pdf_path: Path to the PDF file
#     :return: Extracted text from the images in the PDF
#     """
#     pdf_document = fitz.open(pdf_path)
#     full_text = ""

#     # Iterate through the PDF pages
#     for page_num in range(len(pdf_document)):
#         page = pdf_document.load_page(page_num)
        
#         # Extract images from the page
#         image_list = page.get_images(full=True)
#         if image_list:
#             for img_index, img in enumerate(image_list):
#                 # Get the image XREF (index)
#                 xref = img[0]
                
#                 # Extract the image bytes
#                 base_image = pdf_document.extract_image(xref)
#                 image_bytes = base_image["image"]
                
#                 # Convert to PIL image
#                 image = Image.open(io.BytesIO(image_bytes))
                
#                 # Use Tesseract to do OCR on the image
#                 text = pytesseract.image_to_string(image)
#                 full_text += f"\n--- Page {page_num + 1}, Image {img_index + 1} ---\n{text}\n"
#         else:
#             # Handle cases where there are no images on the page (fallback)
#             full_text += f"\n--- Page {page_num + 1} ---\nNo images found.\n"
    
#     return full_text

# # Example usage
# pdf_path = r'C:/Users/Viswajith/Downloads/Screenshot 2024-10-21 114041.pdf'
# extracted_text = extract_image_text_from_pdf(pdf_path)

# print("Extracted Text:\n", extracted_text)







# import fitz  # PyMuPDF
# import pytesseract
# from PIL import Image
# import io
# import tkinter as tk
# from tkinter import filedialog, scrolledtext, messagebox

# # Specify the correct path to tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Viswajith\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# def extract_image_text_from_pdf(pdf_path):
#     """
#     Extract text from images inside a PDF using PyMuPDF and Tesseract OCR.
    
#     :param pdf_path: Path to the PDF file
#     :return: Extracted text from the images in the PDF
#     """
#     pdf_document = fitz.open(pdf_path)
#     full_text = ""

#     # Iterate through the PDF pages
#     for page_num in range(len(pdf_document)):
#         page = pdf_document.load_page(page_num)
        
#         # Extract images from the page
#         image_list = page.get_images(full=True)
#         if image_list:
#             for img_index, img in enumerate(image_list):
#                 # Get the image XREF (index)
#                 xref = img[0]
                
#                 # Extract the image bytes
#                 base_image = pdf_document.extract_image(xref)
#                 image_bytes = base_image["image"]
                
#                 # Convert to PIL image
#                 image = Image.open(io.BytesIO(image_bytes))
                
#                 # Use Tesseract to do OCR on the image
#                 text = pytesseract.image_to_string(image)
#                 full_text += f"\n--- Page {page_num + 1}, Image {img_index + 1} ---\n{text}\n"
#         else:
#             # Handle cases where there are no images on the page (fallback)
#             full_text += f"\n--- Page {page_num + 1} ---\nNo images found.\n"
    
#     return full_text

# def open_file():
#     """
#     Open a file dialog to select a PDF file and extract text from images in the PDF.
#     """
#     file_path = filedialog.askopenfilename(
#         filetypes=[("PDF Files", "*.pdf")],
#         title="Select a PDF File"
#     )
    
#     if file_path:
#         try:
#             extracted_text = extract_image_text_from_pdf(file_path)
#             text_display.delete(1.0, tk.END)  # Clear previous content
#             text_display.insert(tk.END, extracted_text)  # Display extracted text
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to extract text: {e}")

# # Create the main application window
# root = tk.Tk()
# root.title("PDF Image Text Extractor")

# # Create a button to open the file dialog
# open_button = tk.Button(root, text="Open PDF", command=open_file)
# open_button.pack(pady=10)

# # Create a scrolled text area to display the extracted text
# text_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
# text_display.pack(pady=10)

# # Run the Tkinter event loop
# root.mainloop()






##it can handle text from both pdf and image in a pdf 



# import fitz  # PyMuPDF
# import pytesseract
# from PIL import Image
# import io

# # Specify the correct path to tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Viswajith\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# def extract_text_from_pdf(pdf_path):
#     """
#     Extract text from a PDF using PyMuPDF (Fitz) and Tesseract OCR.
    
#     :param pdf_path: Path to the PDF file
#     :return: Extracted text from the PDF
#     """
#     # Open the PDF
#     pdf_document = fitz.open(pdf_path)
#     full_text = ""

#     # Iterate through all the pages
#     for page_num in range(len(pdf_document)):
#         page = pdf_document.load_page(page_num)

#         # Try to extract text directly
#         text = page.get_text()
#         if text.strip():  # Check if text extraction was successful
#             full_text += f"\n--- Page {page_num + 1} ---\n{text}\n"
#         else:
#             # If no text was found, check for images and perform OCR
#             image_list = page.get_images(full=True)
#             if image_list:
#                 for img_index, img in enumerate(image_list):
#                     # Get the image XREF (index)
#                     xref = img[0]
                    
#                     # Extract the image bytes
#                     base_image = pdf_document.extract_image(xref)
#                     image_bytes = base_image["image"]
                    
#                     # Convert to PIL image
#                     image = Image.open(io.BytesIO(image_bytes))
                    
#                     # Use Tesseract to do OCR on the image
#                     text = pytesseract.image_to_string(image)
#                     full_text += f"\n--- Page {page_num + 1}, Image {img_index + 1} ---\n{text}\n"
#             else:
#                 # Handle cases where there are no images on the page (fallback)
#                 full_text += f"\n--- Page {page_num + 1} ---\nNo text or images found.\n"
    
#     return full_text

# # Example usage
# pdf_path = r'C:/Users/Viswajith/Downloads/Human-Nutrition-2020-Edition-1598491699.pdf'
# extracted_text = extract_text_from_pdf(pdf_path)

# print("Extracted Text:\n", extracted_text)





##it can handle text from both pdf and image in a pdf using tkinter


import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

# Specify the correct path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Viswajith\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF using PyMuPDF (Fitz) and Tesseract OCR.
    
    :param pdf_path: Path to the PDF file
    :return: Extracted text from the PDF
    """
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    full_text = ""

    # Iterate through all the pages
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)

        # Try to extract text directly
        text = page.get_text()
        if text.strip():  # Check if text extraction was successful
            full_text += f"\n--- Page {page_num + 1} ---\n{text}\n"
        else:
            # If no text was found, check for images and perform OCR
            image_list = page.get_images(full=True)
            if image_list:
                for img_index, img in enumerate(image_list):
                    # Get the image XREF (index)
                    xref = img[0]
                    
                    # Extract the image bytes
                    base_image = pdf_document.extract_image(xref)
                    image_bytes = base_image["image"]
                    
                    # Convert to PIL image
                    image = Image.open(io.BytesIO(image_bytes))
                    
                    # Use Tesseract to do OCR on the image
                    text = pytesseract.image_to_string(image)
                    full_text += f"\n--- Page {page_num + 1}, Image {img_index + 1} ---\n{text}\n"
            else:
                # Handle cases where there are no images on the page (fallback)
                full_text += f"\n--- Page {page_num + 1} ---\nNo text or images found.\n"
    
    return full_text

def open_file():
    """Open a file dialog to select a PDF and extract text from it."""
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        try:
            extracted_text = extract_text_from_pdf(pdf_path)
            text_box.delete(1.0, tk.END)  # Clear the text box
            text_box.insert(tk.END, extracted_text)  # Insert the extracted text
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("PDF Text Extractor")

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open PDF", command=open_file)
open_button.pack(pady=10)

# Create a scrolled text box to display the extracted text
text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30)
text_box.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()









