#set up the dictionary of words
import csv
placeholder_list = list(csv.reader(open('dictionary.csv')))
allowed_words = []
for i in placeholder_list:
  for word in i:
    allowed_words.append(word)

#set up the scoring system
placeholder_score = list(csv.DictReader(open('scores.csv')))
scoring = placeholder_score[0]
for i in scoring:
  scoring[i] = int(scoring[i])

#placeholder variables
first_letter = None
score = 0
game = True
used_words = []

#gameplay
def gameplay(submitted_word = input):
  while game == True:
    #placeholder variables
    word = submitted_word.lower()
    submission = list(word)

  #check that submission is a word
    if word in allowed_words:
      x = True
    else:
      if first_letter == None:
        print(f'{word.title()} is not a word! Please try again.')
        continue
      else:
        print(f'{word.title()} is not a word! Please try again. The current letter is {first_letter.upper()}')
        continue

  #check that submission has not been used before in this game
    if word in used_words:
      print(f'{word.title()} has already been used in this game! Please try another word.')
      continue
    else:
      used_words.append(word)

  #check that submission begins with the correct letter
    if first_letter == submission[0]:
      first_letter = submission[-1]
    elif first_letter == None:
      first_letter = submission[-1]
    else:
      print('The first letter of your word must match the last letter of the previous word!')
      continue

  #scores the submission
    for letter in submission:
      if letter in scoring:
        score = score + scoring[letter]
    
    score = score + len(submission)
    
    print(f"Current Score: {score}")






# things needed:
  #discord functions
    # check if user was last person to play
    # react with check
  # need some way of maintaining individual user scores
  #add definitions to csv and create a definition function
  