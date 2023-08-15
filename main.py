# broken keyboard

# display_welcome_blurb
# show_instructions
# show_random_diagnostic_paragraph

import msvcrt
from random import randint
from time import sleep
from time import time

paragraphs = [
    "There are times in life when we need a little encouragement. I'm\n"
    "sure you've been in situations where someone has given you words to\n"
    "lift up your spirits. When you are feeling down, these inspirational\n"
    "paragraphs can be a great pick-me-up. The best thing about inspirational\n"
    "paragraphs is that they aren't preachy or cheesy - they simply tell you\n"
    "how other people have persevered through their own trials and tribulations.",
    "SpongeBob SquarePants is friendly, optimistic, and loyal. His character\n"
    "was based on Charlie Chaplin, Jerry Lewis, Laurel and Hardy, and Pee\n"
    "Wee Herman. He is very gullible and makes many children and even adults\n"
    "laugh at the jokes with all the years the show has been on air. 'This\n"
    "is not your average everyday darkness. This is... ADVANCED darkness\n"
    "Hey, if I close my eyes, it doesn't seem so dark.' This quote was said\n"
    "by SpongeBob in the thirty-fifth episode in the first season called\n"
    "'Rock Bottom'. This is one of the many lines that made people laugh\n"
    "during the first year this show was on air and is just a weird line\n"
    "in general.",
    "Dumbledore is twinkly-eyed and playful but with a serious streak, while\n"
    "McGonagall is the right kind of strict. Also, having her by Dumbledore's\n "
    "side cements their relationship as friends rather than just colleagues\n"
    "rather nicely. Take a look at this quote: 'All this 'You-Know-Who' nonsense\n"
    "– for eleven years I have been trying to persuade people to call him\n"
    "by his proper name: Voldemort.' Professor McGonagall flinched, but Dumbledore,\n"
    "who was unsticking two sherbet lemons, seemed not to notice.",
    "In Hinduism, dogs are a representative of the deity 'Bhirav'. Hinduism \n"
    "worships dogs especially for their honesty, loyalty, and the ability of\n"
    "protection. Among the 12 zodiac signs in Chinese tradition, one zodiac\n"
    "sign is the dog. Dogs have been the second most important domesticated\n"
    "animal in Egyptian history. In ancient Egyption culture, it was an\n"
    "important tradition to bury the dog with his master after his death.\n"
    "Even in Zoroastrianism, dogs are the cleanest, most honest, sacred, and most\n"
    "important animal.",
    "Hard work will definitely pay off. History has known that hard work is an\n"
    "essential part of our lives. Without hard work, there is no success in\n"
    "life. Without hard work, there is no success in life. An idle person, who\n"
    "is seen relaxing all the time, can never achieve success. It is impossible\n"
    "to reach the height of success without hard work. People always think of\n"
    "shortcuts, but there is no shortcut in life. Everything depends on hard work\n"
    "and the way you take up things. We have heard the success stories of Edison,\n"
    "Mahatma Gandhi, Isaac Newton, Saina Nehwal, Roger Federer, and so on. These\n"
    "people are among the many who have led exemplary lives and have become\n"
    "perfect models of how hard work can bring success. They have also taught the\n"
    "world that challenges and failures are nothing but stepping stones to\n"
    "attaining success and that continuous hard work will definitely pay off\n"
    "at the right time.",
    "There are many idiosyncratic typing styles in between novice-style 'hunt\n"
    "and peck' and touch typing. For example, many 'hunt and peck' typists have\n"
    "the keyboard layout memorized and are able to type while focusing their\n"
    "gaze on the screen. Some use just two fingers, while others use 3-6 fingers\n"
    "Some use their fingers very consistently, with the same finger being used\n"
    "to type the same character every time, while others vary the way they use\n"
    "their fingers.",
    "The fastest typing speed ever, 216 words per minute, was achieved by\n"
    "Stella Pajunas-Garnand from Chicago in 1946 in one minute on an IBM\n"
    "electric.As of 2005, writer Barbara Blackburn was the fastest English\n"
    "language typist in the world, according to The Guinness Book of World\n"
    "Records. Using the Dvorak Simplified Keyboard, she had maintained 150\n"
    "wpm for 50 minutes, and 170 wpm for shorter periods, with a peak speed\n"
    "of 212 wpm. Blackburn, who failed her QWERTY typing class in high school\n"
    "first encountered the Dvorak keyboard in 1938, quickly learned to achieve\n"
    "very high speeds, and occasionally toured giving speed-typing demonstrations\n"
    "during her secretarial career. She appeared a Late Night with David\n"
    "Letterman on January 24, 1985, but felt that Letterman made a spectacle\n"
    "of her. Blackburn died in April 1st 2008.",
    "One study examining 30 subjects, of varying different styles and expertise,\n"
    "has found minimal difference in typing speed between touch typists and\n"
    "self-taught hybrid typists. According to the study, 'The number of fingers\n"
    "does not determine typing speed... People using self-taught typing strategies\n"
    "were found to be as fast as trained typists... instead of the number of\n"
    "fingers, there are other factors that predict typing speed... fast typists...\n"
    "keep their hands fixed on one position, instead of moving them hands fixed on\n"
    "one position, instead of moving them over the keyboard, and more consistently\n"
    "use the same finger to type a certain letter.' To quote doctoral candidate Anna\n"
    "Feit: 'We were surprised to observe that people who took a typing course,\n"
    "performed at similar average speed and accuracy, as those that taught typing\n"
    "to themselves and only used 6 fingers on average.'",
]

keymap = {} #empty dictionary to keymap
def initializeKeymap():
    for i in range(256):
        keymap[chr(i)] = chr(i)

def displayWelcomeBlurb():
    print("Welcome to Brocen Keyboard!")
    print("This game will test your typing skills and quick-thinking while challenging your memory. Have fun!")
    print("")

def showInstructions():
    print("Here are the instructions:")
    print("1. You will receive a diagnostic paragraph. Try your best to be as accurate and efficient as possible.")
    print("2. Based on your performance, you will be placed on a level of difficulty.")
    print("3. As you level up, you will notice letters beginning to switch, making it even harder!")
    print("4. Last but not least, have fun!")
    print("")
    print("Press enter to begin") # Find a way to hide user input here
    input()

def showRandomDiagnosticParagraph():
    print("Here is your first paragraph:")
    paragraphIndex = randint(0,len(paragraphs)-1)
    print(paragraphs[paragraphIndex])
    return (paragraphs[paragraphIndex].count(" ")+paragraphs[paragraphIndex].count("\n")+1, paragraphIndex)


def inputDiagnosticParagraph(index):
    start = time()
    i = 0
    realMistakes = 0
    mistakes = 0
    diagnosticParagraph = paragraphs[index]
    userParagraph = [None]*len(diagnosticParagraph)
    backspace = '\b'
    while i < len(diagnosticParagraph):
        char = keymap[msvcrt.getch().decode("utf-8")]
        if char != backspace:  # user typed non-backspace character
            userParagraph[i] = char
            if char != diagnosticParagraph[i]:
                mistakes = mistakes + 1
                realMistakes = realMistakes + 1
            print(char, end='', flush=True)
            i = i + 1
        elif i > 0:  # user typed backspace and wasn't at the very beginning of the paragraph
            i = i - 1
            print('\b \b', end='', flush=True)
            if userParagraph[i] != diagnosticParagraph[i]:
                mistakes = mistakes - 1
    end = time()
    print("\n")
    return ((end - start)/60, mistakes, realMistakes)

#Main Code:
def main():
    initializeKeymap()
    displayWelcomeBlurb()
    sleep(8)
    showInstructions()
    (numwords, index) = showRandomDiagnosticParagraph()
    (duration, mistakes, realMistakes) = inputDiagnosticParagraph(index)
    print("Your average typing speed was {} wpm and you made {} mistakes but you really made {} mistakes.".format(round(numwords/duration,1), mistakes, realMistakes))

if __name__ == "__main__":
    main()