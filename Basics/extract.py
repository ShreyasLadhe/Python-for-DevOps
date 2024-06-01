arn = "arn:aws:iam::123456789012:user/johndoe"
user = arn.split("/")[1] # Second part of the list formed after splittting
print (user)