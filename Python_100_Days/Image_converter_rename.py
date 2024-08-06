####################################################### File format converter
# from PIL import Image
# from pillow_heif import register_heif_opener
# import os


# os.chdir("C:/Users/pgrover/Desktop/Trip footages")

# register_heif_opener()

# heic_files = [photo for photo in os.listdir() if ".HEIC" in photo]

# # print(heic_files)
# for photo in heic_files:
#     temp_img = Image.open(photo)
#     png_img = photo.replace(".HEIC",".png")
#     temp_img.save(png_img)
#     os.remove(photo)





####################################################### File rename sequencer
# import os
# files = os.listdir("name_change_file")
# for index,file in enumerate(files, start=1):
#     if file.endswith(".pdf"): # if ".pdf" in file:
#         os.rename(f"name_change_file/{file}", f"name_change_file/{index}.pdf")
#         print(file)

