# String Concatenation

str1 = "Shreyas"
str2 = "Ladhe"

result = str1 + " " + str2
print (result)

# String Length

text = "This is the text!!"
length = len(text)
print ("Length of string: ",length)

# String Cases

text = "This is the text!!"
uppercase = text.upper()
lowercase = text.lower()

print ("Uppercase: ",uppercase)
print ("Lowercase: ",lowercase)

# String replacement

ext = "This is the text!!"
mod_text = text.replace("the" , "a")

print("Modified Text: ", mod_text)

# String Strip

text = " some spaces around "
strip_text = text.strip()

print("Stripped Text: ", strip_text)

# String Substring

text = "This is a nice text!!"
substring = "nice text"
if substring in text:
    print(substring, "found in the text")