
################ LIST OF OPTIONS #################
moods= ["Happy" , "Sad" ,  "Energized" , "Calm", "Nostalgic"]
genres = ["Pop", "Emo", "Indie", "R&B", "K-pop", "Rap" ]

############### LIST OF RECS BASED ON PRIOR CHOICE ###########################
happy_songs = ["As It Was- Harry Styles" , "New Romantics - Taylor Swift" , "Classic - MKTO"]
sad_songs = ["Heather - Conan Gray" , "Favorite Crime - Olivia Rodrigo", "Cailings- Lizzy McAlpine"]
energized_songs =["Shake It Off- Taylor Swift", "Uptown Funk- Bruno Mars", "Sorry- Justin Bieber"]
calm_songs = ["Love Song- Lana Del Rey", "Home - Wave to Earth", "Blue- Billie Eilish"]
nostalgic_songs = ["Ribs- Lorde", "We Are Young- fun.", "Feel This Moment- Pitbull"]

pop_songs = ["Good Luck Babe- Chapell Roan", "Lunch- Billie Eilish", "Taste- Sabrina Carpenter"]
emo_songs = ["Decode- Paramore", "If I'm James Dean You're Audrey Hepburn- Sleeping With Sirens","Gold Medal Ribbon - Pierce The Veil" ]
indie_songs = ["Where is My Mind?- The Pixies", "Someday- The Strokes", "Mardy Bum- Arctic Monkeys"]
rb_songs = ["No DIggity- Blackstreet", "Family Affair- Mary J. Blige", "If I Aint Got You- Alicia Keys"]
kpop_songs =["Home- BTS", "Miniskirt- AOA", "Chaconne- Enhypen"]
rap_songs = ["I Know ?- Travis Scott", "Bartier Cardi- Cardi B", "Power Trip- J.Cole"]


################### START OF PROGRAM ############################

choices = ["genre", "mood"]

def mood_or_genre(choice):             # defines the function mood_or_genre based on the chosen argument, in this case mood or genre 
        if choice == "mood":
            while True:                #this loop will make sure the program runs until the user instructs it to stop 
                mood_ask = input("Would you like to hear something happy, sad, energized, or calm? ").lower()   #asks for user input to be stored in a variable
                if mood_ask == "happy":
                    print(f'Here are some recommendations:{happy_songs}')  #prints the correct list dependent on users selected choice
                    break                 #this will stop this particular section of code from continuing 
                    
                elif mood_ask == "sad":   
                    print(f'Here are some recommendations: {sad_songs}') ##prints the correct list dependent on users selected choice
                    break                  # #this will stop this particular section of code from continuing 

                elif mood_ask == "energized":
                    print(f'Here are some recommendations: {energized_songs}') ##prints the correct list dependent on users selected choice
                    break               # #this will stop this particular section of code from continuing 

                elif mood_ask == "calm":
                    print(f'Here are some recommendations: {calm_songs}')  ##prints the correct list dependent on users selected choice
                    break               # #this will stop this particular section of code from continuing 

                else:                  #if the user enters a choice not listed....
                    print("Please select a valid mood choice.")  #this will print and continue the code, asking them to retry (since there is no break statement)
     
        if choice == "genre":      #the previous process will repeat for this next choice with different options
            while True: 
                genre_ask = input("Would you like to hear something in the Pop, Emo, Indie, R&B, K-pop, or Rap genre? ").lower()
                if genre_ask == "pop":
                    print(f'Here are some recommendations:{pop_songs}')
                    break

                elif genre_ask == "emo":
                    print(f'Here are some recommendations: {emo_songs}')
                    break

                elif genre_ask == "indie":
                    print(f'Here are some recommendations: {indie_songs}')
                    break

                elif genre_ask == "r&b":
                    print(f'Here are some recommendations: {rb_songs}')
                    break

                elif genre_ask == "k-pop":
                    print(f'Here are some recommendations: {kpop_songs}')
                    break
                
                elif genre_ask == "rap":
                    print(f'Here are some recommendations: {rap_songs}')
                    break
                
                else:
                     print("Please select a valid genre choice.")


mood_or_genre(input("Welcome to the Music Recommendation Tool! Would you like recommendations based on genre or mood? ").lower())  #This invokes the function, asking the primary question at the start of the code.
    

while True:                   #This will run constantly until indicated to stop by the user
    more_recs= input("Would you like more recommendations?: Y/N " ).lower()    #stores user input into a variable 
    if more_recs == 'y':
        mood_or_genre(input("Would you like recommendations based on genre or mood? ").lower())  #This will restart the program if the user selects that they want to continue
    elif more_recs == 'n':
        print("Thank you for your time. I hope you enjoy your recommendations!") 
        break  #if the user selects that they do not want to continue, the program will stop and print a farewell message.
    else:
        print("Please enter a valid choice.")   # if the user selects an option not listed,this will print and continue the code, asking them to retry (since there is no break statement)
