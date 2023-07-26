# broken keyboard

# display_welcome_blurb
# show_instructions
# show_random_diagnostic_paragraph

import msvcrt
import time
from random import randint
from time import sleep

paragraphs = [
    "There are times in life when we need a little encouragement.\n"
    "I'm sure you've been in situations where someone has given you\n"
    "words to lift up your spirits. When you are feeling down, these\n"
    "inspirational paragraphs can be a great pick-me-up. The best thing\n"
    "about inspirational paragraphs is that they aren't preachy or cheesy\n"
    "- they simply tell you how other people have persevered through\n"
    "their own trials and tribulations.",
    "SpongeBob SquarePants is friendly, optimistic, and loyal.His\n"
    "character was based on Charlie Chaplin, Jerry Lewis, Laurel and\n"
    "Hardy, and Pee Wee Herman. He is very gullible and makes many children\n"
    "and even adults laugh at the jokes with all the years the show has\n"
    "been on air. 'This is not your average everyday darkness.' This is...\n"
    "ADVANCED darkness! Hey, if I close my eyes, it doesn't seem so dark.\n"
    "This quote was said by SpongeBob in the thirty-fifth episode in the\n"
    "first season called 'Rock Bottom'. This is one of the many lines\n"
    "that made people laugh during the first year this show was on air\n"
    "and is just a weird line in general.",
    "Dumbledore is twinkly-eyed and playful but with a serious \n"
    "streak, while McGonagall is the right kind of strict. \n "
    "Also, having her by Dumbledore’s side cements their relationship \n"
    "as friends rather than just colleagues rather nicely. Take a look at me\n"
    "All this 'You-Know-Who' nonsense – for eleven years I have been trying\n"
    "to persuade people to call him by his proper name: Voldemort.' Professor\n"
    "McGonagall flinched, but Dumbledore, who was unsticking two sherbet lemons,\n"
    "seemed not to notice. ",
    "In Hinduism, dogs are a representative of the deity 'Bhirav'. Hinduism \n"
    "worships dogs especially for his honesty, loyalty and the ability of\n"
    "protection. Among the 12 zodiac signs in Chinese tradition, one zodiac\n"
    "sign is the dog. Despite being the best friend of humans, Chinese\n"
    "people use them for performing rituals and traditions. Dogs have been\n"
    "the second most important domesticated animal in Egyptian history. In\n"
    "ancient Egyptian culture, it was an important tradition to bury the dog\n"
    "with his master after his death. Even in Zoroastrianism,dogs are the\n"
    "cleanest, most honest, sacred and the most important animal.\n"
    "They especially feed dogs on the death memorial of someone.",
    "Hard work will definitely pay off.\n"
    "History has shown that hard work is an essential part of our lives.\n"
    "Without hard work, there is no success in life. An idle person,\n"
    "who is seen relaxing all the time, can never achieve success. It\n"
    "is impossible to reach the height of success without hard work.\n"
    "People always think of shortcuts, but there is no shortcut in life.\n"
    "Everything depends on hard work and the way you take up things.\n"
    "We have heard the success stories of Edison, Mahatma Gandhi, Isaac Newton,\n"
    "Saina Nehwal, Roger Federer and so on. These people are among the many\n"
    "who have led exemplary lives and have become perfect models of how hard\n"
    "work can bring success. They have also taught the world that challenges\n"
    "and failures are nothing but stepping stones to attaining success and\n"
    "that continuous hard work will definitely pay off at the right time.",
    "There are many idiosyncratic typing styles in between novice-style\n"
    "'hunt and peck' and touch typing. For example, many 'hunt and peck'\n"
    "typists have the keyboard layout memorized and are able to type while\n"
    "focusing their gaze on the screen. Some use just two fingers, while\n"
    "others use 3-6 fingers. Some use their fingers very consistently,\n"
    "with the same finger being used to type the same character every time,\n"
    "while others vary the way they use their fingers.",
    "The fastest typing speed ever, 216 words per minute, was achieved by\n"
    "Stella Pajunas-Garnand from Chicago in 1946 in one minute on an IBM\n"
    "electric.As of 2005, writer Barbara Blackburn was the fastest\n"
    "English language typist in the world, according to The Guinness\n"
    "Book of World Records. Using the Dvorak Simplified Keyboard, she\n"
    "had maintained 150 wpm for 50 minutes, and 170 wpm for shorter\n"
    "periods, with a peak speed of 212 wpm. Blackburn, who failed her\n"
    "QWERTY typing class in high school, first encountered the Dvorak\n"
    "keyboard in 1938, quickly learned to achieve very high speeds, and\n"
    "occasionally toured giving speed-typing demonstrations during her\n"
    "secretarial career. She appeared on Late Night with David Letterman\n"
    "on January 24, 1985, but felt that Letterman made a spectacle of her.\n"
    "Blackburn died in April 1st 2008."
]

def displayWelcomeBlurb():
    print("Welcome to Broken Keyboard!")
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
    paragraphIndex = randint(0,6)
    print(paragraphs[paragraphIndex])

#def takeUserInput():


#Main Code:
def main():
    displayWelcomeBlurb()
    sleep(8)
    showInstructions()
    showRandomDiagnosticParagraph()
    char = msvcrt.getch()
    sleep(3)
    print(char)

if __name__ == "__main__":
    main()


# clear the keyboard buffer
#while msvcrt.kbhit():
#    msvcrt.getch()
