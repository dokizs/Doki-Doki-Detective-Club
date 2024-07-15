
#In Python because of the dollar sign
$ switch = True

#Ren'py
define switch = True


label story:  
    $ renpy.movie_cutscene ("FAKE CHAPTER OPENER.ogv")
    play music t3 fadein 1.0
    scene bg field with wipeleft_scene
    s "Oh, heyyyy!"
    "Oh, there she is!"
    show sayori 1a at t11
    show yuri 1h at t33
    s "Hey, MC!"
    show yuri 1n at t33
    mc "Oh, hey Yuri- {nw}"
    hide yuri with moveoutleft
    mc "{w=1}.{w=1}.{w=1}.{w=1}"
    "My day is great!{w=0.5} How's your day going?{w=0.5} Amazing!!!"
    "That girl never talks to me, I swear."
    "Am I scary or something?"
    show sayori 1r at t11
    s "Do you want a cookie?"
    mc "Huh? Oh..uh.."
    stop music fadeout 1.0 
    menu: 
        "Sure!":
            $ switch = True
        "How about no.":
            $ switch = False
if switch:
    mc "Give it to meh!"
    show sayori at h11
    show sayori 4s at t11
    s "Alright!"
    mc "Delicious-{nw}"
    play sound("warfare_gunshot_exterior_002.mp3")
    scene black
    s "It's kidnapping time!!"
    show aoki 1a at t11
    cd "Whar the hell???"
    
    
else:
    mc "Nah, keep your cookie, Sayo."
    play music ("A Faded Memory.mp3")
    show sayori 1e
    s "Oh...well, okay, I guess.."
    play music t3 
    show sayori 4s
    s "T-That just means more cookies for me!!"
    return