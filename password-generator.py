import random as r #random module
import string as s #using string module to import all letters + numbers + punctuations to use

#making it all into one string
alph = s.ascii_letters + s.digits + s.punctuation 

#defining length of the password
char_length = int(input('Enter the length of password: ')) 

final_pass = "" #empty string for storing password

#looping out to take a random character out one by one and putting into one string
for i in range(char_length): 
    y = r.choice(alph)
    final_pass +=y

print(final_pass) #final password!!
