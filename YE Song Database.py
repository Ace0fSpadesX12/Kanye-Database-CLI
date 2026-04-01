#Kanye West Discography Database
    ##By Sean James##
"""CLI tool that models a large nested data set, 
implements search and random sampling, 
and supports user interaction. 
Skills demonstrated: Python dictionaries, loops, 
functions, data validation, filtering, and JSON handling."""

import time
import random
import json
import sys

ye_discography = {
    "The College Dropout": {
        "Intro (Skit)" : {
            "Duration": 19,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],    #22 Song album
            "Sample" : [],                      #Release date 2004
            "Track Description" : [],
            "Track Number" : 1,
        },
        "We Don't Care" : {
            "Duration": 239,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west, miri ben-ari, ross vannelli"],
            "Producer(s)" : ["kanye west"],
            "Sample" : ["we don't care contains samples of 'I Just Wanna Stop' written by ross vannelli and performed by the jimmy castor bunch"],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Graduation Day" : {
            "Duration": 82,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west", "miri ben-ari", "john stephens"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "All Falls Down" : {
            "Duration": 223,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west", "lauryn hill"],
            "Producer(s)" : ["kanye west"],
            "Sample" : ["contains interpolations of lauryn hill's 'mystery of iniquity', performed here by syleena johnson."],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "I'll Fly Away" : {
            "Duration": 69,
            "Feature(s)" : [],
            "Writer(s)" : ["albert e. brumley"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Spaceship" : {
            "Duration": 324,
            "Feature(s)" : ["consequence", "glc"],
            "Writer(s)" : ["kanye west", "leonard harris", "dexter mills", 
                "marvin gaye", "gwen gordy fuqua", "sandra greene"],
            "Producer(s)" : "kanye west",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "Jesus Walks" : {
            "Duration": 193,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west", "che smith", "miri ben-ari",
                        "curtis lundy"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 7,
        },
        "Never Let Me Down" : {
            "Duration": 324,
            "Feature(s)" : ["jay-z", "j. ivy"],
            "Writer(s)" : ["kanye west", "shawn carter", "james richardson",
                        "michael bolton", "bruce kulick"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "Get Em High" : {
            "Duration" : 289,
            "Feature(s)" : ["talib kweli", "common"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "Workout Plan (Skit)" : {
            "Duration" : 46,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "The New Workout Plan" : {
            "Duration": 322,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 11,
        },
        "Slow Jamz" : {
            "Duration": 316,
            "Feature(s)" : ["twista", "jamie foxx"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 12,
        },
        "Breathe In Breath Out" : {
            "Duration": 246,
            "Feature(s)" : ["ludacris"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west", "Brian Miller"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 13,
        },
        "School Spirit (Skit)" : {
            "Duration": 78,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 14,
        },
        "School Spirit" : {
            "Duration": 182,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 15,
        },
        "School Spirit (Skit 2)" : {
            "Duration": 43,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 16,
        },
        "Lil Jimmy (Skit)" : {
            "Duration": 53,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 17,
        },
        "Two Words" : {
            "Duration": 266,
            "Feature(s)" : ["mos def", "freeway", "the boys choir of harlem"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 18,
        },
        "Through the Wire" : {
            "Duration": 221,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 19,
        },
        "Family Business" : {
            "Duration": 278,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],      
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 20,
        },
        "Last Call" : {
            "Duration": 760,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west", "michael Perretta", "tony Williams", "ken lewis"],
            "Producer(s)" : ["kanye west", "evidence"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 21,
        },
        "Heavy Hitters" : {
            "Duration": 235,
            "Feature(s)" : ["glc"],
            "Writer(s)" : ["kanye west", "leonard Harris"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 22,
        },
    },
    "Late Registration" : {
        "Wake Up Mr. west" : {
            "Duration": 41,
            "Feature(s)" : [],
            "Writer(s)" : ["michael masser", "gerry goffin"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Heard 'Em Say" : {
            "Duration": 203,
            "Feature(s)" : ["adam levine"],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west", "jon brion"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Touch the Sky" : {
            "Duration": 43,
            "Feature(s)" : ["lupe fiasco"],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],     #21 Song album.
            "Sample" : [],                        #Release date 2005
            "Track Description" : [],
            "Track Number" : 3,
        },
        "Gold Digger" : {
            "Duration": 207,
            "Feature(s)" : ["jamie foxx"],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "Skit No. 1" : {
            "Duration": 33,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Drive Slow" : {
            "Duration": 272,
            "Feature(s)" : ["glc", "paul wall"],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "My Way Home" : {
            "Duration": 103,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west", "lonnie Lynn", "gil-scott heron"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : ["Perfmored in it's entirety by common"],
            "Track Number" : 7,
        },
        "Crack Music" : {
            "Duration": 271,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "Roses" : {
            "Duration": 245,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "Bring Me Down" : {
            "Duration": 199,
            "Feature(s)" : ["brandy"],
            "Writer(s)" : [],
            "Producer(s)" : "kanye west",
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "Addiction" : { 
            "Duration": 267,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 11,
        },
        "Skit No. 2" : {
            "Duration": 31,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 12,
        },
        "Diamonds from Sierra Leone (Remix)" : {
            "Duration": 233,
            "Feature(s)" : ["jay-z"],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 13,
        },
        "We Major" : {
            "Duration" : 448,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 14,
        },
        "Skit No. 3" : {
            "Duration" : 33,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 15,
        },
        "Hey Mama" : {
            "Duration" : 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 16,
        },
        "Celebration" : {
            "Duration" : 42,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 17,
        },
        "Skit No. 4" : {
            "Duration" : 78,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 18,
        },
        "Gone" : {
            "Duration" : 333,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 19,
        },
        "Diamonds from Sierra Leone (Bonus Track)" : {
            "Duration" : 238,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 20,
        },
        "Late (Hidden Track)" : {
            "Duration" : 230,
            "Feature(s)" : [],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 21,
        },
    },
    "Graduation" : {
        "Good Morning" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Champion" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Stronger" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "I Wonder" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "Good Life" : {
            "Duration": 0,
            "Feature(s)" : ["t-pain"],
            "Writer(s)" : ["kanye west", "miri ben-ari", "john stephens"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Can't Tell Me Nothing" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "Barry Bonds" : {
            "Duration": 0,
            "Feature(s)" : ["lil wayne"],
            "Writer(s)" : ["kanye west", "miri ben-ari", "john stephens"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 7,
        },
        "Drunk and Hot Girls" : {
            "Duration": 0,
            "Feature(s)" : ["mos def"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "Flashing Lights" : {
            "Duration": 0,
            "Feature(s)" : ["dwele"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "Everything I Am" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "The Glory" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 11,
        },
        "Homecoming" : {
            "Duration": 0,
            "Feature(s)" : ["chris martin"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 12,
        },
        "Big Brother" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["dj toomp"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 13,
        },
        "Good Night" : {
            "Duration": 0,
            "Feature(s)" : ["al be back", "mos def"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 14,
        },
    },
    "808s & Heartbreaks" : {
        "Say You Will" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Welcome to Heartbreak" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Heartless" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "Amazing" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "Love Lockdown" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Paranoid" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "RoboCop" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 7,
        },
        "Street Lights" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "Bad News" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "See You in My Nightmares" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "Coldest Winter" : {
            "Duration": 0,
            "Feature(s)" : ["chris martin"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 11,
        },
        "Pinnocchio Story (Freestyle Live from Singapore) (Hidden Track)" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 12,
        }
    }
}

with open("ye_discography.json", "w") as f: 
    f.write(json.dumps(ye_discography, indent=4))

def feature_artist_search(album_filter= None):
    while True:    
        loop_again = ""
        searched_artist = input("Enter an artist to see if they've been featured on a Kanye West song: ").strip().lower()
        artist_found = False
        total_count = 0
        matches = []
        for album, track_list in ye_discography.items():
            for track, track_details in track_list.items():
                if searched_artist in track_details["Feature(s)"]:
                    artist_found = True
                    total_count += 1
                    matches.append([track, album])  #save each matching track and album
                    print(f"Kanye west has featured with {searched_artist} {total_count} times on the following song(s): \n{matches[0]}, from the album {album}.")

        if artist_found == False:
            print(f"Kanye West has not featured with {searched_artist} on any songs yet.")    
        while loop_again.lower() != "y" and loop_again.lower() != "n":
            loop_again = input("Do you want to search again? (y/n): ")
            if loop_again.lower() == "y":
                continue
            elif loop_again.lower() == "n":
                print("(back to main menu...)")
                main_menu()
            else:
                loop_again = input("Invalid input. Do you want to search again? (y/n): ")

def count_total_ye_songs():
    total_songs = 0
    for album_name, album_tracks in ye_discography.items():
        for song, details in album_tracks.items():
            total_songs += 1
    return total_songs

def random_ye_generator(): 
    while True:
        random_album = random.choice(list(ye_discography.keys()))
        random_track = random.choice(list(ye_discography[random_album].keys()))
        try:
            while "skit" in random_track.lower():
                random_track = random.choice(list(ye_discography[random_album].keys()))
            print(f"Your random Kanye West song is {random_track} from the album {random_album}")
        except IndexError:
            print("Search Error. Please try again.")      
        loop_again = input("Do you want to search again? (y/n): ")
        if loop_again.lower() == "y":
            continue
        elif loop_again.lower() == "n":
            print("(back to main menu...)")
            break
        else:
            print("Invalid input. Please try again.")

def introduction(count_total_ye_songs): 
    for x in range (3):
        print("Initializing Kanye West Song Database...")
        time.sleep(.5)
    print(f"Welcome to the most (prospective) extensive kanye west database on the web. Host of a whopping {count_total_ye_songs} songs across his discography!")
    input("...Press Enter to log in...")

album_alias_titles = {
    "The College Dropout" : {
        "Song Count" : 22,
        "Album Nicknames" : ["tcd", "1", "#1","college dropout", "1st", "dropout", "the college dropout"],
    },
    "Late Registration" : {
        "Song Count" : 21,
        "Album Nicknames" : ["lr", "late registration", "2", "#2", "late reg", "2nd"],
    },
    "Graduation" : {
        "Song Count" : 16,
        "Album Nicknames" : ["grad", "3", "#3", "graduation", "3rd"],
    },
}

def main_menu():
    while True:
        print("Your options in program are: \nRandom Generator \nTrack Search \nCollab Search \nExit")
        user_choice = input("What is your selection? ")
        if user_choice == "Random Generator".strip().lower():
            random_ye_generator()
        elif user_choice == "Exit".lower().strip():
            for x in range (3):
                print("Exiting Kanye West Song Database..")
                time.sleep(0.9)
            print("He made Graduation...")
            sys.exit()
        elif user_choice == "track Search".lower().strip():
            track_search()
        elif user_choice == "collab Search".lower().strip():
            feature_artist_search()
        else:
            #print("Invalid selection. Please select again.")
            invalid_flvr_txt()

def invalid_flvr_txt():
    redo = ["Error. Please try again.", "Invalid input. Please try again.",
        "Please enter a valid input."]
    flv_txt = random.choice(redo)
    print(flv_txt) 

def album_choice():
    while True:
        album_choice = input("Please enter a Kanye West album to index: ").strip().lower()
        for album, info in album_alias_titles.items():
            if album_choice in info["Album Nicknames"]:
                print(f"You've selected the album: {album}, with a total of {info['Song Count']} songs.")
                return album , info["Song Count"]
        else:
            print("Album not found. Please try again.")
                

def song_choice(chosen_album, song_count):
    if chosen_album in ye_discography.keys():
        while True:
            song_choice = int(input("Please enter a track number from the album to index: "))
            for song, info in ye_discography[chosen_album].items():
                if song_choice == info["Track Number"]:
                    print(f"You've selected the song: {song}, with a duration of {info['Duration']} seconds.")
                    return song
            else:
                print(f"Out of index range. There are only {song_count} on this album! Please try again.")

def track_search():
    chosen_album, song_count = album_choice()
    song_choice(chosen_album, song_count)
    main_menu()




#Start_of_Run_Process

introduction(count_total_ye_songs())
main_menu()










#print(f"Kanye west has featured with {searched_artist} {total_count} times on the following song(s): \n{track}, from the album {album}.")






















































































