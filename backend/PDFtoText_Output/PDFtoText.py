import pdftotext
import codecs

def replace_unknow_space(obj):
    obj1=""
    for i in range(0,len(obj)):
        if(obj[i]=='\n' or obj[i]=='\r' or obj[i].isalnum()):
            obj1+=obj[i]
            print("oKA")
        else:
            obj1+=" "
    return obj1



filename="Resume_2"
# Load your PDF
# make sure that file name entered should not contain "
with open(filename+".pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# # If it's password-protected
# with open("secure.pdf", "rb") as f:
#     pdf = pdftotext.PDF(f, "secret")

# How many pages?
print(len(pdf))

f = open(filename, "w",encoding='utf-32')
# Iterate over all the pages
for page in pdf:
    print(page)
   #f.write(page.encode("utf-32","ignore").decode())
f.close()

