#This is a copy of definitions.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for Definitions
#This section defines stuff for the game: sprite poses for the girls, music, and backgrounds
#If you plan on adding new content, pop them over down there and mimic the appropriate lines!
define persistent.demo = False
define persistent.steam = False
define config.developer = False #Change this flag to True to enable dev tools

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)
init python:

    import random
    import string

    def random_string_generator(str_size, allowed_chars):
        return ''.join(random.choice(allowed_chars) for x in range(str_size))

    class GlitchText(renpy.Displayable):

        def __init__(self, length, delay, **kwargs):
            super(GlitchText, self).__init__(**kwargs)

            self.length = length
            self.delay = delay
            self.count = 0
            self.currentText = renpy.text.text.Text(random_string_generator(self.length, string.ascii_letters))

        def render(self, width, height, st, at):

            if self.count == 0:
                self.currentText = renpy.text.text.Text(random_string_generator(self.length, string.ascii_letters)) 


            self.count = (self.count + 1) % self.delay

            width, height = self.currentText.size()

            render = renpy.Render(width, height)
            
            render.blit(renpy.render(self.currentText, width, height, st ,at),(0,-3),False)
        
            renpy.redraw(self, 0)

            return render


    def glitch_tag(tag, argument):
        return [ ( renpy.TEXT_DISPLAYABLE, GlitchText(12,5)) ]

    config.self_closing_custom_text_tags["glitch"] = glitch_tag

#Music
#The Music section is where you can reference existing DDLC audio

#You'll see this in some existing scripts as command 'play music [t1]' for example
#For easier reference, there are comments next to it so you can go DJ on the mod :)
define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)


define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"

define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
#Hey Mod team, our themes aren't defined here in the original script.
#Did some reading around and there was this + "_character" reference elsewhere.
#Anyhow, I'll try 'defining' them and see if it works!

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #I'm the only one with pianos x3
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Hxppy Thoughts with Ukelele & Snapping~!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!

#Yeah, Monika... that should be good.
#So, take it from her and if you want to define music, make sure it exists in the appropriate folder
#Define its "audio.name" and see how it goes! (this should always be .ogg too, I think)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"
define audio.Faded = "<loop 0> A Faded Memory.mp3" #Custom; Sad Musica
define audio.YuriSadge1 = "<loop 0> Lamentation1.mp3" #Custom
define audio.YuriSadge2 = "<loop 0> Lamentation2.mp3" #Custom
define audio.YuriSadge3 = "<loop 0> Lamentation3.mp3" #Custom
define audio.Heartbeat = "<loop 0> HeartBreath.mp3" #Custom
define audio.Heartbeat2 = "<loop 0> HeartBreath (Moni Song).mp3" #Custom


define audio.m1 = "<loop 0>bgm/m1.ogg" #Monika and her spaceroom music
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #Monika music post-deletion

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.shots = "sfx/warfare_gunshot_exterior_002.mp3" #BOW BOW BOW

# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"

image bg field = "field.png"
image bg confrence = "Confrence.png"
image bg HEC = "Home EC.png"
image bg Interrogate = "Interogate.png"
image bg LCH = "Lower Class Home.png"
image bg MCR = "Middle Class Room.png"
image bg MCB = "Middle Class Bath.png"
image bg MCH = "middle class hall.png"
image bg AR = "artroom.png"
image bg SC2 = "sunsetclass.png"
image bg MR = "moniroom.png"
image bg DC = "detectiveclub.png"
image bg SC = "sunsetcorridor.png"
image bg AIR = "aokiinterrigationroom.png"
image bg MCL = "Middle Class Loft.png"
image bg SKD = "sayokitchendecoy.png"
image bg MCL = "Middle Class Loft.png"
image bg SS = "schoolstair.png"
image bg KPR = "KotoPartyRoom.png"






image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

#custom


image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

#------------------------------------------------From hereon, the girl's bodies are defined along with their heads.
#-----------------------------------------here's reference for the left half------the right half--------the head
# Sayori
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1b2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b2.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")


image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki/4t.png")


image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1f2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f2.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

#NEW 
image yuri 5ca = im.Composite((960, 960), (0, 0), "custom yuri/fa.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cb = im.Composite((960, 960), (0, 0), "custom yuri/fb.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cc = im.Composite((960, 960), (0, 0), "custom yuri/fc.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cd = im.Composite((960, 960), (0, 0), "custom yuri/fd.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5ce = im.Composite((960, 960), (0, 0), "custom yuri/fe.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cf = im.Composite((960, 960), (0, 0), "custom yuri/ff.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cg = im.Composite((960, 960), (0, 0), "custom yuri/fg.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5ch = im.Composite((960, 960), (0, 0), "custom yuri/fh.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5ci = im.Composite((960, 960), (0, 0), "custom yuri/fi.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cj = im.Composite((960, 960), (0, 0), "custom yuri/fj.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5ck = im.Composite((960, 960), (0, 0), "custom yuri/fk.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cl = im.Composite((960, 960), (0, 0), "custom yuri/fl.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cm = im.Composite((960, 960), (0, 0), "custom yuri/fm.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cn = im.Composite((960, 960), (0, 0), "custom yuri/fn.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5co = im.Composite((960, 960), (0, 0), "custom yuri/fo.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cp = im.Composite((960, 960), (0, 0), "custom yuri/fp.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cq = im.Composite((960, 960), (0, 0), "custom yuri/fq.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cr = im.Composite((960, 960), (0, 0), "custom yuri/fr.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cs = im.Composite((960, 960), (0, 0), "custom yuri/fs.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5ct = im.Composite((960, 960), (0, 0), "custom yuri/ft.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cu = im.Composite((960, 960), (0, 0), "custom yuri/fu.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cv = im.Composite((960, 960), (0, 0), "custom yuri/fv.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cw = im.Composite((960, 960), (0, 0), "custom yuri/fw.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cx = im.Composite((960, 960), (0, 0), "custom yuri/fx.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cy = im.Composite((960, 960), (0, 0), "custom yuri/fy.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")
image yuri 5cz = im.Composite((960, 960), (0, 0), "custom yuri/fz.png", (0, 0), "custom yuri/1l.png", (0, 0), "custom yuri/1r.png")

image yuri 6ca = im.Composite((960, 960), (0, 0), "custom yuri/fa.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cb = im.Composite((960, 960), (0, 0), "custom yuri/fb.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cc = im.Composite((960, 960), (0, 0), "custom yuri/fc.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cd = im.Composite((960, 960), (0, 0), "custom yuri/fd.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6ce = im.Composite((960, 960), (0, 0), "custom yuri/fe.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cf = im.Composite((960, 960), (0, 0), "custom yuri/ff.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cg = im.Composite((960, 960), (0, 0), "custom yuri/fg.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6ch = im.Composite((960, 960), (0, 0), "custom yuri/fh.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6ci = im.Composite((960, 960), (0, 0), "custom yuri/fi.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cj = im.Composite((960, 960), (0, 0), "custom yuri/fj.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6ck = im.Composite((960, 960), (0, 0), "custom yuri/fk.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cl = im.Composite((960, 960), (0, 0), "custom yuri/fl.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cm = im.Composite((960, 960), (0, 0), "custom yuri/fm.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cn = im.Composite((960, 960), (0, 0), "custom yuri/fn.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6co = im.Composite((960, 960), (0, 0), "custom yuri/fo.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cp = im.Composite((960, 960), (0, 0), "custom yuri/fp.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cq = im.Composite((960, 960), (0, 0), "custom yuri/fq.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cr = im.Composite((960, 960), (0, 0), "custom yuri/fr.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cs = im.Composite((960, 960), (0, 0), "custom yuri/fs.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6ct = im.Composite((960, 960), (0, 0), "custom yuri/ft.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cu = im.Composite((960, 960), (0, 0), "custom yuri/fu.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cv = im.Composite((960, 960), (0, 0), "custom yuri/fv.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cw = im.Composite((960, 960), (0, 0), "custom yuri/fw.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cx = im.Composite((960, 960), (0, 0), "custom yuri/fx.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cy = im.Composite((960, 960), (0, 0), "custom yuri/fy.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
image yuri 6cz = im.Composite((960, 960), (0, 0), "custom yuri/fz.png", (0, 0), "custom yuri/2l.png", (0, 0), "custom yuri/2r.png")
 
image yuri 7ca = im.Composite((960, 960), (0, 0), "custom yuri/f2a.png", (0, 0), "custom yuri/3.png")
image yuri 7cb = im.Composite((960, 960), (0, 0), "custom yuri/f2b.png", (0, 0), "custom yuri/3.png")
image yuri 7cc = im.Composite((960, 960), (0, 0), "custom yuri/f2c.png", (0, 0), "custom yuri/3.png")
image yuri 7cd = im.Composite((960, 960), (0, 0), "custom yuri/f2d.png", (0, 0), "custom yuri/3.png")
image yuri 7ce = im.Composite((960, 960), (0, 0), "custom yuri/f2e.png", (0, 0), "custom yuri/3.png")


image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

#------------------------------------------------Our beloved Monika only has her school uniform here, but that can change!

# Just Monika
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")
image monika 5c = im.Composite((960, 960), (0, 0), "monika/3c.png")


image monika 6a = "monicrazed.png"


image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

image aoki 1a = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/a.png")
image aoki 1b = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/b.png")
image aoki 1c = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/c.png")
image aoki 1crazy = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/crazy.png")
image aoki 1d = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/d.png")
image aoki 1e = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/e.png")
image aoki 1f = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/f.png")
image aoki 1g = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/g.png")
image aoki 1h = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/h.png")
image aoki 1i = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/i.png")
image aoki 1j = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/j.png")
image aoki 1k = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/k.png")
image aoki 1l = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/l.png")
image aoki 1m = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/m.png")
image aoki 1n = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/n.png")
image aoki 1o = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/o.png")
image aoki 1p = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/p.png")
image aoki 1q = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/q.png")
image aoki 1r = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/r.png")
image aoki 1s = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/s.png")
image aoki 1t = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/t.png")
image aoki 1u = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/u.png")
image aoki 1v = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/v.png")
image aoki 1w = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/w.png")

image aoki 2a = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/a.png")
image aoki 2b = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/b.png")
image aoki 2c = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/c.png")
image aoki 2crazy = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/crazy.png")
image aoki 2d = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/d.png")
image aoki 2e = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/e.png")
image aoki 2f = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/f.png")
image aoki 2g = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/g.png")
image aoki 2h = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/h.png")
image aoki 2i = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/i.png")
image aoki 2j = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/j.png")
image aoki 2k = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/k.png")
image aoki 2l = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/l.png")
image aoki 2m = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/m.png")
image aoki 2n = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/n.png")
image aoki 2o = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/o.png")
image aoki 2p = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/p.png")
image aoki 2q = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/q.png")
image aoki 2r = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/r.png")
image aoki 2s = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/s.png")
image aoki 2t = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/t.png")
image aoki 2u = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/u.png")
image aoki 2v = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/v.png")
image aoki 2w = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/1r.png", (0, 0), "aoki/w.png")

image aoki 3a = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/a.png")
image aoki 3b = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/b.png")
image aoki 3c = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/c.png")
image aoki 3crazy = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/crazy.png")
image aoki 3d = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/d.png")
image aoki 3e = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/e.png")
image aoki 3f = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/f.png")
image aoki 3g = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/g.png")
image aoki 3h = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/h.png")
image aoki 3i = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/i.png")
image aoki 3j = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/j.png")
image aoki 3k = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/k.png")
image aoki 3l = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/l.png")
image aoki 3m = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/m.png")
image aoki 3n = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/n.png")
image aoki 3o = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/o.png")
image aoki 3p = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/p.png")
image aoki 3q = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/q.png")
image aoki 3r = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/r.png")
image aoki 3s = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/s.png")
image aoki 3t = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/t.png")
image aoki 3u = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/u.png")
image aoki 3v = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/v.png")
image aoki 3w = im.Composite((960, 960), (0, 0), "aoki/2l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/w.png")

image aoki 4a = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/a.png")
image aoki 4b = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/b.png")
image aoki 4c = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/c.png")
image aoki 4crazy = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/crazy.png")
image aoki 4d = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/d.png")
image aoki 4e = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/e.png")
image aoki 4f = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/f.png")
image aoki 4g = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/g.png")
image aoki 4h = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/h.png")
image aoki 4i = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/i.png")
image aoki 4j = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/j.png")
image aoki 4k = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/k.png")
image aoki 4l = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/l.png")
image aoki 4m = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/m.png")
image aoki 4n = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/n.png")
image aoki 4o = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/o.png")
image aoki 4p = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/p.png")
image aoki 4q = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/q.png")
image aoki 4r = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/r.png")
image aoki 4s = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/s.png")
image aoki 4t = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/t.png")
image aoki 4u = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/u.png")
image aoki 4v = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/v.png")
image aoki 4w = im.Composite((960, 960), (0, 0), "aoki/1l.png", (0, 0), "aoki/2r.png", (0, 0), "aoki/w.png")

image aoki 5a = "aokiblackout.png"

image ka 1a = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/a.png")
image ka 1a1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/a1.png")
image ka 1b = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/b.png")
image ka 1b1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/b1.png")
image ka 1c = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/c.png")
image ka 1c1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/c1.png")
image ka 1d = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/d.png")
image ka 1d1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/d1.png")
image ka 1e = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/e.png")
image ka 1e1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/e1.png")
image ka 1f = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/f.png")
image ka 1f1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/f1.png")
image ka 1g = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/g.png")
image ka 1g1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/g1.png")
image ka 1h = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/h.png")
image ka 1h1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/h1.png")
image ka 1i = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/i.png")
image ka 1i1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/i1.png")
image ka 1j = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/j.png")
image ka 1j1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/j1.png")
image ka 1k = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/k.png")
image ka 1k1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/k1.png")
image ka 1l = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/l.png")
image ka 1l1 = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/l1.png")
image ka 1m = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/m.png")
image ka 1n = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/n.png")
image ka 1o = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/o.png")
image ka 1p = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/p.png")
image ka 1q = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/q.png")
image ka 1r = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/r.png")
image ka 1s = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/s.png")
image ka 1t = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/t.png")
image ka 1u = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/u.png")
image ka 1v = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/v.png")
image ka 1w = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/w.png")
image ka 1x = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/x.png")
image ka 1y = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/y.png")
image ka 1z = im.Composite((960, 960), (0, 0), "mc/1.png", (0, 0), "mc/z.png")

image ka 2a = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/a.png")
image ka 2a1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/a1.png")
image ka 2b = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/b.png")
image ka 2b1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/b1.png")
image ka 2c = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/c.png")
image ka 2c1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/c1.png")
image ka 2d = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/d.png")
image ka 2d1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/d1.png")
image ka 2e = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/e.png")
image ka 2e1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/e1.png")
image ka 2f = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/f.png")
image ka 2f1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/f1.png")
image ka 2g = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/g.png")
image ka 2g1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/g1.png")
image ka 2h = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/h.png")
image ka 2h1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/h1.png")
image ka 2i = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/i.png")
image ka 2i1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/i1.png")
image ka 2j = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/j.png")
image ka 2j1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/j1.png")
image ka 2k = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/k.png")
image ka 2k1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/k1.png")
image ka 2l = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/l.png")
image ka 2l1 = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/l1.png")
image ka 2m = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/m.png")
image ka 2n = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/n.png")
image ka 2o = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/o.png")
image ka 2p = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/p.png")
image ka 2q = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/q.png")
image ka 2r = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/r.png")
image ka 2s = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/s.png")
image ka 2t = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/t.png")
image ka 2u = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/u.png")
image ka 2v = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/v.png")
image ka 2w = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/w.png")
image ka 2x = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/x.png")
image ka 2y = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/y.png")
image ka 2z = im.Composite((960, 960), (0, 0), "mc/2.png", (0, 0), "mc/z.png")

image ka 1ba = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/a.png")
image ka 1ba1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/a1.png")
image ka 1bb = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/b.png")
image ka 1bb1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/b1.png")
image ka 1bc = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/c.png")
image ka 1bc1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/c1.png")
image ka 1bd = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/d.png")
image ka 1bd1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/d1.png")
image ka 1be = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/e.png")
image ka 1be1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/e1.png")
image ka 1bf = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/f.png")
image ka 1bf1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/f1.png")
image ka 1bg = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/g.png")
image ka 1bg1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/g1.png")
image ka 1bh = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/h.png")
image ka 1bh1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/h1.png")
image ka 1bi = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/i.png")
image ka 1bi1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/i1.png")
image ka 1bj = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/j.png")
image ka 1bj1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/j1.png")
image ka 1bk = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/k.png")
image ka 1bk1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/k1.png")
image ka 1bl = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/l.png")
image ka 1bl1 = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/l1.png")
image ka 1bm = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/m.png")
image ka 1bn = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/n.png")
image ka 1bo = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/o.png")
image ka 1bp = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/p.png")
image ka 1bq = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/q.png")
image ka 1br = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/r.png")
image ka 1bs = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/s.png")
image ka 1bt = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/t.png")
image ka 1bu = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/u.png")
image ka 1bv = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/v.png")
image ka 1bw = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/w.png")
image ka 1bx = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/x.png")
image ka 1by = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/y.png")
image ka 1bz = im.Composite((960, 960), (0, 0), "mc/1b.png", (0, 0), "mc/z.png")

image ka 2ba = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/a.png")
image ka 2ba1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/a1.png")
image ka 2bb = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/b.png")
image ka 2bb1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/b1.png")
image ka 2bc = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/c.png")
image ka 2bc1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/c1.png")
image ka 2bd = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/d.png")
image ka 2bd1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/d1.png")
image ka 2be = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/e.png")
image ka 2be1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/e1.png")
image ka 2bf = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/f.png")
image ka 2bf1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/f1.png")
image ka 2bg = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/g.png")
image ka 2bg1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/g1.png")
image ka 2bh = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/h.png")
image ka 2bh1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/h1.png")
image ka 2bi = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/i.png")
image ka 2bi1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/i1.png")
image ka 2bj = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/j.png")
image ka 2bj1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/j1.png")
image ka 2bk = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/k.png")
image ka 2bk1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/k1.png")
image ka 2bl = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/l.png")
image ka 2bl1 = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/l1.png")
image ka 2bm = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/m.png")
image ka 2bn = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/n.png")
image ka 2bo = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/o.png")
image ka 2bp = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/p.png")
image ka 2bq = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/q.png")
image ka 2br = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/r.png")
image ka 2bs = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/s.png")
image ka 2bt = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/t.png")
image ka 2bu = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/u.png")
image ka 2bv = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/v.png")
image ka 2bw = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/w.png")
image ka 2bx = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/x.png")
image ka 2by = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/y.png")
image ka 2bz = im.Composite((960, 960), (0, 0), "mc/2b.png", (0, 0), "mc/z.png")

image cm 1a = "cupcakemess.png"

image mio 1a = im.Composite((960, 960), (0, 0), "mio/a.png", (0, 0), "mio/1.png")
image mio 1ay = im.Composite((960, 960), (0, 0), "mio/ay.png", (0, 0), "mio/1.png")
image mio 1b = im.Composite((960, 960), (0, 0), "mio/b.png", (0, 0), "mio/1.png")
image mio 1c = im.Composite((960, 960), (0, 0), "mio/c.png", (0, 0), "mio/1.png")
image mio 1d = im.Composite((960, 960), (0, 0), "mio/d.png", (0, 0), "mio/1.png")
image mio 1e = im.Composite((960, 960), (0, 0), "mio/e.png", (0, 0), "mio/1.png")
image mio 1f = im.Composite((960, 960), (0, 0), "mio/f.png", (0, 0), "mio/1.png")
image mio 1g = im.Composite((960, 960), (0, 0), "mio/g.png", (0, 0), "mio/1.png")
image mio 1h = im.Composite((960, 960), (0, 0), "mio/h.png", (0, 0), "mio/1.png")
image mio 1i = im.Composite((960, 960), (0, 0), "mio/i.png", (0, 0), "mio/1.png")
image mio 1j = im.Composite((960, 960), (0, 0), "mio/j.png", (0, 0), "mio/1.png")
image mio 1k = im.Composite((960, 960), (0, 0), "mio/k.png", (0, 0), "mio/1.png")
image mio 1l = im.Composite((960, 960), (0, 0), "mio/l.png", (0, 0), "mio/1.png")
image mio 1m = im.Composite((960, 960), (0, 0), "mio/m.png", (0, 0), "mio/1.png")
image mio 1n = im.Composite((960, 960), (0, 0), "mio/n.png", (0, 0), "mio/1.png")
image mio 1o = im.Composite((960, 960), (0, 0), "mio/o.png", (0, 0), "mio/1.png")
image mio 1p = im.Composite((960, 960), (0, 0), "mio/p.png", (0, 0), "mio/1.png")
image mio 1q = im.Composite((960, 960), (0, 0), "mio/q.png", (0, 0), "mio/1.png")
image mio 1r = im.Composite((960, 960), (0, 0), "mio/r.png", (0, 0), "mio/1.png")
image mio 1s = im.Composite((960, 960), (0, 0), "mio/s.png", (0, 0), "mio/1.png")
image mio 1t = im.Composite((960, 960), (0, 0), "mio/t.png", (0, 0), "mio/1.png")
image mio 1u = im.Composite((960, 960), (0, 0), "mio/u.png", (0, 0), "mio/1.png")
image mio 1v = im.Composite((960, 960), (0, 0), "mio/v.png", (0, 0), "mio/1.png")
image mio 1w = im.Composite((960, 960), (0, 0), "mio/w.png", (0, 0), "mio/1.png")
image mio 1x = im.Composite((960, 960), (0, 0), "mio/x.png", (0, 0), "mio/1.png")
image mio 1y = im.Composite((960, 960), (0, 0), "mio/y.png", (0, 0), "mio/1.png")
image mio 1z = im.Composite((960, 960), (0, 0), "mio/z.png", (0, 0), "mio/1.png")

image mio 2a = im.Composite((960, 960), (0, 0), "mio/a.png", (0, 0), "mio/2.png")
image mio 2ay = im.Composite((960, 960), (0, 0), "mio/ay.png", (0, 0), "mio/2.png")
image mio 2b = im.Composite((960, 960), (0, 0), "mio/b.png", (0, 0), "mio/2.png")
image mio 2c = im.Composite((960, 960), (0, 0), "mio/c.png", (0, 0), "mio/2.png")
image mio 2d = im.Composite((960, 960), (0, 0), "mio/d.png", (0, 0), "mio/2.png")
image mio 2e = im.Composite((960, 960), (0, 0), "mio/e.png", (0, 0), "mio/2.png")
image mio 2f = im.Composite((960, 960), (0, 0), "mio/f.png", (0, 0), "mio/2.png")
image mio 2g = im.Composite((960, 960), (0, 0), "mio/g.png", (0, 0), "mio/2.png")
image mio 2h = im.Composite((960, 960), (0, 0), "mio/h.png", (0, 0), "mio/2.png")
image mio 2i = im.Composite((960, 960), (0, 0), "mio/i.png", (0, 0), "mio/2.png")
image mio 2j = im.Composite((960, 960), (0, 0), "mio/j.png", (0, 0), "mio/2.png")
image mio 2k = im.Composite((960, 960), (0, 0), "mio/k.png", (0, 0), "mio/2.png")
image mio 2l = im.Composite((960, 960), (0, 0), "mio/l.png", (0, 0), "mio/2.png")
image mio 2m = im.Composite((960, 960), (0, 0), "mio/m.png", (0, 0), "mio/2.png")
image mio 2n = im.Composite((960, 960), (0, 0), "mio/n.png", (0, 0), "mio/2.png")
image mio 2o = im.Composite((960, 960), (0, 0), "mio/o.png", (0, 0), "mio/2.png")
image mio 2p = im.Composite((960, 960), (0, 0), "mio/p.png", (0, 0), "mio/2.png")
image mio 2q = im.Composite((960, 960), (0, 0), "mio/q.png", (0, 0), "mio/2.png")
image mio 2r = im.Composite((960, 960), (0, 0), "mio/r.png", (0, 0), "mio/2.png")
image mio 2s = im.Composite((960, 960), (0, 0), "mio/s.png", (0, 0), "mio/2.png")
image mio 2t = im.Composite((960, 960), (0, 0), "mio/t.png", (0, 0), "mio/2.png")
image mio 2u = im.Composite((960, 960), (0, 0), "mio/u.png", (0, 0), "mio/2.png")
image mio 2v = im.Composite((960, 960), (0, 0), "mio/v.png", (0, 0), "mio/2.png")
image mio 2w = im.Composite((960, 960), (0, 0), "mio/w.png", (0, 0), "mio/2.png")
image mio 2x = im.Composite((960, 960), (0, 0), "mio/x.png", (0, 0), "mio/2.png")
image mio 2y = im.Composite((960, 960), (0, 0), "mio/y.png", (0, 0), "mio/2.png")
image mio 2z = im.Composite((960, 960), (0, 0), "mio/z.png", (0, 0), "mio/2.png")

image mio 3a = im.Composite((960, 960), (0, 0), "mio/a.png", (0, 0), "mio/3.png")
image mio 3ay = im.Composite((960, 960), (0, 0), "mio/ay.png", (0, 0), "mio/3.png")
image mio 3b = im.Composite((960, 960), (0, 0), "mio/b.png", (0, 0), "mio/3.png")
image mio 3c = im.Composite((960, 960), (0, 0), "mio/c.png", (0, 0), "mio/3.png")
image mio 3d = im.Composite((960, 960), (0, 0), "mio/d.png", (0, 0), "mio/3.png")
image mio 3e = im.Composite((960, 960), (0, 0), "mio/e.png", (0, 0), "mio/3.png")
image mio 3f = im.Composite((960, 960), (0, 0), "mio/f.png", (0, 0), "mio/3.png")
image mio 3g = im.Composite((960, 960), (0, 0), "mio/g.png", (0, 0), "mio/3.png")
image mio 3h = im.Composite((960, 960), (0, 0), "mio/h.png", (0, 0), "mio/3.png")
image mio 3i = im.Composite((960, 960), (0, 0), "mio/i.png", (0, 0), "mio/3.png")
image mio 3j = im.Composite((960, 960), (0, 0), "mio/j.png", (0, 0), "mio/3.png")
image mio 3k = im.Composite((960, 960), (0, 0), "mio/k.png", (0, 0), "mio/3.png")
image mio 3l = im.Composite((960, 960), (0, 0), "mio/l.png", (0, 0), "mio/3.png")
image mio 3m = im.Composite((960, 960), (0, 0), "mio/m.png", (0, 0), "mio/3.png")
image mio 3n = im.Composite((960, 960), (0, 0), "mio/n.png", (0, 0), "mio/3.png")
image mio 3o = im.Composite((960, 960), (0, 0), "mio/o.png", (0, 0), "mio/3.png")
image mio 3p = im.Composite((960, 960), (0, 0), "mio/p.png", (0, 0), "mio/3.png")
image mio 3q = im.Composite((960, 960), (0, 0), "mio/q.png", (0, 0), "mio/3.png")
image mio 3r = im.Composite((960, 960), (0, 0), "mio/r.png", (0, 0), "mio/3.png")
image mio 3s = im.Composite((960, 960), (0, 0), "mio/s.png", (0, 0), "mio/3.png")
image mio 3t = im.Composite((960, 960), (0, 0), "mio/t.png", (0, 0), "mio/3.png")
image mio 3u = im.Composite((960, 960), (0, 0), "mio/u.png", (0, 0), "mio/3.png")
image mio 3v = im.Composite((960, 960), (0, 0), "mio/v.png", (0, 0), "mio/3.png")
image mio 3w = im.Composite((960, 960), (0, 0), "mio/w.png", (0, 0), "mio/3.png")
image mio 3x = im.Composite((960, 960), (0, 0), "mio/x.png", (0, 0), "mio/3.png")
image mio 3y = im.Composite((960, 960), (0, 0), "mio/y.png", (0, 0), "mio/3.png")
image mio 3z = im.Composite((960, 960), (0, 0), "mio/z.png", (0, 0), "mio/3.png")

image mio 4a = im.Composite((960, 960), (0, 0), "mio/a.png", (0, 0), "mio/4.png")
image mio 4ay = im.Composite((960, 960), (0, 0), "mio/ay.png", (0, 0), "mio/4.png")
image mio 4b = im.Composite((960, 960), (0, 0), "mio/b.png", (0, 0), "mio/4.png")
image mio 4c = im.Composite((960, 960), (0, 0), "mio/c.png", (0, 0), "mio/4.png")
image mio 4d = im.Composite((960, 960), (0, 0), "mio/d.png", (0, 0), "mio/4.png")
image mio 4e = im.Composite((960, 960), (0, 0), "mio/e.png", (0, 0), "mio/4.png")
image mio 4f = im.Composite((960, 960), (0, 0), "mio/f.png", (0, 0), "mio/4.png")
image mio 4g = im.Composite((960, 960), (0, 0), "mio/g.png", (0, 0), "mio/4.png")
image mio 4h = im.Composite((960, 960), (0, 0), "mio/h.png", (0, 0), "mio/4.png")
image mio 4i = im.Composite((960, 960), (0, 0), "mio/i.png", (0, 0), "mio/4.png")
image mio 4j = im.Composite((960, 960), (0, 0), "mio/j.png", (0, 0), "mio/4.png")
image mio 4k = im.Composite((960, 960), (0, 0), "mio/k.png", (0, 0), "mio/4.png")
image mio 4l = im.Composite((960, 960), (0, 0), "mio/l.png", (0, 0), "mio/4.png")
image mio 4m = im.Composite((960, 960), (0, 0), "mio/m.png", (0, 0), "mio/4.png")
image mio 4n = im.Composite((960, 960), (0, 0), "mio/n.png", (0, 0), "mio/4.png")
image mio 4o = im.Composite((960, 960), (0, 0), "mio/o.png", (0, 0), "mio/4.png")
image mio 4p = im.Composite((960, 960), (0, 0), "mio/p.png", (0, 0), "mio/4.png")
image mio 4q = im.Composite((960, 960), (0, 0), "mio/q.png", (0, 0), "mio/4.png")
image mio 4r = im.Composite((960, 960), (0, 0), "mio/r.png", (0, 0), "mio/4.png")
image mio 4s = im.Composite((960, 960), (0, 0), "mio/s.png", (0, 0), "mio/4.png")
image mio 4t = im.Composite((960, 960), (0, 0), "mio/t.png", (0, 0), "mio/4.png")
image mio 4u = im.Composite((960, 960), (0, 0), "mio/u.png", (0, 0), "mio/4.png")
image mio 4v = im.Composite((960, 960), (0, 0), "mio/v.png", (0, 0), "mio/4.png")
image mio 4w = im.Composite((960, 960), (0, 0), "mio/w.png", (0, 0), "mio/4.png")
image mio 4x = im.Composite((960, 960), (0, 0), "mio/x.png", (0, 0), "mio/4.png")
image mio 4y = im.Composite((960, 960), (0, 0), "mio/y.png", (0, 0), "mio/4.png")
image mio 4z = im.Composite((960, 960), (0, 0), "mio/z.png", (0, 0), "mio/4.png")

image mio 5a = im.Composite((960, 960), (0, 0), "mio/a.png", (0, 0), "mio/5.png")
image mio 5ay = im.Composite((960, 960), (0, 0), "mio/ay.png", (0, 0), "mio/5.png")
image mio 5b = im.Composite((960, 960), (0, 0), "mio/b.png", (0, 0), "mio/5.png")
image mio 5c = im.Composite((960, 960), (0, 0), "mio/c.png", (0, 0), "mio/5.png")
image mio 5d = im.Composite((960, 960), (0, 0), "mio/d.png", (0, 0), "mio/5.png")
image mio 5e = im.Composite((960, 960), (0, 0), "mio/e.png", (0, 0), "mio/5.png")
image mio 5f = im.Composite((960, 960), (0, 0), "mio/f.png", (0, 0), "mio/5.png")
image mio 5g = im.Composite((960, 960), (0, 0), "mio/g.png", (0, 0), "mio/5.png")
image mio 5h = im.Composite((960, 960), (0, 0), "mio/h.png", (0, 0), "mio/5.png")
image mio 5i = im.Composite((960, 960), (0, 0), "mio/i.png", (0, 0), "mio/5.png")
image mio 5j = im.Composite((960, 960), (0, 0), "mio/j.png", (0, 0), "mio/5.png")
image mio 5k = im.Composite((960, 960), (0, 0), "mio/k.png", (0, 0), "mio/5.png")
image mio 5l = im.Composite((960, 960), (0, 0), "mio/l.png", (0, 0), "mio/5.png")
image mio 5m = im.Composite((960, 960), (0, 0), "mio/m.png", (0, 0), "mio/5.png")
image mio 5n = im.Composite((960, 960), (0, 0), "mio/n.png", (0, 0), "mio/5.png")
image mio 5o = im.Composite((960, 960), (0, 0), "mio/o.png", (0, 0), "mio/5.png")
image mio 5p = im.Composite((960, 960), (0, 0), "mio/p.png", (0, 0), "mio/5.png")
image mio 5q = im.Composite((960, 960), (0, 0), "mio/q.png", (0, 0), "mio/5.png")
image mio 5r = im.Composite((960, 960), (0, 0), "mio/r.png", (0, 0), "mio/5.png")
image mio 5s = im.Composite((960, 960), (0, 0), "mio/s.png", (0, 0), "mio/5.png")
image mio 5t = im.Composite((960, 960), (0, 0), "mio/t.png", (0, 0), "mio/5.png")
image mio 5u = im.Composite((960, 960), (0, 0), "mio/u.png", (0, 0), "mio/5.png")
image mio 5v = im.Composite((960, 960), (0, 0), "mio/v.png", (0, 0), "mio/5.png")
image mio 5w = im.Composite((960, 960), (0, 0), "mio/w.png", (0, 0), "mio/5.png")
image mio 5x = im.Composite((960, 960), (0, 0), "mio/x.png", (0, 0), "mio/5.png")
image mio 5y = im.Composite((960, 960), (0, 0), "mio/y.png", (0, 0), "mio/5.png")
image mio 5z = im.Composite((960, 960), (0, 0), "mio/z.png", (0, 0), "mio/5.png")

image mio 6a = im.Composite((960, 960), (0, 0), "mio/a.png", (0, 0), "mio/6.png")
image mio 6ay  = im.Composite((960, 960), (0, 0), "mio/ay.png", (0, 0), "mio/6.png")
image mio 6b = im.Composite((960, 960), (0, 0), "mio/b.png", (0, 0), "mio/6.png")
image mio 6c = im.Composite((960, 960), (0, 0), "mio/c.png", (0, 0), "mio/6.png")
image mio 6d = im.Composite((960, 960), (0, 0), "mio/d.png", (0, 0), "mio/6.png")
image mio 6e = im.Composite((960, 960), (0, 0), "mio/e.png", (0, 0), "mio/6.png")
image mio 6f = im.Composite((960, 960), (0, 0), "mio/f.png", (0, 0), "mio/6.png")
image mio 6g = im.Composite((960, 960), (0, 0), "mio/g.png", (0, 0), "mio/6.png")
image mio 6h = im.Composite((960, 960), (0, 0), "mio/h.png", (0, 0), "mio/6.png")
image mio 6i = im.Composite((960, 960), (0, 0), "mio/i.png", (0, 0), "mio/6.png")
image mio 6j = im.Composite((960, 960), (0, 0), "mio/j.png", (0, 0), "mio/6.png")
image mio 6k = im.Composite((960, 960), (0, 0), "mio/k.png", (0, 0), "mio/6.png")
image mio 6l = im.Composite((960, 960), (0, 0), "mio/l.png", (0, 0), "mio/6.png")
image mio 6m = im.Composite((960, 960), (0, 0), "mio/m.png", (0, 0), "mio/6.png")
image mio 6n = im.Composite((960, 960), (0, 0), "mio/n.png", (0, 0), "mio/6.png")
image mio 6o = im.Composite((960, 960), (0, 0), "mio/o.png", (0, 0), "mio/6.png")
image mio 6p = im.Composite((960, 960), (0, 0), "mio/p.png", (0, 0), "mio/6.png")
image mio 6q = im.Composite((960, 960), (0, 0), "mio/q.png", (0, 0), "mio/6.png")
image mio 6r = im.Composite((960, 960), (0, 0), "mio/r.png", (0, 0), "mio/6.png")
image mio 6s = im.Composite((960, 960), (0, 0), "mio/s.png", (0, 0), "mio/6.png")
image mio 6t = im.Composite((960, 960), (0, 0), "mio/t.png", (0, 0), "mio/6.png")
image mio 6u = im.Composite((960, 960), (0, 0), "mio/u.png", (0, 0), "mio/6.png")
image mio 6v = im.Composite((960, 960), (0, 0), "mio/v.png", (0, 0), "mio/6.png")
image mio 6w = im.Composite((960, 960), (0, 0), "mio/w.png", (0, 0), "mio/6.png")
image mio 6x = im.Composite((960, 960), (0, 0), "mio/x.png", (0, 0), "mio/6.png")
image mio 6y = im.Composite((960, 960), (0, 0), "mio/y.png", (0, 0), "mio/6.png")
image mio 6z = im.Composite((960, 960), (0, 0), "mio/z.png", (0, 0), "mio/6.png")

image mio 7a = im.Composite((960, 960), (0, 0), "mio/a.png", (0, 0), "mio/7.png")
image mio 7ay = im.Composite((960, 960), (0, 0), "mio/ay.png", (0, 0), "mio/7.png")
image mio 7b = im.Composite((960, 960), (0, 0), "mio/b.png", (0, 0), "mio/7.png")
image mio 7c = im.Composite((960, 960), (0, 0), "mio/c.png", (0, 0), "mio/7.png")
image mio 7d = im.Composite((960, 960), (0, 0), "mio/d.png", (0, 0), "mio/7.png")
image mio 7e = im.Composite((960, 960), (0, 0), "mio/e.png", (0, 0), "mio/7.png")
image mio 7f = im.Composite((960, 960), (0, 0), "mio/f.png", (0, 0), "mio/7.png")
image mio 7g = im.Composite((960, 960), (0, 0), "mio/g.png", (0, 0), "mio/7.png")
image mio 7h = im.Composite((960, 960), (0, 0), "mio/h.png", (0, 0), "mio/7.png")
image mio 7i = im.Composite((960, 960), (0, 0), "mio/i.png", (0, 0), "mio/7.png")
image mio 7j = im.Composite((960, 960), (0, 0), "mio/j.png", (0, 0), "mio/7.png")
image mio 7k = im.Composite((960, 960), (0, 0), "mio/k.png", (0, 0), "mio/7.png")
image mio 7l = im.Composite((960, 960), (0, 0), "mio/l.png", (0, 0), "mio/7.png")
image mio 7m = im.Composite((960, 960), (0, 0), "mio/m.png", (0, 0), "mio/7.png")
image mio 7n = im.Composite((960, 960), (0, 0), "mio/n.png", (0, 0), "mio/7.png")
image mio 7o = im.Composite((960, 960), (0, 0), "mio/o.png", (0, 0), "mio/7.png")
image mio 7p = im.Composite((960, 960), (0, 0), "mio/p.png", (0, 0), "mio/7.png")
image mio 7q = im.Composite((960, 960), (0, 0), "mio/q.png", (0, 0), "mio/7.png")
image mio 7r = im.Composite((960, 960), (0, 0), "mio/r.png", (0, 0), "mio/7.png")
image mio 7s = im.Composite((960, 960), (0, 0), "mio/s.png", (0, 0), "mio/7.png")
image mio 7t = im.Composite((960, 960), (0, 0), "mio/t.png", (0, 0), "mio/7.png")
image mio 7u = im.Composite((960, 960), (0, 0), "mio/u.png", (0, 0), "mio/7.png")
image mio 7v = im.Composite((960, 960), (0, 0), "mio/v.png", (0, 0), "mio/7.png")
image mio 7w = im.Composite((960, 960), (0, 0), "mio/w.png", (0, 0), "mio/7.png")
image mio 7x = im.Composite((960, 960), (0, 0), "mio/x.png", (0, 0), "mio/7.png")
image mio 7y = im.Composite((960, 960), (0, 0), "mio/y.png", (0, 0), "mio/7.png")
image mio 7z = im.Composite((960, 960), (0, 0), "mio/z.png", (0, 0), "mio/7.png")

image mio 8a = im.Composite((960, 960), (0, 0), "mio/a.png", (0, 0), "mio/8.png")
image mio 8ay = im.Composite((960, 960), (0, 0), "mio/ay.png", (0, 0), "mio/8.png")
image mio 8b = im.Composite((960, 960), (0, 0), "mio/b.png", (0, 0), "mio/8.png")
image mio 8c = im.Composite((960, 960), (0, 0), "mio/c.png", (0, 0), "mio/8.png")
image mio 8d = im.Composite((960, 960), (0, 0), "mio/d.png", (0, 0), "mio/8.png")
image mio 8e = im.Composite((960, 960), (0, 0), "mio/e.png", (0, 0), "mio/8.png")
image mio 8f = im.Composite((960, 960), (0, 0), "mio/f.png", (0, 0), "mio/8.png")
image mio 8g = im.Composite((960, 960), (0, 0), "mio/g.png", (0, 0), "mio/8.png")
image mio 8h = im.Composite((960, 960), (0, 0), "mio/h.png", (0, 0), "mio/8.png")
image mio 8i = im.Composite((960, 960), (0, 0), "mio/i.png", (0, 0), "mio/8.png")
image mio 8j = im.Composite((960, 960), (0, 0), "mio/j.png", (0, 0), "mio/8.png")
image mio 8k = im.Composite((960, 960), (0, 0), "mio/k.png", (0, 0), "mio/8.png")
image mio 8l = im.Composite((960, 960), (0, 0), "mio/l.png", (0, 0), "mio/8.png")
image mio 8m = im.Composite((960, 960), (0, 0), "mio/m.png", (0, 0), "mio/8.png")
image mio 8n = im.Composite((960, 960), (0, 0), "mio/n.png", (0, 0), "mio/8.png")
image mio 8o = im.Composite((960, 960), (0, 0), "mio/o.png", (0, 0), "mio/8.png")
image mio 8p = im.Composite((960, 960), (0, 0), "mio/p.png", (0, 0), "mio/8.png")
image mio 8q = im.Composite((960, 960), (0, 0), "mio/q.png", (0, 0), "mio/8.png")
image mio 8r = im.Composite((960, 960), (0, 0), "mio/r.png", (0, 0), "mio/8.png")
image mio 8s = im.Composite((960, 960), (0, 0), "mio/s.png", (0, 0), "mio/8.png")
image mio 8t = im.Composite((960, 960), (0, 0), "mio/t.png", (0, 0), "mio/8.png")
image mio 8u = im.Composite((960, 960), (0, 0), "mio/u.png", (0, 0), "mio/8.png")
image mio 8v = im.Composite((960, 960), (0, 0), "mio/v.png", (0, 0), "mio/8.png")
image mio 8w = im.Composite((960, 960), (0, 0), "mio/w.png", (0, 0), "mio/8.png")
image mio 8x = im.Composite((960, 960), (0, 0), "mio/x.png", (0, 0), "mio/8.png")
image mio 8y = im.Composite((960, 960), (0, 0), "mio/y.png", (0, 0), "mio/8.png")
image mio 8z = im.Composite((960, 960), (0, 0), "mio/z.png", (0, 0), "mio/8.png")

image mc 1a = im.Composite((960, 960), (0, 0), "player/a.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1b = im.Composite((960, 960), (0, 0), "player/b.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1c = im.Composite((960, 960), (0, 0), "player/c.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1d = im.Composite((960, 960), (0, 0), "player/d.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1e = im.Composite((960, 960), (0, 0), "player/e.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1e2 = im.Composite((960, 960), (0, 0), "player/error.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1e3 = im.Composite((960, 960), (0, 0), "player/error1.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1f = im.Composite((960, 960), (0, 0), "player/f.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1g = im.Composite((960, 960), (0, 0), "player/g.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1h = im.Composite((960, 960), (0, 0), "player/h.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1i = im.Composite((960, 960), (0, 0), "player/i.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1j = im.Composite((960, 960), (0, 0), "player/j.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1k = im.Composite((960, 960), (0, 0), "player/k.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1l = im.Composite((960, 960), (0, 0), "player/l.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1m = im.Composite((960, 960), (0, 0), "player/m.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1n = im.Composite((960, 960), (0, 0), "player/n.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1o = im.Composite((960, 960), (0, 0), "player/o.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1p = im.Composite((960, 960), (0, 0), "player/p.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1q = im.Composite((960, 960), (0, 0), "player/q.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1r = im.Composite((960, 960), (0, 0), "player/r.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1s = im.Composite((960, 960), (0, 0), "player/s.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1s2 = im.Composite((960, 960), (0, 0), "player/shock.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1t = im.Composite((960, 960), (0, 0), "player/t.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1u = im.Composite((960, 960), (0, 0), "player/u.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1v = im.Composite((960, 960), (0, 0), "player/v.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1w = im.Composite((960, 960), (0, 0), "player/w.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1x = im.Composite((960, 960), (0, 0), "player/x.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1y = im.Composite((960, 960), (0, 0), "player/y.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 1z = im.Composite((960, 960), (0, 0), "player/z.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")

image mc 2a = im.Composite((960, 960), (0, 0), "player/a.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2b = im.Composite((960, 960), (0, 0), "player/b.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2c = im.Composite((960, 960), (0, 0), "player/c.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2d = im.Composite((960, 960), (0, 0), "player/d.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2e = im.Composite((960, 960), (0, 0), "player/e.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2e2 = im.Composite((960, 960), (0, 0), "player/error.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2e3 = im.Composite((960, 960), (0, 0), "player/error1.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2f = im.Composite((960, 960), (0, 0), "player/f.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2g = im.Composite((960, 960), (0, 0), "player/g.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2h = im.Composite((960, 960), (0, 0), "player/h.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2i = im.Composite((960, 960), (0, 0), "player/i.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2j = im.Composite((960, 960), (0, 0), "player/j.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2k = im.Composite((960, 960), (0, 0), "player/k.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2l = im.Composite((960, 960), (0, 0), "player/l.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2m = im.Composite((960, 960), (0, 0), "player/m.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2n = im.Composite((960, 960), (0, 0), "player/n.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2o = im.Composite((960, 960), (0, 0), "player/o.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2p = im.Composite((960, 960), (0, 0), "player/p.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2q = im.Composite((960, 960), (0, 0), "player/q.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2r = im.Composite((960, 960), (0, 0), "player/r.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2s = im.Composite((960, 960), (0, 0), "player/s.png", (0, 0), "player/1l.png", (0, 0), "player/1r.png")
image mc 2s2 = im.Composite((960, 960), (0, 0), "player/shock.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2t = im.Composite((960, 960), (0, 0), "player/t.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2u = im.Composite((960, 960), (0, 0), "player/u.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2v = im.Composite((960, 960), (0, 0), "player/v.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2w = im.Composite((960, 960), (0, 0), "player/w.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2x = im.Composite((960, 960), (0, 0), "player/x.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2y = im.Composite((960, 960), (0, 0), "player/y.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")
image mc 2z = im.Composite((960, 960), (0, 0), "player/z.png", (0, 0), "player/2l.png", (0, 0), "player/2r.png")

image mc 3a = im.Composite((960, 960), (0, 0), "player/a.png", (0, 0), "player/3.png")
image mc 3b = im.Composite((960, 960), (0, 0), "player/b.png", (0, 0), "player/3.png")
image mc 3c = im.Composite((960, 960), (0, 0), "player/c.png", (0, 0), "player/3.png")
image mc 3d = im.Composite((960, 960), (0, 0), "player/d.png", (0, 0), "player/3.png")
image mc 3e = im.Composite((960, 960), (0, 0), "player/e.png", (0, 0), "player/3.png")
image mc 3e2 = im.Composite((960, 960), (0, 0), "player/error.png", (0, 0), "player/3.png")
image mc 3e3 = im.Composite((960, 960), (0, 0), "player/error1.png", (0, 0), "player/3.png")
image mc 3f = im.Composite((960, 960), (0, 0), "player/f.png", (0, 0), "player/3.png")
image mc 3g = im.Composite((960, 960), (0, 0), "player/g.png", (0, 0), "player/3.png")
image mc 3h = im.Composite((960, 960), (0, 0), "player/h.png", (0, 0), "player/3.png")
image mc 3i = im.Composite((960, 960), (0, 0), "player/i.png", (0, 0), "player/3.png")
image mc 3j = im.Composite((960, 960), (0, 0), "player/j.png", (0, 0), "player/3.png")
image mc 3k = im.Composite((960, 960), (0, 0), "player/k.png", (0, 0), "player/3.png")
image mc 3l = im.Composite((960, 960), (0, 0), "player/l.png", (0, 0), "player/3.png")
image mc 3m = im.Composite((960, 960), (0, 0), "player/m.png", (0, 0), "player/3.png")
image mc 3n = im.Composite((960, 960), (0, 0), "player/n.png", (0, 0), "player/3.png")
image mc 3o = im.Composite((960, 960), (0, 0), "player/o.png", (0, 0), "player/3.png")
image mc 3p = im.Composite((960, 960), (0, 0), "player/p.png", (0, 0), "player/3.png")
image mc 3q = im.Composite((960, 960), (0, 0), "player/q.png", (0, 0), "player/3.png")
image mc 3r = im.Composite((960, 960), (0, 0), "player/r.png", (0, 0), "player/3.png")
image mc 3s = im.Composite((960, 960), (0, 0), "player/s.png", (0, 0), "player/3.png")
image mc 3s2 = im.Composite((960, 960), (0, 0), "player/shock.png", (0, 0), "player/3.png")
image mc 3t = im.Composite((960, 960), (0, 0), "player/t.png", (0, 0), "player/3.png")
image mc 3u = im.Composite((960, 960), (0, 0), "player/u.png", (0, 0), "player/3.png")
image mc 3v = im.Composite((960, 960), (0, 0), "player/v.png", (0, 0), "player/3.png")
image mc 3w = im.Composite((960, 960), (0, 0), "player/w.png", (0, 0), "player/3.png")
image mc 3x = im.Composite((960, 960), (0, 0), "player/x.png", (0, 0), "player/3.png")
image mc 3y = im.Composite((960, 960), (0, 0), "player/y.png", (0, 0), "player/3.png")
image mc 3z = im.Composite((960, 960), (0, 0), "player/z.png", (0, 0), "player/3.png")


image koto 1p3 = im.Composite((960, 960), (0, 0), "kotonoha/1.png", (0, 0), "kotonoha/p3.png")
image koto 1bp3 = im.Composite((960, 960), (0, 0), "kotonoha/1b.png", (0, 0), "kotonoha/p3.png")
image koto 1bu4 = im.Composite((960, 960), (0, 0), "kotonoha/1b.png", (0, 0), "kotonoha/u4.png")
image koto 1bs3 = im.Composite((960, 960), (0, 0), "kotonoha/1b.png", (0, 0), "kotonoha/s3.png")
image koto 1bs3r = im.Composite((960, 960), (0, 0), "kotonoha/1b.png", (0, 0), "kotonoha/s3r.png")



###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
define narrator = Character(ctc="ctc", ctc_position="fixed", window_background=Image ("textbox.png", xalign=0.5, yalign=1.0))
define mco = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#686362") ])
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_sayori.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#7079eb") ])
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_monika.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#73d95c") ])
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_natsuki.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#ff9bca") ])
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_yuri.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#b34bce") ])
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define a = DynamicCharacter('a_name', image='aoki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_aoki.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#791c74") ])
define ka = DynamicCharacter('ka_name', image='mc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_kane.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#343434") ])
define mi = DynamicCharacter('mi_name', image='mio', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_mio.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#eb694f") ])
define mc = DynamicCharacter('mc_name', image='player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_realmc.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#fdd106") ])




define cd = Character('Chief :D', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define km = Character('Mom', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define kd = Character('Dad', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define r = Character('Mrs. Reynolds', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define pr = Character('Officer Reynolds', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define p = Character('???', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define k1 = Character('Kid 1', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define k2 = Character('Kid 2', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define k3 = Character('Kid 3', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define k4 = Character('Kid 4', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define t = Character('Teacher', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define qmc = Character('MC???', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_realmc.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#fdd106") ])
define qmc2 = Character('MC???', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_kane.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#343434") ])
define pa = Character('???', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_aoki.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#791c74") ])
define pl = Character('???', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_libitina.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#b79b82") ])
define kiyomi = Character('Kiyomi',what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_kiyomi.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#ffe898") ])
define qmc2r = Character('MC', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_kane.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#343434") ])
define tl = Character('Teacher', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image ("textbox_libitina.png", xalign=0.5, yalign=1.0), who_outlines=[ (3, "#b89b82") ])
define e = Character('Everyone', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define exk = Character('Everyone (ex Koto)', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define speak = Character('Speaker', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define sspeak = Character('Loudspeaker', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")













define _dismiss_pause = config.developer  

###### Persistent Variables ######
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None

###### Other global variables ######
# It's good practice to define global variables here, just so you know what you can call later

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"

default cd_name = "Chief :D"
default km_name = "Mom"
default kd_name = "Dad"
default r_name = "Mrs. Reynolds"
default pr_name = "Officer Reynolds"
default p_name = "???"

default a_name = "Aoki"
default ka_name = "Kane"
default mi_name = "Mio"
default mc_name = "MC"


# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None
