# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Player = Character("You")
define Goth = Character("Jessie")
define Jock = Character("Noah")
define Mascot = Character("Mascot")

define Pres = Character("College President")

default Goth_Mod = 0
default Jock_Mod = 0
default Mascot_Mod = 0

image mascot:
    "mascot_sample.jpg"
    zoom 0.5
image goth:
    "goth_1.jpg"
    zoom 0.5
image jock:
    "jock_1.jpg"
    zoom 0.5

#Choice_Failure Affects Mascot Reassurance Dialogue (Debating Implementation)

default Choice_Failure = 0

# The game starts here.

label start:

    if persistent.reload:
        $ Goth_Mod = persistent.Goth_Point
        $ Jock_Mod = persistent.Jock_Point
        $ Mascot_Mod = persistent.Mascot_Point
        $ del(persistent.Goth_Point)
        $ del(persistent.Jock_Point)
        $ del(persistent.Mascot_Point)
        $ persistent.Goth_Point = 0
        $ persistent.Jock_Point = 0
        $ persistent.Mascot_Point = 0
        $ del(persistent.reload)
        $ persistent.reload = False
    
    else:
        $ persistent.Goth_Point = 0
        $ persistent.Jock_Point = 0
        $ Goth_Mod = 0
        $ Jock_Mod = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene auditorium

    play music "FoL_Neutral.wav"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "(Today…is the first day of my college career.)"

    "(Well, to be exact, it’s orientation day, so I’m currently not doing anything besides being bored out of my mind by speeches.)"

    Pres "Good morning all! It is my highest pleasure to welcome you all to SCHOOL NAME and have you join the MASCOT NAME family."

    Pres "For those of you on campus for the first time today, please take pride in having been chosen to join one of the nation’s most passionate universities…"

    "(...Right. To be honest, this is one of the only schools that would even accept me with my slightly above average high school grades and no extracurriculars.)"

    "(It seems to have a bit of a…reputation, from what I read online, but I took what I could get.)"

    Pres "…I know that you all may be feeling quite intimidated right now! Rest assured, as our campus community and faculty are an incredibly welcoming and diverse group that are excited to meet new MASCOT NAME(s)!"

    "(Looking around the cafeteria, there are some faculty off to the side near the stage, and the orientation leaders on the other.)"

    show mascot

    "(There’s also the school mascot on the stage…to be honest, it creeps me out a little, but it’s mostly confusing. I mean, who chooses a cupid as a college mascot?)"

    Mascot "GOOOO SCHOOL/MASCOT NAMES~! I’m absolutely de–light–ed to meet you all!"

    hide mascot

    "(Yeah, I get why this school has a reputation.)"

    "(In the audience area, there are actually a few people that I recognize from high school, but I’ve never been too close with any of them.)"

    "(It’s not that I don’t like talking to people…but I’ve never liked approaching anyone first.)"

    "(I’m not sure if they would remember me, either.)"

    "(Tired of hearing about how SCHOOL NAME was the number one best most greatest college in the world, I tap my fingers on the edge of the seat and end up staring at a random corner of the ceiling.)"

    "(I could be home playing video games right now…)"

    "Sigh…"

    "(To be honest, I’d woken up this morning thinking that maybe I’d be a little different today. That maybe something exciting or life-changing would happen)"

    "(Everyone was always hyping up college as the best time of your life, but I’d probably end up spending it the exact same way I’d spent high school at this rate.)"

    "(Now that I’m thinking about it…)"

    "(When faced with the decision of what major to apply for, I’d just chosen ‘undeclared’ without a second thought.)"

    "(At this point, I’m as unremarkable as possible.)"

    "(But maybe...)"

    Pres "…and as you explore campus today, keep in mind the many amazing opportunities waiting for you and create your own unique self!"

    "(The sound of the audience clapping brings me back to the present. Seems like the speech is almost over.)"

    Pres " Keep an eye out for MASCOT NAME as you look around—feel free to take photos and ask for advice!"

    show mascot

    Mascot "I’m alwaaaays happy to help! ^-^"

    hide mascot

    Pres "With that, we will begin the tour in half an hour. In the meantime, please take this opportunity to get to know your fellow students!"

    "(The audience applauds again, and the president and mascot leave the stage. The people around me begin to get up from their seats and disperse.)"

    "(I get up, too, though I have no idea where I’m going.)"

    "(I try to peek my head up above the crowd. It seems like they’re serving free breakfast, so I start heading in that direction.)"

    "(30 minutes to kill…I could probably just sit at some random table and eat by myself.)"

    "(On my way to the food line, I scan the tables for a good place to sit.)"

    "(There’s some people who have already seemed to form their groups—some jock-looking guys are being particularly loud, there’s even a couple sitting close together…though there’s a few people alone, too.)"

    "(!)"

    show goth

    Goth "…"

    "(Accidentally caught the eye of that girl in the corner. I don’t think I want to sit near her.)"

    hide goth
    
    "(I turn my gaze back in the other direction, and just as I’m about to join the line—)"

    show mascot

    Mascot "Helloooooo there, my little cherub! How are you doing on this lovely, fateful morning?"

    "(!)"

    "(I stumble back and nearly bump into someone else. I hadn’t seen that weird mascot approaching at all!)"

    "(Up close, I notice… description when we have the design)"

    Mascot "Are you alright there? Sorry if I scared you~"

    "I–I’m fine, thanks."

    "(I turn to take my leave, but the mascot blocks my path.)"

    Mascot "Are you sure you’re doing okay? You’re looking a little down. If there’s anything at all I can help with, just ask!"

    "I’m okay, just heading to—"

    "Oh! I just remembered. Give me a moment, there’s something realllllly important I need to give you!"

    "(Before I can move away, an object is shoved into my field of vision.)"

    "Here’s your extra-special SCHOOL NAME planner! For free! It’s always important to write things down so you don’t forget them."

    "Oh!…thanks."

    "(I take it and examine the cover. It’s bright pink, of course, with large white lettering across the front and red hearts drawn everywhere.)"

    "Go ahead and write your name on it!"

    "(The mascot hands me a pen from seemingly nowhere, and I scribble my name down in hopes that it will leave me alone.)"

    $ Player.name = renpy.input("What is your name?")
    
    Mascot "[Player.name]! It’s so nice to meet you and welcome you to our lovely campus! Will you be coming to our upcoming fall festival?"

    Player "Uhhh…"

    "(The mascot flips the planner open and points to a date about a month from now, where something has already been written in messy handwriting—along with more cutesy red hearts.)"

    Mascot "Our Fall Festival of Fate! Our most popular and important event of the year! Bring your date to the festival and ensure that you two will hold true love forevermore—or as the rumors say~ ♡"

    Player "A…date?"

    "(Romance is literally the last thing on my mind right now.)"

    Mascot "Of course! This is the absolute perfect time for a young person such as yourself to get out there and find your true love."

    Mascot "Haven’t you ever been in love, [Player.name]?"

    # Create Choice

    Mascot "In any case, you simply must attend the festival with someone special! A once-in-a-lifetime opportunity to find your fated true love is too good to pass up, isn’t it?"

    Player "I’ll…think about it."

    Mascot "I’ll see you there, then, [Player.name]! ^-^"

    Mascot "Any burning questions for me before I leave you to your adventure?"

    # Create Choice

    Player "No, I'm fine."
    
    Mascot "Thennnnn you better start talking to everyone! Don’t forget to use your planner! And if you see me around anytime, come say hi~"

    hide mascot

    "(The mascot disappears as quickly as it appeared.)"

    Player "Whew…"

    "(That was way too fast-paced for me. True love? Fate? I mean, I guess it’s what you might expect from a cupid, but still…)"

    "(It’s not like I was suddenly going to get a date in a month! Right?)"

    "(Right…so why am I actually thinking about it?)"

    "(I look back at the planner in my hands, still open to the festival date.)"

    "(Maybe this is what I’ve been waiting for…)"

    "Choose Where"
    
    menu:

        "Hallway":

            jump Goth_1

        "Cafeteria":

            jump Jock_1

label Goth_1:

    scene hallway

    if persistent.reload:
        $ Goth_Mod = persistent.Goth_Point
        $ Jock_Mod = persistent.Jock_Point
        $ del(persistent.Goth_Point)
        $ del(persistent.Jock_Point)
        $ persistent.Goth_Point = 0
        $ persistent.Jock_Point = 0
        $ del(persistent.reload)
        $ persistent.reload = False
    
    show goth

    Goth "Choice"
        
    menu:
    
        "Bad":

            jump Goth_1_Hate

        "Good":
        
            jump Goth_1_Love

label Goth_1_Hate:

    if Goth_Mod == 0:

        play music "FoL_Tense.wav"

        Goth "G_1 Hate"

        $ persistent.Goth_Point -= 1
        $ Choice_Failure += 1

        #test text
        "Goth Point - 1
        \n Current: [persistent.Goth_Point]"

        hide goth

        jump Mascot_Reassure

    elif Goth_Mod < 0:
        
        Goth "G- Twist_1_Bad"

        $ persistent.Goth_Point += 1

        #test text
        "Goth Point + 1
        \n Current: [persistent.Goth_Point]"

        return

    elif Goth_Mod > 0:
        
        Goth "G+ Twist_1_Good"

        $ persistent.Goth_Point += 1

        #test text
        "Goth Point + 1
        \n Current: [persistent.Goth_Point]"

        return

label Goth_1_Love:

    if Goth_Mod == 0:
        
        Goth "G_1 Love"
    
        $ persistent.Goth_Point += 1

        #test text
        "Goth_Point + 1
        \n Current: [persistent.Goth_Point]"

        return

    elif Goth_Mod < 0:

        play music "FoL_Tense.wav"

        Goth "G- Twist_1_Good"

        $ persistent.Goth_Point -= 1
        $ Choice_Failure += 1

        #test text
        "Goth Point - 1
        \n Current: [persistent.Goth_Point]"

        hide goth

        jump Mascot_Reassure

    elif Goth_Mod > 0:

        play music "FoL_Tense.wav"

        Goth "G+ Twist_1_Good"

        $ persistent.Goth_Point -= 1
        $ Choice_Failure += 1

        #test text
        "Goth Point - 1
        \n Current: [persistent.Goth_Point]"

        hide goth

        jump Mascot_Reassure

label Jock_1:

    scene cafeteria

    show jock
    
    Jock "Choice"
    
    menu:
        
        "Good":
            
            jump Jock_1_Love
        
        "Bad":

            jump Jock_1_Hate

label Jock_1_Love:

    if Jock_Mod == 0:

        Jock "J_1 Love"

        $ persistent.Jock_Point += 1

        #test text
        "Jock_Point + 1
        \n Current: [persistent.Jock_Point]"

        return

    elif Jock_Mod < 0:

        play music "FoL_Tense.wav"
        
        Jock "J- Twist_1_Good"

        $ persistent.Jock_Point -= 1
        $ Choice_Failure += 1

        #test text
        "Jock_Point - 1
        \n Current: [persistent.Jock_Point]"

        hide jock

        jump Mascot_Reassure

    elif Jock_Mod > 0:

        play music "FoL_Tense.wav"
        
        Jock "J+ Twist_1_Good"

        $ persistent.Jock_Point -= 1
        $ Choice_Failure += 1

        #test text
        "Jock_Point - 1
        \n Current: [persistent.Jock_Point]"

        hide jock

        jump Mascot_Reassure

label Jock_1_Hate:

    if Jock_Mod == 0:

        play music "FoL_Tense.wav"

        Jock "Hate"

        $ persistent.Jock_Point -= 1
        $ Choice_Failure += 1

        #test text
        "Jock_Point - 1
        \n Current: [persistent.Jock_Point]"

        hide jock

        jump Mascot_Reassure

    elif Jock_Mod < 0:
        
        Jock "J- Twist_1_Bad"

        $ persistent.Jock_Point += 1

        #test text
        "Jock_Point + 1
        \n Current: [persistent.Jock_Point]"

        return

    elif Jock_Mod > 0:

        Jock "J+ Twist_1_Good"

        $ persistent.Jock_Point += 1

        #test text
        "Jock_Point + 1
        \n Current: [persistent.Jock_Point]"

        return

        

label Mascot_Reassure:

    show mascot

    if Goth_Mod != 0 or Jock_Mod != 0:

        Mascot "Confusion_1"

        return

    elif Choice_Failure == 1:
        
        Mascot "Reassure_1"

        return

    elif Choice_Failure == 2:

        Mascot "Reassure_2"

        return