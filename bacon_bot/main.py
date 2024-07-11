import discord
import asyncio
import os
import requests
import json
import random
import pytz
import re
import time
import io
import aiohttp
import wordLists
import adLibs

from pokemon import jprint
from keep_alive import keep_alive
from datetime import datetime
from bs4 import BeautifulSoup

my_api_key = os.getenv('MY_API_KEY')  #googleapikey
my_cse_id = os.getenv('MY_CSE_ID')

#TO DO: get google search for favorite --, insert all sudoku numbers, get hangman to work with multiple words, work on chess, work on chatbot, make pokemon game.

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
  await client.change_presence(
    activity=discord.Activity(type=discord.ActivityType.watching, name="bacon")
  )

  messageSent = False

  EDT = pytz.timezone('US/Eastern')
  datetimeHere = datetime.now(EDT)
  print(datetimeHere.strftime("%H"))
  print(messageSent)
  if datetimeHere.strftime("%H") == "23" and messageSent == False:
    print("should send")
    yourchannel = client.get_channel(636399538650742795)
    await yourchannel.message.send('Test')
    messageSent = True
  elif datetimeHere.strftime("%H") == 5:
    messageSent = False


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  #commands
  if msg.startswith('$commands'):
    await message.channel.send(
      '$commands \n $time \n $date \n $chat (+ message) \n $inspire \n $links (links of inputed page) \n $google (google input, first 5 results) \n $roll d-  (put number for -) \n $hangman (can add difficulty) \n $pokemon  (says stats of a pokemon) \n $trivia \n $sign  (put birthday mm dd yyyy) \n $picture (not working) \n $sudoku (not working) \n $chess (not working'
    )

  def is_correct(m):
    isright = True
    for letter in str(m.content):
      if letter.isalpha() or letter.isspace():
        continue
      else:
        isright = False
    return m.author == message.author and isright == True

  def is_correctTrivia(m):
    return m.author == message.author

#chatbot

  if msg.startswith('$chat'):
    aftermessage = msg[5:]
    commandknown = False
    if any(word in msg for word in wordLists.hi_words):

      await message.channel.send(random.choice(wordLists.hi_words))
      commandknown = True

    if any(word in msg for word in wordLists.bye_words):
      await message.channel.send(random.choice(wordLists.bye_words))
      commandknown = True

    if aftermessage.startswith('good morning'):
      await message.channel.send('good morning!')
      commandknown = True

    if 'how many' in msg:
      diceRoll = random.randrange(1, 11, 1)
      await message.channel.send(diceRoll)
      commandknown = True

    if 'say' in msg and 'to' in msg:
      whatToSay = msg[msg.index('say') + 4:msg.index('to')]
      person = msg[msg.index('to') + 3:]
      await message.channel.send(whatToSay + person)
      commandknown = True

    if 'on a scale of' in msg:
      numbers = []
      for word in aftermessage.split():
        try:
          number = int(word)
          numbers.append(number)
        except ValueError:
          print("")
      diceRoll = random.randrange(numbers[0], numbers[1] + 1, 1)
      await message.channel.send(diceRoll)
      commandknown = True

    if 'how are you' in msg:
      datePos = int(time.strftime("%d")) % 8
      await message.channel.send("I am " + wordLists.emotion_words[datePos] +
                                 ", how are you?")
      commandknown = True

    if 'favorite' in msg:
      favoritePosition = msg.index('favorite') + 9
      favoriteThing = msg[favoritePosition:]
      if 'is' in msg:
        favoriteThing = msg[favoritePosition:msg.index('is') - 1]
      elif 'are' in msg:
        favoriteThing = msg[favoritePosition:msg.index('are') - 1]
      else:
        favoriteThing = msg[favoritePosition:]

      #randomFavoriteThing  #search for the thing and print a result

      await message.channel.send('My favorite ' + favoriteThing + ' is ')
      commandknown = True

    if 'what is the chance that' in msg:
      thing = msg[30:]
      diceRoll = random.randrange(1, 101, 1)
      await message.channel.send('The chance that ' + str(thing) + " is " +
                                 str(diceRoll) + "%")
      commandknown = True

    #yes or no questions
    if 'can' in msg or 'am i' in msg or 'are you ' in msg or (
        'is' in msg and ' a ' in msg and 'favorite' not in msg) or (
          'will' in msg and 'when' not in msg and 'where' not in msg
          and 'what time' not in msg) or (
            'does' in msg and 'why' not in msg and 'who'
            not in msg) or 'more' in msg or 'less' in msg or 'do you' in msg:
      diceRoll = random.randrange(1, 3, 1)
      if diceRoll == 1:
        await message.channel.send('no')
      if diceRoll == 2:
        await message.channel.send('yes')
      commandknown = True

    if 'when' in msg or 'what year' in msg:
      await message.channel.send(str(random.randrange(1980, 2050, 5)) + "A.D.")
      commandknown = True

    if 'what time' in msg:
      hour = random.randrange(1, 24, 1)
      minute = random.randrange(1, 60)
      timeOfDay = "AM"
      if hour > 12:
        hour = hour - 12
        timeOfDay = "PM"
      if minute < 10:
        minute = "0" + str(minute)
      await message.channel.send(str(hour) + ':' + str(minute) + timeOfDay)
      commandknown = True

    if 'who' in msg:
      await message.channel.send(random.choice(wordLists.people))
      commandknown = True

    if 'why' in msg:
      await message.reply("Because of " + random.choice(wordLists.reasons))
      commandknown = True

    if 'where' in msg:
      await message.channel.send(random.choice(wordLists.places))
      commandknown = True

    if 'bacon' in msg:
      await message.reply('BACON BACON BACON!!!')
      commandknown = True

    if commandknown == False:
      print('unknown command')
      await message.channel.send(aftermessage)

#adlibs
  if msg.startswith('$adlib'):
    adlib = adLibs.randomAdLib()

    while adlib.numberToSwitch > 0:
      await message.channel.send(next(adlib.getinput()))
      userInput = await client.wait_for('message',
                                        check=is_correct,
                                        timeout=20.0)
      print("got user input")
      adlib.setInputs(userInput)

    print("out of loop")
    await message.channel.send(adlib.finalReturn())

#signs         write date xxxxxxxx
  if msg.startswith('$sign'):
    inputOriginal = msg[6:]
    print(inputOriginal)
    input = ""
    for letter in inputOriginal:
      if letter.isnumeric() == True:
        input = input + letter
      else:
        continue
    print(input)
    #zodiac
    total = int(input[0:4])
    print(total)
    if total >= 312 and total <= 419:
      await message.channel.send("Aries")
    elif total >= 420 and total <= 520:
      await message.channel.send("Taurus")
    elif total >= 521 and total <= 621:
      await message.channel.send("Gemini")
    elif total >= 622 and total <= 722:
      await message.channel.send("Cancer")
    elif total >= 723 and total <= 822:
      await message.channel.send("Leo")
    elif total >= 823 and total <= 922:
      await message.channel.send("Virgo")
    elif total >= 923 and total <= 1023:
      await message.channel.send("Libra")
    elif total >= 1024 and total <= 1121:
      await message.channel.send("Scorpius")
    elif total >= 1122 and total <= 1221:
      await message.channel.send("Sagittarius")
    elif total >= 1222 and total <= 119:
      await message.channel.send("Capricornus")
    elif total >= 120 and total <= 218:
      await message.channel.send("Aquarius")
    elif total >= 219 and total <= 320:
      await message.channel.send("Pisces")
    else:
      await message.channel.send("Not a valid date")
#chinese
    print("message for year" + str(input[4:]))
    year = int(input[4:]) % 12
    switcher = {
      0: "monkey",
      1: "Rooster",
      2: "Dog",
      3: "Pig",
      4: "Rat",
      5: "Ox",
      6: "Tiger",
      7: "Rabbit",
      8: "Dragon",
      9: "Snake",
      10: "Horse",
      11: "Sheep"
    }
    await message.channel.send("Chinese sign: " +
                               switcher.get(year, "Invalid year"))

#trivia
  if msg.startswith('$trivia'):
    response = requests.get(f'https://opentdb.com/api.php?amount=1')
    currentQuestionStats = response.json()
    #triviaquestion = json.dumps(currentQuestionStats, sort_keys=True, indent=4)
    #print(currentQuestionStats["results"][0])
    correctAnswer = currentQuestionStats["results"][0]["correct_answer"].lower(
    )

    #print choices
    answerChoices = currentQuestionStats["results"][0]["incorrect_answers"]
    messageToSend = ""
    correctAnswerSent = False
    positionForAnswer = random.randrange(0, len(answerChoices))
    position = 0
    for answer in answerChoices:
      if correctAnswerSent == False:
        if position == positionForAnswer:
          messageToSend = messageToSend + "\n" + answer
          messageToSend = messageToSend + "\n" + correctAnswer
        else:
          messageToSend = messageToSend + "\n" + answer
      else:
        messageToSend = messageToSend + "\n" + answer
      position = position + 1
    soup = BeautifulSoup(currentQuestionStats["results"][0]["question"])
    soup2 = BeautifulSoup(messageToSend)
    text = soup.find("p").string
    text2 = soup2.find("p").string
    await message.channel.send(
      str(text) + "\n **Choices are:** \n" + str(text2))

    #guess
    guess = await client.wait_for('message',
                                  check=is_correctTrivia,
                                  timeout=30.0)
    guess = guess.content.lower()

    #check answer
    if guess == correctAnswer:
      await message.channel.send("*You are correct!*")
    else:
      soup3 = BeautifulSoup(correctAnswer)
      text3 = soup3.find("p").string
      await message.channel.send(
        f"*You are wrong*... The correct answer is {text3}")

#time
  EDT = pytz.timezone('US/Eastern')
  datetimeHere = datetime.now(EDT)
  if msg.startswith('$time'):
    await message.channel.send(datetimeHere.strftime("%X%p"))
  if msg.startswith('$date'):
    await message.channel.send(datetimeHere.strftime("%x"))

#inspire
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

#sad
  if any(word in msg for word in wordLists.sad_words):
    await message.channel.send(random.choice(wordLists.encouragements))

#link
  if msg.startswith('$links'):
    numoflinks = 0
    query = msg[6:]
    page = requests.get(query)
    soup = BeautifulSoup(page.content, 'html.parser')
    listoflinks = ""
    for link in soup.findAll(
        'a', attrs={'href': re.compile("^http://") or re.compile("^http://")}):
      if numoflinks < 6:
        listoflinks = listoflinks + link.get('href') + '\n'
        numoflinks = numoflinks + 1
      else:
        await message.channel.send(listoflinks)
        break

  if msg.startswith('$google'):
    numoflinks = 0
    query = msg[8:]
    url = 'https://www.google.com/search?q=' + query
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    listoflinks = ""
    links = soup.findAll('h3')

    for cite in links:
      if numoflinks < 5:
        cite2 = str(cite)
        cite3 = cite2[cite2.index(">") + 1:]
        cite4 = cite3[cite3.index(">") + 1:]

        if 'span' in cite4:
          cite5 = cite4[cite4.index(">") + 1:]
          cite6 = cite5[:cite5.index("<")]
          listoflinks = listoflinks + str(cite6) + '\n'
        else:
          cite5 = cite4[:cite4.index("<")]
          listoflinks = listoflinks + str(cite5) + '\n'
        numoflinks = numoflinks + 1
      else:
        await message.channel.send(listoflinks)
        break

#roll dice
  if msg.startswith('$roll d'):
    number = int(msg[7:])
    diceRoll = random.randrange(1, number + 1, 1)
    await message.channel.send(diceRoll)

#hangman
  if msg.startswith('$hangman'):
    try:
      difficulty = int(msg[8:])
    except:
      difficulty = 10
    diceRoll = random.randrange(1, 11, 1)
    if diceRoll == 1:
      phrase = random.choice(wordLists.reasons)
      theme = "reasons"
    elif diceRoll == 2:
      phrase = random.choice(wordLists.colors)
      theme = "colors"
    elif diceRoll == 3:
      phrase = random.choice(wordLists.sports)
      theme = "sports"
    elif diceRoll == 4:
      phrase = random.choice(wordLists.foods)
      theme = "foods"
    elif diceRoll == 5:
      phrase = random.choice(wordLists.drinks)
      theme = "drinks"
    elif diceRoll == 6:
      phrase = random.choice(wordLists.spices)
      theme = "spices"
    elif diceRoll == 7:
      phrase = random.choice(wordLists.phrases)
      theme = "phrases"
    elif diceRoll == 8:
      phrase = random.choice(wordLists.jingles)
      theme = "jingles"
    elif diceRoll == 9:
      phrase = random.choice(wordLists.places)
      theme = "places"
    elif diceRoll == 10:
      phrase = random.choice(wordLists.weapons)
      theme = "weapons"
    else:
      phrase = "once upon a time"

    print(phrase)
    phrase2 = phrase.split()

    wordGuessed = False
    hangmanlives = difficulty
    guessedletters = []
    guessingphrase = ""

    for word in phrase2:
      for x in range(len(word)):
        guessingphrase = guessingphrase + "-"
      guessingphrase = guessingphrase + "   "
    await message.channel.send(guessingphrase + '\n' + "theme: " + theme)
    while hangmanlives > 0 and wordGuessed == False:

      try:
        guess = await client.wait_for('message',
                                      check=is_correct,
                                      timeout=10.0)
        guess = guess.content.lower()
        if guess == phrase:
          break
        elif guess in phrase:
          await message.channel.send(guess + " is in the phrase")
          x = 0
          for letter in phrase:
            if letter == guess:
              guessingphrase = guessingphrase[:x] + guess + guessingphrase[x +
                                                                           1:]
              x = x + 1
            else:
              if guessingphrase[x] == '-':
                guessingphrase = guessingphrase[:x] + '-' + guessingphrase[x +
                                                                           1:]
                x = x + 1
              else:
                x = x + 1
                continue
          await message.channel.send(guessingphrase)
          if '-' in guessingphrase:
            continue
          else:
            break
        else:
          if guess in guessedletters:
            await message.channel.send(f'You already guess the letter {guess}')
          else:
            hangmanlives = hangmanlives - 1
            await message.channel.send(
              guess + " was not in the phrase... \n You have " +
              str(hangmanlives) + " guesses remaining")
            guessedletters.append(guess)
      except asyncio.TimeoutError:
        return await message.channel.send(
          f'Sorry, you took too long. It was {phrase}')

    if hangmanlives == 0:
      await message.channel.send(f'You lost... the phrase was {phrase}')
    else:
      await message.channel.send("You Won! \n Good Job!")

#pokemon
  if msg.startswith('$pokemon'):
    pokimon = msg[9:].lower()
    try:
      response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokimon}')
      printMsg = "\n".join(jprint(response.json()))
      if len(printMsg) > 1900:
        await message.channel.send(printMsg[:1000])
        await message.channel.send(printMsg[1001:])
      else:
        await message.channel.send(printMsg)
    except:
      await message.reply(f"Could not find {pokimon}")

#picture
  if msg.startswith("$picture"):
    query = msg[9:]
    url = 'https://www.google.com/search?q=' + query
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find('img')
    print(links)
    link = links["src"]
    print(link)
    url = link[link.find('base64,') + 7:-1]
    print(url)

    async with aiohttp.ClientSession() as session:
      async with session.get(link) as resp:
        if resp.status != 200:
          return await msg.channel.send('Could not download file...')
        data = io.BytesIO(await resp.read())
        await msg.channel.send(file=discord.File(data, 'query'))

#sudoku
  if msg.startswith('$sudoku'):
    #TODO
    sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #step 1. fill sudoku

    #top left
    numbersOnetoNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for first in range(3):
      for second in range(3):
        numberInserted = random.choice(numbersOnetoNine)
        sudoku[first][second] = numberInserted
        numbersOnetoNine.remove(numberInserted)

    #middle
    numbersOnetoNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for first in range(3):
      for second in range(3):
        numberInserted = random.choice(numbersOnetoNine)
        sudoku[first + 3][second + 3] = numberInserted
        numbersOnetoNine.remove(numberInserted)

    #bottomright
    numbersOnetoNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for first in range(3):
      for second in range(3):
        numberInserted = random.choice(numbersOnetoNine)
        sudoku[first + 6][second + 6] = numberInserted
        numbersOnetoNine.remove(numberInserted)

    #top
    numbersOnetoNine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for first in range(3):
      for second in range(3):
        numbersOnetoNine2 = numbersOnetoNine
        numbersOnetoNine2 = numbersOnetoNine2.remove(sudoku[0][0])
        numbersOnetoNine2 = numbersOnetoNine2.remove(sudoku[1][0])
        numbersOnetoNine2 = numbersOnetoNine2.remove(sudoku[2][0])
        numbersOnetoNine2 = numbersOnetoNine2.remove(sudoku[first + 3][3])
        numbersOnetoNine2 = numbersOnetoNine2.remove(sudoku[first + 3][4])
        numbersOnetoNine2 = numbersOnetoNine2.remove(sudoku[first + 3][5])

        numbertoremove = random.choice(numbersOnetoNine2)

        sudoku[first + 3][second] = numbertoremove
        numbersOnetoNine.remove(numbertoremove)

  #step 2. delete numbers (16 remaining)
    numberFilled = 0
    for first in range(9):
      for second in range(9):
        if sudoku[first][second] != 0:
          numberFilled = numberFilled + 1
    numbersToDelete = numberFilled - 16
    for number in range(numbersToDelete):
      for first in range(9):
        for second in range(9):
          if sudoku[first][second] != 0:
            sudoku[random.choice(range(9))][random.choice(range(9))]
  #check solutions (probably wont do this step)

  #step 3. print sudoku
    messageParts = []

    for a in range(9):
      messageParts.append(
        str(sudoku[a][0]) + str(sudoku[a][1]) + str(sudoku[a][2]) +
        str(sudoku[a][3]) + str(sudoku[a][4]) + str(sudoku[a][5]) +
        str(sudoku[a][6]) + str(sudoku[a][7]) + str(sudoku[a][8]) + '\n')
    output = ""
    for a in range(9):
      output = output + str(messageParts[a])
    await message.channel.send(output)


#chess

  if (msg.startswith('$chess')):
    #TODO
    await message.channel.send('Game started, play black or white?')

    async def on_message(message):
      msgChess = message.content

      class whitepawn(x):

        def __init__(self, x):
          self.x = x
          print('white pawn made')
          self.y = 2

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class whiterook(x):

        def __init__(self, x):
          self.x = x
          print('white rook made')
          self.y = 1

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class whiteknight(x):

        def __init__(self, x):
          self.x = x
          print('white knight made')
          self.y = 1

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class whitebishop(x):

        def __init__(self, x):
          self.x = x
          print('white bishop made')
          self.y = 1

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class whitequeen():

        def __init__(self):
          self.x = 4
          print('white queen made')
          self.y = 1

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class whiteking():

        def __init__(self):
          self.x = 5
          print('white king made')
          self.y = 1

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class blackpawn(x):

        def __init__(self, x):
          self.x = x
          print('black pawn made')
          self.y = 7

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class blackrook(x):

        def __init__(self, x):
          self.x = x
          print('black rook made')
          self.y = 8

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class blackknight(x):

        def __init__(self, x):
          self.x = x
          print('black knight made')
          self.y = 8

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class blackbishop(x):

        def __init__(self, x):
          self.x = x
          print('black bishop made')
          self.y = 8

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class blackqueen():

        def __init__(self):
          self.x = 4
          print('black queen made')
          self.y = 8

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      class blackking():

        def __init__(self):
          self.x = 5
          print('white king made')
          self.y = 8

        def move(self, addx, addy):
          self.x = addx + self.x
          self.y = addy + self.y

      whitepawn1 = whitepawn(1)
      whitepawn2 = whitepawn(2)
      whitepawn3 = whitepawn(3)
      whitepawn4 = whitepawn(4)
      whitepawn5 = whitepawn(5)
      whitepawn6 = whitepawn(6)
      whitepawn7 = whitepawn(7)
      whitepawn8 = whitepawn(8)
      whiterook1 = whiterook(1)
      whiterook2 = whiterook(8)
      whiteknight1 = whiteknight(2)
      whiteknight2 = whiteknight(7)
      whitebishop1 = whitebishop(3)
      whitebishop2 = whitebishop(6)
      whiteking = whiteking()
      whitequeen = whitequeen()

      blackpawn1 = blackpawn(1)
      blackpawn2 = blackpawn(2)
      blackpawn3 = blackpawn(3)
      blackpawn4 = blackpawn(4)
      blackpawn5 = blackpawn(5)
      blackpawn6 = blackpawn(6)
      blackpawn7 = blackpawn(7)
      blackpawn8 = blackpawn(8)
      blackrook1 = blackrook(1)
      blackrook2 = blackrook(8)
      blackknight1 = blackknight(2)
      blackknight2 = blackknight(7)
      blackbishop1 = blackbishop(3)
      blackbishop2 = blackbishop(6)
      blackking = blackking()
      blackqueen = blackqueen()

      #chessBoard = [[whiterook1, whitepawn1, None, None, None, None, blackpawn1, blackrook1][whiteknight1, whitepawn2, None, None, None, None, blackpawn2, blackknight1][whitebishop1, whitepawn3, None, None, None, None, blackpawn3, blackbishop1][whitequeen, whitepawn4, None, None, None, None, blackpawn4, blackqueen][whiteking, whitepawn5, None, None, None, None, blackpawn5, blackking][whitebishop2, whitepawn6, None, None, None, None, blackpawn6, blackbishop2][whiteknight2, whitepawn7, None, None, None, None, blackpawn7, blackknight2][whiterook2, whitepawn8, None, None, None, None, blackpawn8, blackrook2]]
      chessBoard = [[]]

      #possible moves list
      possibleMoves = []
      #pawn
      if whitepawn1.y == 2 and chessBoard[
          whitepawn1.x][3] == None and chessBoard[whitepawn1.x][4] == None:
        possibleMoves.append(whitepawn1[whitepawn1.x][3])
        possibleMoves.append(whitepawn1[whitepawn1.x][4])
      else:
        if chessBoard[whitepawn1.x][whitepawn1.y + 1] == None:
          possibleMoves.append(whitepawn[whitepawn1.x][whitepawn1.y + 1])

        #rook
      whiterookblockedx = False

      while whiterookblockedx == False:
        if chessBoard[whiterook1.x + 1][whiterook1.y] != None:
          whiterookblockedx == True
        else:
          whiterook1.x = whiterook1.x + 1
          possibleMoves.append(whiterook[whiterook.x][whiterook.y])

      whiterookblockedy = False
      while whiterookblockedy == False:
        if chessBoard[whiterook1.x][whiterook1.y + 1] != None:
          whiterookblockedy == True
        else:
          whiterook1.y = whiterook1.y + 1
          possibleMoves.append(whiterook[whiterook.x][whiterook.y])

        #bishop
      whitebishopblockedNE = False
      whitebishopblockedSE = False
      whitebishopblockedNW = False
      whitebishopblockedSW = False

      while whitebishopblockedNE == False:
        if chessBoard[whitebishop1.x + 1][whitebishop1.y + 1] != None:
          whitebishopblockedNE == True
        else:
          whitebishop1.y = whitebishop1.y + 1
          whitebishop1.x = whitebishop1.x + 1
          possibleMoves.append(whitebishop[whitebishop.x][whitebishop.y])

      while whitebishopblockedSE == False:
        if chessBoard[whitebishop1.x + 1][whitebishop1.y - 1] != None:
          whitebishopblockedNE == True
        else:
          whitebishop1.y = whitebishop1.y - 1
          whitebishop1.x = whitebishop1.x + 1
          possibleMoves.append(whitebishop[whitebishop.x][whitebishop.y])

      while whitebishopblockedNW == False:
        if chessBoard[whitebishop1.x - 1][whitebishop1.y + 1] != None:
          whitebishopblockedNE == True
        else:
          whitebishop1.y = whitebishop1.y + 1
          whitebishop1.x = whitebishop1.x - 1
          possibleMoves.append(whitebishop[whitebishop.x][whitebishop.y])

      while whitebishopblockedSW == False:
        if chessBoard[whitebishop1.x - 1][whitebishop1.y - 1] != None:
          whitebishopblockedNE == True
        else:
          whitebishop1.y = whitebishop1.y - 1
          whitebishop1.x = whitebishop1.x - 1
          possibleMoves.append(whitebishop[whitebishop.x][whitebishop.y])

        #knight
      if whiteknight[whiteknight.x + 2][whiteknight.y + 1] != None:
        possibleMoves.append(whiteknight[whitebishop.x + 2][whitebishop.y + 1])
      elif whiteknight[whiteknight.x + 2][whiteknight.y - 1] != None:
        possibleMoves.append(whiteknight[whitebishop.x + 2][whitebishop.y - 1])
      elif whiteknight[whiteknight.x - 2][whiteknight.y + 1] != None:
        possibleMoves.append(whiteknight[whitebishop.x - 2][whitebishop.y + 1])
      elif whiteknight[whiteknight.x - 2][whiteknight.y - 1] != None:
        possibleMoves.append(whiteknight[whitebishop.x - 2][whitebishop.y - 1])
      elif whiteknight[whiteknight.x - 1][whiteknight.y + 2] != None:
        possibleMoves.append(whiteknight[whitebishop.x - 1][whitebishop.y + 2])
      elif whiteknight[whiteknight.x + 1][whiteknight.y + 2] != None:
        possibleMoves.append(whiteknight[whitebishop.x + 1][whitebishop.y + 2])
      elif whiteknight[whiteknight.x - 1][whiteknight.y - 2] != None:
        possibleMoves.append(whiteknight[whitebishop.x - 1][whitebishop.y - 2])
      elif whiteknight[whiteknight.x + 1][whiteknight.y - 2] != None:
        possibleMoves.append(whiteknight[whitebishop.x + 1][whitebishop.y - 2])

        #king
      if whiteking[whiteking.x - 1][whiteking.y + 1] != None:
        possibleMoves.append(whiteking[whiteking.x - 1][whiteking.y + 1])
      elif whiteking[whiteking.x][whiteking.y + 1] != None:
        possibleMoves.append(whiteking[whiteking.x + 1][whiteking.y + 1])
      elif whiteking[whiteking.x + 1][whiteking.y + 1] != None:
        possibleMoves.append(whiteking[whiteking.x + 1][whiteking.y + 1])
      elif whiteking[whiteking.x - 1][whiteking.y] != None:
        possibleMoves.append(whiteking[whiteking.x - 1][whiteking.y])
      elif whiteking[whiteking.x + 1][whiteking.y] != None:
        possibleMoves.append(whiteking[whiteking.x + 1][whiteking.y])
      elif whiteking[whiteking.x - 1][whiteking.y - 1] != None:
        possibleMoves.append(whiteking[whiteking.x - 1][whiteking.y - 1])
      elif whiteking[whiteking.x][whiteking.y - 1] != None:
        possibleMoves.append(whiteking[whiteking.x][whiteking.y - 1])
      elif whiteking[whiteking.x + 1][whiteking.y - 1] != None:
        possibleMoves.append(whiteking[whiteking.x + 1][whiteking.y - 1])

      #white
      if (msgChess.startswith('white')):
        await message.channel.send('Im black.')
      #black
      else:
        await message.channel.send('Im white.')

keep_alive()
client.run(os.getenv('TOKEN'))
