'''
Created on Jan 14, 2013

@author: christopherward
'''
def shout(txt):
  new_txt = txt.upper()
  new_txt = new_txt.replace(".", "!")
  new_txt = new_txt.replace("?", "!")
  '''if new_txt[len(new_txt) - 1] != ".":    #not needed
    new_txt = new_txt + "!"'''
  return new_txt

def reverse(txt):
  if isinstance(txt, str) == False: #what does this function do
    return ""
  return txt[::-1]
  
def reversewords(txt):
  if isinstance(txt,str) == False:
      return ""
  
  new_text = ""
  reversed_sentences = []
  
  tmp = txt.replace("?", ".")
  tmp = tmp.replace("!", ".")
  sentences = tmp.split(".")
  sentences = [s.strip() for s in sentences if len(s.strip()) > 0] #puts in an array all sentences that are not all whitespace?
  
  last_sentence = sentences[len(sentences) - 1]
  if last_sentence[len(last_sentence ) -1] == ".":
    sentences[len(sentences) -1] = last_sentence[0:len(last_sentence)-1]  
    
  for sentence in sentences:
    words = sentence.split()
    words.reverse()
    reversed_sentence = ""
    for word in words:
      reversed_sentence += word
      reversed_sentence += " "
    reversed_sentences.append(reversed_sentence[0:(len(reversed_sentence)-1)])
    
  for sentence in reversed_sentences:
    if len(sentence) > 0:
      new_text += sentence
      new_text += ". "
  new_text = new_text.rstrip(" ")   #fixed bug

  return new_text

def reversewordletters(txt):
  if isinstance(txt, str) == False:
    return ""
  
  tmp_text = ""
  new_txt = new_txt.replace("!", ".")
  new_txt = new_txt.replace("?", ".")
  '''
  back_pointer = 0
  front_pointer = 0
  stop_chars = [" ", ".", "?", "!", ",", ":", ";"]
  for i in range(0, len(txt) - 1):      #added "- 1"
    if txt[i] in stop_chars:
      back_pointer = i                 #changed from front_pointer to back_pointer
      
      word_range = range(front_pointer, back_pointer) #changed from front_pointer to back_pointer
      #word_range.reverse()
      for j in word_range:
        tmp_txt += txt[j]
      #tmp_txt == txt[i]
      revtmp_txt == tmp_txt.reverse
      print revtmp_txt
      
      #back_pointer = i+1
    print tmp_txt
    return tmp_text
  '''
def is_vowel(ch):
    if "aeiou".find(ch) >= 0:
        return True
    else:
        return False

def piglatin(s):
        if s[0] == 'q':
            return s[2:] + "-quay"
        if is_vowel (s[0]):
            return s + "-way"
        for index in range(1,len(s)):
            if is_vowel(s[index]):
                return s[index:] +"-"+s[:index]+"ay"
#if no vowels, it returns nothing
        else:
            return
    #!/usr/bin/env python

