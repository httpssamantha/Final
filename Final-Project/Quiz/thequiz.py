
def play_quiz():
    print("Determining your Patronus....")
    print("When chosing your answer, please put the letter that is in brackets.")
    print(" ")
    print(" ")
    print("You enter the woods, and see a small, shapeless light hovering before you.")
    print("As you try to get closer to it, the shapeless light seems to move away from you.")
    print("Curious, you follow the light to see where it goes.")
    print(" ")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*")
    print(" ")
    print("A few feet into the woods, the light seems to stop.")
    print("*...*  Suddenly, you hear a quiet voice say:")
    print("You are ready to begin your journey....")
    print("You can only chose one, (b)lack or (w)hite?")
    Spoints = 0
    Opoints = 0
    JRpoints = 0
    Hpoints = 0
    BW = (input("~,.~*,.~  "))

    if BW=="b" or BW=="B":
        Hpoints += 1
        Opoints += 1
    else:
        if BW=="w" or BW=="W":
            JRpoints += 1
            Spoints += 1
    print(" ")
    print(" ")
    print("Once answering the question, the light grows and becomes little brighter.")
    print("*~,.,~* The light then seems to continue into the forest")
    print("A few feet more, into the woods, the light stops again.")
    print("*...*  The quiet voice comes back and says:")
    print("If you could be known for one thing what would you chose?")
    print(" ")
    print(" (L)eader,  (H)ardworker,  (F)earless, (U)nique")
    Know = (input("~,.~*,.~  "))
    if Know=="L" or Know=="l":
        Spoints += 1
    elif Know=="H" or Know=="h":
        Opoints += 1
    elif Know=="F" or Know=="f":
        JRpoints += 1
    else:
        if Know =="U" or Know=="u":
            Hpoints += 1
    print(" ")
    print(" ")
    print("Once answering the question, the light grows and becomes little brighter.")
    print("*~,.,~* The light then seems to continue into the forest")
    print("A few feet more, into the woods, the light stops again.")
    print("*...*  The quiet voice comes back and says:")
    print("Now you must face a monster who threatens the lives of you, your loved ones, and the world.")
    print("Pick the best way to defeat the monster to save everyone:")
    print("")
    print("(A): The monster is only here for one person. I will get everyone to saftey before fighting the monster myself.")
    print("(B): The monster is not a monster. In fact, I've read all about it and some chamomile tea will calm it down.")
    print("(C): I will fight side by side with my friends to defeat the monster and save the world!")
    print("(D): There is a potion that can temporarily paralyze the monster. I've already made it.")
    Mon = (input("~,.~*,.~  "))
    if Mon=="a" or Mon=="A":
        Spoints += 1
    elif Mon =="B" or Mon=="b":
        Hpoints += 1
    elif Mon=="C" or Mon=="c":
        JRpoints += 1
    else:
        if Mon=="d" or Mon=="D":
            Opoints += 1
    print(" ")
    print(" ")
    print("Once answering the question, the light grows and becomes little brighter.")
    print("*~,.,~* The light then seems to continue into the forest")
    print("A few feet more, into the woods, the light stops again.")
    print("*...*  The quiet voice comes back and says:")
    print("Just a few more questions, you'll know soon.")
    print(" ")
    print("Suddenly, the forest seems to get brighter.")
    print("To your left is a stream.    To your right is a small hut.")
    print("In front of you but in the distance are mountains.")
    print("Behind you is a path.")
    print("*...*  The quiet voice says:")
    print("Make your choice as to how to proceed.")
    print("To the (s)tream, to the (h)ut, to the (m)ountains, or take the (p)ath?")
    Way = (input("~,.~*,.~  "))
    if Way=="p" or Way=="P":
        Spoints += 1
    elif Way=="s" or Way=="S":
        Opoints += 1
    elif Way=="m" or Way=="M":
        JRpoints += 1
    else:
        if Way=="h" or Way=="H":
            Hpoints += 1
    print(" ")
    print(" ")
    print("Once answering the question, the light grows and becomes little brighter.")
    print("The stream, the hut, the mountains, and the path disappear. The forest is just a forest")
    print("*~,.,~* The light then seems to continue into the forest")
    print("A few feet more, into the woods, the light stops again.")
    print("*...*  The quiet voice comes back and says:")
    print("Two more questions to go. What is your favorite class?")
    print("(D)efense Against the Dark Arts, (H)erbology, (Q)uidditch practice, or (D)ivination?")
    Class = (input("~,.~*,.~  "))
    if Class=="D" or Class=="d":
        Spoints += 1
    elif Class=="H" or Class=="h":
        Hpoints += 1
    elif Class=="Q" or Class=="q":
        JRpoints +=1
    else:
        if Class=="D" or Class=="d":
            Opoints += 1
    print(" ")
    print(" ")
    print("Once answering the question, the light grows and becomes little brighter.")
    print("*~,.,~* The light then seems to continue into the forest")
    print("A few feet more, into the woods, the light stops again.")
    print("*...*  The quiet voice comes back and says:")
    print("This is your last and final question ~ answer to life the universe and everything")
    print(" ")
    print("What is your purpose in life?")
    print("To (d)iscover, to (p)rotect, to (c)reate, to (a)chieve")
    Ans = (input("~,.~*,.~  "))
    if Ans=="d" or Ans=="D":
        Opoints += 1
    elif Ans=="P" or Ans=="p":
        Spoints += 1
    elif Ans=="C" or Ans=="c":
        Hpoints += 1
    elif Ans=="a" or Ans=="A":
        JRpoints += 1
    else:
        if Ans=="42":
            print("I see what you did there, but please put in a real answer.")
            ns = (input("~,.~*,.~  "))
            if ns=="d" or ns=="D":
                Opoints += 1
            elif ns=="P" or ns=="p":
                Spoints += 1
            elif ns=="C" or ns=="c":
                Hpoints += 1
            elif ns=="a" or ns=="A":
                JRpoints += 1
    print(" ")
    print("^, .~* ^_ ,. *")
    print(" ")
    if Spoints>Opoints and Spoints>JRpoints and Spoints>Hpoints:
        print("Your patronus is a Stag")
        print("Traditionally seen as ‘King of the Forest’, the stag is the protector of the other animals.")

    elif Opoints>Spoints and Opoints>JRpoints and Opoints>Hpoints:
        print("Your patronus is an Otter")
        print("An otter represents 'that which is hidden, unknown but necessary within the personality.'")
    elif JRpoints>Spoints and JRpoints>Opoints and JRpoints>Hpoints:
        print("Your patronus is a Jack Russel Terrier")
        print("Jack Russels represent loyalty and blind fearlessness.")
    elif Hpoints>Spoints and Hpoints>JRpoints and Hpoints>Opoints:
        print("Your patronus is a Hare")
        print("Hares represent being carefree and thoughts beyond imagination.")
    else:
        print("You are not ready to have a Patronus now. Thank you for taking the time to go on this journey.")

if __name__ == '__main__':
    play_hangman()
