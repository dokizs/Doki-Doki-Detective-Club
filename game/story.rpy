

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
    pause (5.0)
    scene black
    km "Look at her. Fast asleep."
    kd "She's grown up so fast."
    km "Oh, I don't think I could tell her..."
    kd "We can't just tell her at the last minute."
    km "It damnear is the last minute!! She leaves tonight!"
    kd "Well, then we have to tell her now, today. She needs time to say goodbye to her friends."
    km "...{w=1}Very well then."
    pause (1.0)
    scene bg MCR with wipeleft_scene
    show koto 1bi at t11
    pause (3.0)
    km "...Oh, I can't!"
    km "I will speak with her when she gets home!! Dear, could you please tell her for the both of us?"
    kd "...Only for you, dearest."
    "Kotonoha's mother exits the room, leaving her father to break the news."
    "He'd shake her slightly."
    kd "Koto, dear. Wake up..."
    show koto 1bp at t11
    kmc "Five more minutes..."
    show koto 1bi at t11
    kd "Don't do this to me, Koto. Come, please. There's something we must discuss."
    kmc "Hmh..."
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
    kmc "Dad...? It's not even 7 yet, why-{nw}"
    kd "Listen Kotonoha. You're..."
    show koto 1bu at t11
    "Kotonoha's eyes would narrow."
    show koto 1bu3 at t11
    kmc "You wake me up earlier than I need to..and for what? Is it bad?"
    show koto 1bw2 at t11
    kd "Well...it's something a bit...serious."
    show koto 1bv1 at t11 
    kmc "L-Like what, Dad?"
    show koto 1bw2 at t11
    "Kotonoha felt a shiver run down her spine as she waited for an answer."
    "Her parents never usually confronted her on anything, and if she was reading her father's face right, this wasn't a joke or something minor."
    kd "It's school."
    show koto 1bv at t11
    kmc "W-What, did I get a 'B' on my midterm?"
    kd "No. You passed that."
    show koto 4bb at t11
    kmc "Then what is it?"
    kd "You need to start packing."
    show koto 4bf at t11
    kmc "Are we going somewhere?"
    kd "Well..."
    show koto 4bp at t11
    kmc "...Dad...please be honest with me. What's going on?"
    show koto 4bf at t11
    kd  "...Alright, sweetheart. {b}{i}We{/b}{/i} aren't going anywhere persay. But {b}{i}you{/b}{/i} are..."
    show koto 1be at t11
    "The gears inside her head would start to turn, her brain getting to work on figuring out what her father meant, and surely enough, she caught on quick."
    show koto 1bp2 at t11
    kmc "I...I'm moving schools??"
    "Tears would well up in her eyes before she even got a 'yes'."
    kd "...Yes, and you need to pack when you get home. Now, if you think you can get little bit in. It's a lovely place up west."
    kmc "W-What? Dad, that's so far from here! Why didn't you tell me sooner!!"
    kd "Listen, that was a mistake on me and your mothers parts. We decided not to tell you until today. I'm sorry it's such short notice but...you leave tonight."
    kmc "W-What?! That's ridiculous! You're lying!"
    "Silence falls over both of them."
    kmc "You're...not lying."
    kd "Koto, sweetheart, we're both sorry."
    "Her father would reach out to touch her but she gave him the cold shoulder."
    kmc "How...how could you?! First, you switch my schools even though I never wanted to leave, and then you only give me one day to pack?"
    kmc "To say goodbye to {i}all{/i} of my friends??"
    kd "We switched you because it offers more extensive programs than this backwater school!"
    kmc "Oh yeah? Well this 'backwater school'? I love it. With all my heart."
    kmc "And don't even get me started on the 'extra programs' bullshit. I'm a highschooler! I can look into that myself when I'm a senior! It's not time to think about any of that yet!!"
    kmc "I'm only a sophomore, I don't need anything extra right now!"
    kd "...{w=0.5}It's always nice to start early."
    "Kotonoha would grunt and throw her pillow at her desk, frustrated as to why any of this was held from her. She looks back at her father defiantly."
    kmc "I'm not going."
    kd "You must. You've already been unenlisted. Today {b}{i}is{/b}{/i} your last day. If you show up tommorow, you're not a registered student and they'll throw you off campus."
    kd "And if you're not in your new school, they'll prosecute all of us, as you have to be in a school building as a sophomore."
    kd "It has already been done and there's no if's and's or but's about it, young lady."
    "Koto looks defeated. She was powerless in this moment. Everything had been taken care of behind her back."
    "Her father takes a look at his watch."
    kd "Ah, you don't have any more spare time. It's six fifty five already. Just get dressed. You can pack when you get home."
    kmc "B-But-{nw}"
    kd "We can discuss later if necessary. Now, get ready."
    "Her father left the room, leaving Kotonoha alone to think."
    "How could they just do this to her? She knew it was an epidemic. Almost every person she had talked to said that thier parents had packed them up and moved them here."
    "But that's just it. Those parents sent their kids off to {b}this{/b} school. Koto had been in this district since she was a child and now, she had to move to one all the way up west."
    "This would be the last time she saw her room. The last time she saw her parents, her friends, her real home."
    "After high school was college and she had already thought about where she wanted to go and was already taking dual credit classes and saving up for the ridiculously expensive room and board."
    "She had no reason to come back here. Maybe when she finished? But that was 6 years from now! Her friends would be long gone, her parents older, the school filled with new and unfamilar faces."
    "However, this was no time to think about what was shaping up to be her a pretty shitty day. It was 7:05. She needed to get ready for school. She had 8 hours to say goodbye to everyone."
    "And an extra 2 to announce it to the club. What would they even say to her...?...It doesn't matter, at least not yet..."
    "That's later in the afternoon. She hasn't even left the house, let alone gotten ready."
    "She needed to hurry."
    "She'd rush out of her room and into the bathroom, locking herself in it."
    scene bg MCH with wipeleft_scene
    pause (0.3)
    scene bg MCB with wipeleft_scene
    "Her grogginess wore off as she washed her face but the thoughts were still present. How was she going to function like this..?"
    "She couldn't. She wasn't. But she was going to have to. She had her bad days, but today was looking to be the worst. She would have to put on her best poker face and make it through school."
    "She was used to fronting. But not like this...not on such short notice...not about anything this serious..." 
    "Life offically sucks." 
    scene black
    pause (3.0)
    "Chapter 2 or title card or both in video form or otherwise"
    pause (3.0)
    scene bg corridor with wipeleft_scene
    pause (3.0)
    show koto 1u at t11
    pause (1.0)
    "Welp...she had done it. She kept to herself most of today. She told everyone that mattered. First her teachers, even though half of them knew; her closest friends, and now..."
    "She stops in front of the literature club."
    show koto 1p2 at t11
    "For the first time since she's stepped in the building today, her face softens."
    "The literature club...even her close friends got her stern expression and her 'don't tell anyone' speech."
    "But for some reason...she felt as if as soon as she stepped in here, she wouldn't be able to keep it up."
    show koto 1u at t11
    "But! She had to try. She didn't want them to freak out, therefore she had to look calm herself."
    show koto 1q at t11
    pause (.7)
    show koto 1p at t11
    pause (.7)
    show koto 1q at t11
    pause (.7)
    show koto 1p at t11
    pause (.7)
    show koto 1q at t11
    pause (1.0)
    show koto 1p at t11
    pause (3.0)
    show koto 1u at t11
    "She took a few breathes before sliding open the classroom door."
    show koto 1u2 at t11
    kmc "You got this, Koto."
    scene bg club_day with wipeleft_scene
    play music t3 fadein 1.0
    show natsuki 5b at t21
    show yuri 1q at t22
    n "And that's why anteaters are weird!!"
    y "You think they're weird because they...do what they're named after doing?"
    n "Yeah!! Like why can't they be called cakeeaters or somethin?!"
    y "Cakeaters? Really?"
    n "It's better than ants!!!"
    hide yuri
    hide natsuki
    scene bg closet
    show sayori 1u at t21
    show monika 1d at t22
    m "So you did that the other day??" 
    show sayori 4w at t21
    s "The cheer team dared me to! I would never do that on purpose!!"
    m "Even if they did, Sayori, you didn't have to go through with it. You could've reported them to a higher offical. This behavior won't be tolerated inside or outside of this club."
    s "I-I understand..."
    hide sayori
    hide monika
    scene bg club_day
    show koto 1u at t11
    "She'd make her steps a little louder than usual on purpose to catch everyone's attention."
    "Monika almost immediently takes notice and walks over to Kotonoha."
    show koto 1u at t21
    show monika 5a at t22
    m "Koto! Welcome! We were waiting on you to share poems! {nw}"
    kmc "Monika...hey.."
    m "Is something the matter?"
    kmc "Could you just...round everyone up, please? I've got something kind of important to say."
    m "Oh! Uh..well...I suppose so."
    m "You're usually never one to joke so if you say it's something important, I trust you."
    stop music fadeout 1.0 
    "Monika calls out to the rest of the club members and they all reluctantly stop their conversations and walk towards Monika, all sitting down in the front five desks as they tend to do."
    show sayori 1a at t51
    show natsuki 1a at t52
    show yuri 1a at t53
    show monika 1a at t54
    show koto 1a at t55

    m "So...your news...?"









