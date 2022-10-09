#!/usr/bin/env python
# coding: utf-8

# Q. In what modes should the PdfFileReader() and PdfFileWriter() File objects will be opened?

# These files will be opened in binary mode-> read binary (rb) for PdfFileReader() and write binary (wb) PdfFileWriter()

# In[3]:


get_ipython().system('pip install PyPDF2')


# Q2 From a PdfFileReader object, how do you get a Page object for page 5?

# Calling getPage(4) will return a Page object for page 5 since page 0 is the first page

# In[7]:


import PyPDF2 as pdf
pdf_input=open('Age_Declaration_Form.pdf','rb')
pdf2=pdf.PdfFileReader(pdf_input)
pdf_obj=pdf2.getPage(0)# if pdf if of index 5 then we will give here getPage(4) as I have only this pdf so given 0 for 1
pdf_obj.extract_text()


# Q 3What PdfFileReader variable stores the number of pages in the PDF document?
# 
# 

# In[8]:


pdf2.numPages


# Q4. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?

# Before we obtain the page object, the pdf has to be decrypted by calling .decrypt('swordfish')

# In[12]:


#Q5 
pdf_obj.rotateClockwise(180)
#The rotateClockwise() and rotateCounterClockwise() methods. The degrees to rotate is passed as an integer argument


# Q6. What is the difference between a Run object and a Paragraph object?

# Paragraph Object : A document contains multiple paragraphs. A paragraph begins on a new line and contains multiple runs. The Document object contains a list of Paragraph objects for the paragraphs in the document. (A new paragraph begins whenever the user presses ENTER or RETURN while typing in a Word document.)
# 
# Run Objects : Runs are contiguous groups of characters within a paragraph with the same style

# Q7. How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?

# In[13]:


get_ipython().system('pip install docx')


# import docx
# doc = docx.Document('abc.docx')
# doc.paragraphs
# #By using doc.paragraphs

# Q8. What type of object has bold, underline, italic, strike, and outline variables?

# A Run object has bold, underline,italic,strike and outline variables

# Q9. What is the difference between False, True, and None for the bold variable?

# True always makes the Run object bolded and False makes it always not bolded, no matter what the style’s bold setting is. None will make the Run object just use the style’s bold setting

# Q10. How do you create a Document object for a new Word document?

# by calling docx.document()

# Q11. How do you add a paragraph with the text 'Hello, there!'' to a Document object stored in a variable named doc?

# import docx
# doc = docx.Document()
# 
# doc.add_paragraph('Hello there!')
# doc.save('hellothere.docx')

# Q12. What integers represent the levels of headings available in Word documents?

# integer from 0-4
# The integer 0 makes the heading the Title style, which is used for the top of the document. Integers 1 to 4 are for various heading levels, with 1 being the main heading and 4 the lowest subheading

# In[ ]:




