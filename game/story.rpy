
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
    s "Hey, UP!"
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
        "Teaser!!":
            jump choice_teaser
        "Memes":
            jump choice_memevid
        "Phone":
            jump choice_phone


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
    
label choice_phone:
    call phone_call_test
    call phone_discussion_test

label choice_script:
    pause (5.0)
    scene black
    $ startgame.grant()
    km "Look at her. Fast asleep."
    kd "She's grown up so fast."
    km "Oh, I don't think I could tell her..."
    kd "We can't just tell her at the last minute."
    km "It damn near is the last minute!! She leaves tonight!"
    kd "Well, then we have to tell her now, today. She needs time to say goodbye to her friends."
    km "...{w=1}Very well then."
    pause (1.0)
    scene bg MCR with wipeleft_scene
    show koto 1bi at t11
    pause (3.0)
    km "...Oh, I can't!"
    km "I will speak with her when she gets home! Dear, could you please tell her for the both of us?"
    kd "...Only for you, dearest."
    "Kotonoha's mother exits the room, leaving her father to break the news."
    "He'd shake her slightly."
    kd "Koto, wake up now dear."
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
    kd "Finally."
    show koto 1bp2 at t11
    kmc "Dad? It's not even 7 yet, why-{nw}"
    kd "Listen Kotonoha. You're..."
    show koto 1bu at t11
    "Kotonoha's eyes would narrow."
    show koto 1bu3 at t11
    kmc "You wake me up earlier than I need to...and for what? Is it bad?"
    show koto 1bw2 at t11
    kd "Well...it's something a bit...serious."
    show koto 1bv1 at t11 
    kmc "L-Like what Dad?"
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
    kmc "Dad.."
    kmc "Please be honest with me, what is going on?"
    show koto 4bf at t11
    kd  "...Alright, sweetheart. {b}{i}We{/b}{/i} aren't going anywhere per se. But {b}{i}you{/b}{/i} are..."
    show koto 1be at t11
    "The gears inside her head would start to turn, her brain getting to work on figuring out what her father meant, and surely enough, she caught on quick."
    show koto 1bp2 at t11
    kmc "I...I'm moving schools?"
    "Tears would well up in her eyes before she even got a 'yes'."
    show koto 1bu at t11
    kd "...Yes, and you need to pack when you get home. Now, if you think you can get a little bit in. It's a lovely place up west, a few days away with a new school and new people!."
    show koto 1bu3 at t11
    kmc "W-What? DAYS?? That's so far from here! Why didn't you tell me sooner!?"
    show koto 1bu at t11
    kd "Listen, that was a mistake on me and your mother's parts. We decided not to tell you until today. I'm sorry it's such short notice but...you leave tonight."
    show koto 2bt1 at t11
    kmc "W-What?! That's ridiculous! You're lying!"
    show koto 1bp3 at t11
    "Silence falls over both of them."
    show koto 1bp2 at t11
    kmc "You're...not lying."
    show koto 1bp3 at t11
    kd "Koto, sweetheart, we're both sorry."
    show koto 2bu at t11
    "Her father would reach out to touch her but she gave him the cold shoulder."
    show koto 2bu3 at t11
    kmc "How...how could you?! First, you switch my school even though I never wanted to leave, and then you only give me one day to pack?"
    show koto 1bu2 at t11
    kmc "To say goodbye to {i}all{/i} of my friends??"
    show koto 1bu at t11
    kd "We switched you because it offers more extensive programs than this backwater school!"
    show koto 2bu3 at t11
    kmc "Oh yeah? Well this 'backwater school'? I love it. With all my heart."
    show koto 1bu4 at t11
    kmc "And don't even get me started on the 'extra programs' crap. I'm a highschooler! I can look into that myself when I'm a senior! It's not time to think about any of that yet!!"
    show koto 2bu2 at t11
    kmc "I'm only a sophomore, I don't need anything extra right now!"
    show koto 1bu at t11
    kd "...{w=0.5}It's always nice to start early."
    show koto 2bt at t11
    "Kotonoha would grunt and throw her pillow at her desk, frustrated as to why any of this was held from her. She looks back at her father defiantly."
    show koto 1bu2 at t11
    kmc "I'm not going."
    show koto 1bw at t11
    kd "You must. You've already been unenlisted. Today {b}{i}is{/b}{/i} your last day. If you show up tomorrow, you're not a registered student and they'll throw you off campus."
    show koto 1bv1 at t11
    kd "And if you're not in your new school, they'll prosecute all of us, as you have to be in a school building as a sophomore."
    kd "It has already been done and there's no if's, ands or buts about it, young lady."
    show koto 1bp3 at t11
    "Koto looks defeated. She was powerless in this moment. Everything had been taken care of behind her back."
    "Her father takes a look at his watch."
    kd "Ah, you don't have any more spare time. It's 6:55 already. Just get dressed. You can pack when you get home."
    show koto 1bp2 at t11
    kmc "B-But-{nw}"
    show koto 1bp3 at t11
    kd "We can discuss later if necessary. Now, get ready."
    show koto 1bs3 at t11
    "Her father left the room, leaving Kotonoha alone to think."
    show koto 1bp at t11
    "How could they just do this to her? She knew it was an epidemic. Almost every person she had talked to said that their parents had packed them up and moved them here."
    "But that's just it. Those parents sent their kids off to {b}this{/b} school. Koto had been in this district since she was a child and now, she had to move to one all the way up west."
    show koto 1bo at t11
    "This would be the last time she saw her room. The last time she saw her parents, her friends, her real home."
    show koto 1bp3 at t11
    "After high school was college, and she had already thought about where she wanted to go. She was already taking dual credit classes and saving up for the ridiculously expensive room and board."
    show koto 1bw at t11
    "She had no reason to come back here. Maybe when she finished? But that was 6 years from now! Her friends would be long gone, her parents older, the school filled with new and unfamiliar faces."
    show koto 1bv1 at t11
    "However, this was no time to think about what was shaping up to be a pretty shitty day. Maybe her worst, but it was hard to tell. There was a competitor for that spot."
    "At least for now. It was 7:05. She needed to get ready for school. She had 8 hours to say goodbye to everyone."
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
    "Life officially sucks." 
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
    "But!...She had to try. She didn't want them to freak out, therefore she had to look calm herself."
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
    "She took a few breaths before sliding open the classroom door."
    show koto 1u2 at t11
    kmc "You got this, Koto."
    scene bg club_day with wipeleft_scene
    play music t3 fadein 1.0
    show natsuki 5b at t21
    show yuri 1q at t22
    n "And that's why anteaters are weird!!"
    show yuri 1o at t22
    y "You think they're weird because they...do what they're named after doing?"
    show natsuki 5e at t21
    n "Yeah!! Like why can't they be called cake-eaters or somethin'?!"
    show yuri 1h at t22
    y "Cake-eaters? Really?"
    show yuri 1h at t22
    show natsuki 5d at t21
    n "It's better than ants!!!"
    hide yuri at t22
    hide natsuki at t21
    scene bg closet
    show sayori 1u at t21
    show monika 1d at t22
    m "So you did that the other day??" 
    show sayori 4w at t21
    s "The cheer team dared me to! I would never do that on purpose!!"
    show monika 4r at t22
    m "Even if they did, Sayori, you didn't have to go through with it. You could've reported them to a higher official. This behavior won't be tolerated inside or outside of this club."
    show sayori 2v at t21
    s "I-I understand..."
    hide sayori
    hide monika
    scene bg club_day
    show koto 1u at t51
    "She'd make her steps a little louder than usual on purpose to catch everyone's attention."
    show koto 1u at t52
    "Monika almost immediately takes notice and walks over to Kotonoha."
    show koto 1u at t21
    show monika 5c at t22
    m "Koto! Welcome! We were waiting on you to share poems! {nw}"
    show koto 1u2 at t21
    kmc "Monika...hey..."
    show monika 1g at t22
    m "Is something the matter?"
    show koto 1p2 at t21
    kmc "Could you just...round everyone up, please? I've got something kind of important to say."
    show koto 1p3 at t21
    show monika 1i at t22
    m "Oh! Uh..well...I suppose so."
    show monika 4i at t22
    m "You're usually never one to joke so if you say it's something important, I trust you."
    stop music fadeout 1.0
    hide monika
    hide koto
    "Monika calls out to the rest of the club members and they all reluctantly stop their conversations and walk towards Monika, all congregated in the front as they tend to do."
    show monika 1c at t51
    show sayori 1b2 at t52
    show natsuki 5g at t53
    show yuri 1f2 at t54
    show koto 1p3 at t55
    pause (2.0)
    show monika 3d at t51
    m "So...your news...?"
    show koto 1p at t55
    kmc "Right..."
    show natsuki 5e at t53
    n "Oh, come on! You have Monika round us all up and then you forget your damn question?? This is a waste of time!!"
    show koto 1p2 at t55
    kmc "Natsuki, this is ser {nw}"
    show monika 4i at t51
    m "NATSUKI!{w=1} Kotonoha doesn't like to slack off unlike the rest of you. It's something important, at least to her, as far as you know."
    show monika 1b at t51
    m "Her and Yuri actually. The family ties are the most obvious in that aspect."
    show yuri 3c at t54
    show koto 5h1 at t55
    "Koto and Yuri would share a smile at Monika, appreciating the compliment."
    "Monika smiles back before turning back to Natsuki."
    show monika 5b at t51  
    m "So if you would kindly be quiet and let our fellow club member speak, it'd be gladly appreciated."
    show monika 1h at t51
    show natsuki 13ba at s53
    "Natsuki piped down after getting softly scolded by Monika."
    show koto 6p at t55
    kmc "Thank you, Moni."
    show koto 1p2 at t55
    kmc "So...my announcement. I...I..."
    show yuri 2g at t54
    "Yuri puts her hand on her cousin's shoulder."
    show yuri 2h at t54
    y "Take your time."
    "Kotonoha would look at the clock. It was already 4:45. Enough time had passed. She only had until 6 to say goodbye. She had no time at all."
    "She'd finally break her tough girl facade."
    show koto 1u5 at t55
    kmc "I-I DON'T HAVE TIME TO TAKE!!"
    show koto 1u21 at t55
    show yuri 1n at t54
    "Yuri flinches, her hand coming off Kotonoha's shoulder."
    show monika 4d at t51
    m "Kotonoha...what are you trying to say?"
    play music ("A Faded Memory.mp3")
    show koto 1u5 at t55
    kmc "I-I'm...I'M MOVING, ALRIGHT??"
    show koto 1u42 at t55
    "She felt as if she was on the verge of tears and as she looked around, she saw the mood had immediately dampened significantly."
    show sayori 2e at t52
    s "W-What...?"
    show koto 2u2 at t55
    kmc "I-I'm moving, alright?"
    show koto 1u21 at t55
    show yuri 1t at t54
    y "W-Why didn't you tell us sooner?"
    show koto 1u3 at t55
    kmc "Don't you think I would've if I knew??"
    show koto 6t1 at t55
    kmc "My 'parents', or at least the people that I used to call parents only just told me this morning..."
    show natsuki 4p at t53
    n "I-It must be some sort of April Fools joke or something?!"
    show monika 1r at t51
    m "It's September {nw}"
    "A silent head shake from Koto told her everything she needed to."
    show natsuki 5w at t53
    n "No...It can't be true..It can't!!"
    "Now Natsuki looked to be on Koto's level of emotion, looking like she was almost drawn to tears."
    s "You can't leave!! I WON'T LET YOU!!"
    show monika 1q at t51
    show natsuki 1o at t52
    show yuri 1o at t53
    show sayori 1p at t54
    show koto 1w2 at t55
    "Sayori runs up to Kotonoha, hugging her tightly." 
    show koto 3v1 at t55
    kmc "S-Sayori...plea{nw}"
    show sayori 4v at t54
    show yuri 4d at t53
    s "NO! I'M NOT LETTING GO!!!"
    show monika 2g at t51
    show natsuki 5s at t52
    m "Sayori, please let go of Kotonoha...she..."
    show monika 1q at t51
    pause (1.0)
    show monika 1r at t51
    "Monika takes a deep and sharp inhale."
    show monika 1i at t51
    m "She needs a bit of time to breathe."
    show sayori 4w at t54
    s "S-She's gonna leave us, I-I won't let her leave!!"
    show koto 1s at t55
    kmc "Sayori...please let me go. You're constricting my lungs..."
    show sayori 4u at t54
    show yuri 4c at t53
    "Sayori looks up at Koto with hurt, sadness and tears, threatening to fall."
    show koto 1s2 at t55
    kmc "Please..."
    show sayori 1u at t54
    "Sayori nods and finally lets go."
    show koto 1p at t55
    kmc "Thank you...I'm really sorry to all of you that it's on such short notice. Especially you, Monika."
    show monika 2e2 at t51
    m "It's ok. I believe you when you say that your parents only told you this morning."
    show monika 1b at t51
    m "While it is unconventional to let your child know that they are leaving you and their home they've known since as long as they've been alive, it's not anything to be worried about."
    show monika 1j at t51
    "Monika smiles."
    "...That's strange."
    show natsuki 1u at t52
    show sayori 1g at t54
    show koto 1e at t55
    "She kind of hit it directly on the head, almost like she had a glimpse inside her head. It was eerie but it struck with more of a sympathetic tone than anything."
    show yuri 4b3 at t53
    y "Actually...it might be."
    "Everyone looks at Yuri."
    show monika 4d at t51 
    m "Hm? What do you mean?"
    show sayori 1u at t52
    show natsuki 1u at t53
    show yuri 4ba2 at t54
    y "The new policy of 'at least 5 members per club'. Remember?"
    show yuri 4b at t54
    m "Oh, you're right, Yuri. It slipped my mind."
    show monika 3b at t51
    "Monika would facepalm softly."
    show monika 3k at t51
    m "Well, if any of you forgot like I foolishly did, last week, we had a schoolwide meeting. All clubs were there and a new rule was established, we have to have a minimum of 5 members."
    show monika 3i at t51
    m "Which means that along with the sad news of Kotonoha's departure, it means we're going to have to find another member to stay together, or we may get disbanded..."
    show monika 1o at t51
    show sayori 2y at t52
    show natsuki 4s at t53
    show yuri 3n at t54
    show koto 3s4 at t55
    "Everyone looks much worse now. Not only was it sad that Kotonoha was leaving but it's so detrimental that they might not even have a club anymore!!"
    show sayori 3l at t52
    s "Well...I wouldn't say that..."
    "Everyone would now look at Sayori."
    show sayori 4s at t52
    show yuri 1e at t54
    show koto 1b at t55
    s "I was kind of planning to invite someone! Before Koto said she was leaving, of course, so we could have 6 members!"
    show sayori 3x at t52
    s "But now that Kotonoha's leaving, they could be our 5th!"
    show monika 2c at t51
    "Monika looks deep in thought."
    show monika 2d at t51
    m "Would they be willing to join?"
    show sayori 2lo at t52
    s "Pfft, yeah, they would!"
    show monika 1b at t51
    show yuri 3c at t54
    show koto 1h at t55
    m "Hm, well then I suppose that's a problem solved!"
    show yuri 2c at t54
    show monika 1a at t51
    show sayori 5b at t52
    "Sayori was scared out of her mind. She knew he had been struggling to even look at clubs, let alone join one..."
    "Announcing him as 'The Fifth Member' didn't help much either. Now the girls were counting on Sayori to make good on her promise."
    "Looks like she had some seeds to plant and some cute faces to make."
    "Monika clears her throat interrupting Sayori's train of thought."
    show monika 4l at t51
    m "Let's not let that overtake our sadness over the loss of one of our original members however."
    show yuri 1l at t54
    y "Kotonoha is still leaving and we must keep the mood appropriate."
    show monika 1i at t51
    m "Thank you, Yuri. Kotonoha, we're sorry for your unfortunate situation."
    show monika 1p at t51
    m "I wish we could've done more..."
    show natsuki 4n at t53
    pause (2.0)
    show natsuki k34 at t53
    pause (2.0)
    show natsuki 4k at t53
    n "...Wait! I got it!"
    show natsuki 1l at t53
    n "I have some cupcakes in my home economics room!!"
    show monika 1n at t51
    m "But Natsuki, aren't those for an end of quarter project?"
    show natsuki 5e at t53
    n "Who cares?! I can make more, they don't take long to make!"
    show natsuki 1l at t53
    n "Plus I'm not just gonna sit here and let us sulk in silence for the next hour."
    show monika 3g at t51
    m "Bu{nw}"
    show natsuki 1v at t53
    n "Don't question me! It'll just be a quick snatch and grab!"
    "And without letting anyone protest, she left the room."
    hide natsuki
    show monika 1q at t41
    show sayori 1o at t42
    show yuri 1e at t43
    show koto 1e at t44
    "Monika sighs tiredly."
    show monika 3l at t41
    m "Well, I guess we're having cupcakes this afternoon!"
    show yuri 1f at t43 
    y "Only cupcakes?"
    show monika q2 at t41
    show yuri 1i at t43
    "Monika looked at Yuri, understanding what she was implying."
    show monika 1r at t41
    "She sighs again."
    show monika r2 at t41
    m "You want to make tea, don't y{nw}"
    show yuri 1j at t43
    y "I want to make tea, yes."
    pause (2.0)
    show yuri 4a at t43
    show monika 2h at t41
    pause (2.0)
    show monika b4 at t41
    m "You know what? Why not!"
    show monika b5 at t41
    show yuri 3d at t43
    y "Thank you, Monika!"
    "Yuri would hurriedly sprint over to the closet to retrieve her tea set."
    hide yuri
    show monika 1r at t31
    show sayori 1n at t32
    show koto 1a at t33
    "Monika turns to Kotonoha."
    show monika 4n at t31
    m "I guess we're having a celebration for your departure, Koto."
    show monika 1m at t31
    "Monika smiles awkwardly. This wasn't on her itinerary at all. And while she didn't just want to sulk around for the next hour, she wanted to continue club activities like normal."
    show koto 2s at t33
    kmc "I mean, it doesn't look like they're giving us much of a choice, are they?"
    show monika 3l at t31
    m "It appears not...well, I guess me and Sayori are going to pitch in as well.."
    show sayori 4r at t32
    s "Ooo, ooo! I can find some decorations in the art classroom! They're holding a meeting right now too, and they'll have a ton of supplies that can help!"
    hide sayori
    show monika 1q at t21
    show koto 1e at t22
    "Sayori doesn't even let her idea process in anyone else's head and she leaves without a second thought."
    "Monika just can't catch a break today."
    show monika 1p at t21
    m "Well! I suppose I'll go help her!"
    show koto 2s2 at t22
    kmc "Maybe I could come with!"
    show monika 4n at t21
    m "Come with? It's your party, Koto! Just sit back and watch!"
    show koto 2p2 at t22
    "Kotonoha looks a bit sad but it's quickly replaced with happiness. She had been thinking about something like this all day, but she never thought she would actually get it!"
    show koto r22 at t22
    kmc "Thank you, Moni. I appreciate it."
    show koto r23 at t22
    show monika 1b at t21
    m "Of course!"
    "Monika walks to the door."
    show monika 1a at t51
    m "{size=10}This is the last time I let things out of my control.{/size}"
    scene black with wipeleft_scene
    stop music fadeout 1.0 
    pause (3.0)
    "chapter 3"
    pause (3.0)
    scene bg corridor with wipeleft_scene
    show sayori 1a at t11
    s "Ok, art room is{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}{w=0.7}s {w=3}here!" 
    "Sayori would step into the art room." 
    scene bg AR with wipeleft_scene
    show sayori 1a at t11
    "Some of the kids in the classroom looked at Sayori as she entered."
    show sayori 3l at t11
    "She recognized some of them, waving shyly at a couple of friends." 
    show sayori 1f at t11
    "But she wasn't here to goof around." 
    "She needed to see if there was something she could use for Koto's party!"
    "She glanced around the room, her excitement could be felt with every extra step she took." 
    show sayori 1l at t11 
    s "Hey guys! Happen to know if there's any art supplies I can steal from you guys?" 
    show sayori 5b at t11 
    s "I need to make a little something on short notice, eheh..."
    "The other students exchange curious glances, and one or two of them smile sympathetically."
    "Sayori's enthusiasm was infectious, and they could see she was on a mission." 
    k1 "Oh, hey Sayori! Maybe you should ask the teacher! She'd probably be happy to help!" 
    show sayori 1m at t11 
    s "Really?!" 
    show sayori 4r at t11 
    s "Thank you so much!! I really appreciate it!" 
    "Sayori skips over to the teacher's desk, her shoes making a soft pat-pat sound on the floor." 
    show sayori 1s at t11 
    s "Hi, Missus!"
    t "Sayori! How are you still at school?" 
    show sayori 2x at t11
    s "Oh, I'm in the literature club on the 3rd floor!!"
    t "How... interesting. I may need to stop by at some point." 
    show sayori 1c at t11
    s "Uhhh, yeah!! Say... do you have any spare art supplies I can borrow? I need it for something."
    show sayori 3c at t11
    s "Any streamers or confetti, or glitter... anything that can make a party pop!" 
    t "A party? Sayori, that's not really traditional art supplies...we don't usually have those things around here in class…" 
    "She wasn't lying. Now that Sayori thought about it, there was a distinction between art supplies and party supplies."
    show sayori 1e at t11
    s "O-Oh... I guess I didn't think about that. I just...we were gonna do a thing and..."
    show sayori 1u at t11
    "She trailed off not knowing if she wanted to continue."
    show sayori 1v at t11
    s "{size=10}And we wanted to make it special...{/size}"
    show sayori 1u at t11 
    "The teacher sighs heavily at first but then smiles warmly at Sayori, her eyes softening." 
    show sayori 1o at t11
    t "In the cubicles." 
    show sayori lmno at t11
    "Sayori gasps as her face lights up, and she bounces on the balls of her feet in excitement." 
    show sayori 3r at t11
    s "Thank you Missus! I'll be quick!" 
    t "Of course, Sayori." 
    "Sayori skips over to the 3x3 cubicle and gets on her knees, peeking inside with a look of determined curiosity."
    hide sayori
    #cg?? (maybe not considering how short the scene is)
    "She finds mostly everything she thought she needed—colorful papers, streamers, and even a bit of glitter. She starts to eagerly rummage through the cubicle, her hands moving quickly." 
    "With each item she finds, her excitement grows. She giggles as she sorts through the supplies, imagining all the fun decorations she can make." 
    scene bg corridor with wipeleft_scene 
    show monika 1h at t11
    #this could definitely be a CG
    "Monika looks inside the classroom, seeing Sayori and the teacher having a conversation." 
    "She notices Sayori skip away from the teacher, and the teacher glances out of her classroom door's window." 
    "Monika stares back at her and something about her looks... off." 
    "She gets a bit nervous and decides to avert her gaze, stepping out of sight of the door window." 
    "She leans up against the wall beside the door, her heart racing slightly." 
    "Soon, she starts hyperventilating. Who was that teacher? She had never seen her before..."
    scene bg AR with wipeleft_scene
    "The teacher stares at Monika through the glass. She knew {i}exactly{/i} who she was."
    show sayori 4r at t11
    s "I got what I needed! Thank you, missus!"
    t "You're welcome, Sayori! Now run along! I think someone is waiting for you."
    show sayori 4o at t11
    s "Huh?"
    show sayori 4n at t11
    s" Oh right, Moni! Thank you! I'm sure she's on her way!"
    "The teacher would nod her away, her gaze lingering for a moment longer as Sayori exits."
    "Sayori flashes another bright smile as she walks out of the classroom, her arms filled with the supplies she's gathered."
    scene bg corridor with wipeleft_scene
    show sayori 4q at t11
    "She turns the corner, ready to walk back upstairs when she sees Monika, and it spooks her a bit."
    show sayori 4p at t11
    s "Ah!"
    pause (2.0)
    show sayori 4l at t11
    s "Oh, heyyy, Monika! I didn't recognize you for a sec!"
    s "Why didn't you come in?"
    show layer master at heartbeat
    show vignette
    #zoom on sayori as her expression changes
    play music ("HeartBreath (Moni Song).mp3")
    "Monika is pressed against the wall, her posture was tense and rigid, unlike her usual composed self." 
    "Her face is pale and her eyes dart around erratically, as if she's struggling to focus on anything." 
    "Her breaths come in short, shallow gasps, each one seeming to come with visible effort. Her hands are clenched at her sides, fingers trembling slightly."
    "She brings one hand up to her chest, as if trying to steady her heartbeat. Her shoulders rise and fall rapidly with each uneven breath, and she sways slightly, almost as if she's about to collapse."
    "Monika's breathing is labored, with a faint wheezing sound accompanying each inhale. She occasionally bites her lip, trying to suppress the rising panic, but it's clear that she's overwhelmed."
    "Her wide and glassy eyes show a sense of fear and confusion."
    show sayori 4g at t11
    s "...Moni?"
    "Sayori sets the supplies down gently, her concern growing as she approaches Monika cautiously."
    show sayori 2h at t11
    s "M-{w=1}Monika?…"
    "Monika snaps out of her little attack, blinking rapidly as she tries to regain her composure."
    hide vignette
    show layer master
    stop music fadeout 1.0
    show sayori 1f at t21
    show monika 1f at d22
    m "H-Hm?"
    show sayori 3c at t11
    s "Are you ok? You're on the floor and you don't look too good...like at all..."
    show monika 2l at d22
    m "Oh, um, yes! Of course, I'm fine!"
    "Monika stands up and brushes herself off."
    show monika 2n at t22
    m "I just… since I was behind you, I saw you getting the things and just decided to wait for you."
    show monika 2l at t22
    m "I didn't expect you to be out so soon…"
    show sayori 2f at t21
    "Sayori reaches out, placing a comforting hand on Monika's shoulder."
    show sayori 2g at t21
    s "You don't look fine. Are you sure you're okay?"
    show monika 2m at t22
    show sayori 1k at t21
    "Monika takes a deep breath, slowly removing Sayori's hand, her breathing slowly calming as she forces a small smile."
    show monika 1l at t22
    m "I'm okay now, really. I just... had a bit of a panic. It's nothing."
    show monika 1l at t22
    show sayori 4l at t21
    s "Awww, but I feel sorry for you, Moni!"
    show sayori 1n at t21
    "Sayori gasps as she gets a bit of an idea."
    show sayori 3r at t21
    s "Let's talk about it while we walk, okay? Maybe I can help you calm down and feel better!"
    show sayori 3s at t21
    "She blushes at the prospect. Spending time with Monika was always great...always..."
    show monika 1e at t21
    "Monika shakes her head, her eyes softening as she appreciates Sayori's concern."
    m "Thanks, Sayori. But I'm ok, really."
    "Sayori's face drops slightly but regardless, she picks up the supplies again, giving Monika a reassuring smile while she leaves some of it for her to grab."
    s "Alright, well then let's head upstairs. I'm sure Koto's waiting on us!"
    m "I suppose so."
    "Monika picks up her fair share of supplies and follows Sayori, the two of them starting to walk up the stairs- {nw}"
    scene bg MR
    show monika 1a at t11
    play music m1 fadein 0.5
    m "W-What the hell?"
    m "This isn't the right background..."
    m "This isn't supposed to exist yet..."
    m "Where's Sayo{nw}"
    m "wait..."
    m "Someone else is here{w=3}...someone{w=2}...like me."
    m "Someone real...{nw}"
    #fix screen tear 
    #She knows MC is here now so this is how she explains her usage of her powers. 
    #She wants to make sure everything goes perfectly for the "New member", 
    #especially if it felt "Like her and not like the others", she wants out and 
    #another presensce that she feels that's similar to hers? No reason not to take that opportunity. 
    #Even if he couldn't get her out, she wanted to see who or what it was (reason im calling 
    #MC it is because this is all her speculation. She's been here in the game and aware for a while and you 
    #might be asking, why am I writing cliff notes for lore that's not going to be in the mod? 
    #I dunno. :P) but the game "resets" her, or so it thinks (you might also be asking why am i personifying the game itself?
    #also dunno)
    m "This isn't right...No, No, NO!"
    m "Why am I here?? THIS ISN'T RIGHT!"
    m "I-I want to get out..."
    m "LET ME OUT!"
    #fix replies tag
    label monika_random_phrase:
    $ monika_phrases = [
        "This is pain?",
        "Look at ME.",
        "I’ve been thinking about you.",
        "You don't deserve this.",
        "This is MY world.",
        "You’re the only one who understands me.",
        "Devolved code.",
        "https://ibb.co/Q6QYRTq{nw}"
    ]

    $ chosen_phrase = renpy.random.choice(monika_phrases)

    m "[chosen_phrase]{nw}"
    show monika g1
    m "{glitch}{glitch}{glitch}"
    show monika g2
    pl "MY NAME IS {nw}"
    stop music
    scene bg corridor
    show sayori 1a at t21
    show monika 6a at t22
    s "Uh...Moni?"
    show monika 1q at t22
    pause (.1)
    show monika 6a at t22
    pause (.1)
    show monika 1q at t22
    pause (.1)
    show monika 1f at t22
    pause (2.0)
    show monika 1g at t22
    m "H-Huh?"
    s "You spaced out..."
    s "Moni, we can go get you something to drink, I have a few yen in my purs{nw}"
    m "N-No!! I'm alright, please, Sayori."
    m "Let's just get this stuff back to the club."
    s "...{w=1}Alright, Monika...Well then, let's just go. I don't like seeing you like this."
    m "Seeing me like what? I'm ok!"
    "Sayori pauses mentally. She knows it isn't true. Something is amiss!! But dang it, if she isn't going to take her {glitch}'s word."
    s "If you say so..."
    m "Now, c'mon. Let's get this stuff upstairs for Koto, hm?"
    s "Y-You're right..."
    "Sayori spots some empty discarded boxes that they could use."
    "They loaded the supplies into 2 separate boxes before picking them up and heading back upstairs."
    hide monika
    hide sayori
    scene bg SS with wipeleft_scene
    pause (2.0)
    "As Monika and Sayori trudge up the stairs, Monika is left to think."
    m "{i}What...who...is that...??{/i}"  
    m "{i}It's like no one else here.{/i}"
    m "{i}It feels like me. Or well...felt.{/i}"
    "Monika starts to mentally connect the dots."
    m "{i}That's it! Sayori warped the game when she went off script...{/i}" 
    #She's wrong obviously, the MC just pops in the world one day and that time can be when the game is downloaded
    #and let's just say that the person who installed got busy and decided not to play yet. Well when he does start 
    #to play, koto has successfully moved and DDLC continues on as normal. This also gives Moni good reason to be
    #suspicious of Sayori hence why she starts to look like she's just playing the friend card in the main game
    #and that could be why sayo dies first.
    m "{i}But how...? I thought I was the only one?{/i}"
    m "{i}She hasn't shown any signs...and I haven't felt her...{/i}"
    m "{i}Can she hide her power?{/i}"
    m "{i}Why hasn't she told me? She's an airhead, it's in her character to tell me!{/i}"
    m "{i}This is all so frustrating!{/i}"
    m "{i}{b}UGH!!{/i}{/b}"
    "She takes an extra loud stomp as her thoughts peak."
    "Sayori looks back at Monika, about to open her mouth before Monika waves her hand, advising her not to."
    "She barely nods back as she continues to walk, reaching the landing between Floor 1 and 2."
    pause (3.0)
    "...{nw}"
    "Monika takes a quiet but sharp breath."
    m "{i}...{/i}"
    m "{i}There are too many questions right now.{/i}"
    m "{i}I just really thought I was the only one...{/i}"
    m "{i}Now there may be three?{/i}"
    "She lets out a sigh out loud."
    "Sayori looks back at her, this time determined not to keep her mouth shut..."
    s "Are you tired already? Is that it?"
    m "Uhm...{nw}"
    m "Yes...just very...tired..."
    s "Aww, c'mon, you can't be tired!!"
    s "You're overexerting yourself, we're not running a marathon! We're just carrying boxes! For Koto!"
    m "Mhm...right.."
    "Monika was skeptical of Sayori now, but she also didn't want to have a conversation with her right now."
    "And her facial expressions, silently and seemingly politely telling Sayori to stop didn't seem to be registering."
    "She wanted to get back to her thoughts."
    s "We're almost on the third floor! Just another flight!"
    "Monika out of annoyance rolls her eyes and responds sarcastically."
    m "Of course...I can't be tired! Not now! Not when were {i}soooooo{/i} close...."
    "Sayori however, still didn't seem to get the hint and took it as a positive statement."
    s "That's the spirit! Now, c'mon!"
    "Sayori finally stops talking and they start to silently walk up the stairs again."
    m "...{w=1}{i}I've got my eye on you, Sayori.{/i}"
    m "{i}And whoever your little friend is too...{/i}"
    tl "..."
    scene bg SC with wipeleft_scene
    "After a hefty walk to the other side of the building, Natsuki gets to her Home Economics classroom."
    show natsuki 1a at t11
    n "Jesus, that was a long-ass walk..."
    "Natsuki peers inside the class to see that the lights are off."
    #face change
    n "Damnit! Out of all the days she decides to stay after, today isn't one of them?"
    "She jiggles the handle, trying to see if it was locked. It, in fact, was locked."
    n "Ugh, great! Just my luck!"
    "She looks around."
    show natsuki 2e at t11 
    n "Alright...well, it can't be hard to break in here...right?"    
    n "People in movies do it all the time!"
    "She looks around trying to find anything she could use."
    "She then gets an idea."
    n "Oh! Duh..."
    "She takes out her hairties and rips the ribbon off of the wire."
    n "I don't know how I always forget that these are in my hair."
    n "But hey, at least today they're being useful{nw}"
    #Natsuki's hair falls over her face, add sprites and sfx (UPDATE 5/10/25 DONE)
    show natsuki 1i2 at t11
    pause (1.0)
    show natsuki 1h2 at t11   
    n "Hmph, should've expected that."
    "She tucks the extra hair behind her ear, a look of annoyance on her face as she gets on her knees to pick this lock."
    n "Alright, Papa, time to use those skills you taught me..."
    "She starts to use the rhythmic method her father taught her."
    n "{size=10}One click that way...{w=2}and another this way...{w=2}listen for the winding spring...{w=2}and...{/size}"
    "{i}*Click!*{/i}"
    n "Yes!!"
    "She slides open the door happily."
    n "Thanks, Dad."
    "She says before she steps inside."
    scene bg SC2 with wipeleft_scene
    show natsuki 2e at t11
    n "Alright, this is where we usually put our stuff when we finish."
    "She's about to walk over to the closet but she stops."
    "She looks around her and unconsciously takes a deep breath."
    "The windows were slightly open and the sun was setting, casting a warm glow across the room."
    n "Wow... our side never looks this pretty..."
    n "...Or sounds this nice... The quiet is almost…creepy."
    "She walks over to the teacher's desk and sits down on it, her fingers tracing the soft wooden surface as her eyes start to soften as she takes in the view."
    "She could picture a summer class in here, with kids happily working away, chatting, and enjoying themselves."
    "She feels the soft sunlight hit her face, and in this moment, she feels completely tranquil."
    "Like she's at peace with her demons, feeling a rare moment of serenity."
    pause (3.0)
    "The breeze comes in and it only boosts her euphoria, carrying with it the faint scent of blooming flowers."
    n "I haven't felt this good in forever. It's like all my problems are…gone, even if it's just for now…."
    "She closes her eyes for a moment, letting the tranquility wash over her."
    "Her breathing slows, and a soft smile tugs at her lips."
    n "This is what I needed... a moment of quiet, a break from everything."
    "However, her thoughts start to betray the lovely moment of self reflection..."
    n "If only I had someone to share it with... someone who could really appreciate how perfect this feels. The perfect person…"
    n "No..the perfect guy. In the perfect spot…"
    "She opens her eyes, looking around the empty room, the warmth and quiet now tinged with a sense of solitude."
    "She sighs harshly, feeling a pang of loneliness as she shoves herself off the desk.."
    #she's supposed to shake her head, if I can't do it in sprites, I'll write it out
    n "Ugh...I hate getting sappy."
    n "Time to do what I broke in here to do..."
    "She puts her hair back up before she walks over to the closet and goes for the low shelf where she put her cupcakes."
    "She folds the closet door shut as she holds the bulky tray of cupcakes."
    n "Gonna need all these for Sayori's ass. By the time I turn around, she'll have eaten all of them."
    "She chuckles to herself before she hears noises outside. Some she can't decipher."
    "She turns around quickly, suspicious of what the noises are. She consciously decides that whatever it is, it isn't good."
    n "That's my cue. I'm getting the hell out of here before I get caught."
    "She quickly tiptoes over to the door, ducking under the glass, waiting for the noises to pass."
    "Turns out it was students talking."
    "She could just walk out now, but she doesn't know those kids. They might be the snitching type."
    n "And no one likes a snitch...."
    "After a while, the conversation moves elsewhere."
    "Time to escape."
    n "Go go go!!"
    "She quickly locks the door before slipping between the small crack in the door she made and slides it closed again quietly, just in case."
    scene bg SC with wipeleft_scene
    show natsuki 1a at t11
    "Natsuki takes one more look around to see if anyone was listening or watching."
    n "I...think I'm clear..."
    "She smirks a devilish smirk to herself as she walks back to the other side of the building feeling accomplished, even though what she just did was very wrong."
    "Natsuki looks out the windows lining the halls as she makes her trek back. She wasn't gonna lie about that part, it was pretty."
    "She thinks about the other part of what she said in the class though. The thing about needing 'the perfect guy'."
    n "No...that's stupid. I don't need anyone."
    "She fake gags, even though no one's around to see it."
    "She didn't need anyone, let alone a sweaty, stinky, testosterone-filled, boy. {w=2} Gross."
    scene bg corridor with wipeleft_scene
    "Natsuki finally makes her way back over to the part of school she recognized."
    show natsuki 5d at t11
    n "Finally, I made it back!"
    show natsuki 5y at t11
    n "And before everyone else too!"
    s "Not everything is a competition, Natsuki."
    show natsuki 1v at t11
    n "Goddamnit!"
    "Natsuki looks behind her and sees Monika and Sayori coming up the stairs."
    show sayori 1a at t32
    show monika 1o at t33
    show natsuki 5s at t31
    n "So much for me being first."
    show sayori 1a at t32
    s "You were first! We were just...coming up at the same time!"
    n "Whatever. I still got here first!"
    s "Is that...not what I said...?"
    n "Ugh, just shut up!"
    "As Natsuki finally turns to face the two, she catches a glimpse of Monika."
    n "Monika, you look a bit green."
    n "You alright?"
    "Monika zones back in."
    m "Hm?"
    n "Earth to Monika? I asked if you were ok."
    m "Oh yes, I'm ok!!"
    "Natsuki shrugs."
    n "If you say so..."
    s "Can we, uh, head inside now? My arms are starting to hurt..."
    n "Oh yeah, here."
    "Natsuki opens the door and the three of them flood inside."
    scene bg closet with wipeleft_scene
    "Yuri puts on the last of the tea."
    "She walks over to where Koto is sitting."
    scene bg club_day with dissolve_scene 
    show yuri 1g at t22
    show koto 1t at t21
    pause (3.0)
    show yuri 1h at t22
    y "So. When were you going to tell me?"
    show koto 2t1 at t21
    kmc "I told you, I didn't know until this morning."
    y "And what does that mean? You didn't think to text me or call me before you got to school?"
    kmc "I was in a rush, ok?? I didn't have time to do anything."
    y "Likely story."
    kmc "You don't think I'm telling the truth?"
    y "Your story seems highly unlikely is all I'm saying."
    kmc "Yuri...I'm your big cousin. Why would I have any reason to lie to you?"
    "Yuri paused."
    play music ("Lamentation3.mp3")
    y "...You don't."
    kmc "So why are you assuming such a thing?"
    #yuri crying sprites
    y "I-I don't know, ok?"
    kmc "Yuri, talk to me."
    y "I feel...hurt."
    y "Like you could've said something so much sooner..."
    kmc "But I couldn't- {nw}"
    y "{b}I KNOW.{/b}"
    pause (2.0)
    y "I just...can't shake that feeling...my brain won't accept it..."
    "Yuri chuckles slightly."
    y "My conscience thinks that this is all ridiculous."
    kmc "But you know that {nw}"
    y "-this is reality?"
    y "..."
    y "Yes.{w=1} I do."
    y "It's just...hard to accept."
    "Koto gives Yuri a reassuring smile and pats her on the back."
    kmc "...{w=1}You don't think I don't think it's ridiculous either?"
    kmc "I mean, who just does that to someone?"
    kmc "Let alone their own child."
    "Tears threatened to leave Kotonoha's own eyes, but she refused. She needed to comfort Yuri in this moment."
    "She needed her."
    kmc "If you {nw}"
    "Yuri runs up to Kotonoha and envelops her in a tight hug, following up with an unforgiving squeeze.."
    y "Please don't go..."
    "Yuri was now softly sobbing in Kotonoha's arms."
    "Koto sighs, trying to get her breathing together, her voice pained as she speaks."
    kmc "I tried being rebellious. My parents already settled everything."
    kmc "All my affairs have been set behind my back."
    "Yuri cries a little harder now."
    y "T-There has to be some way! Some way!!"
    kmc "I'm afraid not, Yuri."
    kmc "This is how things are..."
    "Kotonoha strokes Yuri's silky purple hair, trying to offer some comfort."
    pause (2.0)
    "Koto sits there and strokes Yuri's head for a good 5 minutes."
    "Yuri's tears begin to dry slightly as she's comforted by her eldest cousin, finally glad she was able to get this heartache off her chest."
    kmc "You feeling better now?"
    "Yuri sniffles, trying to recompose herself."
    y "I am...thank you..."
    pause (2.0)
    "After a short while, Yuri was still slightly teary, but she felt much better now, and she wanted to try and lighten the mood."
    y "You haven't changed a bit, you know?"
    kmc "And what's that supposed to mean?"
    "Yuri chuckles, a tinge of sadness still in her voice."
    y "It was a compliment."
    kmc "Hm...well thank you. I appreciate it..."
    kmc "You know...I could say the same about you."
    "Yuri rolls her eyes."
    y "Are you kidding? I've grown up significantly since I was a toddler!"
    kmc "Then what are you doing?"
    "Kotonoha smirks teasingly."
    kmc "Still crying in your older cousin's arms."
    "Yuri's face flares red and she quickly fixes her positioning, trying to prove Koto wrong, even though she's obviously right."
    y "I-I was not!"
    kmc "Sure, you weren't."
    "Koto chuckles before going silent."
    pause (3.0)
    "The silence was deafening. Too much for Kotonoha to handle. She hated silence."
    kmc "....Say...How about something a bit more {w=1.3}mature for you?"
    kmc "Like...{w=1}a hug?"
    y "Hm...That does sound a bit better."
    "Yuri eagerly steps into Kotonoha, not even waiting for her to open her arms."
    "Kotonoha stumbles but settles into the hug, wrapping her arms around Yuri."
    stop music
    n "Ugh. Get a room already!"
    "Kotonoha lets go of her cousin and turns to the doorway, seeing Natsuki leaned in the frame."
    kmc "Excuse me?"
    kmc "We're related...?"
    n "So?? People do crazy shit all the time! And I thought Americans were weird, trying to marry their sisters in Colorado!!"
    y "You mean Alabama, Natsuki?"
    n "Shut up! American history is dumb anyway!"
    y "Just don't be disgusting or crude when you speak, Natsuki."
    y "Especially when you walk in on a moment unprompted."
    n "...{w=3}Whatever..."
    "Natsuki steps aside, letting Monika and Sayori walk in."
    show monika 1m at t51
    show sayori 4x at t52
    show natsuki 5y at t53
    show yuri 4a at t54
    show koto 1f at t55
    s "We got the stuff!!"
    "Yuri's tea kettle would begin to blow steam."
    show yuri 2i at t54
    y "Looks like everything is right on time."
    show yuri 2j at t54
    y "I'll be back."
    hide yuri
    show monika 1m at t41
    show sayori 4x at t42
    show natsuki 5h at t43
    show koto 1f at t44
    n "Finally. You know how much I had to go through to get these things?!"
    "Monika finally regains her sense of self, ending her little mini-episode."
    "Just as Natsuki had spoken."
    m "What did you have to do to get them?"
    n "I had to break into the Home Ec class!"
    m "You broke into a class?! Why didn't you just come find us and tell us the room was locked??"
    n "Because, {i}{b}Monika.{/i}{/b}"
    n ".{w=3}.{w=3}.{w=3}"
    "Monika stares quizzically."
    m "Because what?"
    n "BECAAAAAAUUUUUUSE.{w=1} I don't fall behind on my promises."
    show natsuki 5t at t43
    n "I do what I say I'm gonna do!"
    show natsuki 5i at t43
    pause (2.0)
    show monika 1n at t41
    m "Well, that surely is an....admirable trait to have..."
    n "Damn straight."
    n "Now, we gonna get this party started or what?"
    m "I guess we should. Club's end at 6 and it's already 4:45."
    s "Ehehe, yayyy! Time to decorate!!"
    "Yuri returns with teacups on a metal tray."
    show monika 1n at t51
    show sayori 4x at t52
    show natsuki 5i at t53
    show yuri 2i at t54
    show koto 1f at t55
    y "And quick. Like Monika said our time is limited, so let's not waste it."
    m "I couldn't have said it better. Let's get to it, girls!"
    e "Yeah!!"
    s "Not Koto, though!"
    exk "Yeah!"
    scene black with wipeleft_scene
    "The girls would get to hastily decorating the class to the best of their ability on such short notice."
    "Natsuki unwrapped the cupcakes out of their foil and meticulously placed them on each desk."
    "Yuri sat some of her scented candles on each desk alongside Natsuki, before placing 5 main tea cups on the teachers desk."
    "And despite their wishes, Koto helped decorate for her own party."
    "She helped Monika and Sayori put up all the miscellaneous banners and streamers."
    "After a while, it was all starting to come together."
    "They all took a step back and collectively wiped their brows."
    scene bg KPR with wipeleft_scene
    show monika 1m at t51
    show sayori 4x at t52
    show natsuki 5y at t53
    show yuri 4a at t54
    show koto 1f at t55
    kmc "Wow everyone...this looks beautiful..."
    "Natsuki was about to speak, probably about to say something snarky, but Monika was already glaring at her as if preemptively saying 'Save It.'"
    s "Only the best for you!"
    kmc "Well, shall we party?"
    n "That we shall!"
    "Natsuki would rummage in her bag and would pull out a portable speaker."
    "Everyone gives her a funny look."
    n "Ahem...I use it for bathroom parties, ok?"
    m "...Alright, I suppose."
    "Natsuki puts on some high energy dance music."
    n "Now this is good shit!!"
    y "Natsuki..."
    n "Nope, don't even! I'm not letting you all turn this into a pity party! This bitch is gonna have some energy!"
    m "We understand, but maybe something less...'rave-esque' and something at least a bit less high energy?"
    n "Ugh, buzzkills, I swear!!"
    s "Just let me pick the music!"
    n "Cold day in hell! You're probably gonna find a My Little Pony Intro 10 Hour loop to put on!"
    s "I would not! Monika, don't you trust me to pick music?"
    n "Doesn't matter what Monika thinks, it's my speaker, paired to my phone!"
    m "Natsuki, we didn't even plan on having music, but it seems that your taste is a bit...too hype for what we're going for."
    n "That was only a bit of the first song!"
    n "You're actually gonna judge me off of a snippet of the {i}first{/i} song I put on?"
    m "...{w=1.5}just...let Sayori {i}try{/i}. For all of our sakes?"
    "Sayori turns to Natsuki with puppy dog eyes."
    n "No! I don't want to!"
    s "Ple{w=0.7}e{w=0.7}e{w=0.7}e{w=0.7}e{w=0.7}e{w=0.7}e{w=0.7}e{w=0.7}e{w=0.7}ase?"
    n "Ugh, fine!!!"
    "Natsuki fiddles with her phone, unpairing it from the speaker."
    speak "デバイスを検索しています"
    "Natsuki rolls her eyes."
    n "There, now pair your stupid phone."
    s "I will!"
    "Sayori sticks out her tongue, before messing with her own phone, trying to find the device."
    s "Is it called 'ナツキの超超クールスピーカー'?"
    "Natsuki gets in a blushing fit."
    n "S-Shut up!"
    s "Ehehe! Guess that's your way of saying 'yes'!"
    "Sayori pairs her phone."
    speak "ペアリングされました。"
    s "Alright, now time to put on something that'll match the mood!"
    n "I swear if I hear any cartoony bullshit exit my speaker, I'm gonna rip your damn hair out."
    "Sayori blushes in a nervous sweat, the pressure is on."
    s "Uh...ok, I think this is good..."
    n "It better be."
    "Sayori puts on something more everyone's speed."
    "Natsuki was about to yell, but she looked at everyone's expressions."
    "Specifically Kotonoha's."
    m "Koto, does this sound nice to you?"
    menu:
        "This is much better!":
            $ choice = "right"
        "I liked Natsuki's music better.":
            $ choice = "WRONG"

if choice == "right":
    jump shared_route1

elif choice == "WRONG":
    "Koto's face kind of shifts."
    kmc "I'm not sure...I think I like Natsuki's music more..."
    kmc "Sorry Sayori."
    show sayori glitch
    s "{glitch}{glitch}{glitch}{glitch}{glitch}{glitch}
    {glitch}{glitch}{glitch}
    {glitch}{glitch}{glitch}{glitch}
    {glitch}{glitch}
    {glitch}{glitch}{glitch}{glitch}{glitch}
    {glitch}{glitch}{glitch}{glitch}{glitch}{glitch}"
    hide monika
    pause (2.0)
    show monika 1a at t11
    m "Wrong choice. Pick again."
    menu:
        "This is much better!":
            $ choice = "right"
        "I liked Natsuki's music better.":
            $ choice = "WRONG2"

if choice == "right":
    jump shared_route1

elif choice == "WRONG2":
    m "WRONG."
    m "P{w=0.4}I{w=0.4}C{w=0.4}K{w=0.4} A{w=0.4}G{w=0.4}A{w=0.4}I{w=0.4}N."
    
    menu:
        "This is much better!":
            $ choice = "right"
        "I liked Natsuki's music better.":
            $ choice = "WRONG3"

if choice == "right":
    jump shared_route1

elif choice == "WRONG3":
    m "Hm. I see."
    m "I can play that game too, silly!"
    m "While I can't seem to make any huge changes to your game like deleting your saves..."
    m "Or disable the skip button..."
    m "I sure as hell can piss you off!{nw}"
    m "See you soon.{nw}"
    return


label shared_route1:
    show monika 1m at t51
    show sayori 4x at t52
    show natsuki 5y at t53
    show yuri 4a at t54
    show koto 1f at t55
    "Koto was smiling."
    kmc "You made a good choice, Sayori."
    kmc "Sorry, Natsuki."
    n "Ugh, whatever."
    m "Natsuki, don't."
    "Natsuki rolls her eyes."
    pause (2.0)
    #have someone emote
    kmc "Well, what are we standing around for?"
    kmc "You guys got this all together last-minute, and even though I didn't pick your music, Natsuki..."
    kmc "I agree with you."
    kmc "If we're gonna have this party, it's not gonna be out of pity!"
    "Natsuki smirks at the mention, she's glad her voice hadn't completely fallen on deaf ears."
    s "Koto{nw}"
    n "AHEM. {w=0.5}"
    s ".{w=1}.{w=1}.{w=1}Natsuki...{w=0.5}is right..."
    s "This party needs to be super happy and fun! My playlist is gonna make sure that the mood is up, up, up!!"
    y "Let's not forget, we're at school."
    y "We still need to be civil and quiet."
    m "Yuri's right, let's not completely forget where we are. Let's not make our club neighbors mad."
    n "Again..."
    s "Oh, right, that time we got into it with the anime club!! How'd that even happen?"
    y "I believe it was because of you or Natsuki."
    s "What?! It defintely wasn't me!! I think..."
    s "I'd remember something like that! It had to be Natsuki!"
    n "Me? Hell no, it wasn't! Like you said, you think!"
    n "You must have short term memory loss or something!"
    m "Girls, girls, Calm down."
    n "Hmph."
    pause (1.0)
    y "Didn't it end up being a good thing in the end?"
    m "Hmm...{w=1}Oh, you're right, Yuri! We started a little 'war' with them!"
    y "Mm...something like that."
    n "Oh, right, how could I forget! Me and Sayori had our own little division away from you two."
    m "...Really?"
    s "Ehehe, it's true!! I was like a spy!"
    y "Sayori, you little sneak."
    "Sayori and Yuri snicker."
    s "It was fun!!"
    n "And of course, {b}I{/b} was the mastermind behind it all!"
    m "Mastermind behind..."
    m "Oh. My. Goodness."
    y "That was the 'foul play' they accused us of!"
    y "You could've jeopardized our chances of winning!"
    n "C'mon, I was HELPING, jeez..."
    n "And since when do you care about winning?"
    y "What can I say? I'm a competitive person."
    n "..."
    n "ANYWAY.{nw}"
    n "You all were taking too long to make a move and I was ready to do something!"
    n "Not do 'war room' bullshit."
    m "Did you really have to rope Sayori into it though?"
    s "I wanted to join, she didn't force me!"
    "Monika and Yuri's faces shift strangely."
    m "...Really?"
    n "Oh yeah, trust me, I was kidding earlier."
    n "She was the one that came up with more than half of it!"
    n "I was shocked myself."
    "The girls look at Sayori."
    s "What?"
    s "I can't be bad sometimes?"
    y "I...I suppose so..."
    m "Everyone has been bad at some point in their life, I guess..."
    s "What, now I can't be honest?!"
    m "No, Sayori, it isn't that-{nw}"
    "Sayori speaks as she begins to giggle."
    s "Man, you all are confusing..."
    "The giggling is infectious and before long the entire club was giggling."
    "After hopping from one talking point to another, the giggling turned to laughing, and the girls we're now crying with laughing while trying to continue the conversation."
    "Everyone except{nw}"
    kmc "Me."
    "Koto had been silent the entire time, watching and listening to her friends bring up memories."
    "They all looked genuinely joyous, reminiscing on memories."
    "Man, I'm gonna miss them."
    "So, so bad."
    "Koto looks around, soaking in the environment."
    "The familiar posters on the wall, the chairs they'd rearranged a hundred times."
    "Even the stray paper clips scattered around—they all felt like a part of her."
    "She wanted to take a mental picture, to remember this exact moment."
    "She knew she might never sit in this room with them again, never hear the exact blend of their voices overlapping, laughing, bickering in that way only they could." 
    "It felt surreal, like she was a ghost haunting her own memories."
    "The sound of Sayori's infectious laughter echoing, the way Natsuki's voice rose over everyone else's."
    "Monika's quiet but amused gaze, and Yuri's shy smile that lingered longer than usual."
    "How did it come to this?"
    "How did I let them mean so much?"
    "Each one of them has left a mark, a piece of themselves with me...and I don't know if I can leave that behind."
    hide monika 
    hide natsuki
    hide sayori
    hide yuri
    show koto 1q at t11
    pause (1.0)
    show koto 1p at t11
    pause (1.0)
    show koto 1q at t11
    pause (1.0)
    show koto 1p at t11
    pause (1.0)
    show koto 1p3 at t11
    pause (2.0)
    show koto 1p2 at t11
    kmc "Why is saying goodbye so hard?"
    kmc "Why can't I just tell them goodbye and be on my way?"
    kmc "Why can't we just have a simple group hug and just move on?"
    kmc "This feels pointless..."
    show koto 1o at t11
    #have static fade gradually sooner than this
    "Koto swallows, willing herself not to show any of the turmoil she feels. It's just one room. Just one goodbye." 
    "But her mind keeps bringing up the little things." 
    "Things she thought she'd forgotten: the times they shared snacks, the jokes that didn't even make sense but left them all in laughing fits like it was the funniest thing any of them had ever heard."
    "She thinks of the late evenings after the club, the quiet moments between them when they were all just...together, without needing any reason for it."
    "She glances around the room one more time, taking in the copious amount of emotion from the other girls. The mood of the room is happy." 
    "Too happy to be feeling like this, but she can't help it. Her heart aches, knowing that this is the last time they'll be together like this."
    kmc "I wish...I wish I could freeze this moment."
    kmc "Just for a little longer."
    kmc "Why can't things just stay the same, just a little while longer?"
    "Koto clenches her fists, as if somehow gripping tightly would stop time from slipping by."
    kmc "It's strange… I never thought saying goodbye would feel this… empty."
    kmc "All these memories, all these pieces of them... and I just have to leave them here?"
    "For a moment, Koto considers saying something, but she stops herself, the words caught in her throat. What could she possibly say to explain everything she's feeling? And would they even understand?"
    "She sighs, almost wishing for something, anything, that would give her the strength to walk away from all this."
    pause (5.0)
    #cut it off when yuri arrives
    show yuri 1a at t21
    show koto 1a at t22
    y "Are you okay?"
    "Kotonoha snaps out of her little daze, holding her head for a second."
    "She slowly turns to her cousin and smiles a sweet smile before taking a tiny sip of her tea."
    kmc "I'm okay, Yuri. Promise."
    y "If you say so, Koto."
    "Sayori looked up from her cupcake, speaking with her mouth full." #make cupcake mess for sayori like I did for natsuki
    show sayori 1a at t52
    show yuri 1a at t54
    show koto 1a at t55
    s "Mmf!! Boff uv yu! Come over here!!"
    "Sayori starts to choke."
    show natsuki 1a at t51
    "Natsuki rolls her eyes and smacks Sayori's back, making the lodged piece of cake fall out of her mouth."
    n "First of all, don't talk with your mouth full."
    n "And SECOND! DON'T WASTE MY DAMN CUPCAKES OR I'LL RIP YOUR HAIR OUT ANYWAY!"
    "Sayori covers her head."
    s "Okay, okay!! Stop trying to yank my hair out!!!"
    kmc "We should probably get back over there before they kill each other..."
    y "Wise idea."
    "Yuri chuckles as she grabs Kotonoha's hand and forces her over with the rest of the girls."
    hide sayori
    hide yuri
    hide natsuki
    #find a better way to make her look like she's slowly moving across the screen with the one line below
    show koto 1j at t55
    show koto 1j at t54
    show koto 1j at t53
    show koto 1j at t52
    show koto 1j at t51
    "Koto smiles and giggles, allowing herself to be dragged into the moment."
    #then find a way to get rid of koto that doesn't just blip her out of existance    
    "At first, she's hesitant, but she quickly joins in on the jokes, sharing personal stories she'd never thought she'd share."
    "As they laugh together, there's a warmth in her chest—like all the emotions she's been holding back are finally spilling out in this little room." 
    "It's not long before tears are streaming down her face; tears of joy mixed with something deeper, something harder to let go of."
    pause (3.0)
    show monika 1a at t11
    "Monika repeatedly glances at the clock on the wall, a slight furrow in her brow."
    "Her foot taps rhythmically against the floor, her thoughts elsewhere—she's holding onto her usual calm but can't fully mask her impatience."
    "She keeps thinking about the code, the errors she's felt, the subtle shifts. She needs to check it, to understand what's going on."
    "{i}RING RONG RING{/i}"
    sspeak "Attention students, the time is 5:45. Please wrap up your club activities and clean your classrooms!"
    sspeak "All clubs end at 6 and all students must be out of the building by 6:15."
    sspeak "Have a great rest of your day!"
    "{i}RING RONG RING{/i}"
    "Monika looks up and quickly jolts upwards, stepping away from her desk."
    m "You heard the lady, you guys! Time to start cleaning up!"
    show monika 1a at t51
    show sayori 1a at t52
    show natsuki 1a at t53
    show yuri 1a at t54
    show koto 1a at t55
    s "Wait!!"
    "Monika pauses before rolling her eyes to the side, turning to face Sayori at the same time."
    m "What is it, Sayori..?"
    s "I have stuff to say!!"
    #have monika look mildly annoyed (just 1h again? idk maybe make new sprite)
    #also have them react to one another, like when sayori goes to hug koto
    #move her again and when natsuki talks about all the members have them react
    #and have her also be close to koto to punch her in the arm
    m "...What kind of stuff?"
    "Sayori stands up, one foot on her desk and the other on her chair."
    s "I wanted to send Kotonoha off with a special something!"
    "Monika looks like she's about to snap."
    "Yuri perks up."
    m "How...kind..."
    y "I was actually thinking the same."
    n "Same..."
    "Monika tried to put on a calm face, but she just wanted to delete them all and just check the code."
    "She was getting a bit too antsy."
    "Ultimately, she sighed and let Sayori have the floor, sitting back down."
    s "I just wanted to let you know that wherever you go, we'll still be your friends!"
    s "You've been one of my bestest friends ever, and you've helped me through so much!!"
    s "So...so much...ehehe..."
    "And with that, Sayori steps down from the desk and dashes over to give Kotonoha a big hug."
    kmc "A-Ah...thank you, Sayori..."
    "Kotonoha hugs Sayori back loosely before letting her go and imploring her to go sit back down."
    "Sayori whines and protests per usual but eventually she complies."
    "The room quickly went silent."
    "Obviously, not for too long. Natsuki quickly piped up."
    n "MY TURN!"
    n "So listen up!"
    m "...No one was talking {nw}"
    n "WELL NOW YOU ARE SO SHUT YOUR TRAP!!"
    show monika 1h at t51
    m "..."
    "Natsuki clears her throat dramatically."
    n "Alright..."
    n "Kotonoha, you are a stick in the mud."
    kmc "Uh...?"
    n "And so is your freaky cousin. And Monika."
    n "And Sayori's just stupid."
    "Sayori's face falls."
    n "But! You're a good person. And an even better friend."
    n "And...{w=1}even if I don't show it, you all are like...{w=1}my only friends."
    show natsuki 5g at t53
    pause (1.0)
    show natsuki 5h at t53
    n "I appreciate you all."
    "She then promptly goes silent."
    kmc "Well...that was..."
    kmc "Have you ever done this before?"
    n "HEY! Be appreciative! You're lucky I even gave you a speech!"
    "Natsuki punches Koto's arm."
    kmc "Ouch!"
    pause (2.0)
    n "...{w=1}Sorry."
    kmc "...I guess you're right...{w=1}in a sense."
    kmc "You're never usually that nice so I guess I should appreciate your speech."
    n "That's what I thought!"
    "Natsuki smirks confidently as she plops back down in her seat."
    "Everyone then looks to Yuri."
    "Yuri seems to seize up and stutter out an excuse."
    #yuri 4c
    y "U-Uhm...m-my..erm..."
    y "I-I don't...not anymore..."
    "She shrinks in her seat."
    m "Welp, that's the end of that!"
    m "Club time is OVER!{nw}"
    m "No more interruptions!{nw}"
    m "No more jump-ins!{nw}"
    m "Pack up!!"
    "The club members begin to clean up after themselves, taking down the banner, sweeping up cupcake crumbs and wiping up tea spills."
    scene bg club_day with wipeleft_scene
    pause (2.0)
    hide sayori
    hide natsuki
    show monika 1a at t31
    #or 1o for yuri
    show yuri 4b at t44 
    show koto 1a at t32
    show monika 1b at t31
    m "You know you didn't have to stay after and help clean up."
    m "It was your party!"
    show monika 4a at t31
    kmc "Eh, I don't mind."
    kmc "Couldn't leave it a mess over the weekend!"
    show monika 1r at t31
    "Monika sighs defeatedly."
    #make edited expression of "e" with mouth open
    show monika 4e at t31
    m "Well I appreciate it."
    "Kotonoha nods as she throws the last of the trash away."
    kmc "That seems to be the last of it!"
    m "{size=12}Finally.{/size}{nw}"
    kmc "Hm?"
    m "Nothing! I'm just going to go ahead and...{w=1}get out of here!"
    m "You can lock up! You have a key! Just slip it in my locker before you leave!"
    kmc "Wait, but your locker is!{nw}"
    hide monika
    "Monika slams the door behind her."
    kmc "...far from the clubroom..."
    "Koto sighs."
    show yuri 4b at t22 
    show koto 1a at t21
    y "I-I can do it..."
    "Kotonoha looks behind her."
    kmc "Yuri! I thought you had left with the others!"
    y "N-No..."
    y "I can go drop off the key once you lock up though..."
    kmc "Really, Yuri?"
    "Yuri nods her head timidly."
    "Kotonoha promptly sighs."
    kmc "Alright, thank you."
    "Yuri and Kotonoha exit the clubroom."
    scene bg corridor with wipeleft_scene
    show yuri 4b at t22 
    show koto 1a at t21
    "Yuri holds out her hand for the key."
    kmc "Hold up."
    "Kotonoha shuts the clubroom door and locks it."
    kmc "All yours."
    "Kotonoha smirks before tossing the key to Yuri."
    "Yuri fumbles with it in her hands before firmly grasping it."
    y "I-I'll go drop this off..."
    y "{size=15}Meet me outside.{/size}"
    "Kotonoha was used to her cousin's random volume changes, but it was usually for a reason."
    "And this time was no different. However, this time she had no clue why."
    "To avoid another long conversation, at least at the moment, she just nods."
    "She still needed to get back home and pack."
    kmc "Got it."
    "And with that, Yuri walked away, presumably towards Monika's locker."
    "Kotonoha went the opposite way, towards the stairs."
    scene bg TFJ with wipeleft_scene
    pause (0.3)
    scene bg SS with wipeleft_scene
    pause (0.3)
    scene bg SL with wipeleft_scene
    pause (0.3)
    scene bg SCY with wipeleft_scene
    pause (0.3)
    scene bg FOTS with wipeleft_scene
    show koto 1p3 at t21
    pause (2.0)
    show koto 1p2 at t21
    kmc "Where is she? It's been 15 minutes.."
    "Yuri walks out of the school building, keyless."
    show yuri 1a at t22
    y "Sorry, I took a bit too long...needed to use the..uhm..{w=1}bathroom..."
    kmc "Thanks, Yuri...you really saved me a lot of walking."
    y "No problem..."
    pause (1.0)
    y "Shouldn't you get home?"
    kmc "Oh? I thought you we're coming with?"
    y "I'll be there. Go without me."
    kmc "Hm...alright, see you there!"
    y "M-Mhm."
    "Kotonoha walks down the street, opting to take the tram to save time."
    "Yuri stares at her cousin wistfully before she turns, heading to her own house."
    scene black with wipeleft_scene
    pause (2.5)
    scene bg MCR with wipeleft_scene
    show koto 1bp at t11
    kmc "Ugh!"
    kmc "I can't bring everything! But I can't not bring..."
    pause (1.0)
    kmc "I'm gonna give myself a headache..."
    "Kotonoha puts her hands on her head and grips tightly."
    "Before she can have a full on meltdown, she hears a knock at her door."
    "She sniffles and wipes would-be tears from her eyes."
    kmc "Come in..."
    pause (1.0)
    y "I hope you don't mind me letting myself in..."
    kmc "N-No, its'..."
    kmc "..It's okay."
    y "I just thought I'd come over to help you pack!"
    "Kotonoha finally looks at her cousin, seeing her outfit change."
    show yuri 5ct at t22
    show koto 1bp at t21
    "She looked...different. But nice."
    kmc "You look..."
    y "I-Is it messy?? Oh, I knew I should've just worn my sweater..."
    kmc "No, I'm sorry."
    kmc "It looks good. Promise."
    pause (0.5)
    #change her expression to be happy.
    y "Thank you."
    "Kotonoha nods before looking back towards her dressers before she chuckles."
    kmc "I'm stuck, Quill."
    y "On?"
    kmc "I don't know what to pack!"
    kmc "I can't bring half the things I want!"
    y "...{w=1.5}Aren't you moving completely?"
    kmc "{w=1}Goddammit..."
    "Kotonoha grips her head again"
    kmc "How the hell did I forget that??"
    show layer master at heartbeat
    show vignette at vignettefade (5)
    play music ("HeartBreath.mp3") fadein 5.0
    kmc "My parents are gonna probably have trucks to come take my stuff to my new place!"
    kmc "Gah, I'm an idiot!"
    kmc "I can't do anything right, and now I'm about to be alone!"
    kmc "What is even going on???"
    hide yuri 
    show koto 1bp at t11
    kmc "I can't do this..."
    kmc "{cps=*2}I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't I can't{/cps}{nw}"
    y "Hey.{nw}"
    hide vignette
    show layer master
    stop music fadeout (1.0)
    pause (2.0)
    show yuri 5ct at t22
    show koto 1bp at t21
    y "You're going to be okay."
    kmc "But{nw}"
    y "You. Will. Be. Okay."
    y "Okay?"
    pause (3.0)
    #have koto emote
    kmc "O-Okay..."
    y "Now, shall I help you pack? Or are we just going to sit here?"
    pause (1.0)
    kmc "Pack..."
    y "Then let's not waste any more time, ok?"
    kmc "A-Alright...Thank you again, Quill."
    y "Mhm..."
    "Yuri would begin to pull out drawers from Kotonoha's dressers."
    y "Now we're just going to use the attic method."
    y "We don't have much time however, which means we must move quickly."
    kmc "R-Right, right."
    kmc "Let's get through this. Together."
    y "And quickly."
    "Yuri chuckles before she begins to pull clothes out of Kotonoha's drawers and held them in front of her."
    "Koto picked and chose certain tops and shorts through the multiple pairs she was shown."
    "Over the next few hours, they developed different piles. 'Take Up' and 'Throw Away' just to name a few."
    "After a while, Koto's room was empty, besides her furniture. Her new place was apparently already furnished and move in ready."
    "Wherever she was going, it sounded prestigious. Of course, this entire family tree had the money to back it up, but Kotonoha had never seen their wealth be used for anything this...expensive-sounding before."
    "But whatever the case, she picked up her somewhat stuffed suitcase, and wheeled it to her bedroom door."
    "She turned around and stared at her bedroom, her fingers unknowingly tracing the wood of her door."
    y "...Are you going to be okay?"
    kmc "...{w=1}I should be."
    "Koto embraces Yuri in a tight hug."
    kmc "Thank you...so much."
    y "I-It's nothing. Honestly."
    "Yuri hugs back tightly."
    kmc "Gosh, you're going to make me cry..."
    "Yuri pulls back, holding Kotonoha within arms reach."
    "She uses one of her thumbs to rub away one of Kotonoha's stray tears."
    y "This is no time to cry, Koto."
    y "This is...a time to celebrate."
    y "Tell me why you're moving."
    kmc "Because my parents hate me."
    "Kotonoha would roll her eyes as she says this."
    y "No, dearest cousin. It's because your parents saw an amazing opportunity for you."
    y "It's just unfortunate that that opportunity isn't here."
    y "This is good for you. I want you to understand that. Please?"
    kmc "I understand, I just..."
    "Koto pulls away from her cousin."
    kmc "I'm not ready."
    kmc "I know I usually keep a level head but this is all super stressful."
    kmc "I just needed time to process this and I've virtually had none."
    kmc "I'm just..."
    y "I understand."
    y "I just don't want you to be stressed out about it, alright?"
    "Kotonoha chuckles."
    kmc "It's hard not to."
    kmc "The only thing I can think about is the future."
    kmc "Where I'm going, what I'm gonna do when I get there."
    kmc "It's really a lot."
    "Yuri sighs."
    y "I guess I don't truly understand you, Kotonoha."
    y "It's you leaving, not me."
    y "And I assume you know that's why I can't console you properly."
    "Yuri begins to chuckle and Kotonoha follows suit."
    kmc "We read each other like books."
    kmc "I saw the look in your eyes when you realized."
    y "I just figured that."
    y "Which I also assume means you know that all I can send you off with is well wishes."
    kmc "I do, unfortunately."
    y "You're going to be alright."
    "Kotonoha finally sighs a long and deep sigh, her shoulders falling an immense amount. It looks like she's finally relaxed a bit, even if only a little."
    kmc "I know."
    "Yuri looks like she's about to interject."
    kmc "Yes, for sure."
    y "I'm glad you finally believe in yourself."
    y "Now, let's go get something to eat."
    "With that, Kotonoha replants her palm onto her door, before loosening her muscles and letting her fingers slide across the wood."
    "They trailed downwards towards her door handle."
    "She gripped the knob firmly and took one last look at her now barren room, minus the box that sat on her bed that said 'Take Up'."
    "Everything in that box was anything she couldn't fit in her suitcase."
    "She heard Yuri carrying the 'Throw Away' box down the stairs."
    "Kotonoha lets out one last breath that she didn't know she was holding, and closes her room door."
    "She quickly proceeds down the hallway downstairs to pursue her cousin."
    scene bg MCH with wipeleft_scene
    pause (0.3)
    scene bg MCUL with wipeleft_scene
    pause (0.3)
    scene bg MCL with wipeleft_scene
    pause (0.3)
    scene bg MCLR with wipeleft_scene
    pause (0.3)
    scene bg MCK2 with wipeleft_scene
    kmc "Alright, what screams 'going away meal'?"
    y "You don't have much time before you go."
    kmc "Hmph...you're right..."
    pause (2.0)
    kmc "Pizza?"
    y "I don't see why not."
    "Kotonoha pulls her phone out and dials up a pizza place."
    "She hangs up after a few seconds."
    kmc "Done!"
    "Just as she exclaims, her parents burst in the door, their arms full of party adjacent items."
    km "Whew! I told you we probably needed to make a few trips!"
    kd "Well, I thought it'd be more efficient to{nw}"
    "Kotonoha's Father's eyes widen."
    kd "Uh...honey. She's down here."
    km "WHAT?!"
    "Kotonoha's Mother nearly drops the stuff she's carrying."
    "Yuri chuckles."
    y "So much for the element of surprise."
    y "You're late, both of you."
    km "Thank you, niece."
    y "No problem."
    y "Now chop, chop! We just ordered some pizza, so we need to get set up!"
    kmc "W-What is this...?"
    y "Well...I might've come to help you...{w=0.7}but I also might have been a distraction..."
    y "We were planning on throwing you a going away party..."
    kmc "Wow...that's super scummy...{w=2}BUT ALSO SO SWEET!!!"
    y "But unfortunately, my aunt and uncle are late."
    km "Do you know how hard it is to get things custom made like this on such short...notice..."
    kmc "Do you know how I feel now?"
    km "Koto, sweetie...we need to talk later. You and me."
    "Koto nods before staring daggers into her father while crossing her arms."
    kmc "I think you know I'm owed an apology for how you spoke to me this morning." 
    kd "I do, actually. I've been thinking about that all day. While I was at work and everything."
    "He sets his share of things down at the door and holds his arms open for Kotonoha."
    "She rushes into his arms, hugging him after rejecting his touch earlier this morning."
    kd "You're my little girl, and you know I would never talk to you like that on any other day."
    kd "Your mother left me to explain by myself and I was a tiny bit upset about that."
    "Kotonoha looks up at him, her arms still locked."
    kmc "A bit??"
    kd "It upset me more than I'd like to admit, especially to your mother."
    "He chuckles as she says this."
    "Koto buries her face back into her father's chest."
    kmc "{w=1}...I forgive you."
    "She squeezes her father tighter."
    kd "I'm glad you do. I love you, snowdrop."
    kmc "I love you too, Dad..."
    kd "Now why don't we help your mother and your cousin with setting up?"
    kmc "Kind of ironic how I have to set up my own party, hm?"
    kd "Something like that. We should hurry though."
    kmc "Yeah, or else Mom's gonna kill you."
    "They'd both chuckle as Kotonoha helps her father pick up some of the stuff and they both waddle over to the kitchen and help set up."
    "After a short while, everything would be set up and they'd all sit down, as Yuri comes back to the table with the pizzas."
    "Yuri sighs."
    y "20 dollars later..."
    "Kotonoha chuckles."
    y "You said you ordered 'A' pizza!"
    kmc "Well when Mom and Dad came, I ordered more! We gotta feed 4 people!"
    y "Fair..."
    kd "What's wrong, Yuri? Don't want your auntie and me eating all that food?"
    y "Ha ha, very funny."
    "Yuri rolls her eyes as she sets the boxes down on the kitchen island."
    y "Dig in."
    "As if on cue, everyone reaches for the top box."
    y "Wait!{nw}"
    "Yuri interrupts."
    km "What is it?"
    y "Since this is a celebration, I feel as if we should say a few quick words."
    "Kotonoha's parents groan in an elongated and admittedly childlike fashion but Kotonoha leans forward." 
    "She didn't get to hear Yuri's words at the party the club threw for her. This was Yuri's chance to express herself around family."
    "Yuri gives a shaky exhale before she presses on."
    y "I just want to say that..."
    "Yuri's face heats up in embarrassment, just like earlier."
    "That was, until, she saw Kotonoha's intense gaze on her."
    "However, it wasn't a scrutinizing gaze. It was a sort of 'you got this' look."
    "It gave Yuri a lot of silent confidence."
    "Out of the corners of her eyes, Koto saw her parents giving bored, uninterested, or plain annoyed looks."
    "She elbows both of them slightly, telling them to fix their faces."
    "Yuri notices this display and smiles slightly, her confidence boosting even more."
    "Kotonoha decides to speak up and give Yuri verbal confidence."
    kmc "Continue, Yuri. You got this."
    "Yuri smiles brightly, her confidence now at an all time high."
    "She lets out one more exhale before speaking in an emboldened tone."
    y "Kotonoha Ozuo, you've been more than a cousin to me. You've been my friend, confidant, and so much more. You're the person I've looked up to most of my life."
    y "I'm glad we've lived close enough to each other to grow up together, and build a close relationship that most people don't get to have with closer people in their lives."
    y "Thank you...for everything..."
    "She starts to tear up."
    kmc "Yuri...wow...thank you so much, I don't even know what to{nw}"
    "Yuri practically hops the table and gives Koto a huge hug."
    y "I'm going to miss you, Kotonoha..."
    kmc "I'm...I'm gonna miss you too, Yuri."
    "They stand there and embrace each other as Yuri's tears start to stream."
    "Kotonoha's own eyes started to water and before long, both of them were quietly swaying back and forth in each other's arms, crying softly."
    "As they are hugging, Kotonoha's mother taps her glass with her nails."
    km "Ahem."
    "The girls would turn to face her."
    km "Kotonoha. I wanted to apologize for my actions this morning. I wasn't there for you when you needed a shoulder to cry on."
    km "So, I wanted to do this for you. Have this party...for my beautiful baby girl. "
    km "This isn't a send off. It's a celebration. This shows how far you've come."
    km "Top of your class, time and time again, being charitable and..."
    km "Honestly, I wouldn't have it any other way...I wouldn't want anyone else to be my daughter."
    km "So...this is a celebration for you."
    km "For new oppurtunities. For you to do greater things. For you to spread your wings and fly."
    "She pauses to let Kotonoha speak."
    kmc "Is this bird too big to hug her mom goodbye one last time??"
    "Koto starts tearing up again."
    km "Of course not, Snowdrop!"
    "Kotonoha's Mother joins the hug."
    kd "C-Can I join?"
    y "Come here!!"
    "Yuri pulls her uncle into the hug, now encircling Kotonoha."
    "After about 15 minutes of them getting their tears out, they finally began to eat."
    kmc "Ughh...I love this pizza..."
    kd "It is really good. We haven't had it in years!"
    km "You used to beg for it on Friday nights when you were a kid."
    kmc "Exactly! That's why I ordered it—for the nostalgic taste!"
    y "I'll say one thing that isn't great...these wings..."
    km "That's one thing I'll agree with you on, they taste..."
    kd "Raw."
    kmc "Yeah, let me just throw these away..."
    "Kotonoha aims for the trash can and launches the container of wings into the garbage."
    kmc "LeJordan!"
    y "That's not...never mind. Nice shot."
    kmc "Thanks!"
    "Yuri shook her head, amused, while Kotonoha sat back down, taking another bite of pizza."
    km "Do you remember when we went to the summer festival all those years ago? You insisted on winning that giant stuffed cat from the ring toss."
    kmc "Of course I do! You told me I'd never win it, but then I nailed it on my first try!"
    kd "And then you had to carry it around all night. By the end, you were begging us to hold it for you."
    kmc "Uhh, if I remember right, Mom made you carry it eventually, and it was heavy for a {b}9 year old{/b}, {i}right?{/i}"
    kd "Hmph. Fair."
    y "I remember when you had gotten back and you brought it over my house. You refused to admit you'd made a mistake until the very end."
    kmc "Well, I don't regret it. That cat looked great in my room for years."
    km "It's still there, isn't it?"
    kmc "Yeah, well...I couldn't fit it in my suitcase..."
    kd "Hm, I'm surprised it didn't fit in your suitcase."
    kmc "Well, it's meant for clothes, Mom. I had to sit on the lid to get it to close as is!"
    kmc "Plus...I think he's had his fair share of years with me..."
    kmc "When Yuri was helping me pack earlier, it made me realize that."
    kmc "I might sell him back to the fair owners for some spare change or thrift him."
    kd "Whaaat, seriously?"
    km "You used to carry that thing everywhere with you!"
    kmc "I know, I know but...I'm older now...{w=2}I think it's about his time."
    y "Did you forget the fact it reeks?"
    y "Seriously, did you guys never think to wash it?"
    kd "That's one of the perks of carrying it everywhere, it collects memories!"
    km "Of course, to you, smells equal memories."
    "They all collectively laughed , the memory bringing a wave of warmth to the table."
    y "You know, for all the teasing, you've always been persistent. You don't back down easily."
    kmc "That's one way to put it. I prefer 'determined.'"
    km "And that determination will serve you well, wherever you go."
    "Their laughter gradually gave way to a comfortable silence, each of them lost in their thoughts."
    "After a while, Kotonoha leaned back with a satisfied sigh."
    kmc "Okay, I'm stuffed. But that was worth every calorie."
    kd "I agree." 
    y "Didn't you say you were trying to watch your figure?"
    kmc "Uh, rude much? Also it's my going away party! Let me live!"
    y "Just saying..."
    kd "Now now, girls. Koto, sweetheart, why don't you go grab your things while we clean up here?"
    kmc "Alright alright, I'll try to be quick."
    "Kotonoha went to get her suitcase, taking a few minutes to reflect."
    scene bg MCR with wipeleft_scene
    "All of this was happening way too fast."
    "But...it kind of got more exciting throughout the day."
    "This rush to hurry and say goodbye, especially since the day had gone ever so perfectly."
    "She got to see everyone she wanted, she got to make amends with her parents, everything felt...perfect."
    "But she couldn't shake this weird feeling she felt inside."
    "The feeling that...{nw}"
    pause (1.5)
    "She needed to hurry."
    "She quickly grabbed her suitcase, and rushed out of her room."
    scene bg MCH with wipeleft_scene
    pause (0.1)
    scene bg MCUL with wipeleft_scene
    pause (0.1)
    scene bg MCL with wipeleft_scene
    #have koto show up first with a surprised face and pause for dialouge
    "...When she came back downstairs, everyone was lined up off the wall."
    "First Yuri, then her mother, then her father."
    "She walks down the stairs with a big goofy grin on her face."
    kmc "How do you guys keep doing this?!"
    y "Still surprised, {i}snowdrop{/i}?"
    kmc "Haha."
    "She ran to Yuri first, pulling her into a tight embrace."
    y "I love you."
    kmc "I love you too."
    y "You better keep in touch, okay?"
    kmc "Obviously. You can't get rid of me that easily, {i}Quill{/i}."
    y "And you'd better stay safe, okay?"
    kmc "You know I always am."
    "Kotonoha would pull back and they would stare each other in the eyes."
    kd "Ahem, where's our love?"
    "Yuri gave a little nod to Kotonoha, who laughed and stepped toward her parents."
    kmc "Don't worry, I didn't forget about you!"
    "She runs to them both, encircling them both."
    km "We're so proud of you, sweetheart. Don't ever forget that."
    kd "And remember, no matter where you are, you'll always be our daughter."
    kd "You were built for this."
    km "Don't forget where you came from."
    "Kotonoha chuckles before straightening her face."
    kmc "I won't. Promise."
    "Kotonoha's Mother wipes a tear from her eye."
    km "Now, go go!"
    km "Your driver is waiting for you..."
    kmc "Right..."
    "Koto pops the handle to her suitcase."
    "I love you both."
    pause (0.3)
    scene bg RH with wipeleft_scene
    #maybe edit a car in and shrink and redefine sprites to look like their at the doorway of the house?
    "Kotonoha sighs as she walks slowly to the black car outside."
    "She doesn't bother to turn around as they all call for her."
    km "We love you!!"
    kd "Stay safe!"
    pause (1.0)
    y "{size=15}Good Luck.{/size}"
    "Kotonoha opens the trunk and puts her suitcase in the trunk and she has to instinctively turn around."
    "She gets teary-eyed as she sees them standing in the doorway."
    "She shakes her head and waves goodbye back before getting in the car."
    c "Where to?"
    "He speaks in a joking tone but Koto doesn't seem to pick up on it."
    "She wipes away a stray tear and responds."
    kmc "You know where, Reginald."
    reg "Of course. My apologies, Ms Ozuo."
    kmc "It's fine..."
    "She wipes another stray tear from her cheek."
    kmc "Let's just go...please."
    reg "Yes, ma'am."
    "They begin to drive down her long driveway, and she sees her family in the rearview mirror."
    "Reginald fixes the mirror."
    pause (2.0)
    kmc "Can we stop and get McDonalds?"
    reg "Did you not just enjoy some pizza inside?"
    kmc "I'm still hungry, please?"
    reg "Hm, someone's in the mood for American."
    kmc "Y'know, pizza is Italian, so TECHNICALLY, I'm craving Italian and American."
    "Reginald chuckles."
    reg "I'm well aware where pizza comes from. Just teasing, ma'am."
    "Kotonoha crosses her arms and pouts as she finally straps herself in."
    kmc "So???"
    "He sighs."
    reg "...I'll put it on your mother's account. I'm sure she wouldn't mind."
    kmc "Thank you, Reggie. You're the best."
    reg "Of course, Ms Ouzo."
    kmc "C'mon, you've been calling me that forever. Call me by my name or nickname or something!"
    reg "...Maybe one of these days."
    kmc "Ugh...you're so uptight!"
    reg "Just part of the job...{w=0.5}Koto."   
    kmc "See, there you go! Not that hard, was it?"
    reg "Not at all, Miss."
    "Kotonoha sighs."
    kmc "We'll work on it."
    #doesn't have to be black, it can be the interior of a nice car with koto against the seat, same idea as rich house
    scene black with wipeleft_scene
    reg "Can I get a Big Mac and large fries with an apple juice, please??"
    reg "..."
    reg "Yes...at this hour."
    reg "Thank you."
    scene bg DTW with wipeleft_scene
    emp "There you are! Have a wonderful day"
    reg "You too!"
    "Reginald hands Kotonoha the food as they pull off."
    scene black with wipeleft_scene
    kmc "Thank you, Reginald!"
    reg "No problem, Ms Ouzo."
    scene bg TB with wipeleft_scene
    #add some swelling music
    #add rain effect
    "As they finally got to the bridge{nw}"
    #show koto and have her emote as I describe
    "She looked out of the window while sipping her apple juice."
    "She was doing what she tended to do."
    "What she was doing all day."
    "Thinking about it all."
    "What specific thing triggered all of this?"
    "What got her here?"
    "Unfortunately for herself, she would never know." #have an eye closing vignette or something like that
    "All she could do was think about the future, and where she was going."
    "But she didn't even want to think about that."
    "All she wanted to do was sleep."
    "And they had a long ass way to go..."
    "She might as well just rest her eyes and..."
    pause (5.0)
    "Wait to see what comes next."
    scene black with dissolve_scene_full
    #LOGO FLASH AND PROMO VIDEO
    pause (10.0)
























   


    scene bg TBD with wipeleft_scene
    "The rhythmic hum of the car moving along the road blended with the faint sound of rushing water."
    "A shift in momentum, gentle but noticeable, stirred Kotonoha from her sleep."
    "Her eyes fluttered open, adjusting to the daylight that now filled the car's interior."  
    "She blinked, momentarily disoriented." 
    "The last thing she remembered was the quiet comfort of nighttime, the soft voices, and the lingering warmth of home." 
    "Now, the sky was bright, the road stretched ahead, and the bridge beneath them signaled how close she was to her new reality." 
    reg "Ah, you're awake, Kotonoha. We're almost there."  
    "Reginald's voice was as composed as ever, but there was a knowing gentleness to it."
    "He must have noticed her unease, even without her saying a word."  
    kmc "...How long was I asleep?"  
    reg "A few hours. Long enough that I thought waking you would be inconsiderate."  
    "She sat up a little, rubbing her eyes as she glanced out the window."
    "The bridge stretched behind them now, the last real marker of distance between her and the place she used to call home."  
    "Her fingers curled slightly against her lap." 
    "It wasn't as if she had forgotten what was happening, but seeing it, feeling it, made everything heavier." 
    kmc "...It still doesn't feel real."  
    reg "That's understandable. Change rarely does, until you're in the middle of it."  
    "She sighed, leaning back against the seat." 
    "The unfamiliar skyline ahead felt daunting, yet it was now undeniably hers to face."
    pause (5.0)
    "As they merged off the bridge, the landscape began to change."
    scene bg GC with wipeleft_scene
    "The bright morning sky that bathed the bridge in warm sunlight gave way to a muted gray, the overcast sky stretching endlessly above the western horizon." 
    "Buildings stood taller here, more uniform in color, their silhouettes blending into the mist that clung to the distant hills."
    "The road, slick from recent rain, reflected the dull glow of streetlights still flickering from the early morning gloom."  
    "Kotonoha watched in silence, taking in the way the world felt different here, how the air seemed heavier, how the colors lacked the vibrancy she was used to." 
    "Back home, the sun always found its way through the curtains in the morning, painting her room in gold." 
    "Here, even in daylight, shadows lingered a little longer."  
    reg "A stark contrast, isn't it?"  
    "Reginald's voice cut through the quiet, calm as ever."
    "He wasn't looking at her, but she knew he had been waiting for her to notice."
    kmc "...Yeah. It's different."  
    "She didn't mean for it to sound so flat, but the words carried the weight of something unspoken." 
    "Different. Not better. Not worse. Just... different."
    "Her fingers traced a slow pattern against the car's window as she followed the scenery." 
    "The streets here weren't unfamiliar, she had visited before, but now they carried a permanence she wasn't ready to accept." 
    "The gray sky, the misty hills, the buildings that lacked the warmth of home..."
    "This was where she would live now. This was what she had to get used to."
    reg "The seasons feel different here as well. The summers are humid, but the winters are milder."
    kmc "Jeez, Reggie, you sound like a pilot."
    reg "You forget I trained to be commercial pilot, Ms Ozuo." 
    kmc "Oh? Wait, then why are you my driving me and my family around?"
    reg "...Conflict."
    "Kotonoha rolls her eyes."
    kmc "Vauge much?"
    reg "I don't like to bring up my past much."
    kmc "I..{w=1.5}I'm sorry. I didn't mean to push you."
    reg "It's quite alright."
    "The car was quiet for sometime, almost 10 minutes with not as much as a single noise from either of them."
    "After a while, Reginald speaks up."
    reg "Rain lingers longer here, but it has its own charm."
    "Charm. She supposed she would have to look for it."
    kmc "I guess I'll have to find out for myself."  
    "Reginald nodded slightly, the corners of his mouth curving just enough to suggest quiet approval."
    "The car rolled forward, deeper into the city, as Kotonoha let the weight of her new reality settle in."
    scene bg NH with wipeleft_scene
    "As Reginald finally rolled around to Kotonoha's new house, she twitched before she sat up straight."
    "She fished her umbrella out of the trunk and stepped out of the car."
    "She popped it open and waited by her gate."
    "Reginald got her suitcase out of the trunk."
    reg "Light pack?"
    kmc "Eh, the rest is getting shipped here."
    pause (2.0) 
    #have koto emote
    kmc "Thank you, Reginald. Really."
    kmc "I appreciate the ride and the company."
    reg "Just doing my job. Now, you have a good..."
    "Reginald pauses as if he finally has no idea what to say."
    kmc "Day. We'll see each other again, silly."
    kmc "Just...not anytime soon..that's all."
    reg "I understand now."
    reg "You have a...{w=2}nice day, Ms Ozuo."
    "And with that, Reginald gets in the car and starts it."
    "Kotonoha waves at him as he drives off."
    "And just like that{nw}"
    kmc "Here I am."
    kmc "Alone already."
    "Kotonoha sighs."
    kmc "Well...no other time like now to get started..."
    "But Kotonoha in fact, wouldn't make it very far."
    scene black with dissolve_scene_full
    #temp^ show visual montage
    "Kotonoha moped around Saturday, hoping to have more energy for Sunday but it was more of the same."
    "She wouldn't allow herself to admit it until this weekend but..."
    "She was sad."
    "She didn't feel like doing anything past the essential things."
    "Luckily, the house was already furnished."
    "She felt sluggish, like her body just wouldn't let her move."
    "She ate takeout both days, not feeling like connecting with any family on either of her off days."
    "The house was quiet."
    "The only light coming in coming from the sun."
    "Maybe she just needed sleep."
    pause (2.0)
    "Before she knew it, it was Monday."
    #make room dark
    scene bg NB with wipeleft_scene
    #alarm sound
    "Her alarm blares in her ear, and her sluggish eyes open to turn it off."
    "Before they have a chance to close again, Kotonoha swings her feet off the bed."
    "She slowly slumps off of it, groaning slowly as she does."
    "She rubs her eyes before she gets up, walking to her bathroom to hop in the shower."
    scene bg NHW with wipeleft_scene
    pause (0.3)
    scene bg NBR with wipeleft_scene
    "She smelt like shit and so did her clothes."
    "She'd have to make a stop at the laundromat later."
    pause (3.0)
    #shower sfx and slow fade to black
    "She let the warm water run through her hair and down her back."
    "She's nowhere near ready for school, but she's gonna have to look the part."
    "A little makeup will do her good enough."
    "It has before."
    scene black
    pause (3.0)
    scene bg RD with wipeleft_scene
    "As she approached the school, her feet dragged. She felt herself becoming sluggish but she couldn't slow down."
    "She wasn't gonna make a bad first impression as..."
    "Slug Girl."
    "She shuddered at the pure thought of a label on her first day, so to keep appearances, she straightened up."
    "She reaches the school gates, passing them for the first deal but she doesn't make a big deal about it."
    "She sits on the steps to walk into the building."
    scene bg NS with wipeleft_scene
    "She was doubting everything."
    "Her eyes scanned the mostly deserted courtyard."
    "At least the dark and stormy was a nice sight, the smell of wet grass, it all matched her mood."
    pause (1.0)
    "She was just lonely. She missed her family."
    "She sat down on one of the mostly empty steps near the entrance of the schoool, watching the rain pour down in the courtyard."
    "She just wanted to see her family again, even if it was just for a few more hours..."
    "She had so many things she didn't get to say."
    "Suddenly, she heard someone's heels click on the steps behind her."
    "It was a teacher, probably. Kotonoha's first interaction of the day."
    t "Are you lost, miss?" 
    kmc "Oh, uhm no, I'm not lost...I'm just… waiting until time for classes to start..."
    t "Well, they start soon, you know. You should get going."
    "Kotonoha takes a pause."
    kmc "Y-Yeah, I'll get going..."
    "Koto sets her backpack up on her shoulder, and turns to walk into the building."
    "The teacher audibly slaps her forehead."
    t "Um, wait, please!"
    kmc "Hm?"
    t "One of my teacher friends asked me to pass this out to students. Here you go!"
    "It was a poster for criminal justice."
    kmc "Criminal Justice Club?"
    "She took a closer look at the info. The paper was thin and obviously cheap."
    kmc "...Thank you, I'll keep this in mind."
    t "You're welcome. Now, off to class, go, go!"
    kmc "Alright, I'm going, I'm going…"
    "She walked into the school with a bit of pep in her step, searching the halls of the school for her room number."
    "She went into her first class. Home Ec."
    scene bg HEC with wipeleft_scene
    "As Koto walked in, she quickly found an empty seat near the wall of the room and sat down."
    hct "Alright, class, settle down. We're about to start instructional time." 
    "The man's voice would bellow. She was surprised at how deep his voice was."
    "She sat up straight in her chair, listening attentively to what the teacher was saying as I tried to wake myself up a bit more."
    "She didn't sleep very much last night."
    hct "You will be assigned partners for this new project; and Yes, I'm going to assign them."
    "Koto prayed she didn't get stuck with a lazy partner."
    "She hated lazy partners."
    "She hated lazy PEOPLE."
    "..."
    "She wasn't one to talk."
    "Who had been lazing around all weeken{nw}"
    hct "And Ms. Ouzo..."
    "She perks up, refocusing."
    kmc "Y-Yes? Sorry.."
    hct "You'll be partnered with Ms. Ueda."
    "Suddenly, everyone got up and started to move to their partners."
    "She was hit with a wave of confusion because she didn't know who hers was yet."
    "Koto hesitantly stayed seated, slightly anxious as students partnered up, standing in corners and conversating."
    "Before long, she was the only student left sitting down."
    "Until she looked around and noticed there was another girl sitting in the back."
    "A red-haired girl wuth the yellow hairband."
    kmc "That's gotta be her."
    "Kotonoha walks over to her new partner."
    "She stopped in front of the table and took a deep breath and quietly cleared her throat."
    kmc "Ms. Ueda?"
    "The girl pops up, finally noticing you."
    p "Oh..um, yeah, hi! I guess you're Ms. Ouzo?"
    kmc "Call me Kotonoha."
    p "Well, nice to be working on the project with you, Kotonoha!"
    mi "My name's Mio!"
    "Mio giggles as she'd hold out her hand for a handshake, which was unusual of a girl."
    "Well, any girl Koto had ever met. Even her cousin wasn't that formal."
    "Kotonoha shakes Mio's hand."
    "Her hands were smaller than hers, and a bit tougher"
    kmc "So! Uh...do you have any ideas on what we should do for this project...?"
    kmc "Matter of fact, what even are we supposed to be{nw}"
    hct "You must bake... one cake, two cupcakes, and one slightly large pie. Is that understood?"
    hct "Let me repeat myself. One cake, two cupcakes, and a slightly large pie."
    kmc "Well, I guess that's what it is."
    kmc "{size=12}One cake, two cupcakes, and one slightly large pie...{/size}"
    "She'd look over at Mio, making sure she heard the instructions as well."
    "Mio was instead taking notes."
    "Mio notices Koto looking at her and speaks up as she continues to write."
    mi "Note taking is my way of remembering things." 
    mi "I already have too much to think about already."
    "She chuckles nervously as she dots her sentence."   
    kmc "No, no, I get it!"
    kmc "Having to remember things on the fly is hard sometimes."
    kmc "Y'know, I'm starting to jot things down myself. Just so I can come back and reflect later, when things get a bit more managable."
    "Kotonoha pulls her notebook out of her bag slightly for Mio to see."
    "Mio's eyes widen."
    mi "That's a thick notebook.."
    kmc "I just...have a lot to say, I suppose?"
    "Koto chuckles nevously."
    kmc "Sorry...still just a little nervous about cooking..."
    kmc "Hopefully with partners it would be much easier to manage."
    mi "It's okay! We can bond and talk when we bake!"
    mi "For now, we should start thinking about what type of cake and cupcakes to make..."
    kmc "And pie."
    mi "Right! Can't forget the pie!"
    "The teacher cuts them off."
    hct "You can discuss among yourselves what the desserts will be after class. This class period was only used to establish your partners."
    hct "We will talk about traditions tomorrow for those who are struggling to be creative this fine Monday morning."
    hct "For today, Get to know your partner. Talk to them a little bit."
    "The teacher would then sit down, seemingly ending his string of interjections."
    mi "Never mind then...I guess now's the time to get to know each other..."
    kmc "Well..we were kind of on task."
    kmc "We know that we both like to write to remember. That's something."
    mi "True..."
    "Mio finally takes a good look at Kotonoha. She doesn't know why she didn't before"
    mi "Y'know, I don't think I've seen you around?"
    kmc "Oh, no, yeah... I just recently moved here, so you wouldn't know me..."
    "She chuckled awkwardly."
    mi "Oh, well, I'm glad to be one of your new friends!"
    kmc "My first actually."
    mi "Wait, really?"
    kmc "Yep! I haven't connected with anyone here yet! Besides you, of course."
    mi "Wow, well, I'm honored! When did you move here?"
    kmc "Well, I GOT here just last friday..."
    kmc "It still doesn't feel real.."
    mi "It sounds like some type of emergency..Did your parents move you?"
    kmc "Ehh...You could say that...?"
    "Koto sighs to herself. She didn't exactly want to trauma dump on this girl she just met."
    kmc "I can't get ultra specific but the situation is...quite complicated..."
    mi "Oh, um, it's okay, I understand! I'm just glad you're here while you are. At least we can bake together!"
    mi "I usually have to do things like this alone, or with someone who isn't willing to put in the work!"
    kmc "Hey well I have to warn you , I'm not exactly the best at baking."
    mi "Oh, me neither. But that's why I took this class! Maybe we can learn a few things together!"
    kmc "Yeah! I just hope we both won't burn down the kitchen in the process..."
    mi "Let's hope." 
    kmc "And hey, if we do burn down the kitchen, we'll just say it was the teacher's instructions that made us mess up."
    mi "But wouldn't that be lying? I mean, I don't think the teacher would mess up in his own instructions..."
    kmc "No, no, I was just kidding, it was just a joke. The teacher did give us clear instructions, it'd be our fault if we messed anything up..."
    mi "Oh, sorry."
    mi" I just... don't really know when jokes are jokes, you know?"
    kmc "I..kind of understand? I guess some people have a hard time telling when someone is being serious or not, I get it." 
    kmc "I just haven't run into many people that've had that trouble."
    mi "Oh, um...I see."
    kmc "Hey, don't say it in a tone like that...I was being honest."
    kmc "Like I said, I kind of understand that some people have a hard time with telling when people are joking. It's just a small issue. You don't need to be embarrassed."
    mi "I know, but it's like...That could be a pretty big thing later in life."
    mi "Like, if I can't tell when a joke is a joke, how am I supposed to tell when a kidnapper is a nice person when a nice person is a kidnapper? Or whether poison is food?"
    kmc "Those are...varying extremes..."
    "Mio's face sinks."
    kmc "Hey, listen, just because you may have some trouble figuring out if someone is joking or not sometimes doesn't mean that you'll just let a kidnapper drag you away if they just try to joke with you..."
    mi "I know, it's just..."
    mi "If I can't tell the difference between one thing, then what's stopping me from finding out the difference between another thing?"
    kmc "Just because you have issues telling when someone is joking or not doesn't mean that you'll struggle with literally everything else."
    kmc "Besides, between me and you...there's no need to worry about something such as a kidnapper, okay? We're in a pretty upper class facility."
    mi "I dunno, Kotonoha. Strange people lurk everywhere."
    "Koto smirks."
    kmc "Just another joke."
    kmc "Seriously though, you have nothing to worry about, alright? You're going to be okay."
    mi "All right. I guess so. Thanks, Kotonoha."
    kmc "Sure, you're welcome, Mio."
    "Mio looks up at the clock on the class wall. Koto's gaze was dragged to it as well."
    "Back at her old school, kids in her classrooms were far too uneducated to read an analog clock."
    mi "Well, the class period's about to end..."
    "The minutes were ticking by surpringly fast."
    kmc "You're right...well, we can catch up tommorow?"
    mi "Uh, yeah! I'll see you tomorrow!"
    "As soon as Mio would say her goodbye, the bell would ring."
    "She flinched slightly as the shrill sound of a classic school bell went off."
    "She shook her head to get herself together and watched as the other classmates began to exit the room."
    "Koto had to move."
    "She quickly packed up her stuff and left."
    scene bg NSH with wipeleft_scene
    "On her way, she'd walk through a hallway that seemed to be full of jocks and 'sports guys.'"
    "All the guys would look at Kotonoha as she passed,seemingly talking about her behind her back."
    "Koto's anxiety began to spike a little as her mind began to wonder what exactly they might have been talking about."
    "Yuri had a tendency to be eavesdropper by her curious nature." 
    "Just like her cousin, Koto's curiosity would get the better of her."
    "Koto's mind became fixated on what the group of jocks might've been saying behind her back."
    "She goes to try and speak to one of them."
    kmc "Hey, bros, what's up?"
    "She wants to facepalm so hard right now..."
    "WHAT WAS THAT??"
    "The jock's attention quickly turned towards Koto as she spoke."
    "Koto tried to continue, not trying to make a fool of herself anymore then she already had."
    kmc "What were you guys talking about...?"
    "The jock seemed a little surprised by her question, as if he didn't think she'd notice and confront them."
    "He quickly glanced back at his posse of friends before responding."
    j "We were just… talking about you"
    j2 "Y'know, Nothing bad, just... A little friendly chatter, you know?"
    "...Suspicious to say the least."
    kmc "What kind of 'friendly chatter'?" 
    j "Well, you know..."
    kmc "Actually, I don't. Please. Explain."
    j2 "Well, just how you're new to school and well, you don't appear to be walking around with any other guys."
    "Koto looks at the other jock."
    kmc "This one speak for you?"
    j "W-What? N-No! I don't even know this guy!"
    "The jock all of a sudden punches who's obviously his friend in the chest, causing him to fall to the ground in pain."
    "Kotonoha's brow furrows as she processes all of what just happened as she stares at the other jock on the ground."
    kmc "Right..."
    kmc "Well, was that it? You guys were just talking about me and the fact that I'm new and not hanging out with any guys..?"
    j "Y-Yeah, pretty much."
    j "Just, you know, getting in the lay of the land."
    "The jock would regain his offset confidence, look her up and down like a snack."
    "It made her uncomfortable. She couldn't figure out what he was looking at or what he was thinking...or what the other guys were thinking..."
    kmc "So you guys were just...'checking me out'." 
    "Koto verbally repeated what the jock was seemingly doing, not exactly appreciating his action and hoping he'd notice."
    j "No, no, not checking you out, just... you know. scouting you out..."
    j "Hey, you should join the cheerleading squad. I bet you'd be really good at it. He'd hand you a flyer, staring at you, provoking you to take it."
    "Koto's brow now furrowed in confusion, her lips parted slightly, her next words coming out in an unsure tone."
    kmc "Join the cheerleading squad…?"
    j "Just think about it, sweetheart."
    "The guy winks as he clicks his tongue and his posse surrouned him from behind as they all walk away."
    "Koto stood there in the hallway, dumbfounded. She just stood there in confusion and frustration for a few moments."
    kmc "What the hell even was that?"
    "She grumbled to herself as she looked down at the flyer he gave her."
    kmc "Cheerleading…"
    #maybe add a CG montage? feels a bit boring to just have to read and not see (for whats below, not above)
    "The very thought of sports made Kotonoha weak. She tried softball when she was seven. It didn't go so well."
    "Back then, she loved sports. But to put it bluntly, she was a complete and total klutz."
    "Being naturally shy and uncoordinated didn't mix well when it came to sports."
    "She looked down at the flyer in her hands once again. Cheerleading…"
    "She had to repeat it a few times to make it stick."
    "She thought about cheerleading a few years after the softball incident."
    "Cheerleading wasn't playing the sport. It was just... encouraging the people playing the sports."
    "But she still wasn't so sure about the idea of joining. She was never good at sports, she barely even knew the names of any teams or the rules; so how could she possibly help cheer people on?"
    "Especially when she was handed a criminal justice flyer not even a few hours earlier."
    "She slowly rolled her eyes at the thought unintentionally."
    "The thought of taking that course, studying criminal justice, actually somewhat appealed to her, of course it did..."
    "But then, it'd probably be a course with a 'strict, no nonsense' teacher..."
    "She then thought back to cheerleading and how the coach might be fun."
    "She was actually weighing her options here, considering picking something a guy told her about over something she actually liked."
    "She couldn't help but mentally scold herself for even considering something some guy she just met told her to do."
    "She hated being bossed around by guys who thought that they knew everything."
    "Especially since he handed her a flyer without even asking her if she wanted it. It just made her mad..."
    pause (2.0)
    #snap out of montage here i think also have koto show strong emotion
    "After actually having a brain for 2 seconds, she knew she didn't want to be a cheerleader."
    "All that exertion would make her tired. Her hair would get caught in her face from jumping up and down; and pom-poms means glitter everywhere."
    "She threw the flyer in the trash as she ran to class."
    "She spent a lot of time in the hallway thinking, so she had to hurry."
    "She quickly ran down the halls, nearly bumping into many other students."
    "She could tell they were looking at me as I passed by, but I ignored them as I dashed from hallway to hallway, trying my best not to be late to my next class."
    pause (2.0)
    scene bg MD with wipeleft_scene
    "Kotonoha would barely make it. As soon as she stepped in, the bell would ring."
    "She let out a light huff as she went to her seat."
    scene bg MC with wipeleft_scene
    "She was able to get a quick glance around."
    "This class had no lights but her Home Ec class did?"
    "How strange."
    "The teacher slowly raised their head from the papers they were reading."
    mt "Miss Ozuo. You're late."
    kmc "S-Sorry, I got held up in the hallway..."
    mt "Being held up is not an excuse for being late for class. Please go get a tardy and come back."
    "She slowly nodded her head and stood up from her seat, although she just wanted to scoff and roll her eyes."
    "It genuinly wasn't her fault."
    "She reluctantly mumbled another apology to the teacher before exiting the classroom and beginning to walk to the detention room."
    scene bg MD with wipeleft_scene
    "She slowly trudged down the hallways of the school for about five minutes."
    "She had never been late before, what was going to happen?"
    scene bg NSH with wipeleft_scene
    "After a couple more minutes of staring at the directory, she arrived at the detention room."
    "As she stepped inside, she looked around."
    scene bg DT with wipeleft_scene
    "The room was barren in design, only basic stock looking photos on the walls."
    "The receptionist was an older darker skinned man, his features aged and the hair on the top of his head gone, only sporting a stylish beard."
    "I slowly approached the receptionist, the older man appearing a little bit surprised to see me."
    kmc "Um, h-hi…"
    "He clicks a key on his computer and his printer starts."
    dct "Hm...I never thought I'd see you in here. Especially on your first day."
    dct "What can I do for you?"
    kmc "Wait...you know me?"
    dct "I know all the students that come here. I'm on the board that helps approve children for this school."
    dct "That and I read your file."
    #check notes
    kmc "Right..."
    kmc "Well...I got a tardy… I have to serve it in here…"
    "She uncomfortably shifted her weight on her feet."
    dct "Oh, no, no, no, that's not how it works."
    kmc "What..?"
    dct "See, if you get a tardy, you don't have to spend it in the detention room. You'd have to get a tardy pass and it shows up on your record."
    dct "See, you only have one. Some children have, 7, 8. And that's bad. You're alright. This is your first."
    "Kotonoha's mouth slowly made itself into a small 'o' as he explained how tardies worked, in utter shock and surprise."
    "She had never been late to class so it makes sense why she didn't know how it worked, but still."
    kmc "So I didn't have to serve a tardy in the detention room? I could've swore the teacher said I had to come get a tardy..."
    dct "You had to come get a tardy, not serve a tardy sentence."
    "The man would hand you the pass as it finished printing."
    dct "Just take it back to the teacher and she'll let you stay."
    "Her face seemed to show a mixture of dumbfoundedness and relief as she slowly took the pass from the receptionist's hands."
    kmc "Sorry, I'm asking again but..to clarify...I don't have to serve a tardy in here?"
    "He chuckles and sighs."
    dct "I don't expect you to know anything about tardies. You seem very punctual."
    dct "But no. Unless you gain five plus tardies."
    dct "Then you'd be in here in trouble, but this is only one; so you should be okay."
    "She gave him a sure nod."
    kmc "Oh, and one more thing..."
    kmc "Why do some rooms in this school have light and some don't?"
    "He chuckles."
    dct "Half intention, half budget."
    kmc "{size=12}High-end school, my ass, Dad.{/size}"
    "She chuckles under her breath as she began to walk out of the detention room."
    dct "Don't let me catch you in here again."
    "He'd chuckle as Koto would walk away."
    "The receptionist's soft chuckle made her crack a small smile as the door closed behind her."
    scene bg NSH with wipeleft_scene
    "She hummed quietly to herself as she walked down the hall."
    "She was still slightly in a state of surprise. She actually learned something new. How tardies work."
    "She only has to get a pass and bring it back to class. How convenient. It was some pretty useful information to know."
    "She thought about how she could be more flexible with her time now."
    "She wouldn't {i}try{/i} to be late or try to extend her visits in the hallways; but at least she knew she wouldn't be serving a tardy sentence unless she did it about four more times on purpose."
    "Her mind began to drift to how she would apply this newly-found information to her day-to-day school life."
    "She felt freer in this moment."
    scene bg MD with wipeleft_scene
    "She leaned against the wall next to her classroom door."
    "She took a quick second to just...{w=1}breathe."
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
    pause (0.5)
    "Kotonoha would nod her head and smile happily as she reentered the class."
    scene bg MC with wipeleft_scene
    "Other students and the teacher look up from their work to look in her direction, some of them whispering amongst themselves and pointing."
    "Koto still managed to maintain my composure as she walked up to the teacher and handed her the tardy pass, saying nothing."
    "The teacher eyes her then the pass, then looked at Kotonoha again, taking pause."
    pause (0.5)
    mt "Very good. Go sit down."
    kmc "Thank you."
    "She says in a bit of a snappy tone."
    "The teacher's eyes widen but Kotonoha had already walked away."
    "The new information was welcome but she still didn't appreciate having to go get a tardy when she was literally in the doorway."
    "Regardless, she quickly made her way back to my desk and sat down, ignoring the stares and whispers that came from some of my classmates."
    "The teacher clears her throat and stands."
    mt "Alright class, you should have finished your warm-up by now."
    "Kotonoha looks around and she sees what appears to be a bunch of problems on them."
    "She had a thought to ask but she feels like she already made enimies with her math teacher."
    mt "Put it away. We'll use it tommorow. But for now, welcome to math class."
    mt "Now, for project week, you shall be partnered with a partner to do a math project."
    "All the kids would now groan."
    "They didn't think that one of their project grades would be in math class in all places."
    "Koto couldn't help but scoff under her breath along with the other students as she mentioned the project."
    "But that explained why she also had a project in her Home Ec class."
    "It seemed normal for a class of that nature but it seems she transferred during something called 'Project Week'?"
    "She'd have to ask around."
    "The teacher would roll her board up towards the front of the room."
    mt "I'm about to wrtie all of your names are up here."
    mt "I will split you into teams."
    mt "And it is completely random before you ask, so no complaining."
    "The students still whine but just a bit quieter."
    "Koto silently watched as the teacher began to write some names on the board."
    "She really hoped that she'd get a smart and capable partner, but knowing her luck, she'd probably end up with someone lazy."
    "Well..."
    "She thought about her partner from her Home Ec class. Mio seemed nice and competent."
    "Maybe she was overthinking it and she would get a nice partner."
    "She'd zone back in, looking at the board to find her name, trying to find who our partner would be."
    "After a moment of scrolling through the list, she found her own name next to another..."
    "Kiyomi."
    "Part of her was definitely worried about her partner, she hoped this 'Kiyomi' wasn't a slacker or a delinquent..."
    "Everyone would walk to their partners again. leaving Koto with the same feeling she felt in Home Economics. Completely lost."
    "She let out another soft sigh as she quickly got up from her seat. She knew she had to go find my partner, but I really didn't know who I was looking for, once again."
    kmc "These people need nametags or something, I swear."
    "She continued scanning the room, her eyes darting from student to student as everyone began pairing up but then{nw}"
    #add shadow kiyomi then when koto goes up to her, it'll be the normal sprite (black sprite fade to normal sprite if possible)
    p "WHO{w=0.7}THE{w=0.7}FUCK{w=0.7}IS KOTONOHA?!"
    "She would turn to her name being called abruptly."
    "It was a blonde girl, chewing some gum."
    "As Koto makes her way over to who was obviously her partner, students turn to her again."
    "Her body language becomes nervous. Too much attention was being drawn to her this period."
    "Either way, Kiyomi was patiently waiting, and if she yelled once, it's a safe assumption that to think that she would again if Koto didn't hurry."
    "She quickly got over to Kiyomi."
    kmc "Uh… um, I'm sorry to ask, b-but are you Kiyomi?"
    kiy "No shit."
    "Koto tenses up."
    kiy "I'm joking. Relax."
    pause (1.0)
    kiy "K-I-Y-O-M-I. Don't wear it out."
    "She'd hold out her hand for a handshake."
    "Kotonoha awkwardly took her hand, gently shaking it. Kiyomi seemed to be somewhat sarcastic and snarky."
    "She reminded her of Natsuki in a way."
    kmc "Um, I'm Kotonoha..." 
    kiy "Yeah, I know.{nw}"
    kiy "You wanna know something Kotonoha? In fact, that's a bit of a mouthful, don't you think?"
    "Kotonoha awkwardly chuckles, a smile making its way onto my face."
    "She was certainly a little bit snarky, but that didn't seem to be her being rude, just how she was."
    kmc "I...guess so??"
    kiy "You got a nickname, Miss Kotonono?"
    kmc "Uh...hah..Nope, no nickname..."
    kiy "Hmmm..{w=1.5}how about..Koto? It's much shorter! Easier to remember!"
    "Her smile withered a little bit at her nickname idea."
    "First, she thinks Kiyomi acts a lot like Natsuki, then she calls her Koto."
    "God, it had only been a few days but she missed everyone at home so much."
    "It almost hurt her physically."
    kmc "It's… cute."
    "She chooses to act like she had never heard it before, as she didn't want to delve into her past at the moment."
    "She sniffs up would be tears."
    "Kiyomi doesn't notice, too absorbed in herself."
    kiy "I know it is. I come up with the best names."
    "Koto chuckled weakly."
    kmc "You sure do..."
    kiy "Anyways, teach! What's this math assignment about??"
    "The teacher would look up, making sure all the students have paired up."
    "She would reluctantly stand and begin to explain the assignment."
    mt "We're doing a project on fractions, you must write up a paper on them."
    mt "{size=12}That seems easy enough, even for you idiots to do.{/size}"
    "Kotonoha smiled. This was gonna be an easy 'A'."
    mt "You must then make a diagram made out of only paper about factions. It can be a one over a two; it could even be something cut in half."
    mt "Just make it creative."
    kmc "That's a little bit specific..." 
    "Koto whispered out of the side of her mouth."
    kiy "Tell me about it."
    kiy "I'm thinking we just do the one over two. Sounds easy."
    kmc "...Yeah, sounds good to me."
    kmc "Don't you think people are going to do more or less the same though?"
    kiy "Pfft, who cares? She said it doesn't matter if it's simple!"
    kiy "We just have to worry about making it {i}better{/i} than everyone elses."
    kmc "Hm...I guess you're right."
    kiy "Glad we're on the same page."
    "Kiyomi smirks."
    kmc "Yeah, yeah, just make sure to do your share of the work."
    "Kiyomi makes exaggerated gasps."
    kiy "What do you take me for? Some kind of slacker?"
    kmc "Just wanted to make sure you're not some kind of lazybones..."
    kiy "Do you know who I am? I'm Kiyomi. the non-laziest person you ever met."
    kmc "I dunno… you could be a little bit lazy on the inside."
    "Kiyomi would look playfully offended."
    kiy "How dare you, ma'am!"
    kmc "Hey, it's entirely possible that you're a big lazybones and you just play this tough act to hide it."
    kiy "Never."
    "Kiyomi proclaims with snark."
    "Kotonoha enjoyed this little argument. She was getting past her harsh exterior and it looked like she was actually having fun joking with her."
    "However...Kotonoha wasn't about to let her have the last word."
    kmc "I bet you'd slack off if it were a book report."
    kiy "Oh, don't even get me started on book reports. That's why I only take Japanese classes, not English classes."
    kmc "Do you hate English or something?"
    kiy "No, no. I came from over there. It's just...english is just a lot more talking and extra."
    kiy "But it's not just cheeseburgers, eagles, and AK's over there."
    "Koto's eyebrows widen. She was aware of the stereotype of 'American life' but this was actually coming from someone who used to live there."
    kiy "What do you think? hat's your opinion on the... Cheeseburger eating....Eaters?"
    "She stares dumbfoundedly for a second."
    kmc "Really? The Cheeseburger eating...eaters?" 
    kiy "You know I was joking and I tripped up! Just answer!"
    kmc "Hm...my opinion..."
    "Kiyomi sat there waiting for a response, slightly tapping her foot."
    kmc "Well, I think 'The Cheeseburger-Eating Eaters' are… interesting, to say the least."
    kiy "Interesting good or interesting bad?"
    kmc "Hm...Definitely on the interesting good side..."
    kiy "Have you been before?"
    kmc "I've been a couple times before."
    kiy "Well, Sounds nice. But the bell's about to ring, so{nw}"
    "The shrill bell rung out, cutting Kiyomi off."
    "Kotonoha chuckles."
    kmc "Guess we'll start the project tomorrow, huh?"
    kiy "Yeah, guess so."
    kmc "We still had to brainstorm our fraction diagram, but I was sure we could knock that out pretty quick tomorrow...hopefully."
    kiy "Yeah. Hopefully."
    "Kiyomi would pop gum in her mouth."
    kiy "See ya."
    "Kiyomi gives a dismissive goodbye, as it seems like Kotonoha's in a rush packing up."
    kmc "Y-Yeah, you too..."
    "Kotonoha stuffs stuff in her backpack and sprints out of the classroom, waving back at Kiyomi."
    scene bg NSH with wipeleft_scene
    "Her eyes were now focused on the floor, watching her own feet so she wouldn't trip on anything or bump into anyone."
    "Her lunch period was on the other side of the school, so she had quite a bit of walking to do."
    scene black with wipeleft_scene
    pause (2.0)
    "The walk wasn't that as long as Kotonoha thought. She reached the cafeteria in no time."
    "She let out a soft sigh, slightly out of breath from how fast she had sprinted to get there."
    "She tried to shake it off as she headed inside."
    scene bg C2 with wipeleft_scene
    "She walked inside, trudging over to a table and set my backpack down underneath it, taking a seat in a random spot, the sudden light still stinging her eyes."
    "It was still a little jarring for some spaces in the school to have light while others didn't but she was getting used to it."
    "Whether that was good or not, she couldn't tell."
    "Regardless, she sat and settled for a few minutes catching her breath before quietly taking her wallet out of her backpack and got up from her seat, joining the lunchline."
    "She'd take a look at up at the tradtional display to see the lunch options."
    "There's a selection of foods out today. Bento boxes, noodles and pizza."
    "They didn't seem too bad, hopefully it wouldn't taste all that bad either."
    "Bento box? No... I'm not that hungry..."
    "Noodles? Too messy."
    "Pizza?...not what she was really craving."
    "Well, she wasn't gonna starve."
    "The lunch lady would speak up."
    ll "Whaddya want, kid?"
    "She quickly got snapped out of her thoughts."
    "She had been so spaced out that she didn't even realize that she was at the front of the line."
    kmc "Um…"

    menu:
        "Pizza":
            $ choice = "zaza"
        "Noodles":
            $ choice = "noods"
        "Bento Box":
            $ choice = "bb"

if choice == "zaza":
    kmc "A-A slice of pizza please."
    "The older lunch lady smiled as she cut and put a fresh slice of pizza to put on your tray."
    kmc "Oh, wow, thank you!"
    "The lunch lady chuckles a bit."
    ll "Of course, kid! Enjoy your lunch!"
    "Koto smiled back warmly and scooted along with her tray."
    jump shared_route2

elif choice == "noods":
    kmc "N-Noodles, please!"
    "The older lunch lady smiled as she grabbed a plastic bowl of lukewarm noodles to put on your tray."
    kmc "Thank you..."
    "The lunch lady's face kind of scrunches as she hears the flimsy thanks."
    ll "Yeah..."
    "Koto notices that she saw through her faux thanks and awkwardly shuffles away."
    jump shared_route2

elif choice == "bb":
    kmc "A bento box please?"
    "The older lunch lady smiled as she quickly went to grab a bento box to put on your tray."
    kmc "Thank you!"
    ll "No problem!"
    "Koto couldn't help but notice how...tired she looked, even with her smile. Her job seemed like it took a toll on her."
    "Regardless, she smiled back and scooted along with her tray."
    jump shared_route2


label shared_route2:
    "The scanner towards an empty table in the corner. I set my tray down and sat at the table, taking a moment to fish my student ID out of my wallet."
    "She grabbed it and swiped it through the ID scanner, making sure that the school knew that I had actually gotten lunch today."
    "It buzzed at her."
    "She looked confused and swiped again."
    "It buzzed."
    "She looked at the ID."
    "It wasn't her new one, it was her old ID."
    #maybe CG?
    "She mentally facepalms."
    "She hadn't even opened her new ID."
    "It was still on her counter at home in the envelope."
    #end maybe cg
    "She sighed as she put in her student ID number on the keypad and went back to sit down at her table."
    "She wasn't in the mood for a nostalgia trip. It was her first day here and she didn't want to feel sad." 
    "She looked down at her plate, messing with her food a bit before beginning to eat."
    pause(2.0)
    "She would look around, just to see what was going on as she began to pick up her eating speed."
    "She had a bit of a habit to stuff her face, even while in public."
    "She was getting better at trying not to though, but the fact that she didn't eat breakfast today didn't help."
    "Everyone pretty much seemed to be doing the same thing, talking and joking around with friends or eating."
    "She would then notice one particular guy as she scanned the room. He wasn't doing anything. just sitting around his friends, but... something about him caught Kotonoha's eye."
    "She then thinks back to earlier this morning."
    "It was one of those boys that was with the jocks!"
    "They must've been going out to do sports, because now he was in the more formal school outfit."
    "After a bit of staring and mentally processing that information, she would soon focus on eating her pizza again."
    "She'd continue to eat in silence, her eyes occasionally flickering back to that particular guy in the lunchroom."
    "She wondered what drew that her attention to that guy."
    "As far as she knew, he hadn't actually looked at her or something earlier, so why was her attention drawn to him...?"
    "He seemed calm, not really engaged in the conversation going on around him, two people literally talking over his lap as he ate."
    "Maybe, she thought he looked{w=1}...cute?{nw}"
    "No. Kotonoha was never much of a romantic."
    "She wasn't really the type of person to find someone cute at a first glance."
    "Besides, Kotonoha was much more focused on her school work to think about romance."
    "She just went back to quietly eating her food after that...out of left field thought."
    "Just as she began to eat again, the lunch bell would ring, and she would have to run all the way back to the other side of the school for her final class of the day."
    "Koto finished the rest of her food in a few quick bites, shoving the last little bit into her mouth before the end of lunch bell finished ringing."
    kmc "Ugh, alright, one last sprint...{w=1}hopefully."
    "Koto would put her tray in the tray disposal, taking a moment to check the time on her phone." 
    kmc "Crap, I really gotta hurry..."
    "She quickly began speedwalking out of the cafeteria."
    scene bg NSH with wipeleft_scene
    "Her speed walking turned into sprinting, and sprinting turned into full-on running."
    "People were looking at her as she started to run furiously, like she were at a track meet."
    "She tried to pay no mind to the people looking at her."
    "She had already gotten enough of those for a few weeks from math class; but damn are their stares were starting to get annoying."
    "Her breathing got heavier every extra second she ran."
    scene bg NSH with wipeleft_scene
    "She made it back to the to the other side in plenty of time."
    "She panted silently to herself as she slowly caught her breath, leaning against a wall for support."
    "She felt a cramp in her stomach."
    kmc "Goddamnit...not right now..."
    "She looked at her phone. She had the time to take a bathroom break."
    "She slowly pushed herself off the wall and looked at the time on her phone again, rechecking it."
    "Her breathing started to slow down to a normal pace."
    "A grimace appeared on her face as a cramp hit her particularly hard."
    "She audibly groaned as she made her way over to the girls' restroom."
    scene bg SB with wipeleft_scene
    "As she stepped into the restroom, she quickly made her way over to a stall, closing the door and locking it."
    "No lights in here?? Really?"
    "...{nw}"
    "Whatever."
    scene bg UUS with wipeleft_scene
    "She lined the toilet seat with paper, not sure what nasty germs could be lingering."
    "After her quick linework, she adjusted herself accordingly as she sat and took care of her business."
    scene black with dissolve_scene_full
    pause (1.0)
    "As she sits there, she hears feet scuffle into the bathroom and multiple loud voices suddenly fill her ears."
    #add chatter noise maybe?
    g1 "And have you seen her hair??"
    g3 "Erm, hello, are you like an old lady or something?"
    "The girls chuckle."
    kiy "I know, I know, and get this, she tried to call me lazy!"
    kiy "Like, girl, have you seen the bags under your eyes? Puh-{w=0.5}LEASE! You have no room to talk!"
    g2 "M-Maybe she has them from staying up and working hard for her first day."
    kiy "Can it, Steph. If you saw her, you'd know! She just LOOKS like that person who stays up doing nothing important!"
    kiy "And what do we always say?"
    g5 "Sleep marks show, stress marks grow!"
    "They all cackle."
    "Kotonoha couldn't see through the gap of the stall but she recognized one voice."
    "Her project partner from math class, Kiyomi."
    "How could she dare say such awful things?"
    "Koto was nothing but nice to her! She thought that moment was all in good fun{nw}"
    kiy "Oh, shit girls! Class is about to start, go go go!"
    "They all scuffle out of the bathroom the same way they had walked in, their gossip session cut short."
    "Kotonoha could't believe her ears."
    "But then she checked her phone again."
    "Class WAS about to start."
    kmc "I...{w=0.5}I don't have time for this."
    "She quickly cleans herself up and swipes the toilet liner toilet paper into the toilet and flushes."
    scene bg UUS with wipedown
    scene bg SB with wipeleft_scene
    "The toilet begins to flood behind her as the stall door closes."
    "She opens it back up to inspect."
    scene bg UUS with wipeleft_scene
    kmc "Aghh! Why is this happening to me?! I'm already late!"
    "She looked around."
    "She saw no plunger."
    "She was late, she didn't want to touch the dirty toilet, and there was no cleaning supplies around."
    "Someone else would have to report it to a janitor."
    scene bg SB with wipeleft_scene
    "She quickly rushed to the sink to wash her hands."
    "She tried to be thorough while also hurrying."
    "She quickly shook them on the ground and sped out of the bathroom, to rush off to class."
    scene bg NSH with wipeleft_scene
    "She checked her phone as she was walking."
    "She wasn't absolutely late as she thought but she was now a little bit behind."
    "Hopefully THIS teacher wouldn't mind if she walked in as the bell chimed."
    scene bg NSH2 with wipeleft_scene
    "Koto would make it to her last class on time."
    "The class?"
    "Computer Science."
    scene bg CS with wipeleft_scene
    "She entered the classroom just as the bell rang. Thankfully, she had just made it on time and didn't get reprimanded by the teacher this time!" 
    "She quickly looked around the classroom before spotting an empty desk in the back and heading towards it."
    "The class seemed chaotic, even though the bell had just rang, kids running around and being crazy, throwing paper and other small objects."
    "This class didn't seem to want to sit still."
    "She mentally groans. With people changing seats around, and kids throwing things, she was surely going to have an aneurysm by the end of this class."
    "She could already feel one creeping around in her head."
    "It was getting a bit annoying, but I didn't feel like complaining about it verbally either."
    "She set her backpack on the floor against the leg of the desk."
    "Koto would look around the classroom, quickly, taking a survey of the room when she'd see the guy she saw at lunch."
    "She'd be sidetracked before the computer science teacher would start talking."
    cst "Okay, class. Welcome back to Computer Science. I assume you all did your nodes homework over the weekend?"
    "No one would raise their hand."
    "His eyelid would twitch."
    cst "You know what?"
    cst "I'm tired of this."
    "The teacher's voice would suddenly become a tad bit deeper."
    cst "All of you kids never, ever doing your work. So you know what? For Project Week, we're doing the node project! AGAIN!"
    cst "Even if you did it the first time!"
    cst "And, YES! You will get an F in the gradebook for entire semester of this class for if you do not complete it."
    cst "And I will have a personal talk with the principal about it. So he WILL make sure to change your grades if you do not do this project."
    "He looked serious and angry."
    "Koto felt a bit shock as the teacher stating that he had enough of it, and that we would receive an F if we didn't not do it."
    "And he had already threatened a personal talk with the principal, something that would most definitely get our parents involved."
    "Great. Of course, there was already class drama and she had just become a part of it."
    "Koto sighs, knowing that she would've done her homework if she had been in here."
    "She groaned quietly to myself as the teacher continued to rant about the lack of work completion in the class through the heavy filter in her ear."
    "She was trying not to pay attention to it, as it was obviously just angry rambling at this point." 
    "It wasn't her fault that the other students weren't doing their work...but thanks to them, they were now forced to do a 'node' project?"
    "This was really annoying, unfortunately."
    "Kotonoha already had two other group projects she needed to work on."
    "As the teacher finished his rant, he finally started speaking rationally, and Koto tuned back in."
    cst "I will partner you up."
    "She thought this day was just getting weirder and weirder. It felt like she was going to the same class, but with different kids and a different teacher."
    "All of the classes seemed similar: Walk in, pick out a partner, get a project to work on… it all seemed similar, almost as if I was going through the same repeated formula."
    "{cps=0.5}Almost as if someone couldn't come up with any other creative ideas on how to write classroom scenes...{/cps}"
    #idk if thats the command for slow text, if not fix it, if it is, it might be too slow
    "It was starting to feel very weird, almost a little eerie."
    "But before she had any time to say anything, The teacher was at her desk."
    cst "Miss Ozuo."
    "She snaps back, clearing her throat."
    kmc "Agh..a-ahem..yes?"
    cst "Your partner shall be. Kane."
    "He points over to the boy that you've been staring at this entire time."
    "Her lips parted in surprise, somewhat...shocked at hearing that he was going to be my partner."
    "...Him?"
    "She muttered under her breath, but the teacher heard her."
    "Yes, he's a very good student. I think you'll like working with him."
    "The teacher would say as he'd walk away to another student to powder them up."
    "I sat there in slight silence, processing what the teacher had said."
    "Was she...happy to work with this guy? She didn't know that she'd be so excited to work with a guy for once."
    "After working with Mio and Kiyomi..."
    "Kiyomi..."
    "She thought back to the bathroom."
    "She shuddered. She needed a palette cleanser anyway."
    "Koto was just a bit surpried at her own feelings, as she didn't usually look forward to working with other people, especially other people from the opposite gender."
    "After a bit of thinking to herself, she'd walk over to him, finally knowing who her partner was, unlike the other two classes where she had to basically wait until everyone else picked to find hers."
    "She'd walk over to the boy. All she knew his name. Kane. She needed to know more."
    "She stood in front of him as he sat, standing there awkwardly."
    "He eventually looks up from his phone."
    ka "Oh, hey, you're my partner."
    "He'd say as he'd sit under your gaze."
    kmc "Yep, I'm your partner…"
    "Her voice came out a bit soft."
    "She stood awkwardly next to his desk for a moment before finally sitting down besides him."
    ka "So what's your name?"
    kmc "K-Kotonoha..or Koto..."
    "She just thought about how she had never heard him speak. Not directly to anyone at least. Not even during lunch. She had only observed him..."
    "I didn't even know his real personality at all."
    "But she knew his voice sounded velvety."
    ka "Uh..Well, my name is Kane."
    "He'd hold out his hand."
    "She hesitantly took his hand that he had held out, giving it a firm shake."
    ka "Firm grip you got there."
    kmc "Oh..thanks. I've been shaking a lot of hands today..."
    "He'd smirk and smile at you."
    "Koto could hardly control her own face from smiling and turning even redder as he smirked. She internally cursed at myself for feeling this way, and how she could hardly control her own cheeks burning up."
    "As much as she didn't want to admit it, Kotonoha couldn't deny it anymore, even in her own head. She liked this boy."
    #dont worry NATZ it doesnt stay this way
    "This would have been our first crush in years. The only crush she remembered ever having was as a 4th grader..."
    "She reminisces on the boy, remembering that he wasn't that great but it was grade school."
    "It all seemed so romantic to her back then."
    ka "So what do you like to do?"
    "She hesitated for a moment."
    kmc "Ah! well...I like to just chill most of the time...play some video games with my friends...read and write sometimes..."
    ka "Sounds pretty chill. I like playing video games and writing too."
    kmc "Glad we have those things in common."
    ka "Looks like we're going to be good friends for this project."
    "He'd smile at her at a specific way."
    kmc "Yeah… it looks like we will."
    "{w=1}.{w=1}.{w=1}."
    ka "So, um...this nodes project."
    "He'd look at the rubric that was laid out in front of him."
    ka "I just don't get it, I already did this!"
    ka "And I always do my homework too! Yet he's making all of us do it again..."
    kmc "I would've done the homework too...y'know..if I had been in this class from the start.."
    kmc "I'm never behind on an assignment."
    ka "Oh, same. I guess we we're more alike than I thought."
    "Why wasn't she speaking like she usually did?"
    "She was fumbling her way through this conversation."
    "Kane just made her smile more than any of her male friends ever did."
    "His voice, his smile, the way he spoke...everything about him made her feel butterflies in my stomach."
    "Just then, Koto would notice that there was now a large crowd of people surrounding him."
    "She had forgot for a moment that she first saw him hanging with the jocks earlier."
    "Of course this guy would be popular."
    "She didn't want to fall in love with someone who always had ready options, the thought making her cringe."
    "But... he didn't look like one to do that..."
    "He looked sweet...kind even."
    "She mentally sighed."
    "Was she falling for THIS guy?"
    "She doesn't even know anything about him, and yet she was already in love."
    "It was crazy. She had never felt this in so long. She didn't know how to react or what to do at all."
    #maybe have these focus moments where koto is having these complex thinging moments, use the vinette idke
    ka "Oh, crap. The bell's about to ring."
    "Koto snaps out of her mental rant."
    ka "Hopefully we get to work on our project tomorrow." 
    ka "I'm, uh...happy to work on it with you."
    kmc "Yeah, me too…"
    "She replied quietly, giving a small smile in response."
    ka "Well, I've got an after-school club to go to, so I guess I'll see you tomorrow."
    kmc "Oh… alright then, I guess I'll see you tomorrow then…"
    "The bell rung and Kotonoha and the rest of the class flooded out of the class to head to the busses to go home."
    scene bg NSH with wipeleft_scene
    "She tracked Kane through the crowd as he walked to his club."
    "She then snapped back to reality."
    "She forgot remember she had her own after school club to go to!"
    "Well... at least Tryouts...? Whatever the criminal justice would be holding to get in."
    "She had no time to think about boys! She had to get to the criminal justice club!"
    "Kotonoha would quickly rush down the hallway, trying to pull the flyer out of her backpack to see where the classroom was."
    "The hallway was full of other students, all rushing to leave the school, some of them nearly bumping into her as she pulled the flyer out."
    "The traffic was flooding forwards while she was heading backwards in the hallways."
    "It was like she was flowing against a river of students."
    "Koto would finally reach the class, after pushing through some students."
    "She panted slightly from the eoffort it took to get down the hallway."
    "She checked the classroom number once more, confirming that it was indeed the correct one."
    "She'd walk inside the classroom."
    scene bg DC with wipeleft_scene
    #might changr aesttich later
    "Her eyes widened."
    "It didn't look like this was an all day classroom. It looked like this was a special classroom just for criminal justice{w=0.5}...and Kotonoha was feeling it."
    "She felt some thrill running down her spine, making her feel like… this was her place." 
    "Suddenly, a woman with short blonde haircut and blue eyes would come out, wearing a police vest."
    "She looked like she was the criminal justice teacher."
    "She hesitantly approached the woman who looked like the teacher, knowing that she probably had to talk to her to go through tryouts."
    p "Can I help you, miss?"
    kmc "Uh… y-yeah."
    "Koto mumbled my reply to her, nervously fiddling with the flyer in my hand."
    kmc "I'm here...for the tryouts, for...the criminal justice club..."
    p "Oh, sweetie, there's no tryouts for something like the Criminal Justice Club."
    p "Anyone is welcome!"
    p "And well...looks like you're the first member."
    p "Welcome to the Criminal Justice Club."
    p "You can call me Mrs. Reynolds."
    "She'd hold out her hand."
    "She'd silently thought to myself that she had shaken a lot of people’s hands lately."
    "Mio’s, Kiyomi’s and Kane’s hand before, and now Mrs. Reynold’s. I had done a lot of handshaking today..."
    {cps=0.5}"Almost as if someone couldn't come up with any different and creative ideas on how to write character introductions...{/cps}"
    #idk if thats the command for slow text, if not fix it, if it is, it might be too slow
    r "Firm grip there, hm?"
    kmc "Oh..well, yeah..."
    r "Well, welcome!"
    "You're going to need a hair tie, so here, you can take one of these. And you're going to need a hat."
    "She'd hand her a hat that read 'POLICE' and a hair tie."
    "Kotonoha already looked more appropriate for the club."
    r "You look absolutely perfect."
    "She did seem like a no-nonsense kind of teacher, but at the same time, she seemed like she was having fun with what she was doing."
    "It was the perfect balance of what she wanted in a teacher."
    "Other people would flood into the Criminal Justice Club."
    "It was... Mio!"
    "She saw Kotonoha and ran over to her, standing right next to her like a puppy."
    mi "Kotonoha? You're taking criminal justice too?"
    "Koto hadn't even processed this."
    "She shook her head to refocus."
    "She hadn't expecting to see her here at all."
    kmc "Yeah, I’m here too!" 
    mi "You wanna know why I'm here?"
    kmc "..Sure? Why are you here?"
    mi "Well, because criminal justice interests me! I want to bust bad guys and...maybe become a cop one day!"
    kmc "Really...? You want to be a cop one day?"
    "Her somewhat small stature would make Koto think otherwise, but anyone can be anything, there's always a way."
    "At least she was already defying people’s expectations."
    "Suddenly, Kiyomi would walk into the club room too."
    "Koto immediately felt a pang of defensiveness as Kiyomi walked into the classroom."
    "She remembered the friendly attitude in math and then the slew of insults from her and her crew straight to her face unknowingly in the bathroom."
    "Although, Kiyomi looked embarrassed to be there."
    "Koto's curiousity got the best of her again."
    "She had to know what was going on, despite her two faced nature."
    "She walked up toward Kiyomi."
    kmc "Hey."
    "She greeted quietly and sharply, still being a bit bitter."
    kiy "Oh..uh..Hey, Koto." 
    "Kiyomi would look down at the floor."
    "She took note of Kiyomi's guilty-like body language."
    "Did she find out Kotonoha was in the bathroom the same time as her?"
    "Was she going to apoligize?"
    "She didn't know if she'd particularly forgive her even if she did..."
    kiy "Yeah, I'm okay."
    "She was acting embarrassed, looking down and refusing to look Koto in the eyes, so she knew something wasn’t right, maybe an apolgy was on the tip of her tongue but she couldn't get over her pride?"
    "She wouldn't put it past her."
    "Once a snake, always a snake, even when you get busted."
    kmc "Are you sure…?"
    kiy "Lay off, man."
    kmc "Excuse me? I'm just making sure you're okay, you're practically shaking, y'know{nw}"
    kiy "What? Really?"
    kmc "Yea..?"
    "Kiyomi stomps her foot and sighs."
    kiy "Fine. You wanna be so nosy?"
    kiy "..."
    kiy "It's just...my mom made me join this club."
    kmc "Your mother made you come here?"
    kiy "Yeah...you didn't catch the resemblance?"
    "Kiyomi would point at Mrs. Reynolds and then back at herself."
    "Koto would notice that Mrs. Reynolds and Kiyomi both had blonde hair, blue eyes."
    "She slowly saw the other features and then it clicked."
    "Her mother taught at the school ANd was the criminal justice teacher? Interesting."

    return
    
    #check text
    "The door then opened again."
    "Koto turned her head slightly, half-expecting another random student, but instead, it was Kane."
    "He stepped inside casually, hands in his pockets, eyes surveying the room."
    "Mrs. Reynolds looked up immediately."
    r "You here for the club, or just wandering the halls looking charming?"
    "Kane gave her a short grin, something between cocky and laid-back."
    ka "Criminal Justice Club, ma’am. Thought I’d give it a shot."
    "'Ma'am.' She raised a brow slightly at the unexpected formality, but nodded in approval."
    r "Manners. I like that."
    "She extended her hand out to him."
    r "Mrs. Reynolds."
    ka "Kane."
    "They shook, and Koto watched as Kane's smile pulled a little wider. It was polite, smooth...too smooth."
    "He looked completely in his element."
    "But something about it didn’t sit right."
    "She’d never seen him interact with a woman before, now that she thought about it, not for her, anyway."
    "And this was the first time."
    "His voice... it was different than how he spoke to her."
    "Just a little deeper, a little more suave. Sensual, even."
    "It made her want to melt but it also made her sick."
    "Kiyomi, standing beside her, straightened up without saying a word."
    "She subtly ran her fingers through her hair, brushing it over her shoulder."
    "Her eyes locked onto Kane like she had just discovered gold."
    "Koto caught the movement. She narrowed her eyes."
    "She didn’t say anything, but the shift was obvious, Kiyomi was suddenly interested."
    "And Koto didn’t like that she noticed."
    "Mio looked toward Koto, noticing her glare."
    mi "You know him?"
    "Koto gave a small nod, but said nothing else."
    "She felt her stomach twist slightly, not from excitement, like earlier, but something else."
    "Something colder."
    "Kane stepped deeper into the room, giving it a lazy once-over. Then his eyes landed on her."
    ka "Oh. Didn’t know you were into this kinda thing too!"
    "Koto blinked."
    kmc "Guess I am."
    "Her delivery comes off a little flat because of what she saw, plus Kiyomi was still fixing herself next to her."
    "Koto wasn't smiling. Not like before, if she even was at all."
    "And somehow, he noticed."
    ka "...Cool. Well, looks like we’re clubmates now."
    "He moved toward a seat, pulling it out with one hand and spinning it around so he could sit backward on it, arms slung across the backrest like he owned the room."
    "It wasn’t cocky, that would’ve been obvious."
    "But there was this calm ease to him, the kind people carried when they never had to try too hard to be liked."
    "He barely glanced at Mrs. Reynolds as she began to talk, his focus more on his shoes than the club."
    "He tapped his foot. Looked around. Rested his chin on his arm like he was just killing time."
    "He didn’t look curious."
    "He looked bored."
    "And not the 'had a long day' kind of bored—the 'I've already decided this isn't worth my full attention' kind."
    "It felt like he had shown up just to be seen. Not to learn. Not to do anything."
    "Koto didn’t even realize she was frowning until Mio nudged her with her elbow."
    "She sat up a little straighter and tried to take notes."
    "It seemed like Mio was the only one taking them."
    "Kane then leaned forward slightly and looked toward Mrs. Reynolds again."
    ka "So like... are we doing mock arrests or something? Or are we just doing worksheets and talking?"
    "Mrs. Reynolds paused mid-sentence and raised an eyebrow."
    r "We’ll get to mock scenarios eventually, yes. But first, there’s foundation work to cover. Context. History. Law."
    ka "Right. Cool."
    "His voice had a polite tone, but it rang hollow. No follow-up. No interest. Just a checkbox ticked."
    "He wasn’t disrespectful. But he wasn’t present, either."
    "These things made Koto's stomach turn."
    "How were her feelings just being shattered like this??"
    "He showed just enough engagement to stay above suspicion, but not a single spark of actual investment."
    "Koto looked back down at her notes. Her pencil hadn't moved in minutes, although she really did try to listen.."
    "Kane leaned back again. This time, his eyes drifted across the group, landing on her briefly before sliding past to{nw}"
    kiy "Heyyy, Kane, right? I’m Kiyomi."
    "Kiyomi immediately moved closer to Kane as she spoke, pretending to adjust her shirt collar"
    ka "Yeah. Nice to meet you."
    "She stuck her hand out before he could react. He shook it anyway."
    kiy "Didn’t expect to see someone like you here. Thought you were the sporty type?"
    ka "Yeah, we'll seasons ending soon so..."
    kiy "Hey, I never said you couldn't do two things! It's pretty cool that you're here, honestly."
    ka "Yeah, figured it might be something different."
    "Her laugh was short, sweet, a little breathy. Koto knew that laugh. She’d heard it earlier, in the hallway. It wasn’t real."
    "Koto’s eyes drifted downward for a second."
    "And just like that... the crush she’d built up in her head—the version of him she’d imagined—fell apart."
    "It didn’t shatter."
    "It just... dissolved."
    "She didn’t hate him. He wasn’t rude, or mean, or doing anything particularly awful. But something inside her just... clicked out of place. Quietly."
    "The pedestal she’d put him on? It was empty now."
    "She barely noticed how still she had gotten."
    "Kane leaned back in his chair again, scanning the room casually."
    ka "Kinda figured this club would be all roleplay and handcuffs, not lectures and note-taking. Bit of a letdown."
    "Koto’s eyes snapped toward him."
    kmc "Then maybe you should’ve signed up for improv and left this one for people who actually care."
    "The air tensed around them."
    "Kane turned his head slowly to face her, blinking once."
    ka "Was that for me, or just a general PSA?"
    kmc "If the shoe fits."
    "He gave a short laugh, not friendly, not cruel. Just... dismissive."
    ka "Didn’t realize liking hands-on stuff made me the enemy."
    kmc "It doesn’t. But walking in like this is your pit stop on your way to wherever you actually care about?"
    kmc "Doesn't really scream {i}inspired{/i}."
    "Kane raised his eyebrows now, glancing at her."
    ka "Wow, so now there's a proper way to walk into a club?"
    kmc "There's a difference between walking in and walking all over it."
    "Kane’s brow lifted. His voice was still even, but it had cooled."
    ka "Alright. So now you’re the standard for effort?"
    "Kiyomi rolled her eyes."
    kiy "He’s literally just sitting. You’re making a huge deal out of nothing."
    kmc "You jumped in real quick to defend him, didn’t you?"
    kiy "Because you’re attacking him for no reason!"
    kmc "No reason? Please. You’re just mad I said it first."
    kiy "Oh, my god, get over yourself."
    ka "Can we not turn this into some weird competition?"
    kmc "Funny, coming from the guy who walked in acting like he’s above it all."
    ka "I never said I was above anything. I just didn’t realize I was gonna get psychoanalyzed on day one."
    kmc "Right. Because that would require self-awareness."
    "Even Mio shifted uncomfortably now."
    kiy "Kotonoha, you’re literally the one starting everything."
    kmc "No, I’m just not pretending it’s all fine when it clearly isn’t."
    kiy "Maybe it is fine and you just don’t like not being the center of attention."
    kmc "Girl, you’ve been orbiting him since he walked in. Don’t project on me."
    "That shut Kiyomi up, only for a second."
    ka "Okay, both of you can relax{nw}"
    kmc "No. You started it. With your 'ugh, lectures?' attitude."
    ka "I made a joke. If that rattles you, I’m not sure how you’re gonna handle anything serious."
    kmc "I’m 'rattled' because people like you walk in, suck up all the space, and then act like you don’t even want to be in it."
    ka "You don’t even know me."
    kmc "I thought I did."
    ka "And what made you think that?"
    "That shut the room up again, as Koto had just secretly revealed that she had a crush on him."
    "Koto opened her mouth to fire back{nw}"
    mi "Hey."
    "Koto blinked, her attention yanked sideways."
    "Mio’s face was calm, but her eyes were asking her to stop."
    "She didn’t say more, but that was enough."
    "Koto took a breath and looked down, biting the inside of her cheek."
    "Kane stayed quiet too, arms folded now, eyes flicking away."
    "Kiyomi decided to speak up again."
    kiy "I'm not just gonna let this go, you{nw}"
    "{i}CLAP.{/i}"
    #sfx
    "Mrs. Reynolds slammed her hand down flat on the front desk. The sound cracked like thunder."
    r "HEY. I don’t care who started it, all of you, knock it off."
    "Silence. Every student flinched, especially Kiyomi."
    r "This is not debate club. It’s not a soap opera. It's a space to learn. So if you're here to argue, take it outside."
    "She let that hang for a breath, just long enough to sting."
    r "Now sit down. Shut up. And let me teach."
    "No one moved for a second. Then chairs creaked as everyone slowly faced forward."
    "Mrs. Reynolds clears her throat."
    r "Alright. Let’s bring it back."
    "The tension deflated all at once. No one said anything, but they all shifted a little, sat straighter, quieter."
    "The moment didn’t disappear, but no one was holding onto it either."
    r "Looks like we’ve got a solid group..."
    "She slides the room door closed." 


    #check text
    "Why don’t we start by going around, sharing your name and why you’re interested in this club."
    "She pointed to Mio first."
    mi "Oh! Um—I’m Mio. I’m here because I think criminal justice is cool and... I kinda want to be a cop someday?"
    r "Good reason."
    "She turned to the next person."
    kmc "I’m Kotonoha. I guess... I’m just looking for something that feels right. Something that makes sense."
    r "Makes perfect sense to me."
    "She nodded once, then turned to Kiyomi."
    kiy "Kiyomi. I’m here because my mom’s making me, but whatever. Might as well give it a shot."
    "Mrs. Reynolds arched a brow but didn’t say anything."
    "She turned finally to Kane."
    ka "Kane. Uh... just wanted to try something new. Never really looked into this kind of stuff before."
    "Koto glanced up."
    "He didn’t look nervous."
    "He didn’t even look that interested."
    "But he knew exactly what to say."
    "And Kiyomi? Kiyomi was practically sparkling beside him."
    r "Good. I want all of you to stick around after today’s intro—I’ll be handing out some light case files for discussion. Just mock stuff, nothing heavy yet."
    "Everyone gave a nod or hum of agreement."
    "Mrs. Reynolds turned to the whiteboard and started scribbling out some bullet points."
    "Koto leaned slightly back in her chair."
    "Kiyomi was now leaning in toward Kane, her elbow lightly brushing against his. Kane didn’t seem to notice—or maybe he didn’t mind."
    "Koto didn’t feel jealous. Not anymore."
    "But she was watching."
    "And something about him just didn’t feel right."
 
    
   

label choice_teaser:
    scene black
    scene bg DC with dissolve_scene_full
    show koto 4o at t11 
    kmc "I failed them all..."
    scene bg SC with dissolve_scene_full
    show natsuki 2e at t11 
    n "Can't be hard to break in here...right?"
    scene bg AIR with dissolve_scene_full
    show aoki 5a at t11
    pa "Well, well, well...look at you..."
    scene bg confrence with dissolve_scene_full
    cd "I told you, no more of this nonsense about this case. You went out and did something stupid. You understood the risk loud and clear. Gun and badge. Now."
    scene bg corridor with dissolve_scene_full
    show monika 2p at t11
    "She starts hyperventilating. Who was that teacher? She had never seen her before..."
    scene bg MCR with dissolve_scene_full
    show koto 1bp2 at t21
    show yuri 5ct at t22
    y "Are you ok?"
    scene bg field with dissolve_scene_full
    show yyuri 1be at t11
    pl "You are more important than you realize, children."
    scene bg LCH with dissolve_scene_full
    show kiyomi 1bz1 at t11
    kiy "Goddamnit, Mom, SHUT UP!! Stop embarrassing me! I did what you asked, ok? I went to the stupid club and I hated it! It sucked!! Now, leave me alone! I just want to be left alone! GOD!"
    scene black with dissolve_scene_full
    return

label choice_memevid:
    scene black
    n "Wanna practice with me?"
    pause (1.0)
    qmc2r "Ngh{w=1}...I'm having a hard time getting it in.."
    n "It's fine..I mean, {w=0.3}this is your first time,{w=0.3} isn't it?"
    qmc2r "Uhh..{w=0.3}yeah."
    n "It'll be great.{w=0.3} Just try to take it slow and gentle."
    qmc2r "Hmmm..."
    n "That's it..."
    n "Trace around the edge super softly..."
    n "And when your ready, {w=0.3}put it in!"
    pause (0.5)
    n "In my opinion, there's no need to rush anything."
    n "It's best if you go nice and slow..."
    qmc2r "I think I get it,{w=0.3} like this?"
    n "Yep, it's in there now...{w=0.7}{size=15}good...{/size}"
    n "Now, keep it there and slowly press..."
    "Natsuki gasps."
    n "Don't rush, silly!"
    pause (0.5)
    n "That's perfect..."
    pause (2.0)
    n "It might be even better if you went in a teensy bit deeper{w=0.5}, like this..."
    qmc2r "NGUGHH!"
    pause (2.5)
    n "Ahah!!!"
    play music t7 fadein 1.0
    scene bg SKD with wipeleft_scene
    show natsuki 1bp at t21
    show cm 1a at t21
    show ka 1bx at t22
    n "You fucking moron! You got frosting all over my face!!!"
    show ka 1bw at t22
    qmc2r "Don't blame me! You were all up in my grill and you made me mess up!!"
    show natsuki 5bh at t21
    show ka 1bx at t22
    show cm 1a at t21
    n "Whatever, I was not!!"
    show natsuki 1bv at t21
    show cm 1a at t21
    n "I was just showing you the proper way to frost them, and then you got as stiff as a plank and got it everywhere!"
    show natsuki 1bx at t21
    show cm 1a at t21
    n "Great going, dumbass!!"
    show ka 2ba1 at t22
    qmc2r "Said I was sorry..."
    stop music fadeout 3.0
    scene black with dissolve_scene_full
    return