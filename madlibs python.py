while True:
    print("0----MADLIBS----0 ")
    gamemode = input("select gamemode(1, 2, 3): ")

    if gamemode == str(1):

         print("This is (adjective)! I wish I could (verb) those guys! (name) sure is such a guy, I'm telling you. Too bad they lost their (body part). Perhaps you could send your condolences to them by sending them (object). If you're planning on visiting them, you could try going to (place).")

         adj = input("enter  an adjective: ")
         verb = input("enter a verb: ")
         name = input("enter a name: ")
         body_part = input("enter a name of a body part: ")
         object = input("enter an object: ")
         place = input("enter a place: ")

         madlib = f"This is {adj}! I wish I could {verb} those guys! {name} sure is such a nice guy, I'm telling you. Too bad they lost their {body_part}. Perhaps you could send your condolences to them by giving them {object}."
         print(madlib)



    elif gamemode == str(2):
        print("Today, I went to (place), it was (adj)! I met (name), (name2), and (name3) in my time there. I told them that I bought (object). The sad part is that I hurt my (body part) in the process of buying that said item. Anyway, I told them that I'm going to go (verb) with my sister so I said my goodbye to them.")

        place = input("enter a place: ")
        adj = input("enter an adjective: ")
        name1 = input("enter a name: ")
        name2 = input("enter another name: ")
        name3 = input("enter a final name: ")
        obj = input("enter an object: ")
        body_part = input("enter a body part: ")
        verb = input("enter a verb: ")

        madlib2 = f"Today, I went to {place}, it was {adj}! I met {name1}, {name2}, and {name3} in my time there. I told them that I bought {obj}. The sad part is that I hurt my {body_part} in the process of buying that said item. Anyway, I told them that I'm going to go {verb} with my sister so I said my goodbye to them."
        print(madlib2)


    elif gamemode == str(3):
        print("I remember being in (place), and suddenly a person wearing (clothing) approaches me and asks me a question about (noun or verb). I was (adjective) and don't know how to respond to that. The person touched my (body_part) and told me a story I forgot what's it about, then they left me with (object) for me to keep.")


        place = input("enter a place: ")
        clothing = input("enter a name of clothing: ")
        noun_verb = input("enter a noun or a verb: ")
        adj = input("enter an adjective: ")
        body_part = input("enter a body part: ")
        obj = input("enter an object: ")


        madlib3 = f"I remember being in {place}, and suddenly a person wearing {clothing} approaches me and asks me a question about {noun_verb}. I was {adj} and don't know how to respond to that. The person touched my {body_part} and told me a story I forgot what's it about, then they left me with {obj} for me to keep."
        print(madlib3)

    elif gamemode != [str(1), str(2), str(3), "easteregg", "easter egg"]:
        print("Enter 1, 2 or 3 to select gamemode!")

    elif gamemode == "easteregg" or "easter egg":
        print("Congratulations, you have discovered an easter egg")
        print("Did you know: the first video game to ever had an easter egg is the 1979 game Adventure for the Atari 2600 created by Warren Robinett. A 15-year-old Adam Clayton was the first player to ever discover it!")



    


    

    


    

