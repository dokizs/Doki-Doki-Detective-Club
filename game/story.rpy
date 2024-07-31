

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
    kmc "My asswipes that I used to call parents only just told me this morning..."
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
    "Everyone looks at Yuri." #when everyone's focused on yuri she switches positons
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
    n "I'm not just gonna sit here and let us sulk in silence for the next hour."
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
    "Monika smiles awkwardly. This wasn't on her itinerary at all. And while she didn't just want to sulk around for the next hour, she wanted to continue club activities."
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
    m "{size=10}This is the last time I let things out of my control.{/size}"
    scene black with wipeleft_scene
    stop music fadeout 3.0 
    pause (3.0)
    "chapter 3"
    pause (3.0)
    scene bg corridor with wipeleft_scene
    show sayori 1a at t11
    s "Ok, art room isssssssssss {w=3}here!"
    "Sayori would step into the art room."
    scene bg AR with wipeleft_scene
    "Some of the kids in the classroom looked at Sayori as she entered. She recognized some of them. But she wasn't here to goof around." 
    "She needed to see if there was something she could use for Koto's party!!"
    show sayori 1l at t11
    s "Hey guys! Happen to know if there's any art supplies I can borrow for a bit?" 
    show sayori 5b at t11
    s "I need to make a little something on short notice, eheh..."
    k1 "Oh, hey Sayori! Maybe you should ask the teacher! She'd probably be happy to help!"
    show sayori 1m at t11
    s "Really?!"
    show sayori 4r at t11
    s "Thank you so much!!"
    "Sayori happily skips over to the teachers desk."
    s "Hi, Missus!"
    t "Sayori! How are you still at school?"
    s "Oh, I'm in the literature club on the 3rd floor!!"
    t "How...interesting. I may need to stop by at some point."
    s "Uhhh, yeah!! Say...do you have any spare art supplies I can borrow? I need it for something. Any streamers or confetti, or glitter..."
    t "Sayori, that's not really traditional art supplies..."
    s "O-Oh..."
    "The teacher sighs but then smiles at Sayori."
    t "In the cubicles."
    "Sayori perks up."
    s "Thank you Missus!"
    t "Of course, Sayori."
    "Sayori skips over to the 3x3 cubicle and gets on her knees, peeking inside of them."
    "She found mostly everything she thought they needed and she started to ravage the cubicle."
    scene bg corridor with wipeleft_scene
    show monika 1a at t11
    "Monika would look inside the classroom, seeing Sayori and the teacher having a conversation."
    "She sees the Sayori skip away from the teacher, and the teacher glances out of her classroom door's window."
    "Monika stares back at her and something about her looks...off."
    "She gets a bit nervous and decides to avert her gaze, stepping out of sight of the door window."
    "She just leans up against the wall beside the door, and waits."
    "She starts hyperventilating. Who was that teacher? She had never seen her before..."
    scene bg AR with wipeleft_scene
    "The teacher would stare at Monika through the glass. She knew {i}exactly{/i} who she was."
    show sayori 1a at t11
    s "I got what I needed! Thank you, missus!!!"
    t "You're welcome, Sayori! Now run along! I think someone is waiting for you."
    s "Huh? Oh right, Moni!! Thank you! I'm sure she's on her way!!"
    "The teacher would nod her away."
    "Sayori flashes another smile as she walks out of the classroom."
    scene bg corridor with wipeleft_scene
    show sayori 1a at t11
    "She turns the corner, ready to walk back upstairs when she sees Monika, and it spooks her a bit."
    s "Ah! Oh, heyyy, Monika! Why didn't you come in?"
    "Monika was still leaning against the wall, hyperventilating."
    s "...Moni?"
    "Sayori sets the supplies down and tries to approach Monika."
    "Monika snaps out of her little attack."
    show sayori 1a at t21
    show monika 1a at t22
    m "H-Huh?"
    s "I asked why you didn't come in? Are you feeling ok?"
    m "I-I'm alright, Sayori...I see you got the materials..."
    s "Oh, yeah, I did!"
    "She'd pick the stuff back up."
    s "Could you help carry some of it back upstairs?"
    m "O-Of course..."
    "Monika grabs some things from Sayori and they both walk back upstairs."
    scene bg MR
    show monika 1a at t11
    m "W-What the hell?"
    m "No, No, No. This isn't right..."
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








    










    
    
    





    





