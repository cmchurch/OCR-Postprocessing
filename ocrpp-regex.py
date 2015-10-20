import re

#open file
f = open("/home/cmchurch/jdv_20141018/1878-p1.pdf.txt","r")
text = f.read().decode('utf8')
f.close

#remove the disclaimer from the file [beginning of line (\A) to "bnf.fr" non-greedy (?)]
p = re.compile('\A.*?@bnf\.fr',re.MULTILINE|re.DOTALL)
text = p.sub('',text)

#fix hyphenated words (-\n) | fix broken lines (\n\w) | remove long strings > 2 of non-alpha characters (^\w]{2,})
pattern = re.compile(r'(-\n|\n\w|[^\w]{2,})',re.UNICODE)
text = pattern.sub(' ',text).lower()

#print text
print text
