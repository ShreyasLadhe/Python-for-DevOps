import re
# Regular Expressions

# Regex findall()
text = "The big white bear"
pattern = r"white"

search = re.search(pattern, text)
if search:
    print ("Pattern found: ", search.group())
else:
    print ("Pattern not found")

# Regex match()
text = "The small blue fish"
pattern = r"small"

match = re.match(pattern, text)
if match:
    print ("Match found: ", match.group())
else:
    print ("Match not found")

# Regex replace()
text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

#Regex split()
text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)