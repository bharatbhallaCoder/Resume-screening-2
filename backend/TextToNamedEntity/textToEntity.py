import spacy 
import pdftotext
filename="Resume_2"
nlp = spacy.load('en_core_web_sm') 


with open("../PDFtoText_Output/"+filename+".pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
    
for page in pdf:
    print(page)
    sentence = page
    doc = nlp(sentence) 
    for ent in doc.ents: 
	    print(ent.text, "         ",ent.label_,spacy.explain(ent.label_)) 
