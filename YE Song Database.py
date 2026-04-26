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
            "Writer(s)" : ["kanye west", "miri ben-ari", "ross vannelli"],
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
            "Producer(s)" : ["kanye west"],
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
            "Sample" : ["contains excerpts of 'Someone That I Used to Love' by natalie cole"],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Heard 'Em Say" : {
            "Duration": 203,
            "Feature(s)" : ["adam levine"],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west", "jon brion"],
            "Sample" : ["contains excerpts of 'Someone That I Used to Love' by natalie cole"],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Touch the Sky" : {
            "Duration": 43,
            "Feature(s)" : ["lupe fiasco"],
            "Writer(s)" : [],
            "Producer(s)" : ["kanye west"],     #21 Song album.
            "Sample" : ["contains samples of 'move on up' as performed by curtis mayfield"],                        #Release date 2005
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
            "Track Description" : ["Performed in it's entirety by common"],
            "Track Number" : 7,
        },
        "Crack Music" : {
            "Duration": 271,
            "Feature(s)" : ["The Game"],
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
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 13,
        },
        "We Major" : {
            "Duration" : 448,
            "Feature(s)" : ["nas", "really doe"],
            "Writer(s)" : ["kanye west"],
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
            "Feature(s)" : ["consequence", "common"],
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
            "Writer(s)" : ["kanye west", "elton john", "bernie taupin"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Champion" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west", "antony williams", "walter becker", "donald fagen"],
            "Producer(s)" : ["kanye west", "brian 'allday' miller"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Stronger" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west", "mike dean"],
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
            "Producer(s)" : ["kanye west", "dj toomp", "mike dean"],
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
            "Feature(s)" : ["kid cudi"],
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
            "Feature(s)" : ["young jeezy"],
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
            "Feature(s)" : ["mr hudson"],
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
            "Feature(s)" : ["lil wayne"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "Coldest Winter" : {
            "Duration": 0,
            "Feature(s)" : [],
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
    },
    "My Beautiful Dark Twisted Fantasy" : {
        "Dark Fantasy" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Gorgeous" : {
            "Duration": 0,
            "Feature(s)" : ["kid cudi", "raekwon"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Power" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "All of the Lights (Interlude)" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "All of the Lights" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Monster" : {
            "Duration": 0,
            "Feature(s)" : ["jay-Z", "rick ross", "nicki minaj", "bon iver"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "So Appalled" : {
            "Duration": 0,
            "Feature(s)" : ["swizz beatz", "jay-z", "pusha t", "cyhi the prynce" ],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 7,
        },
        "Devil in a New Dress" : {
            "Duration": 0,
            "Feature(s)" : ["rick ross"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "Runaway" : {
            "Duration": 0,
            "Feature(s)" : ["pusha t"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "Hell of a Life" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "Blame Game" : {
            "Duration": 0,
            "Feature(s)" : ["john legend"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 11,
        },
        "Lost in the World" : {
            "Duration": 0,
            "Feature(s)" : ["bon iver"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 12,
        },
        "Who Will Survive in America" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 13,
        }
    },
    "Yeezus" : {
        "On Sight" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Black Skinhead" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "I Am a God" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "New Slaves" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "Hold My Liquor" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "I'm in It" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "Blood on the Leaves" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 7,
        },
        "Guilt Trip" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "Send it Up" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "Bound 2" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        }
    },
    "The Life of Pablo" : {
        "Ultralight Beam" : {
            "Duration": 0,
            "Feature(s)" : ["chance the rapper"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Father Stretch My Hands, Pt. 1" : {
            "Duration": 0,
            "Feature(s)" : ["kid cudi", "kelly price"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Pt. 2" : {
            "Duration": 0,
            "Feature(s)" : ["desiigner"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "Famous" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "Feedback" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Low Lights" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "Highlights" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 7,
        },
        "Freestyle 4" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "I Love Kanye" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "Waves" : {
            "Duration": 0,
            "Feature(s)" : ["chris brown"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "FML" : {
            "Duration": 0,
            "Feature(s)" : ["the weeknd"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 11,
        },
        "Real Friends" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 12,
        },
        "Wolves" : {
            "Duration": 0,
            "Feature(s)" : ["vic mensa", "sia"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 13,
        },
        "Frank's Track" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : ["Performed in it's entirety by Frank Ocean"],
            "Track Number" : 14,
        },
        "Siiiiiiiiilver Surffffeeeeer Intermission" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 15,
        },
        "30 Hours" : {
            "Duration": 0,
            "Feature(s)" : ["andre 3000"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 16,
        },
        "No More Parties in LA" : {
            "Duration": 0,
            "Feature(s)" : ["kendrick lamar"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 17,
        },
        "Facts (Charlie Heat Version)" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 18,
        },
        "Fade" : {
            "Duration": 0,
            "Feature(s)" : ["post malone", "ty dolla sign"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 19,
        },
        "Saint Pablo" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 20,
        }
    },
    "Ye" : {
        "I Thought About Killing You" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Yikes" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "All Mine" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "Wouldn't Leave" : {
            "Duration": 0,
            "Feature(s)" : ["partynextdoor"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "No Mistakes" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Ghost Town" : {
            "Duration": 0,
            "Feature(s)" : ["partynextdoor", "070 shake", "kid cudi"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "Violent Crimes" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 7,
        }
    },
    "Jesus is King" : {
        "Every Hour" : {
            "Duration": 0,
            "Feature(s)" : ["sunday service choir"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 1,
        },
        "Selah" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 2,
        },
        "Follow God" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 3,
        },
        "Closed On Sundays" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 4,
        },
        "On God" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 5,
        },
        "Everything We Need" : {
            "Duration": 0,
            "Feature(s)" : ["ty dolla sign", "ant clemons"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 6,
        },
        "Water" : {
            "Duration": 0,
            "Feature(s)" : ["ant clemons"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 7,
        },
        "God Is" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 8,
        },
        "Hands On" : {
            "Duration": 0,
            "Feature(s)" : ["fred hammond"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 9,
        },
        "Use This Gospel" : {
            "Duration": 0,
            "Feature(s)" : ["clipse", "kenny g"],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 10,
        },
        "Jesus is Lord" : {
            "Duration": 0,
            "Feature(s)" : [],
            "Writer(s)" : ["kanye west"],
            "Producer(s)" : ["kanye west"],
            "Sample" : [],
            "Track Description" : [],
            "Track Number" : 11,
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
                    matches.append((track, album))  #save each matching track and album
        if artist_found:
            print(f"Kanye west has featured with {searched_artist.title()} {total_count} time(s) on the following song(s): ")
            for track, album in matches:
                print(f"{track}, from the album {album}.")          
            #print(f"Kanye west has featured with {searched_artist} {total_count} times on the following song(s): \n{matches}, from the album {album}.")
        elif artist_found == False and searched_artist.lower().strip() == "kanye west" or searched_artist == "ye":
            print("Kanye West has featured with Kanye West on ALL songs!")
        elif artist_found == False:
            print(f"{searched_artist.title()} has not featured with Kanye West on any songs yet.")    
        while loop_again.lower() != "y" and loop_again.lower() != "n":
            loop_again = input("Do you want to search again? (y/n): ").strip().lower()
            if loop_again.lower() == "y":
                continue
            elif loop_again.lower() == "n":
                print("(back to main menu...)\n")
                main_menu()
            else:
                loop_again = input("Invalid input. Do you want to search again? (y/n): ").strip().lower()

def count_total_ye_songs():
    total_songs = 0
    for album_name, album_tracks in ye_discography.items():
        for song, details in album_tracks.items():
            total_songs += 1
    return total_songs

total_ye_songs = count_total_ye_songs()

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
        print("Initializing YeTabase...")
        time.sleep(.5)
    print(f"Welcome to the most (prospective) extensive Kanye West database on the web. Host to a whopping {count_total_ye_songs} songs across his discography!")
    input("...Press Enter to log in...")

album_alias_titles = {
    "The College Dropout" : {
        "Song Count" : 22,
        "album nicknames" : ["tcd", "1", "#1","college dropout", "tcdo", "1st", "1st album", "dropout", "the college dropout"],
    },
    "Late Registration" : {
        "Song Count" : 21,
        "album nicknames" : ["lr", "late registration", "late", "reg", "2", "#2", "late reg", "2nd album", "2nd"],
    },
    "Graduation" : {
        "Song Count" : 14,
        "album nicknames" : ["grad", "3", "#3", "graduation", "3rd", "3rd album"],
    },
    "808s & Heartbreaks" : {
        "Song Count" : 12,
        "album nicknames" : ["808s & heartbreaks", "4", "#4", "808s and heartbreaks", "808s", "heartbreaks", "4th album", "4th", "808", "hb"],
    },
    "My Beautiful Dark Twisted Fantasy" : {
        "Song Count" : 16,
        "album nicknames" : ["my beautiful dark twisted fantasy", "twisted fantasy", "5", "#5", "5th album", "dark fantasy", "5th", "mbdtf", "dtf", "tf"],
    },
    "Yeezus" : {
        "Song Count" : 13,
        "album nicknames" : ["yeezus", "6", "#6", "6th", "6th album"],
    },
    "The Life of Pablo" : {
        "Song Count" : 20,
        "album nicknames" : ["the life of pablo", "7", "7th", "tlop", "pablo", "life of pablo", "7th album"],
    },
    "Ye" : {
        "Song Count" : 7,
        "album nicknames" : ["ye", "8", "8th", "8th album"],
    },
    "Jesus is King" : {
        "Song Count" : 11,
        "album nicknames" : ["jesus is king", "9", "9th", "9th album", "jik"],
    },
    "Donda" : {
        "Song Count" : 32,
        "album nicknames" : ["donda", "10", "10th", "10th album"],
    },
}

#Shorthand album titles
TCD = album_alias_titles["The College Dropout"]["album nicknames"]
LR = album_alias_titles["Late Registration"]["album nicknames"]
Graduation = album_alias_titles["Graduation"]["album nicknames"]
_808s = album_alias_titles["808s & Heartbreaks"]["album nicknames"]
MBDTF = album_alias_titles["My Beautiful Dark Twisted Fantasy"]["album nicknames"]
Yeezus = album_alias_titles["Yeezus"]["album nicknames"]
TLOP = album_alias_titles["The Life of Pablo"]["album nicknames"]
Ye = album_alias_titles["Ye"]["album nicknames"]
JIK = album_alias_titles["Jesus is King"]["album nicknames"]
DONDA = album_alias_titles["Donda"]["album nicknames"]


def main_menu():
    while True:
        print("Your options in program are as follows: \n\n1.) Random Generator - Generates a random Kanye West song of the day \n2.) Track Search - Search for a song by track number from different Kanye West albums for details on it \n3.) Collab Search - Search to see how many times a specific artist has worked with Kanye West \n4.) Trivia Mode - Play a trivia game to see how well you know Kanye West \n5.) Exit Program - Terminate runtime")
        user_choice = input("\nWhat is your selection? ").strip().lower()
        if user_choice == "Random Generator".strip().lower() or user_choice == "1":
            random_ye_generator()
        elif user_choice == "track Search".lower().strip() or user_choice == "2":
            song_search(album_choice())
        elif user_choice == "collab Search".lower().strip() or user_choice == "3":
            feature_artist_search()
        elif user_choice == "trivia mode".lower().strip() or user_choice == "4":
            trivia_mode()
        elif user_choice == "Exit".lower().strip() or user_choice == "5":
            for x in range (3):
                print("Exiting Kanye West Song Database..")
                time.sleep(0.9)
            print("He made Graduation...")
            sys.exit()
        else:
            #print("Invalid selection. Please select again.")
            invalid_flvr_txt()

def invalid_flvr_txt():
    redo = ["Error. Please try again.", "Invalid input. Please try again.",
        "Please enter a valid input."]
    flv_txt = random.choice(redo)
    print(flv_txt) 

def album_choice():
    search_again = True
    while search_again:
        album_choice = input("Please enter a Kanye West album to search through: ").strip().lower()
        found = False
        for album, info in album_alias_titles.items():
            if album_choice in info["album nicknames"]:
                print(f"You've selected the album: {album}, with a total of {info['Song Count']} songs.\n")
                search_again = False
                found = True
                selected_album, details = album, info
                break
        if not found:
            print("Album not found. Please try again.") 

    tracklists = ye_discography[selected_album]

    #print(tracklists, details)

    for n, song in enumerate(tracklists, start=1):
        print(str(n) + ".", song)
    
    song_query = int(input("\nEnter the song number you would like details for: "))

    selected_song = None

    for song_name, song_data in tracklists.items():
        if song_data["Track Number"] == song_query:
            selected_song = (song_name, song_data)
            break
    
    while True:
        if selected_song:
            name, data = selected_song
            print(f"\n🎵 {name}")
            print(f"Track Number: {data['Track Number']}")
            print(f"Duration: {data['Duration']} seconds")
            print(f"Features: {', '.join(data['Feature(s)']).title().strip() or 'None'}")
            print(f"Writers: {', '.join(data['Writer(s)']).title().strip()}")
            print(f"Producers: {', '.join(data['Producer(s)']).title().strip()}")
            print(f"Samples: {', '.join(data['Sample']) or 'None'}")
            print(f"Track Description: {', '.join(data['Track Description']).title().strip() or 'None'}")
            break
        else:
            print("Song not found.")
        
    main_menu()
    

def song_search(album_choice):
    chosen_album = album_choice([0])
    for album, tracklists in ye_discography.items():
        for tracklist, details in tracklists.items():
            if album == chosen_album:
                print(tracklist, details["Track Number"], details["Song Title"], details["Feature(s)"])

def trivia_mode():    
    current_score = 0
    hi_score = {"high score": 0}
    trivia_list = []

    with open("Trivia_High_Score.json", "r") as f:
        hi_score = json.load(f)
    
    for album, songs in ye_discography.items():
        for song in songs.keys():
            trivia_list.append([album, song])
    
    print("Try to answer which albums a set of Kanye West songs are from. Can you complete his entire discography?")
    print("You can guess using full album names or abbreviations (e.g., TCD, LR, Graduation, 808s, MBDTF, Yeezus, TLOP, etc.")
    print("*" * 10)
    
    if hi_score.get("high score", 0) > 0:
        print(f"Your current high score is: {hi_score['high score']}.")
    
    while current_score < total_ye_songs:
        trivia_item = random.choice(trivia_list)
        trivia_album, trivia_question = random.choice(trivia_list)
        player_answer = input(f"Which Kanye West album is the song {trivia_question} from? ").lower().strip()

        if player_answer in TCD and trivia_album == "The College Dropout":
            current_score += 1
            trivia_list.remove(trivia_item)
            print(f"Correct! Score: {current_score}")
        elif player_answer in LR and trivia_album == "Late Registration":
            current_score += 1
            trivia_list.remove(trivia_item)
            print(f"Correct! Score: {current_score}")
        elif player_answer in Graduation and trivia_album == "Graduation":
            current_score += 1
            trivia_list.remove(trivia_item)
            print(f"Correct! Score: {current_score}")
        elif player_answer in _808s and trivia_album == "808s & Heartbreaks":
            current_score += 1
            trivia_list.remove(trivia_item)
            print(f"Correct! Score: {current_score}")
        elif player_answer in MBDTF and trivia_album == "My Beautiful Dark Twisted Fantasy":
            current_score += 1
            trivia_list.remove(trivia_item)
            print(f"Correct! Score: {current_score}")
        elif player_answer in Yeezus and trivia_album == "Yeezus":
            current_score += 1
            trivia_list.remove(trivia_item)
            print(f"Correct! Score: {current_score}")
        elif player_answer in TLOP and trivia_album == "The Life of Pablo":
            current_score += 1
            trivia_list.remove(trivia_item)
            print(f"Correct! Score: {current_score}")
        elif player_answer in Ye and trivia_album == "Ye":
            current_score += 1
            trivia_list.remove(trivia_item)
            print(f"Correct! Score: {current_score}")
        elif player_answer in JIK and trivia_album == "Jesus Is King":
            current_score += 1
            trivia_list.remove(trivia_item)
            print(f"Correct! Score: {current_score}")
        else:
            print(f"Oops! {trivia_question} is actually from the album {trivia_album}.")
            print(f"Game Over! Your score was {current_score} out of a possible {total_ye_songs}. Better luck next time!\n")            
            if current_score > hi_score['high score']:
                    with open("Trivia_High_Score.json", "w") as f:
                        json.dump({"high score": current_score}, f)
            break        
        if current_score == total_ye_songs:
            print(f"Congratulations! You're a Kanye West superfan! You got all {current_score} songs out of a possible {total_ye_songs}.")
            if current_score > hi_score['high score']:
                with open("Trivia_High_Score.json", "w") as f:
                    json.dump({"high score": current_score}, f)
            break

#Start_of_Run_Process
introduction(count_total_ye_songs())
main_menu()

#total = 0
#for song in ye_discography["Yeezus"].keys():
#  total += 1
#  print(str(total)+".", song)  #Detailed track details tentative


#py -m PyInstaller --onefile "Ye Song Database.py" Future turn to exe command 


#for album, tracklist in ye_discography.items():
   # for song, song_details in tracklist.items():
  #      if album == "Ye": 
 #           print(song)



































































