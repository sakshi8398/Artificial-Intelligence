import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from pyswip import Prolog
#from pyswip.core import *
from pyswip.prolog import Prolog
from nltk import download
nltk.download('punkt')

swipl = Prolog()
swipl.consult("C:/Users/Sakshi/Desktop/AI/Assignment5/advisorySystem1.pl")

#taking user input for advisory system and processing it using nlp concept

#first input
inplist = []
inp1 = input("Are you interested in knowing the details of computer how it work or just happy with using it?(yes/no)")
tok1 = word_tokenize(inp1)
print("\n\n...tokens are ...", tok1)

ps = PorterStemmer()
for wod in tok1:
    print("\n..word is..",wod)
    stem1 = ps.stem(wod)
    print("...stem is ...", stem1)
    inplist.append(wod)

print("\n.. list is ", inplist)

f = open("Afacts.txt", 'w')
if 'yes' in inplist or 'no' in inplist:
    f.write("computer_systems({}).".format(inplist[0]))

#second input

inplist = []
inp2 = input("What would you prefer working on a computer or working manually?(computer,manually)")
tok2 = word_tokenize(inp2)
print("\n\n...tokens are ...", tok2)

ps = PorterStemmer()
for wod in tok2:
    print("\n..word is..",wod)
    stem1 = ps.stem(wod)
    print("...stem is ...", stem1)
    inplist.append(wod)

print("\n.. list is ", inplist)

f = open("Afacts.txt", 'a')
if 'computer' in inplist or 'manually' in inplist:
    print("computer")
    f.write("\ncomputer_or_manually({}).".format(inplist[0]))

    
#third input
inplist = []
inp3 = input("Are you better in solving problems?(solving_problem, solved_problem_as_application)")
tok2 = word_tokenize(inp3)
print("\n\n...tokens are ...", tok2)

ps = PorterStemmer()
for wod in tok2:
    print("\n..word is..",wod)
    stem1 = ps.stem(wod)
    print("...stem is ...", stem1)
    inplist.append(wod)

print("\n.. list is ", inplist)

f = open("Afacts.txt", 'a')
if 'solving_problem' in inplist or 'solved_problem_as_application' in inplist:
    print("computer")
    f.write("\nbetter_in_solving_problem({}).".format(inplist[0]))

#fourth input    

inplist = []
inp4 = input("Do you like dealing with numbers like manipulating it playing around it ?(yes,no)")
tok2 = word_tokenize(inp4)
print("\n\n...tokens are ...", tok2)

ps = PorterStemmer()
for wod in tok2:
    print("\n..word is..",wod)
    stem1 = ps.stem(wod)
    print("...stem is ...", stem1)
    inplist.append(wod)

print("\n.. list is ", inplist)

f = open("Afacts.txt", 'a')
if 'yes' in inplist or 'no' in inplist:
    print("computer")
    f.write("\nwork_with_numbers({}).".format(inplist[0]))

#fivth input
inplist = []
inp5 = input("Would you like to develop technology or like to simply apply it?(apply, develop)")
tok2 = word_tokenize(inp5)
print("\n\n...tokens are ...", tok2)

ps = PorterStemmer()
for wod in tok2:
    print("\n..word is..",wod)
    stem1 = ps.stem(wod)
    print("...stem is ...", stem1)
    inplist.append(wod)

print("\n.. list is ", inplist)

f = open("Afacts.txt", 'a')
if 'apply' in inplist or 'develop' in inplist:
    print("computer")
    f.write("\ntechnology({}).".format(inplist[0]))

#sixth input
inplist = []
inp6 = input("Do you have interest in Maths?(yes,no)")
tok2 = word_tokenize(inp6)
print("\n\n...tokens are ...", tok2)

ps = PorterStemmer()
for wod in tok2:
    print("\n..word is..",wod)
    stem1 = ps.stem(wod)
    print("...stem is ...", stem1)
    inplist.append(wod)

print("\n.. list is ", inplist)

f = open("Afacts.txt", 'a')
if 'yes' in inplist or 'no' in inplist:
    print("computer")
    f.write("\nmaths({}).".format(inplist[0]))

#seventh input
inplist = []
inp7 = input("Are you interested in dealing with circuits and learning more about it?(yes,no)")
tok2 = word_tokenize(inp7)
print("\n\n...tokens are ...", tok2)

ps = PorterStemmer()
for wod in tok2:
    print("\n..word is..",wod)
    stem1 = ps.stem(wod)
    print("...stem is ...", stem1)
    inplist.append(wod)

print("\n.. list is ", inplist)

f = open("Afacts.txt", 'a')
if 'yes' in inplist or 'no' in inplist:
    print("computer")
    f.write("\ndeal_with_circuits({}).".format(inplist[0]))
    
#eigth input
inplist = []
inp8 = input("Do you have interest in chemistry?(yes,no)")
tok2 = word_tokenize(inp8)
print("\n\n...tokens are ...", tok2)

ps = PorterStemmer()
for wod in tok2:
    print("\n..word is..",wod)
    stem1 = ps.stem(wod)
    print("...stem is ...", stem1)
    inplist.append(wod)

print("\n.. list is ", inplist)

f = open("Afacts.txt", 'a')
if 'yes' in inplist or 'no' in inplist:
    print("computer")
    f.write("\nchemistry({}).".format(inplist[0]))

#ninth input
inplist = []
inp9 = input("Do you have interest in physics?(yes,no)")
tok2 = word_tokenize(inp9)
print("\n\n...tokens are ...", tok2)

ps = PorterStemmer()
for wod in tok2:
    print("\n..word is..",wod)
    stem1 = ps.stem(wod)
    print("...stem is ...", stem1)
    inplist.append(wod)

print("\n.. list is ", inplist)

f = open("Afacts.txt", 'a')
if 'yes' in inplist or 'no' in inplist:
    print("computer")
    f.write("\nphysics({}).".format(inplist[0]))

#tenth input
inplist = []
inp9 = input("Do you have interest in biology?(yes,no)")
tok2 = word_tokenize(inp9)
print("\n\n...tokens are ...", tok2)

ps = PorterStemmer()
for wod in tok2:
    print("\n..word is..",wod)
    stem1 = ps.stem(wod)
    print("...stem is ...", stem1)
    inplist.append(wod)

print("\n.. list is ", inplist)

f = open("Afacts.txt", 'a')
if 'yes' in inplist or 'no' in inplist:
    print("computer")
    f.write("\nbiology({}).".format(inplist[0])) 

f.close()
