import os

path = r"C:\Users\lesh\Desktop\Study\KBTU\PP2\Syllabus PP2.docx"

existence = os.access(path, os.F_OK)
print("Existence: ",existence)

readability = os.access(path, os.R_OK)
print("Readability: ", readability)

writability = os.access(path, os.W_OK)
print("Writability: ", writability)

executability = os.access(path, os.X_OK)
print("Executability: ", executability)