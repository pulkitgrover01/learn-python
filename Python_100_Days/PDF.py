
#########################################################################################################

# import os

# os.getcwd
# print("current working", os.getcwd())
# os.chdir("C:/Users/pgrover/Desktop/python-games/learn-python/Merge_PDF")
# print("done", os.getcwd())

################################################################################################ Combined_PDF_File

# from PyPDF2 import PdfWriter

# fileses = PdfWriter()

# input1 = open("Gaurav_Kumar_Chunera__Motion_Graphics_Artist.pdf", "rb")
# input2 = open("Laxminarayan Swain Resume-1.pdf", "rb")
# input3 = open("Palak Goel Resume 2024.pdf", "rb")
# input4 = open("resume-ananya.pdf", "rb")
# input5 = open("Resume-Vishal-Kapoor.pdf", "rb")

# fileses.append(input1)
# fileses.append(input2)
# fileses.append(input3)
# fileses.append(input4)
# fileses.append(input5)

# os.chdir("C:/Users/pgrover/Desktop/python-games/learn-python/Merge_PDF/Edited_files")

# with open("CV_combined.pdf","wb") as output:
#     fileses.write(output)

# fileses.close()
# output.close()



######################################################################################## Only_Fist_Page_of_PDF

# os.chdir("C:/Users/pgrover/Desktop/python-games/learn-python/Merge_PDF")


# from PyPDF2 import PdfWriter

# fileses = PdfWriter()

# input1 = open("Gaurav_Kumar_Chunera__Motion_Graphics_Artist.pdf", "rb")
# input2 = open("Laxminarayan Swain Resume-1.pdf", "rb")
# input3 = open("Palak Goel Resume 2024.pdf", "rb")
# input4 = open("resume-ananya.pdf", "rb")
# input5 = open("Resume-Vishal-Kapoor.pdf", "rb")

# fileses.merge(position=4, fileobj=input1, pages=(0,1))
# fileses.merge(position=3, fileobj=input2, pages=(0,1))
# fileses.merge(position=0, fileobj=input3, pages=(0,1))
# fileses.merge(position=1, fileobj=input4, pages=(0,1))
# fileses.merge(position=2, fileobj=input5, pages=(0,1))

# os.chdir("C:/Users/pgrover/Desktop/python-games/learn-python/Merge_PDF/Edited_files")

# with open("CV_First_Page_combined.pdf","wb") as output:
#     fileses.write(output)

# fileses.close()
# output.close()


#######################################################################


# from PyPDF2 import PdfWriter
# import os

# os.chdir("C:/Users/pgrover/Desktop")

# pdf_list = [files for files in os.listdir() if ".pdf" in files]

# ......................................................
# pdf_list = []
# for file in os.listdir():
#     if ".pdf" in file:
#         # print(files)
#         files = file
#         pdf_list.append(files)   
# print(pdf_list)
# .......................................................



# merger = PdfWriter()

# merger.append(pdf_list[1], pages=(0,1))
# merger.append(pdf_list[0], pages=(0,1))
# merger.append(pdf_list[3], pages=(0,1))
# merger.append(pdf_list[2], pages=(0,1))

# merger.write("Check_merged-pdf.pdf")
# merger.close()

















