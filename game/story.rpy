
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
        "Teaser!!":
            jump choice_teaser
        "Memes":
            jump choice_memevid


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
    kmc "You wake me up earlier than I need to..and for what? Is it bad?"
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
    kd  "...Alright, sweetheart. {b}{i}We{/b}{/i} aren't going anywhere persay. But {b}{i}you{/b}{/i} are..."
    show koto 1be at t11
    "The gears inside her head would start to turn, her brain getting to work on figuring out what her father meant, and surely enough, she caught on quick."
    show koto 1bp2 at t11
    kmc "I..I'm moving schools?"
    "Tears would well up in her eyes before she even got a 'yes'."
    show koto 1bu at t11
    kd "...Yes, and you need to pack when you get home. Now, if you think you can get little bit in. It's a lovely place up west."
    show koto 1bu3 at t11
    kmc "W-What? Dad, that's so far from here! Why didn't you tell me sooner!?"
    show koto 1bu at t11
    kd "Listen, that was a mistake on me and your mothers parts. We decided not to tell you until today. I'm sorry it's such short notice but...you leave tonight."
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
    kmc "How...how could you?! First, you switch my schools even though I never wanted to leave, and then you only give me one day to pack?"
    show koto 1bu2 at t11
    kmc "To say goodbye to {i}all{/i} of my friends??"
    show koto 1bu at t11
    kd "We switched you because it offers more extensive programs than this backwater school!"
    show koto 2bu3 at t11
    kmc "Oh yeah? Well this 'backwater school'? I love it. With all my heart."
    show koto 1bu4 at t11
    kmc "And don't even get me started on the 'extra programs' bullshit. I'm a highschooler! I can look into that myself when I'm a senior! It's not time to think about any of that yet!!"
    show koto 2bu2 at t11
    kmc "I'm only a sophomore, I don't need anything extra right now!"
    show koto 1bu at t11
    kd "...{w=0.5}It's always nice to start early."
    show koto 2bt at t11
    "Kotonoha would grunt and throw her pillow at her desk, frustrated as to why any of this was held from her. She looks back at her father defiantly."
    show koto 1bu2 at t11
    kmc "I'm not going."
    show koto 1bw at t11
    kd "You must. You've already been unenlisted. Today {b}{i}is{/b}{/i} your last day. If you show up tommorow, you're not a registered student and they'll throw you off campus."
    show koto 1bv1 at t11
    kd "And if you're not in your new school, they'll prosecute all of us, as you have to be in a school building as a sophomore."
    kd "It has already been done and there's no if's and's or but's about it, young lady."
    show koto 1bp3 at t11
    "Koto looks defeated. She was powerless in this moment. Everything had been taken care of behind her back."
    "Her father takes a look at his watch."
    kd "Ah, you don't have any more spare time. It's six fifty five already. Just get dressed. You can pack when you get home."
    show koto 1bp2 at t11
    kmc "B-But-{nw}"
    show koto 1bp3 at t11
    kd "We can discuss later if necessary. Now, get ready."
    show koto 1bs3 at t11
    "Her father left the room, leaving Kotonoha alone to think."
    show koto 1bp at t11
    "How could they just do this to her? She knew it was an epidemic. Almost every person she had talked to said that thier parents had packed them up and moved them here."
    "But that's just it. Those parents sent their kids off to {b}this{/b} school. Koto had been in this district since she was a child and now, she had to move to one all the way up west."
    show koto 1bo at t11
    "This would be the last time she saw her room. The last time she saw her parents, her friends, her real home."
    show koto 1bp3 at t11
    "After high school was college, and she had already thought about where she wanted to go. She was already taking dual credit classes and saving up for the ridiculously expensive room and board."
    show koto 1bw at t11
    "She had no reason to come back here. Maybe when she finished? But that was 6 years from now! Her friends would be long gone, her parents older, the school filled with new and unfamilar faces."
    show koto 1bv1 at t11
    "However, this was no time to think about what was shaping up to be a pretty shitty day. Maybe her worst, but it was hard to tell. There was a competetor for that spot."
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
    show yuri 1o at t22
    y "You think they're weird because they...do what they're named after doing?"
    show natsuki 5e at t21
    n "Yeah!! Like why can't they be called cakeeaters or somethin?!"
    show yuri 1h at t22
    y "Cakeaters? Really?"
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
    m "Even if they did, Sayori, you didn't have to go through with it. You could've reported them to a higher offical. This behavior won't be tolerated inside or outside of this club."
    show sayori 2v at t21
    s "I-I understand..."
    hide sayori
    hide monika
    scene bg club_day
    show koto 1u at t51
    "She'd make her steps a little louder than usual on purpose to catch everyone's attention."
    show koto 1u at t52
    "Monika almost immediently takes notice and walks over to Kotonoha."
    show koto 1u at t21
    show monika 5c at t22
    m "Koto! Welcome! We were waiting on you to share poems! {nw}"
    show koto 1u2 at t21
    kmc "Monika...hey.."
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
    show monika 1a at t51
    show sayori 1a at t52
    show natsuki 1a at t53
    show yuri 1a at t54
    show koto 1a at t55
    m "So...your news...?"
    kmc "Right..."
    n "Oh, come on! You have Monika round us all up and then you forget your damn question?? This is a waste of time!!"
    kmc "Natsuki, this is ser {nw}"
    m "NATSUKI! Kotonoha doesn't like to slack off unlike the rest of you. It's something important, at least to her, as far as you know."
    m "Her and Yuri actually. The family ties are the most obvious in that aspect."
    "Koto and Yuri would share a smile at Monika, appreciating the compliement."
    m "So if you would kindly be quiet and let our fellow club member speak, it'd be gladly appreciated."
    "Natsuki piped down after getting softly scolded by Monika."
    kmc "Thank you, Moni."
    kmc "So...my announcement. I...I..."
    "Yuri puts her hand on her cousins shoulder."
    y "Take your time."
    "Kotonoha would look at the clock. It was already 4:45. Enough time had passed. She only had until 6 to say goodbye. She had no time at all."
    "She'd finally break her tough girl facade."
    kmc "I-I DON'T HAVE TIME TO TAKE!!"
    "Yuri flinches, her hand coming off Kotonoha's shoulder."
    m "Kotonoha...what are you trying to say?"
    play music ("A Faded Memory.mp3")
    kmc "I-I'm...I'M MOVING, ALRIGHT??"
    "She felt as if she was on the verge of tears and as she looked around, she saw the mood had immiedently dampened signifigantly."
    s "W-What...?"
    kmc "I-I'm moving, alright?"
    y "W-Why didn't you tell us sooner?"
    kmc "Don't you think I would've if I knew??"
    kmc "My 'parents' or at least the people that I used to call parents only just told me this morning..."
    n "I-It must be some sort of April Fools joke or something?!"
    m "It's September {nw}"
    "A silent head shake from Koto told her everything she needed to."
    n "No...It can't be true..It can't!!"
    "Now Natsuki looked to be on Koto's level of emotion, looking like she was almost drawn to tears."
    s "You can't leave!! I WON'T LET YOU!!"
    show monika 1a at t51
    show natsuki 1a at t52
    show yuri 1a at t53
    show sayori 1a at t54
    show koto 1a at t55
    "Sayori runs up to Kotonoha, hugging her tightly." #sayori crying
    kmc "S-Sayori...plea{nw}"
    s "NO! I'M NOT LETTING GO!!!"
    m "Sayori, please let go of Kotonoha...she..."
    "Monika takes a deep and sharp inhale."
    m "She needs a bit of time to breathe."
    s "S-She's gonna leave us, I-I won't let her leave!!"
    kmc "Sayori...please let me go. You're constricting my lungs..."
    "Sayori looks up at Koto with hurt, sadness and tears threatening to fall."
    kmc "Please..."
    "Sayori nods and finally lets go."
    #sayori goes back to normal but stays where she is, moves back to og position later
    kmc "Thank you...I'm really sorry to all of you that it's on such short notice. Especially you, Monika."
    m "It's ok. I believe you when you say that your parents only told you this morning."
    m "While it is unconventional to let your child know that they are leaving you and their home they've known since as long as they've been alive, it's not anything to be worried about."
    "Monika smiles."
    "...That's strange."
    "She kind of hit it directly on the head, almost like she had a glimpse inside her head. It was eerie but it struck with more of a sympathetic tone than anything."
    y "Actually...it might be."
    "Everyone looks at Yuri." #when everyone's focused on yuri, saysay switches positons
    m "Hm? What do you mean?"
    show monika 1a at t51
    show sayori 1a at t52
    show natsuki 1a at t53
    show yuri 1a at t54
    show koto 1a at t55
    y "The new policy of '5 members per club'. Remember?"
    m "Oh, you're right, Yuri. It slipped my mind."
    "Monika would facepalm softly."
    m "Well, if any of you forgot like I foolishly did, last week, we had school wide meeting. All clubs were there and a new rule was established, we have to have over 5 members."
    m "Which means that along with the sad news of Kotonoha's departure, it means we're going to have to find another member to stay together, or we may get disbanded..."
    "Everyone looks much worse now. Not only was it sad that Kotonoha was leaving but it's so detrimental that they might not even have a club anymore!!"
    s "Well...I wouldn't say that..."
    "Everyone would now look at Sayori."
    s "I was kind of planning to invite someone! Before Koto said she was leaving, of course, so we could have 6 members!!"
    s "But now that Kotonoha's leaving, they could be our 5th!!"
    "Monika looks deep in thought."
    m "Would they be willing to join?"
    s "Pfft, yeah, they would!!"
    m "Hm, well then I suppose that's a problem solved!!"
    "Sayori was scared out of her mind. She knew he had been struggling to even look at clubs, let alone join one..."
    "Announcing him as 'The Fifth Member' didn't help much either. Now the girls were counting on Sayori to make good on her promise."
    "Looks like she had some seeds to plant and some cute faces to make."
    "Monika clears her throat interuptting Sayori's train of thought."
    m "Let's not let that overtake our sadness over the loss of one of our original members however."
    y "Kotonoha is still leaving and we must keep the mood right."
    m "Thank you, Yuri. Kotonoha, we're sorry for your unfortunate situation."
    m "I wish we could've done more..."
    pause (5.0)
    #natsuki changes expressions (intervals)
    n "...Wait! I got it!"
    n "I have some cupcakes in my home economics room!!"
    m "But Natsuki, aren't those for a project?"
    n "Who cares?! I can make more, they don't take awfully long to make!"
    n "Plus I'm not just gonna sit here and let us sulk in silence for the next hour."
    m "Bu{nw}"
    n "Don't question me! It'll just be a quick snatch and grab!"
    "And without letting anyone protest, she left the room."
    hide natsuki
    show monika 1a at t41
    show sayori 1a at t42
    show yuri 1a at t43
    show koto 1a at t44
    "Monika sighs tiredly."
    m "Well, I guess we're having cupcakes this afternoon!"
    y "Only cupcakes?"
    "Monika looked at Yuri, understanding what she was implying."
    "She sighs again."
    m "You want to make tea, don't y{nw}"
    y "I want to make tea, yes."
    pause (2.0)
    #have monika emote
    m "You know what? Why not!"
    y "Thank you, Monika!"
    "Yuri would hurridly sprint over to the closet to retreive her tea set."
    hide yuri
    show monika 1a at t31
    show sayori 1a at t32
    show koto 1a at t33
    "Monika turns to Kotonoha."
    m "I guess we're having a celebration for your departure, Koto."
    "Monika smiles awkwardly. This wasn't on her itinerary at all. And while she didn't just want to sulk around for the next hour, she wanted to continue club activities like normal."
    kmc "I mean, it doesn't look like they're giving us much of a choice, are they?"
    m "It appears not...well, I guess me and Sayori are going to pitch in as well.."
    s "Ooo, ooo! I can find some decorations in the art classroom! They're holding a meeting right now too, and they'll have a ton of supplies that can help!"
    "Sayori doesn't even let her idea process in anyone elses head and she leaves without a second thought."
    hide sayori
    show monika 1a at t21
    show koto 1a at t22
    "Monika just can't catch a break today."
    m "Well! I suppose I'll go help her!"
    kmc "Maybe I could come with!"
    m "Come with? It's your party, Koto! Just sit back and watch!"
    "Kotonoha looks a bit sad but it's quickly replaced with happiness. She had been thinking about something like this all day, but she never thought she would actually get it!"
    kmc "Thank you, Moni. I appreciate it."
    m "Of course!"
    "Monika walks to the door."
    show monika 1a at t51
    m "{size=10}This is the last time I let things out of my control.{/size}"
    scene black with wipeleft_scene
    stop music fadeout 3.0 
    pause (3.0)
    "chapter 3"
    pause (3.0)
    scene bg corridor with wipeleft_scene
    show sayori 1a at t11
    s "Ok, art room is{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}s{w=0.7}{w=0.7}s {w=3}here!" 
    "Sayori would step into the art room." 
    scene bg AR with wipeleft_scene
    "Some of the kids in the classroom looked at Sayori as she entered. She recognized some of them, waving shyly at a couple of friends." 
    "But she wasn't here to goof around." 
    "She needed to see if there was something she could use for Koto's party!!"
    "She glanced around the room, her excitement could be felt with every extra step she took." 
    show sayori 1l at t11 
    s "Hey guys! Happen to know if there's any art supplies I can steal from you guys?" 
    show sayori 5b at t11 
    s "I need to make a little something on short notice, eheh..."
    "The other students exchange curious glances, and one or two of them smile sympathetically. Sayori's enthusiasm was infectious, and they could see she was on a mission." 
    k1 "Oh, hey Sayori! Maybe you should ask the teacher! She'd probably be happy to help!" 
    show sayori 1m at t11 
    s "Really?!" 
    show sayori 4r at t11 
    s "Thank you so much!! I really appreciate it!" 
    "Sayori skips over to the teacher's desk, her shoes making a soft pat-pat sound on the floor." 
    s "Hi, Missus!" 
    t "Sayori! How are you still at school?" 
    s "Oh, I'm in the literature club on the 3rd floor!!"
    t "How... interesting. I may need to stop by at some point." 
    s "Uhhh, yeah!! Say... do you have any spare art supplies I can borrow? I need it for something. Any streamers or confetti, or glitter... anything that can make a party pop!" 
    t "A party? Sayori, that's not really traditional art supplies...we don't usually have those things around here…" 
    "She wasn't lying. Now that Sayori thought about it, there was a distinction between art supplies and party supplies." 
    s "O-Oh... I guess I didn't think about that. I just...we were gonna do a thing and..."
    "She trailed off not knowing if she wanted to continue."
    #cri
    s "{size=10}And we wanted to make it special...{/size}" 
    "The teacher sighs heavily at first but then smiles warmly at Sayori, her eyes softening." 
    t "In the cubicles." 
    "Sayori gasps as her face lights up, and she bounces on the balls of her feet in excitement." 
    s "Thank you Missus! I'll be quick!" 
    t "Of course, Sayori." 
    "Sayori skips over to the 3x3 cubicle and gets on her knees, peeking inside with a look of determined curiosity." 
    "She finds mostly everything she thought she needed—colorful papers, streamers, and even a bit of glitter. She starts to eagerly rummage through the cubicle, her hands moving quickly." 
    "With each item she finds, her excitement grows. She giggles as she sorts through the supplies, imagining all the fun decorations she can make." 
    scene bg corridor with wipeleft_scene 
    show monika 1a at t11 
    "Monika would look inside the classroom, seeing Sayori and the teacher having a conversation." 
    "She notices Sayori skip away from the teacher, and the teacher glances out of her classroom door's window." 
    "Monika stares back at her and something about her looks... off." 
    "She gets a bit nervous and decides to avert her gaze, stepping out of sight of the door window." 
    "She leans up against the wall beside the door, her heart racing slightly." 
    "Soon, she starts hyperventilating. Who was that teacher? She had never seen her before..."
    scene bg AR with wipeleft_scene
    "The teacher would stare at Monika through the glass. She knew {i}exactly{/i} who she was."
    show sayori 1a at t11
    s "I got what I needed! Thank you, missus!!!"
    t "You're welcome, Sayori! Now run along! I think someone is waiting for you."
    s "Huh? Oh right, Moni!! Thank you! I'm sure she's on her way!!"
    "The teacher would nod her away, her gaze lingering for a moment longer as Sayori exits."
    "Sayori flashes another bright smile as she walks out of the classroom, her arms filled with the supplies she's gathered."
    scene bg corridor with wipeleft_scene
    show sayori 1a at t11
    "She turns the corner, ready to walk back upstairs when she sees Monika, and it spooks her a bit."
    #scared
    s "Ah!"
    pause (2.0)
    #expression change from surprised to calm
    s "Oh, heyyy, Monika! Why didn't you come in?"
    show layer master at heartbeat
    show vignette
    play music ("HeartBreath (Moni Song).mp3")
    "Monika is pressed against the wall, her posture was tense and rigid, unlike her usual composed self." 
    "Her face is pale and her eyes dart around erratically, as if she’s struggling to focus on anything." 
    "Her breaths come in short, shallow gasps, each one seeming to come with visible effort. Her hands are clenched at her sides, fingers trembling slightly."
    "She occasionally brings one hand up to her chest, as if trying to steady her heartbeat. Her shoulders rise and fall rapidly with each uneven breath, and she sways slightly, almost as if she’s about to collapse."
    "Monika's breathing is labored, with a faint wheezing sound accompanying each inhale. She occasionally bites her lip, trying to suppress the rising panic, but it’s clear that she’s overwhelmed."
    "Her wide and glassy eyes show a sense of fear and confusion."
    s "...Moni?"
    "Sayori sets the supplies down gently, her concern growing as she approaches Monika cautiously."
    s "M-{w=1}Monika?…"
    "Monika snaps out of her little attack, blinking rapidly as she tries to regain her composure."
    hide vignette
    show layer master
    stop music fadeout 1.0
    show sayori 1a at t21
    show monika 1a at t22
    m "H-Hm?"
    s "Are you ok? You're on the floor and you don't look too good...like at all..."
    m "Oh, um, yes! Of course, I'm fine!"
    "Monika stands up and brushes herself off."
    m "I just… since I was behind you, I saw you getting the things and just decided to wait for you. I didn't expect you to be out so soon…"
    "Sayori reaches out, placing a comforting hand on Monika's shoulder."
    s "You don't look fine. Are you sure you're okay?"
    "Monika takes a deep breath, slowly removing Sayori's hand, her breathing slowly calming as she forces a small smile."
    m "I'm okay now, really. I just... had a bit of a panic. It's nothing."
    s "Awww, but I feel sorry for you, Moni!."
    "Sayori gasps as she gets a bit of an idea."
    s "Let's talk about it while we walk, okay? Maybe I can help you calm down and feel better!!"
    "She blushes at the prospect. Spending time with Monika was always great..."
    "Monika shakes her head, her eyes softening as she appreciates Sayori's concern."
    m "Thanks, Sayori. But I'm ok, really."
    "Sayori's face drops slightly but regardless, she picks up the supplies again, giving Monika a reassuring smile while she leaves some of it for her to grab."
    s "Alright, well then let's head upstairs. I'm sure Koto's waiting on us!!"
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
    #another presense that she feels thats similar to hers? No reason not to take that oppurtunity. 
    #Even if he couldn't get her out, she wanted to see who or what it was (reason im calling 
    #MC it is because this is all her speculation. Shes been here in the game and aware for a while and you 
    #might be asking, why am I writing cliff notes for lore thats not going to be in the mod? 
    #I dunno. :P) but the game "resets" her, or so it thinks (you might also be asking why am i personifying the game itself?
    #also dunno)
    m "This isn't right...No, No, NO!"
    m "Why am I here?? THIS ISNT RIGHT!"
    m "I-I want to get out..."
    m "LET ME OUT!"
    #fix replies tag
    m "fix replies tag"
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
    s "...{w=1}alright Monika, well then let's just go. I don't like seeing you like this."
    m "Seeing me like what? I'm ok!"
    "Sayori pauses mentally. She knows it isn't true. Something is amiss!! But dang it, if she isn't going to take her {glitch}'s word."
    s "If you say so..."
    m "Now, c'mon. Let's get this stuff upstairs for Koto, hm?"
    s "Y-You're right..."
    "Sayori spots some empty discarded boxes that they could use."
    "They loaded the supplies into 2 separate boxed before picking them up and heading back upstairs."
    hide monika
    hide sayori
    scene bg SS with wipeleft_scene
    pause (2.0)
    "As Monika and Sayori trudge up the stairs, Monika is left to think."
    m "{i}What...who...is that..??{/i}"  
    m "{i}It's like no one else here.{/i}"
    m "{i}It feels like me. Or well...felt.{/i}"
    "Monika starts to mentally connect the dots."
    m "{i}That's it! Sayori warped the game when she went off script...{/i}" 
    #She's wrong obviously, the MC just pops in the world one day and that time can be when the game is downloaded
    #and lets just say that the person who installed got busy and decided not to play yet. Well when he does start 
    #to play, koto has successfully moved and DDLC continues on as normal. This also gives Moni good reason to be
    #suspicious of Sayori hence why she starts to look like she's just playing the friend card in the main game
    #and that could be why sayo dies first.
    m "{i}But how..? I thought I was the only one?{/i}"
    m "{i}She hasn't shown any signs...and I haven't felt her...{/i}"
    m "{i}Can she hide her power?{/i}"
    m "{i}Why hasn't she told me? She's an airhead, it's in her character to tell me!{/i}"
    m "{i}This is all so frusterating!!{/i}"
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
    "Sayori looks back at her, this time determined not to keep her mouth shut.."
    s "Are you tired already? Is that it?"
    m "Uhm...{nw}"
    m "Yes...just very...tired..."
    s "Aww, c'mon, you can't be tired!!"
    s "You're overexerting yourself, we're not running a marathon! We're just carrying boxes! For Koto!"
    m "Mhm...right.."
    "Monika was skeptical of Sayori now, but she also didn't want to have a conversation with her right now."
    "And her facial expressions, silently and seemingly politely telling Sayori to stop didn't seem to be registering."
    "She wanted to get back to her thoughts."
    s "We're almost at the third floor! Just another flight!"
    "Monika out of annoyance rolls her eyes and responds sarcastically."
    m "Of course...I can't be tired! Not now! Not when were {i}soooooo{/i} close...."
    "Sayori however, still didn't seem to get the hint and took it as a positive statement."
    s "That's the spirt! Now, c'mon!"
    "Sayori finally stops talking and they start to silently walk up the stairs again."
    m "...{w=1}{i}I've got my eye on you, Sayori.{/i}"
    m "{i}And whoever your little friend is too...{/i}"
    tl "..."
    scene bg SC with wipeleft_scene
    "After a hefty walk to the other side of the building, Natsuki gets to her Home Economics class."
    show natsuki 1a at t11
    n "Jesus, that was a long ass walk..."
    "Natsuki peers inside the class to see that the lights are off."
    #face change
    n "Damnit!! Out of all the days she decides to stay after, today isn't one of them?"
    "She jiggles the handle, trying to see if it was locked. It, in fact, was locked."
    n "Ugh, great! Just my luck!!"
    "She looks around."
    show natsuki 2e at t11 
    n "Alright...well, it can't be hard to break in here...right?"    
    n "People in movies do it all the time!"
    "She looks around trying to find anything she could use."
    "She then gets an idea."
    n "Oh! Duh..."
    "She takes out her hairpins."
    n "I don't know how I always forget to take these out when I'm doing my pigtails."
    n "But hey, at least today they're being useful{nw}"
    #Natsuki's hair falls over her face, add sprites and sfx
    pause (3.0)
    n "Hmph, should've expected that."
    "She tucks the extra hair behind her ear, a look of annoyance on her face as she gets on her knees to pick this lock."
    n "Alright, Daddy, time to use those skills you taught me..."
    "She starts to use the rythmic method her father taught her."
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
    n "Wow... our side never looks this pretty.."
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
    "However, her thoughts start to betray the lovely moment of self reflection.."
    n "If only I had someone to share it with... someone who could really appreciate how perfect this feels. The perfect person…"
    n "No..the perfect guy. In the perfect spot…"
    "She opens her eyes, looking around the empty room, the warmth and quiet now tinged with a sense of solitude."
    "She sighs harshly, feeling a pang of loneliness as she shoves herself off the desk.."
    #she's supposed to shake her head, if i can't do it in spirtes, I'll write it out
    n "Ugh...I hate getting sappy."
    n "Time to do what I broke in here to do..."
    "She walks over to the closet and goes for the low shelf where she put her cupcakes."
    "She folds the closet door shut as she holds the bulky tray of cupcakes."
    n "Gonna need all these for Sayori's ass. By the time I turn around, she'll have eaten all of them."
    "She chuckles to herself before she hears noises outside. Some she can't decipher."
    "She turns around quick, suspicious of what the noises are. She consciously decides that whatever it is, isn't good."
    n "That's my que. I'm getting the hell out of here before I get caught."
    "She quickly tip toes over to the door, ducking under the glass, waiting for the noises to pass."
    "Turns out it was students talking."
    "She could just walk out now, but she doesn't know those kids. They might be the snitching type."
    n "And no one likes a snitch...."
    "After a while, the conversation moves elsewhere."
    "Time to escape."
    n "Go go go!!"
    "She quickly locks the door before slipping between the small crack in the door she made and slides it closed again quietly, just in case."
    scene bg SC with wipeleft_scene
    show natsuki 1a at t11
    "Natsuki takes one more look around to see if anyone was listening or watching to the naked eye."
    n "I...think I'm clear..."
    "She smirks a devilish smirk to herself as she walks back to the other side of the building feeling accomplished, even though what she just did was very wrong."
    "Natsuki looks out the windows lining the halls as she makes her trek back. She wasn't gonna lie about that part, it was pretty."
    "She thinks about the other part of what she said in the class though. The thing about needing 'the perfect guy'."
    n "No...that's stupid. I don't need anyone."
    "She fake gags, even though no ones around to see it."
    "She didn't need anyone, let alone a sweaty, stinky, testosterone filled, boy. {w=2} Gross."
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
    "Yuri puts on the last of tea."
    "She walks over to where Koto is sitting."
    scene bg club_day with dissolve_scene 
    show yuri 1g at t22
    show koto 1t at t21
    pause (3.0)
    show yuri 1h at t22
    y "So. When were you going to tell me?"
    show koto 2t1 at t21
    kmc "I told you, I didn't know until this morning."
    y "And what's that mean? You didn't think to text me or call me before you got to school?"
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
    "Yuri runs up to Kotonoha and envelops her in tight hug."
    y "Please don't go..."
    "Yuri was now softly sobbing in Kotonoha's arms."
    "Koto sighs, her voice pained as she speaks."
    kmc "I tried being rebelious. My parents already settled everything."
    kmc "All my affairs have been set behind my back."
    "Yuri cries a little harder now."
    y "T-There has to be some way! Some way!!!"
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
    y "Are you kidding? I've grown up signifigantly since I was a toddler!"
    kmc "Then what are you doing?"
    "Kotonoha smirks teasingly."
    kmc "Still crying in your older cousins arms."
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
    n "Ugh. Gay."
    "Kotonoha lets go of her cousin and turns to the doorway, seeing Natsuki leaned in the frame."
    kmc "Excuse me?"
    kmc "We're related...?"
    n "So?? People do crazy shit all the time! and I thought americans were weiro, trying to marry their sisters in Colarado!!"
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
    y "Ill be back."
    hide yuri
    show monika 1m at t41
    show sayori 4x at t42
    show natsuki 5h at t43
    show koto 1f at t44
    n "Finally. You know how much I had to go through to get these things?!"
    "Monika finally regains her sense of self, ending her little mini epiisode."
    "Just as Natsuki had spoken."
    m "What did you have to do to get them?"
    n "I had to break into the Home Ec class!"
    m "You broke into a class?! Why didn't you just come find us and tell us the room was locked??"
    n "Because, {i}{b}Monika.{/i}{/b}"
    n ".{w=3}.{w=3}.{w=3}"
    "Monika stares quizzically."
    m "Because what?"
    n "BECAUSEEEEEEEEEEEEEEEEE.{w=1} I don't fall behind on my promises."
    show natsuki 5t at t43
    n "I do what I say I'm gonna do!"
    show natsuki 5i at t43
    pause (2.0)
    show monika 1n at t41
    m "Well, that surely is an....admirable trait to have..."
    n "Damn straight."
    n "Now we gonana get this party started or what?"
    m "I guess we should. Club's end at 6 and it's already 4:45."
    s "Ehehe, yayyy! Time to decorate!!"
    "Yuri returns with teacups on a metal tray."
    show monika 1n at t51
    show sayori 4x at t52
    show natsuki 5i at t53
    show yuri 2i at t54
    show koto 1f at t55
    y "and quick. Like Monika said our time is limited, so let's not waste it."
    m "I couldn't have said it better. Let's get to it, girls!"
    e "Yeah!!"
    s "Not Koto, though!"
    exk "Yeah!"
    scene black with wipeleft_scene
    "The girls would get to hastily decorating the class to the best of their ability on such short notice."
    "Natsuki unwrapped the cupcakes out of their foil and meticulously placed them on each desk."
    "Yuri sat some of her scented candles on each desk alongside Natsuki, before placing 5 main tea cups on the teachers desk."
    "And despite their wishes, Koto helped decorate for her own party."
    "She helped Monika and Sayori put up all the miscillanious banners and streamers."
    "After a while, it was all starting to come togetther."
    "They all took a step back and collectivly wiped their brows."
    scene bg KPR with wipeleft_scene
    show monika 1m at t51
    show sayori 4x at t52
    show natsuki 5y at t53
    show yuri 4a at t54
    show koto 1f at t55
    kmc "Wow everyone...this looks beautiful..."
    "Natsuki was about to speak, probably about to say something snarky, but Monika was already glaring at her as if retroactivly saying 'Save It.'"
    s "Only the best for you!"
    kmc "Well, shall we party?"
    n "That we shall!"
    "Natsuki would rummage in her bag and would pull out a portable speaker."
    "Everyone gives her a funny look."
    n "Ahem...I use it for bathroom parties, ok?"
    m "...Alright, I suppose."
    n "Natsuki puts on some high energy dance music."
    n "Now this is good shit!!"
    y "Natsuki..."
    n "Nope, don't even! I'm not letting you all turn this into a pity party! This bitch is gonna have some energy!"
    m "We understand, but maybe something less...'rave-equse' and something at least a bit less high energy?"
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
            jump choice_Sayori
        "I liked Natsuki's music better.":
            jump choice_Natsuki
    

    label choice_Natsuki:
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
            jump choice_Sayori
        "I liked Natsuki's music better.":
            jump choice_Natsuki2

    label choice_Natsuki2:
    m "WRONG."
    m "P{w=0.4}I{w=0.4}C{w=0.4}K{w=0.4} A{w=0.4}G{w=0.4}A{w=0.4}I{w=0.4}N."
    
    menu: 
        "This is much better!":
            jump choice_Sayori
        "I liked Natsuki's music better.":
            jump choice_Natsuki3

    
    
    label choice_Natsuki3:
    m "Hm. I see."
    m "I can play that game too, silly!"
    m "While I can't seem to make any huge changes to your game like deleting your saves like a little flower..."
    m "Or disable the skip button..."
    m "I sure as hell can piss you off!"
    m "See you soon.{nw}"
    return

    
    label choice_Sayori:
    "Koto was smiling."
    kmc "You made a good choice, Sayori."
    kmc "Sorry, Natsuki."
    n "Ugh, whatever."
    m "Natsuki, don't."
    "Natsuki rolls her eyes."
    pause (2.0)
    #have someone emote
    kmc "Well, what are we standing around for?"
    kmc "You guys got this all together last minute, and even though I didn't pick your music, I agree with you."
    kmc "If we're gonna have this party, it's not gonna be out of pity!"
    "Natsuki smirks at the mention, she's glad her voice hadn't completly fallen on deaf ears."
    s "Koto{nw}"
    n "AHEM. {w=0.5}"
    s ".{w=1}.{w=1}.{w=1}Natsuki...{w=0.5}is right..."
    s "This party needs to be super happy and fun! My playlist is gonna make sure that the mood is up, up, up!!"
    y "Let's not forget, we're at school, we still need to be civil and quiet."
    m "Yuri's right, let's not completely forget where we are. Let's not make our club neighbors mad."
    n "Again..."
    s "Oh, right, that time we got into it with the anime club!! How'd that even happen?"
    y "I believe it was because of you or Natsuki."
    s "What?! It definitly wasn't me!! I think..."
    s "I'd remember something like that! It had to be Natsuki!"
    n "Me? Hell no, it wasn't! Like you said, you think!"
    n "You must have short term memory loss or something!"
    m "Girls, girls, Calm down."
    n "Hmph."
    pause (1.0)
    y "Didn't it end up being a good thing in the end?"
    m "Hmm...Oh, you're right, Yuri! We started a little 'rivalry' with them!"
    n "Oh, right, how could I forget! Me and Sayori had our own little division away from you two."
    m "Really?"
    s "Ehehe, it's true!! I was a spy!"
    y "Sayori, you little sneak."
    "Sayori and Yuri snicker."
    s "It was fun!!"
    n "And of course, {b}I{/b} was the mastermind behind it all!"
    m "Mastermind behind...oh. my. goodness."
    y "That was the 'foul play' they accused us of!"
    y "You could've jeapordized our chances of winning!"
    n "C'mon, I was HELPING, jeez..."
    n "You all were taking too long to leap, and I was feeling froggy!"
    m "Did you really have to rope Sayori into it though?"
    s "I wanted to join, she didn't force me!"
    "Monika and Yuri's faces shift strangely."
    m "...Really?"
    n "Trust me, I was kidding earlier."
    n "She was the one that came up with more than half of it!"
    n "I was shocked myself."
    "The girls look at Sayori."
    s "What?"
    s "I can't be bad sometimes?"
    y "I..I suppose so..."
    m "Everyone has been bad at some point in their life, but it's usually on accident..."
    s "What, now I can't be honest?!"
    m "No, Sayori, it isn't that-{nw}"
    "Sayori speaks as she begins to giggle."
    s "Man, you all are confusing..."
    "The giggling is infectious and before long the entire club was giggling."
    "After hopping from one talking point to another, the giggling turned to laughing, and the girls we're now crying laughing while trying to continue the conversation."
    "Everyone except{nw}"
    kmc "Me."
    "Koto had been silent the entire time, watching and listening to her friends bring up memories."
    "They all looked genuinely joyous, reminiscing on memories."
    "Man, I'm gonna miss them."
    "So, so bad."
    "Koto looks around, soaking in the enviroment."
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
    kmc "Why are we just do a simple group hug and just move on?"
    kmc "This feels pointless..."
    show koto 1o at t11
    #have static fade gradually sooner than this
    pause (5.0)
    #cut it off when yuri arrives
    show yuri 1a at t21
    show koto 1a at t22
    y "Are you okay?"
    "Kotonoha snaps out of her little daze, holding her head for a second."
    "She slowly turns to her cousin and smiles a sweet smile before taking a tiny sip of her tea."
    kmc "I'm okay, Yuri. Promise."
    y "If you say so, Koto."
    "Sayori looked up from her cupcake, speaking with her mouth full." #make cupcake mess for sayori like i did for natsuki
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
    s "Okay, okay!! Stop trying to yank my hair out, yeesh!!!"
    kmc "We should probably get back over there before they kill each other..."
    y "Wise idea."
    "Yuri chuckles as she grabs Kotonoha's hand and forces her over with the rest of the girls."





    
    

    return



    
label choice_teaser:
    scene black
    scene bg DC with dissolve_scene_full
    show koto 4p at t11 
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
    kiyomi "Goddamnit, Mom, SHUT UP!! Stop embarrassing me! I did what you asked, ok? I went to the stupid club and I hated it! It sucked!! Now, leave me alone! I just want to be left alone! GOD!"
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
    








    










    
    
    





    





