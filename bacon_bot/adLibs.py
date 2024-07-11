import wordLists
import random
import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('averaged_perceptron_tagger')

class randomAdLib():
  #get wiki page content
  def __init__(self):
    self.wikiPage = random.choice(wordLists.adLibs)
  
    url = 'https://en.wikipedia.org/wiki/' + self.wikiPage
    page = requests.get(url)
    soup = BeautifulSoup(page.content , 'html.parser')
    [s.extract() for s in soup(['script'])]
    visible_text = soup.getText()
    start = random.randrange(1900, 5000)
    while visible_text[start:start + 1].isupper() != True:
      start = start + 1
    end = start + 500
    while visible_text[end:end + 1] != ".":
      end = end + 1
    adlibSection = str(visible_text[start:end + 1])

    self.numberToSwitch = 0
    self.numberNouns = 0
    self.numberProperNouns = 0
    self.numberPluralNouns = 0
    self.numberAdjectives = 0
    self.numberVerbs = 0
    self.numberAdVerbs = 0
    self.indexesSwitching = []
    self.numberTimesSwitching = 0
    self.finalReturnVar = ""

    self.adlibSection2 = adlibSection.split()
    self.adlibReturn = ""
    adlibTypes = nltk.pos_tag(self.adlibSection2)

  #replace words
    index = 0
    for word in self.adlibSection2:
      shouldReplace = random.randrange(0, 10)
      if shouldReplace == 1:
        if adlibTypes[index][1] == "NN":
          self.adlibSection2[index] = "INSERT_NOUN"
          self.numberNouns += 1
          self.numberToSwitch += 1
          self.indexesSwitching.append(index)
        elif adlibTypes[index][1] == "NNP":
          self.adlibSection2[index] = "INSERT_PROPER_NOUN"
          self.numberProperNouns += 1
          self.numberToSwitch += 1
          self.indexesSwitching.append(index)
        elif adlibTypes[index][1] == "NNS":
          self.adlibSection2[index] = "INSERT_PLURAL_NOUN"
          self.numberPluralNouns += 1
          self.numberToSwitch += 1
          self.indexesSwitching.append(index)
        elif adlibTypes[index][1] == "RB":
          self.adlibSection2[index] = "INSERT_ADVERB"
          self.numberAdVerbs += 1
          self.numberToSwitch += 1
          self.indexesSwitching.append(index)
        elif adlibTypes[index][1] == "JJ":
          self.adlibSection2[index] = "INSERT_ADJECTIVE"
          self.numberAdjectives += 1
          self.numberToSwitch += 1
          self.indexesSwitching.append(index)
        elif adlibTypes[index][1] == "VB":
          self.adlibSection2[index] = "INSERT_VERB"
          self.numberVerbs += 1
          self.numberToSwitch += 1
          self.indexesSwitching.append(index)
      index += 1
    

    self.inputs = self.numberNouns + self.numberProperNouns + self.numberPluralNouns + self.numberAdVerbs + self.numberAdjectives + self.numberVerbs

  #getuserwords
  def getinput(self):
    print("nouns: " + str(self.numberNouns) + "propernouns: " + str(self.numberProperNouns) + "plural nouns: " + str(self.numberPluralNouns) + "adverbs: " + str(self.numberAdVerbs) + "adjectives: " + str(self.numberAdjectives) + "verbs: " + str(self.numberVerbs))
    self.numberToSwitch -= 1
    for number in range(self.numberNouns):
      self.numberNouns -= 1
      yield "Choose a noun"
    for number in range(self.numberProperNouns):
      self.numberProperNouns -= 1
      yield "Choose a proper noun"
    for number in range(self.numberPluralNouns):
      self.numberPluralNouns -= 1
      yield "Choose a plural noun"
    for number in range(self.numberAdVerbs):
      self.numberAdVerbs -= 1
      yield "Choose an adverb"
    for number in range(self.numberAdjectives):
      self.numberAdjectives -= 1
      yield "Choose an adjective"
    for number in range(self.numberVerbs):
      self.numberVerbs -= 1
      yield "Choose a verb"

  def finalReturn(self):
    for word in self.adlibSection2:
      self.adlibReturn = self.adlibReturn + str(word) + " "
    self.finalReturnVar = "**" + self.wikiPage + "**" + "\n" + self.adlibReturn
    return "**" + self.wikiPage + "**" + "\n" + self.adlibReturn

  def setInputs(self, input):
    word = str(input.content)
    self.adlibSection2[int(self.indexesSwitching[self.numberTimesSwitching])] = word
    self.numberTimesSwitching += 1
    return "got input" + word