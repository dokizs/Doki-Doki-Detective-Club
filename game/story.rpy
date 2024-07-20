

label story:  
    $ renpy.movie_cutscene ("FAKE CHAPTER OPENER.ogv")
    play music t3 fadein 1.0
    scene bg club_day
    pause (1.0) 
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
            jump choice_sure
        "How about no.":
            jump choice_no
        "???":
            jump choice_script

label choice_sure:
    mc "Give it to meh!"
    show sayori at h11
    show sayori 4s at t11
    s "Alright!"
    mc "Delicious-{nw}"
    play sound("warfare_gunshot_exterior_002.mp3")
    scene black
    s "It's kidnapping time!!"
    show koto 1a at t11
    cd "Whar the hell???"
    

label choice_no:
    mc "Nah, keep your cookie, Sayo."
    play music ("A Faded Memory.mp3")
    show sayori 1e
    s "Oh...well, okay, I guess.."
    play music t3 
    show sayori 4s
    s "T-That just means more cookies for me!!"
    

label choice_script:
    scene black
    km "Look at her. Fast asleep."
    kd "She's grown up so fast."
    km "Oh, I don't think I could tell her..."
    kd "We can't just tell her at the last minute."
    km "It damnear is the last minute!!{w=2} She leaves tonight!"
    kd "Well, then we have to tell her now, today. {w=2} She needs time to say goodbye to her friends."
    km "... {w=1}Very well then."
    pause (1.0)
    scene bg MCR with wipeleft_scene
    show koto 1bi at t11
    pause (3.0)
    km "{w=1}Oh, I can't!"
    km "I will speak with her when she gets home!!{w=2} Dear, could you please tell her for the both of us?"
    kd "...{w=2}Only for you, dearest."
    "Kotonoha's mother exits the room, {w=1}leaving her father to break the news."
    "He'd shake her slightly."
    kd "Koto, dear. Wake up..."
    show koto 1bp at t11
    kmc "Five more minutes..."
    show koto 1bi at t11
    kd "Don't do this to me, Koto.{w=1} Come, please. There's something we must discuss."
    kmc "Huh..."
    show koto 1bp at t11
    pause (.1)
    show koto 1bw at t11
    pause (.1)
    show koto 1bp at t11
    pause (.1)
    show koto 1bw at t11
    pause (1.0)
    kd "finally."
    show koto 1bp2 at t11
    kmc "Dad...? It's not even 7 yet, why-"
    kd "Listen Kotonoha. You're..."
    show koto 1bu at t11
    "Kotonoha's eyes would narrow."
    show koto 1bu3 at t11
    kmc "You wake me up earlier than I need to..and for what? Is it bad?"
    show koto 1bw2 at t11
    kd "Well...it's something a bit...serious."
    show koto 1bv1 at t11
    kmc "L-Like what, Dad?"
    "Kotonoha felt a shiver run down her spine as she waited for an answer."
    "Her parents never usually confronted her on anything, and if she was reading her father's face right, this wasn't a joke or something minor."




