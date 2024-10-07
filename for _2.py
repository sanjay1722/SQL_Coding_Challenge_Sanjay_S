'''2. Accept a String from User an do the following :
1. Find the Length
2. Display String in reverse
2. Display every alternate Character in Upper Case
3. Find out No of Vowels in the String
4. Accept Username and Date of Birth (dd-mon-yy) from User
Create a Password String which will be combination of
1st 4 letters of username and last 2digits of Date of Birth
followed by $ sign
5. Encrypt the String and return Encrypted String
(Assume your Algorithm)'''

user_string = input("Enter a string: ")

string_length = len(user_string)
print("Length of the string: {}".format(string_length))

reversed_string = user_string[::-1]
print("Reversed string: {}".format(reversed_string))

alternate_uppercase = ""
for i in range(len(user_string)):
    if i % 2 == 0:
        alternate_uppercase += user_string[i].upper()  
    else:
        alternate_uppercase += user_string[i]           
print("Alternate characters in uppercase: {}".format(alternate_uppercase))

vowels = "aeiouAEIOU"
vowel_count = 0
for char in user_string:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the string: {}".format(vowel_count))


username = input("Enter your username: ")
dob = input("Enter your Date of Birth (dd-mon-yy): ")

password = username[:4] + dob[-2:] + "$"
print("Generated password: {}".format(password))

encrypted_password = ""
for char in password:
    encrypted_password += chr(ord(char) + 3)  # Shift each character by 3 in ASCII
print("Encrypted password: {}".format(encrypted_password))
