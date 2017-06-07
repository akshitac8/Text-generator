import random,string

vowels='aeiou'
consonants='qwtrtyplkjhgfdszcvbnm'
letters=string.ascii_lowercase
count=int(raw_input("enter the no. of string you want"))
length=int(raw_input("length of the string"))
letter_input=[]

for q in range(length):
    letter_input.append(raw_input(".Enter 'c' consonant 'v' vowel 'l' for any:"))

def generator():
      gen_letter=''
      for st in letter_input:
            if(st == 'v'):
                letter=random.choice(vowels)
            elif(st == 'c'):
                letter=random.choice(consonants)
            elif(st  == 'l'):
                letter=random.choice(letters)
            else:
                letter=st
            gen_letter += letter
      return gen_letter
  

for i in range(count):
    print(generator())
    
