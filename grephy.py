import re
import io

#regexIn = open('test.txt', 'r')
#lineScan = file.readlines()
#alphTrack = int(6)
#alphabet = []
#for i in range(lineScan):
#  if i in alphabet
#    
#  else
#    alphabet.append(regexIn.readline())
  #print(alphabet)
#for char in alphabet:
#  print(char, end="")
#def readFile(file):
#  try:
#    with open(fileName, 'test') as inString:
#      regExStr = inString.read()
#      return regExStr

"""What you're seeing above are numerous failed attempts/ ideas at simply importing lines of regEx from a file.
The idea I began to implement below (as I came up with from seeing some scattered tutorials and code samples online)
was to first import a file, then parse that file into a string via a function (the first function seen).
That resulting string would be put through another function and turned into an NFA after being parsed again (seen partially in the second function).
That NFA might eventually have been turned into a DFA through an additional function.
Then, all these functions would be brought together via the bottom Main function.
Missing elements that would be added would include try/exception exception handling for all functions,
completed cases for parsing in the createNFA function, and then of course creating and finishing a DFA function.
And obviously making all this code, well, actually work.
Unfortunately, I didn't think to use Python until two days ago; I was stumbling around in Java and Javascript
with what little time I had worked on this last week (due to a multitude of circumstances).
I apologize, again, as I thought I would have vastly more to show for all this time...
"""

def fileInput(file):
  alphabet = set()
  for char in fileInput:
    alphabet.add(char)
  return alphabet

class createNFA(object):
  def __init__(self, fileAlph)
    regOut = []
    i = 0
    while(i < lens(fileAlph)
      if(fileAlph[i] == '+'):
        regOut.append(i)
      elif(fileAlph[i] == ''):
        regOut = 
      elif
      i = i + 1
          
def main():
  regInput = file.read()
  rawOut = fileInput(file)
  print(rawOut)
        
