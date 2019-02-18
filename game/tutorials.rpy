## This file is used to write the tutorials
## When you make a mode using this template, you may delete this file
## and modify the lines nested in #### #### in script-example.rpy

## This part of the code is used to create the tutorial selection screen.

#Each tutorial is defined by its name (caption) and its label,
#items is the list of caption and label of each tutorial
#init python is necessary because items is a List, a python object

init python:

    items = [(_("Start Game"),"example_chapter")
        ,(_("Yuri Test"),"tutorial_route_p1")
        ,(_("Natsuki Test"),"tutorial_route_p2")
        ,(_("Monika Test"),"tutorial_route_p3")
        ,(_("Sayori Test"),"tutorial_route_p4")
        ,(_("Sprite Effects"),"tutorial_route_p5")
        ,(_(""),"tutorial_route_p6")
        ,(_("Sprite Test"),"tutorial_route_p7")
        ,(_("Sprite Positions"),"tutorial_route_p8")
        ,(_(""),"tutorial_route_p9")
        ,(_("Sound Test"),"sound_test")
        ,(_("Music Test"),"music_test")
        ,(_("Background Test"),"background_test")]



#Define the properties of the object textbutton. textbutton is made by two parts:
#button and button_text. To customize textbutton, both botton and button_text need to be modified
#This part is usually found in gui.rpy

define adj = ui.adjustment()
define gui.tutorial_button_width = 500
define gui.tutorial_button_height = None
define gui.tutorial_button_tile = False
define gui.tutorial_button_borders = Borders(25, 5, 25, 5)

define gui.tutorial_button_text_font = gui.default_font
define gui.tutorial_button_text_size = gui.text_size
define gui.tutorial_button_text_xalign = 0.0
define gui.tutorial_button_text_idle_color = "#000"
define gui.tutorial_button_text_hover_color = "#fa9"

#Define the styles used for tutorial_vbox, tutorial_button and tutorial_button_text
#The line properties gui.button_properties("tutorial_button") assigns all attributes of gui.tutorial_button to the style tutorial_button and the style tutorial_button_text

style tutorial_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing 5

style tutorial_button is default:
    properties gui.button_properties("tutorial_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style tutorial_button_text is default:
    properties gui.button_text_properties("tutorial_button")
    outlines []

#Tutorial selection screen
#This screen was based on the tutorial screen of Tutorial of Ren'Py

screen tutorial_choice(items):
        style_prefix "tutorial"

        fixed:

            area (125, 40, 600, 450)

            bar adjustment adj style "vscrollbar" xalign -0.05

            viewport:
                yadjustment adj
                mousewheel True

                vbox:

                    for i_caption,i_label in items:
                        textbutton i_caption:
                            action Return(i_label)

                    null height 20

                    textbutton _("Back to Title Screen.") action Return(False)


#If the player has already read the introduction, then the game jumps directly to the tutorial menu
#Otherwise, the game first jumps to the introduction (example_chapter_explanation)

label tutorial_selection:

    stop music fadeout 2.0

    #This set's up the scene with a background and music
    scene bg club_day
    with dissolve_scene_full
    play music t3

    #let's see if the menu works...

    show monika 3a at tcommon(950)

    $ m(_("Debug Screen."), interact=False)

    call screen tutorial_choice(items)

    if _return is False:
        jump end_tutorial

    call expression _return from _call_expression

    jump tutorial_selection

#When you end the tutorial

label end_tutorial:

    with dissolve

    return


#Tutorials

#Sound Effects (Note: Only the first four are defined in definitions.rpy.
#If you want to play any other  sound, use this format: play sound "sfx/<sfx name>.ogg"

label background_test:
    
    m "Looks like they're{nw}"
    m "Oh hi."
    
    scene bg:
        "mod_assets/residential.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "residential.png"
    
    scene bg:
        "mod_assets/corridor.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "corridor.png"
    
    scene bg:
        "mod_assets/club.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "club.png"
    
    scene bg:
        "mod_assets/club-skill.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "club-skill.png"
    
    scene bg:
        "mod_assets/closet.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "closet.png"
    
    scene bg:
        "mod_assets/class.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "class.png"
    
    scene bg:
        "mod_assets/house.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "house.png"
    
    scene bg:
        "mod_assets/house.jpg"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "house.jpg"
    
    scene bg:
        "mod_assets/sayori_bedroom.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "sayori_bedroom.png"
    
    scene bg:
        "mod_assets/bedroom.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "bedroom.png"
    
    scene bg:
        "mod_assets/bedroom_dark.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "bedroom_dark.png"
    
    scene bg:
        "mod_assets/kitchen.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "kitchen.png"
    
    scene bg:
        "mod_assets/notebook.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "notebook.png"
    
    scene bg:
        "mod_assets/warning.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "warning.png"
    
    scene bg:
        "mod_assets/warning2.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "warning2.png"
    
    scene bg:
        "mod_assets/poem.jpg"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "poem.jpg"
    
    scene bg:
        "mod_assets/poem_y1.jpg"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "poem_y1.jpg"
    
    scene bg:
        "mod_assets/poem_y2.jpg"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "poem_y2.jpg"
    
    scene bg:
        "mod_assets/splash.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "splash.png"
    
    scene bg:
        "mod_assets/splash-white.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "splash-white.png"
                       
    scene bg:
        "mod_assets/blackness.png"
    with wipeleft
    show monika 3a at t11 zorder 2
    m "blackness.png"
    
    m "Returning..."
    
    return

label music_test:
    
    stop music
    show monika 3a at t11 zorder 2
    m "Stoping music..."
    
    m "Next: Title Theme"
    play music t1
    m "Next: Ohayou Sayori!"
    play music t2
    m "Next: Ohayou Sayori! (Wobble)"
    play music t2g
    m "Next: Ohayou Sayori! (Rapid Glitch Noise)"
    play music t2g2
    m "Next: Ohayou Sayori! (Gradual Pitch Increase)"
    play music t2g3
    m "Next: Main Theme"
    play music t3
    m "Next: Main Theme (Off Key Notes)"
    play music t3g
    m "Next: Main Theme (Start From Weird Note)"
    play music t3g2
    m "Next: Main Theme (Reverb + Strange Wet Noises)"
    play music t3g3
    m "Next: Main Theme"
    play music t3m
    m "Next: Dreams of Love and Literature"
    play music t4
    m "Next: Static + Error Noise"
    play music t4g
    m "Next: Okay, Everyone! (1)"
    play music t5
    m "Next: Okay, Everyone! (2)"
    play music t5b
    m "Next: Okay, Everyone! (3)"
    play music t5c
    m "Next: Play With Me"
    play music t6
    m "Next: Play With Me (Bitcrushed Melody Piano)"
    play music t6g
    m "Next: Play With Me (Sped-up + Reversed)"
    play music t6r
    m "Next: Play With Me (Yuri Death)"
    play music t6s
    m "Next: Poem Panic!"
    play music t7
    m "Next: Poem Panic! (First Melody Loop)"
    play music t7a
    m "Next: Poem Panic! (Act Two Argument)"
    play music t7g
    m "Next: Daijbou!"
    play music t8
    m "Next: My Feelings"
    play music t9
    m "Next: My Feelings (Harpsichord + Fast)"
    play music t9g
    m "Next: My Confession"
    play music t10
    m "Next: My Confession (Yuri)"
    play music t10y
    m "Next: Sayo-nara"
    play music td
    m "Next: Just Monika"
    play music m1
    m "Next: I Still Love You"
    play music mend
    m "Next: Ghost Menu Theme"
    play music ghostmenu
    m "Next: Low Sawtooth Wave"
    play music g1
    m "Next: Lower Sawtooth Wave"
    play music g2
    m "Next: Heartbeat"
    play music hb
    m "Next: end-voice.ogg"
    play music "bgm/end-voice.ogg"
    m "Next: Your Reality"
    play music "bgm/credits.ogg"
    m "Next: s_kill_early.ogg"
    play music "bgm/s_kill_early.ogg"
    m "Returning..."
    
    return
    
label sound_test:
    
    stop music
    show monika 3a at t11 zorder 2
    m "Stoping music..."
    
    m "closet_open.ogg"
    play sound "sfx/closet_open.ogg"
    pause 1
    m "closet_close.ogg"
    play sound "sfx/closet_close.ogg"
    pause 1
    m "page_turn.ogg"
    play sound "sfx/page_turn.ogg"
    pause 1
    m "fall.ogg"
    play sound "sfx/fall.ogg"
    pause 1
    m "s_kill_glitch1.ogg"
    play sound "sfx/s_kill_glitch1.ogg"
    pause 1
    m "fall2.ogg"
    play sound "sfx/fall2.ogg"
    pause 1
    m "giggle.ogg"
    play sound "sfx/giggle.ogg"
    pause 1
    m "glitch1.ogg"
    play sound "sfx/glitch1.ogg"
    pause 1
    m "glitch2.ogg"
    play sound "sfx/glitch2.ogg"
    pause 1
    m "glitch3.ogg"
    play sound "sfx/glitch3.ogg"
    pause 1
    m "gnid.ogg"
    play sound "sfx/gnid.ogg"
    pause 1
    m "interference.ogg"
    play sound "sfx/interference.ogg"
    pause 1
    m "monikapound.ogg"
    play sound "sfx/monikapound.ogg"
    pause 1
    m "mscare.ogg"
    play sound "sfx/mscare.ogg"
    pause 1
    m "slap.ogg"
    play sound "sfx/slap.ogg"
    pause 1
    m "smack.ogg"
    play sound "sfx/smack.ogg"
    pause 1
    m "stab.ogg"
    play sound "sfx/stab.ogg"
    pause 1
    m "yurideath.ogg"
    play sound "sounds/yurideath.ogg"
    pause 8
    m "crack.ogg"
    play sound "sfx/crack.ogg"
    pause 1
    m "eyes.ogg"
    play sound "sfx/eyes.ogg"
    pause 1
    m "Returning..."
    
    return
    

label tutorial_route_p1:

    show yuri 1a at t11 zorder 2

    m "There’s no better way to become better at poetry than writing poems."
    show yuri 1b at t11 zorder 2
    m "And in the same way, there’s no better way to become better at modding than making mods."
    show yuri 1c at t11 zorder 2
    m 3a "So, let’s make a mod together! I have got the perfect idea."
    show yuri 1d at t11 zorder 2
    m 5a "Let’s make my own route!"
    show yuri 1e at t11 zorder 2
    m 5b "The one the game never gave us..."
    show yuri 1f at t11 zorder 2
    m 1a "Of course, as both and I are new at programming, we should keep it simple."
    show yuri 1g at t11 zorder 2
    m 1h "We’ll need Ren’Py but unfortunately I can’t access it from here."
    show yuri 1h at t11 zorder 2
    m 3a "So I’m counting on you to help me."
    show yuri 1i at t11 zorder 2
    m 4a "Make sure you follow exactly my instructions, okay? In coding, a single mistake can totally break a program."
    show yuri 1j at t11 zorder 2
    m "First, verify that you installed Ren’Py. Then make a copy of Doki Doki Literature Club’s directory and put it in the directory of Ren’Py."
    show yuri 1k at t11 zorder 2
    m "Rename the directory of the game 'DDLC Monika Route'."
    show yuri 1l at t11 zorder 2
    m "Put the files of DDLC Mod Template inside DDLC Monika Route’s directory."
    show yuri 1m at t11 zorder 2
    m "Try to launch Ren’Py and then try to start DDLC Monika Route."
    show yuri 1n at t11 zorder 2
    m 4f "If there’s an error then you might have made a mistake with the files..."
    show yuri 1o at t11 zorder 2
    m 4o "Unfortunately, I can’t help you...If it works then we can go the next step."
    show yuri 1p at t11 zorder 2
    m 2a "Go to DDLC Monika Route’s game directory and delete 'tutorial.rpy'. That file just contains this tutorial but we won’t need it to make my route."
    show yuri 1q at t11 zorder 2
    m 3a "Then you need to edit 'script.rpy'. You can edit it with any text editor. Open the file and find the line \n'\ \ \ \ call prologue from _call_prologue'"
    show yuri 1r at t11 zorder 2
    m "Replace it with \n'\ \ \ \ call monika_route from _call_monika_route'"
    show yuri 1s at t11 zorder 2
    m 3b "By the way, you should notice there are 4 spaces before that line."
    show yuri 1t at t11 zorder 2
    m 4a "Be very careful about the number of spaces! In Ren’Py and Python spaces are very important. I won’t go into details now, but indenting lines with spaces is very important."
    show yuri 1u at t11 zorder 2
    m "And it does have to be spaces. Tabs don't work the same way."
    show yuri 1v at t11 zorder 2
    m "Once the line is replaced, save the file. Create an empty text file. Rename it monika_route_script.rpy. Check if the extension is .rpy. Rpy file is the type of files used for Ren’Py scripts."
    show yuri 1w at t11 zorder 2
    m "Open monika_route_script.rpy and write \n'label monika_route:'."
    show yuri 1x at t11 zorder 2
    m "Then jump a line and write \n'\ \ \ \  return'\n Save the file."
    show yuri 1y at t11 zorder 2
    m 4i "Alright, we managed to finish the first part of our mod. Let me explain the meaning of what you just wrote."
    show yuri 1z at t11 zorder 2
    m 1a "In a book, each chapter are followed one after another. Chapter two is written after chapter two and so on. But in Ren’Py this is different."
    show yuri 2a at t11 zorder 2
    m "The order isn’t determined by the place of each chapter in the scripts but by the keywords 'label', 'call' and 'jump'"
    show yuri 3a at t11 zorder 2
    m "When the game begins and when you click on New Game, the game jumps to the chapter whose label is 'start'. Then the game reads and executes what is inside the block under the label 'start'."
    show yuri 4a at t11 zorder 2
    m "When it reaches the keyword 'call' or 'jump', the game proceeds to the chapter whose label followed the keyword."
    show yuri 1y1 at t11 zorder 2
    m 2b "In the case of our mod, when the game reads '\ \ \ \ call monika_route from _call_ monika_route', it jumps to the chapter labeled monika_route."
    show yuri 1y2 at t11 zorder 2
    m 3a "Please don’t mind 'from _call_monika_route', it’s quite advanced stuff and I don’t understand it well too."
    show yuri 1y3 at t11 zorder 2
    m 4b "The chapter monika_route is defined in the file we created, monika_route_script.rpy. But as you can see, there is nothing inside it except from 'return'."
    show yuri 1y4 at t11 zorder 2
    m "The keyword 'return' makes the game goes back to the latest chapter that was accessed through 'call'. If it doesn't exist, the game goes back to the main menu."
    show yuri 1y5 at t11 zorder 2
    m 4a "If you try to play the mod, you’ll see nothing when you click New Game. That’s because the game returns to the main menu as soon as it jumps to monika_route."
    show yuri 1y6 at t11 zorder 2
    m 1e "Okay! Let’s stop here for now. I hope I didn’t overwhelm you with information..."
    show yuri 1y7 at t11 zorder 2
    m 2a "If there’s still an error when you try playing the mod, there's a script named t1.rpy inside the folder named monika_route_answer. t1.rpy is what you should have written in monika_route_script.rpy."
    show yuri 1y8 at t11 zorder 2
    m "You can copy-paste the content of t1.rpy to monika_route_script.rpy but don’t forget to delete the # character in front of each line."
    show yuri 1y9 at t11 zorder 2
    m "In Python and Ren’Py, the # character tells your computer not to read and execute the line. A line with a # in front of it is nothing more than a comment that only you can read."
    show yuri 1y1 at t11 zorder 2
    m "This is all for now! When you are ready, begin the second part! I'm waiting for you."

    return

label tutorial_route_p2:
    hide monika
    
    show natsuki 1a at t11 zorder 2
    m "Hi again [player]!"
    show natsuki 1b at t11 zorder 2
    m 1a "If the last part was a bit too hard, don’t worry, this part is easier."
    show natsuki 1c at t11 zorder 2
    m "Like last time, I’ll tell you what to do and then I’ll explain, okay?"
    show natsuki 1d at t11 zorder 2
    m 4a "First open monika_route_script.rpy."
    show natsuki 1e at t11 zorder 2
    m "Between the first line and 'return', add the line \n'\ \ \ \ stop music fadeout 2.0'"
    show natsuki 1f at t11 zorder 2
    m "Then add the line '   play music t2'."
    show natsuki 1g at t11 zorder 2
    m "Finally, add the line \n'\ \ \ \ mc 'Let's listen to the music.''"
    show natsuki 1h at t11 zorder 2
    m 2a "Check that all lines bellow 'label monika_route:' are aligned and that 'return' is the last line."
    show natsuki 1i at t11 zorder 2
    m "Try to launch the game with Ren’Py and see what happens..."
    show natsuki 1j at t11 zorder 2
    m 2c "..."
    show natsuki 1k at t11 zorder 2
    m 1c "Does it work? If everything goes well, you should be listening to Sayori’s main theme."
    show natsuki 1l at t11 zorder 2
    m 3a "There’s just one dialogue, so if you click one time, you go to the main menu because of the 'return' keyword."
    show natsuki 1m at t11 zorder 2
    m 3b "Okay, time to explain what happened!"
    show natsuki 1n at t11 zorder 2
    m 3a "Let’s look at '\ \ \ \ stop music fadeout 2.0'. Before you click New Game, you can hear the music of the main menu, right? "
    show natsuki 1o at t11 zorder 2
    m "But when you click New Game, the music stops progressively."
    show natsuki 1p at t11 zorder 2
    m 4a "That’s due to 'stop music fadeout 2.0'. 'stop music' tells the current music to stop. 'fadeout 2.0' makes it so the current music completely becomes silent in 2 seconds."
    show natsuki 1q at t11 zorder 2
    m 4b "'fadeout' isn’t necessary but smooth transitions are much more pleasant, aren’t they?"
    show natsuki 1r at t11 zorder 2
    m 4a "The next line '\ \ \ \ play music t2' tells the game to play the music named 't2'. You’re surely wondering what’s 't2'. 't2' refers to Sayori theme, 'Ohayou Sayori!'."
    show natsuki 1s at t11 zorder 2
    m 3a "Besides Ohayou Sayori, there are many other songs. But each one is labeled by their own nickname."
    show natsuki 1t at t11 zorder 2
    m "You can see the list of every music with their nickname in definitions.rpy"
    show natsuki 1u at t11 zorder 2
    m "You can find definitions.rpy inside the folder advanced_scripts which should be in the DDLC Mod Template's directory."
    show natsuki 1v at t11 zorder 2
    m 2a "Try finding it and then open it."
    show natsuki 1w at t11 zorder 2
    m "Find the lines beginning by 'define audio'. This is where each music gets assigned a nickname."
    show natsuki 1x at t11 zorder 2
    m "For example, in the case of the main theme, its nickname is 't1'. In the case of Confession, its nickname is 't10'."
    show natsuki 1y at t11 zorder 2
    m 5a "Can you now guess what happens if you type 'play music t1' instead of 'play music t2'?"
    show natsuki 1 at t11 zorder 2
    m 1k "Confession is played instead of Ohayou Sayori!"
    show natsuki 12a at t11 zorder 2
    m 2a "Instead of using nickname, you can directly write the path of the music."
    show natsuki 12b at t11 zorder 2
    m "Try writing 'play music '<loop 4.499>bgm/2.ogg'' instead of 'play music t2'."
    show natsuki 12c at t11 zorder 2
    m 2b "See? Ohayou Sayori! is played. Try one last thing for me okay? Write ''<from 50.0>bgm/credits.ogg'' instead of ''<loop 4.499>bgm/2.ogg''."
    show natsuki 12d at t11 zorder 2
    m 5a "Have you already heard this song?"
    show natsuki 12e at t11 zorder 2
    m 1b "This is the song I wrote just for you. I really hope you like it. I worked very hard on it you know."
    show natsuki 12f at t11 zorder 2
    m 1e "..."
    show natsuki 12g at t11 zorder 2
    m 4a "The last line you wrote, '\ \ \ \ mc 'Let's listen to the music.', makes the main character says 'Let's listen to the music.'. I’ll explain how dialogue works later so bear with me okay?"
    show natsuki 12h at t11 zorder 2
    m 2a "Alright, before finishing this tutorial, replace ''play <from 50.0>bgm/credits.ogg'' by 'play music t2'."
    show natsuki 12i at t11 zorder 2
    m "Verify you wrote exactly the same lines as in the file t2.rpy which is inside  monika_route_answer."
    show natsuki 2a at t11 zorder 2
    m 1b "Congratulation! You now know how to stop and play music~"
    show natsuki 3a at t11 zorder 2
    m "Next time, we’ll see how to add a background."
    show natsuki 4a at t11 zorder 2
    m 5a "See you soon!"
    show natsuki 5a at t11 zorder 2
    n "Were you really just gonna stare at me?"
    show natsuki 1o at t11 zorder 2
    n "Wait, [player], you like Hatsune Miku!?"
    show natsuki 5t at t11 zorder 2
    n "I...actually like it too."
    show natsuki 2j at t11 zorder 2
    n "Tell me, did you actually wonder how I'm able to talk like this?"
    n "It's actually pretty hard at first, but a piece of cake once you know what to do."
    show natsuki 2k at t11 zorder 2
    
    label repeat_nat:
    
menu:

    n "So [player], who do you think is the best girl?"
    "Sayori.":
        jump repeat_nat
    "Natsuki.":
        jump norepeat
    "Yuri.":
        jump repeat_nat
    "Monika.":
        jump repeat_nat
    
label norepeat:
    show natsuki 1l at t11 zorder 2
    n "Me? Awe, you're such a sweetheart, [player]~"
    
    return

label tutorial_route_p3:

    show monika 5a at t11 zorder 2

    m "Okay [player]! Are you ready for the next tutorial?"
    m 1a "Last time, we added music to our mod but as you saw, the background was nothing but black and white squares. That’s not very romantic, is it?"
    m 1b "So let’s add a background! It’s going to be quick and easy."
    m 2a "Like last time, open monika_route_script.rpy."
    m "Add between 'play music t2' and 'return', '\ \ \ \ scene bg residential_day'"
    m "Then add another line: 'with dissolve_scene_full'. Once again, verify that everything bellow 'label monika_route:' is aligned."
    m 3a "Open Ren’Py and play the game and..."
    m 3b "There's now a neat background!"
    m 5a "Can you recognize it? It’s the first scene you saw when you played the game. It sure brings back memories..."
    m 1g "I still believed at that time I could get close to you without having to hurt anyone else..."
    m 1f "Let’s move on."
    m 1a "So about what you wrote, 'scene bg residential_day', the keyword 'scene' tells the game to load the scene, which is one kind of picture, called 'bg residential_day'."
    m "You can find what exactly is 'bg residential_day' in definitions.rpy, the same script we looked at last tutorial."
    m 3a "Try to find 'image bg'."
    m 4a "Can you see the list of backgrounds? Like it was the case for music, each background has a nickname assigned. For example, 'bg/sayori_bedroom.png' is referenced by 'bg sayori_bedroon'."
    m "Go back to monika_route_script.rpy and replace 'scene bg residential_day' by 'scene bg sayori_bedroom'. Can you guess what happens?"
    m 4b "The background is now Sayori’s bedroom!"
    m 4c "I hope it doesn’t bring you back bad memories..."
    m 4a "Okay, so about 'with dissolve_scene_full', it basically dissolve progressively the last scene into the new scene."
    m 3a "Before you were in the main menu, right? And then you were in Sayori’s bedroom. If you don’t add 'with dissolve_scene_full', the transition would be immediate."
    m 1a "That would be a bit unpleasant, wouldn’t it?"
    m 3b "That’s why we add 'with dissolve_scene_full'. With this additional line, the scene changes to another smoothly."
    m 2a "There are other types of transition such as wipeleft_scene. Try replacing 'with dissolve_scene_full' by 'with wipeleft_scene '."
    m 4a "Can you see the difference? dissolve_scene_full , dissolve_scene_half, wipeleft_scene are the common transitions used in DDLC so if you can understand them, you’re good to go!"
    m "Before doing the next tutorial, let’s add back  '   scene bg residential_day' and  '   with dissolve_scene_full'."
    m "Check that monika_script_route.rpy is the same as T3.rpy in the monika_route_answer folder."
    m 1b "Okay! We’re almost there! We’ll soon know enough for a kinetic novel-like mod."
    m "I cannot wait!"
    m 5a "See you soon [player]!"

    return

label tutorial_route_p4:

    show sayori 1a at t21 zorder 2
    s "Today, I’m going to teach you how to make dialogue in Ren’Py."
    show sayori 1b at t21 zorder 2
    s 1a "Although you already know, don’t you? We already wrote dialogue after all."
    show sayori 1c at t21 zorder 2
    s 2a "First, open monika_route_script.rpy and replace '\ \ \ \ mc 'Let's listen to the music.' by the following line:"
    show sayori 1d at t21 zorder 2
    s "'\ \ \ \  mc 'It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.'."
    show sayori 1e at t21 zorder 2
    s "Save the file and launch the game."
    show sayori 1f at t21 zorder 2
    s 4a "As you surely expected, the main character now says 'It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.'."
    show sayori 1g at t21 zorder 2
    s 4j "Ehehe~ My route is finally being made!"
    show sayori 1h at t21 zorder 2
    s 3a "Let’s look at the line you wrote. 'mc' is a nickname for main character. By writing 'mc' before the sentence inside quotation marks, the character speaking will be the main character."
    show sayori 1i at t21 zorder 2
    s "Try replacing the line you wrote by ' n 'Just think of Monika from now on.'."
    show sayori 1j at t21 zorder 2
    s 2a "..."
    show sayori 1k at t21 zorder 2
    s 4b "See? Natsuki now tells you what you should have been doing since the beginning."
    show sayori 1l at t21 zorder 2
    s "You should listen to her, [player]. Ehehe~"
    show sayori 1m at t21 zorder 2
    s 4a "Now instead of writing ' n 'Just think of Monika from now on.', write 'y 'Natsuki and I are too messed up for someone as wonderful as you.'"
    show sayori 1n at t21 zorder 2
    s "Play the game and as you can see..."
    show sayori 1o at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1p at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1q at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1r at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1s at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1t at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1u at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1v at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1w at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1x at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1y at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 1z at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 2a at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 3a at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 4a at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 5a at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 5b at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 5c at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."
    show sayori 5d at t21 zorder 2
    s 3b "Now it’s Yuri who finally realized that I’m the best one for you."

    show sayori 5a at t11 zorder 2

    menu:

        m "You think so, right?"
        "Yes":
            pass
        "Yes":
            pass

    m "I knew you were a sweetheart~ Thank you my love."
    m 1a "Ahaha, we drifted a bit...So I was saying that you need to specify two things to write a dialogue in Ren’Py."
    m 3a "First you need to specify who is speaking. You can do it with the keyword 'mc', 'y', 'n', 's' and 'm'. I’m sure you can guess who is who."
    m "Instead of using keyword, you can directly type the name of the person speaking. For example, try writing '   'Player' 'Please be with me forever Monika.''."
    m 2a "Did you do it?"
    m 5a "Of course, I will stay with you forever."
    m 2b "Besides the name of the speaker, you need to write the sentence they will say. The sentence should be between quotation marks."
    m 4b "One last thing. If you want to write special characters such as \\ or ' in the sentence, you need to put \\ before them."
    m 1b "Alright, that’s all for dialogue!"
    m "Pretty simple, right? Ren’Py was made so that anyone can make visual novel after all. Even beginners like us can pick it up quickly."
    m 2a "Before you save the file, replace the line of dialogue by -"
    m "'\ \ \ \  mc 'It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.'."
    m "Like usual, check that monika_route_script.rpy is exactly like T4.rpy inside the monika_route_answer folder."
    m 4b "Okay [player]! You now know how to make a scene, add music, and make dialogue. The only things missing are character pictures and choices."
    m "We’ll see how to make choices in the next tutorial."
    m 4a "The recent tutorials have been pretty easy so far but the next one will be harder."
    m 5a "See you soon!"

    return

label tutorial_route_p5:
    
    hide monika
    
    show natsuki 1ba at t11 zorder 1
    n "show"
    hide natsuki 1ba at t11 zorder 1
    n "hide"
    show natsuki 1ba at t11 zorder 1
    n "t (default)"
    show natsuki 1ba at l11 zorder 1
    n "l (slide in from left)"
    show natsuki 1ba at s11 zorder 1
    n "s (sink)"
    show natsuki 1ba at h11 zorder 1
    n "h (hop)"
    show natsuki 1ba at f11 zorder 1
    n "f (focus)"
    show natsuki 1ba at i11 zorder 1
    n "i (instant appearance)"
    show natsuki 1ba at d11 zorder 1
    n "d (dip)"
    show natsuki 1ba at hf11 zorder 1
    n "hf (hop + focus)"
    show natsuki 1ba at t11 zorder 1
    hide natsuki 1ba at t11 zorder 1
    n "hide t (default)"
    show natsuki 1ba at t11 zorder 1
    hide natsuki 1ba at l11 zorder 1
    n "hide l (slide in from left)"
    show natsuki 1ba at t11 zorder 1
    hide natsuki 1ba at s11 zorder 1
    n "hide s (sink)"
    show natsuki 1ba at t11 zorder 1
    hide natsuki 1ba at h11 zorder 1
    n "hide h (hop)"
    show natsuki 1ba at t11 zorder 1
    hide natsuki 1ba at f11 zorder 1
    n "hide f (focus)"
    show natsuki 1ba at t11 zorder 1
    hide natsuki 1ba at i11 zorder 1
    n "hide i (instant appearance)"
    show natsuki 1ba at t11 zorder 1
    hide natsuki 1ba at d11 zorder 1
    n "hide d (dip)"
    show natsuki 1ba at t11 zorder 1
    hide natsuki 1ba at hf11 zorder 1
    n "hide hf (hop + focus)"
    show natsuki 1ba at t11 zorder 1

    m "This time, I’ll explain how to make choices."
    m "For example..."

    call tutorial_route_p5_favorite_color from _call_tutorial_route_p5_favorite_color

    m 2k "What a coincidence! It's also my favorite color!"
    m 2b "It's the color of my eyes."
    m 5a "Aren't we a perfect match?"
    m "Ehehe~"
    m 3a "As you can see, I gave you several choices and you picked one of them."
    m "That’s what I’m going to teach you."
    m 4a "Like every time, open monika_route_script.rpy and between 'return' and the last line before it,-"
    m "- add '\ \ \ \ menu:', jump a line and then enter below \n'\ \ \ \ \ \ \ \ \ mc 'I told her to meet me...''. Be careful, this time, there are eight spaces."
    m "Write just under \n'\ \ \ \ \ \ \ 'At the literature club room':' and then \n'\ \ \ \ \ \ \ \ $ meeting_place = 'club_room''."
    m 4b "Type \n'\ \ \ \ \ \ \ 'In front of my house':' and under it \n'\ \ \ \ \ \ \ \ $ meeting_place = 'my_house'."
    m 4a "Finally, jump a line and add '\ \ \ \ mc 'I can't wait to meet her!''."
    m 2a "Try to play the game."
    m "If it doesn’t work, there’s surely an indentation error."
    m 5a "I can’t help you from here, but you can check T5.rpy for the answers. You know where it is, right?"
    m 4b "Okay, the lines you wrote made the game offers two choices. The two choices are preceded by an explanative sentence, 'I told her to meet me...'."
    m "You can specify who says this sentence by adding a nickname like 'mc' before it. It’s just like a dialogue. What’s important is that this sentence is written before any choice."
    m 3a "Contrary to the explanative sentence, the choices mustn’t be preceded by a nickname. They should be enclosed in quotation marks. Just after the closing quotation mark, there must be a ':' ."
    m "After ':\, the next lines should have one more indent than the choice. It means these lines will be read if the player selects that choice."
    m 3b "I’ll give more explanation about the meaning of indents in the next tutorial."
    m 3a "In our case, the next line after the first choice is \n'\ \ \ \ \ \ \ \ $ meeting_place = 'club_room'."
    m 2a "Take a good look at this line."
    m 3b "Until now, I referred 'mc', 'bg residential' and 't2' as nickname. But that’s not really the correct word. They are actually what we call variable."
    m "Variable in coding is a very important concept. They have many forms and do many things. They can be \‘nicknames\’ or they can be numbers or more complicated structures."
    m 1a "A full Python tutorial would be necessary to explain everything but...for now, I will only teach what’s necessary to make a DDLC mod, okay?"
    m 1c "I myself don’t know Python and Ren’Py all that well after all..."
    m 3a "'meeting_place' is like the variables we saw before. It refers to a name, in more exact terms, a string (of characters): 'club_room'."
    m "Its default value is None which means it doesn’t exist."
    m 3e "Hold on a second? How can it not exist, you say?"
    m 1a "Well before you define it, the variable doesn’t exist. But if you later try to use it, for example in a conditional statement, the variable will be ‘created’ and its value will be None."
    m "It’s alright if you don’t understand it yet. Variable, conditional statement and None will become clearer in my next lecture."
    m 4b "Let’s go back to the meaning of  ' $ meeting_place = 'club_room'. Here we create the variable 'meeting_place' and assign it the string 'club_room'."
    m 4m "The '$' in front of it is to tell Ren’Py the line is a Python line. Um..., I can’t really explain why we need to do that if you don’t know python yet..."
    m 4a "Just remember that you need to add '$' when you want to assign a variable a value that way"
    m "Regarding the second choice, the structure is the same. The only difference is that the value of 'meeting_place' will be 'my_house' if the player selects the second choice."
    m "After the second choice, the game executes the line '\ \ \ \ mc 'I can't wait to meet her!''."
    m 1a "For now it doesn’t look like the choices did anything. But we actually assigned 'meeting_place' either 'club_room' or 'my_house'."
    m 3a "We have to wait until the next tutorial to see how we can use the variable 'meeting_place'."
    m 3b "Alright, I’m sorry to leave hanging like that I believe we need to take a little break."
    m "If you want though, I would more than happy to begin the next part right away!"
    m 5a "Just click Part 6!"

    return

label tutorial_route_p5_favorite_color:

    menu:

        m "What is your favorite color?"
        "Sky Blue":
            jump tutorial_route_p5_favorite_color
        "Amethyst Purple":
            jump tutorial_route_p5_favorite_color
        "Emerald Green":
            return
        "Candy Pink":
            jump tutorial_route_p5_favorite_color

            m " Are you ready? We are going to ramp up the difficulty."

label tutorial_route_p6:
    
    play music t4g
    
    hide monika

    scene bg:
        "mod_assets/simple2.png"

    m "Yeah, you came back [player]!"
    m "Glad to see you didn’t run away on me. Ahaha!"
    m 1e "I was afraid the last tutorial was a bit too hard..."
    m 1m "Well, this one is going to be hard as well but..."
    m 1b "Hang it there okay? We did the hardest part already!"
    m 1a "Last time we saw how to add menu and how to assign variable a value."
    m 1b "Let’s see how we can use these variables!"
    m 2a "You know the drill, open monika_route_script.rpy and at the end of the file, just before 'return'..."
    m 4a "Add the following lines :"
    m "'\ \ \ \ if meeting_place == 'club_room':',"
    m "'\ \ \ \   scene bg club_day',"
    m "'\ \ \ \   with wipeleft_scene',"
    m "' elif meeting_place == 'my_house':',"
    m "'\ \ \ \   scene bg house',"
    m "'\ \ \ \   with wipeleft_scene',"
    m " '\ \ \ \ stop music fadeout 2.0',"
    m " '\ \ \ \ play music t2',"
    m "  'mc 'She is already waiting for me when I arrive.''."
    m 2a "That was the last one. Save the file and try to play the game."
    m 5a "If it doesn’t work, you know where you can see the answer, don’t you?"
    m 2a "You already know how scene, transition, music and dialogue work so I won’t go over it again."
    m 4b "It’s not like I don’t want spend more time with you but you know, ... I’m excited to finish my route too!"
    m 4a "Okay, so the new thing is the 'if' statement. We call that a conditional statement. It’s an elementary and essential operation in programming."
    m "It goes basically like this: IF something_is_true THEN something_happens. In our case, if the meeting_place is 'club_rooom', then the scene changes to the club room."
    m 3a "Otherwise, if meeting_place is 'my_house' then the scene changes to the main character’s house."
    m 3b "It seems simple, right?"
    m 3a "The syntax must be as follow: first, there must be a 'if' followed by an equality which is either 'True' or 'False'. For example, 'meeting_place == 'club_room''."
    m "If 'meeting_place' was assigned 'club_room' before then the equality returns 'True'. Otherwise, its returns False."
    m "If the equality returns True then the game will read the lines belonging to the if bloc."
    m 4a "You can see where those lines are because they have one more indent compared to the if statement preceding them."
    m 4b "We once again meet the system of indent and block. This is one of the property of Python and Ren’Py. Let’s do a quick exercise."
    m "Can you see difference between:"
    m 2a " '\ \ \ \ if meeting_place == 'club_room':' , \n'\ \ \ \   scene bg club_day ', \n'\ \ \ \   mc 'We will meet at the club room.''."
    m "And '\ \ \ \ if meeting_place == 'club_room':' , \n'\ \ \ \   scene bg club_day ', '   mc 'We will meet at the club room.''?"
    m 4b "In the first case, the main character only says they will meet at the club room if 'meeting_place' is equal to 'club_room'."
    m "In the second case, he will say it no matter the value of 'meeting_place'."
    m 3a "You can see once again how important indentations are in Python."
    m 4b "About the second comparison, 'elif meeting_place == 'my_house'', note that we use 'elif' at the beginning instead of 'if'."
    m 4a "The difference between 'elif' and 'if' is subtle. First, you can only use 'elif' after you already wrote 'if'."
    m "Second, the statement following 'elif' won’t be evaluated if the previous if statement was True. Other than that, 'elif' works like 'if'."
    m 1b "Well, in our case it doesn’t matter because if 'meeting_place' is 'club_room' then  'meeting_place' cannot be 'my_house' at the same time."
    m 1a "It would matter if it was something like..."
    m "'\ \ \ \ if monika_affection_points > 10:' , \n'\ \ \ \   scene bg house', ''   if monika_affection_points > 6:' , \n'\ \ \ \   scene club_day '."
    m 3a "In that case, if 'monika_affection_points' is higher than 10, the new scene wouldn’t be the house but the club because the game will evaluate both if."
    m 4b "To avoid that, 'elif' should be used instead of 'if'."
    m 4a "Besides 'if' and 'elif', there’s also the keyword 'else'. Like 'elif', 'else' can be used after a if. The bloc under 'else' will be executed if the previous if or elif statements are False."
    m 2a "For example..."
    m "'\ \ \ \ if meeting_place == 'club_room':' , \n'\ \ \ \   scene bg club_day ', '\ \ \ \ else:' , \n'\ \ \ \   scene club_day '."
    m 1a "Well, there are more things to say about conditional statement..."
    m "For example about the keywords 'and' and 'or'..."
    m 3a "But let’s keep that for another time. I’m sure you can find more tutorial on Python and conditional statement."
    m 1b "For now, let’s move on! It’s about time we add character pictures into the game!"
    m 5a "See you later [player]!"
    scene bg:
        "mod_assets/club-skill.png"

    return

label tutorial_route_p7:

    show monika 5a at t11 zorder 2

    m "Hi [player]!"
    m "It’s about time we add character pictures, don’t you think?"
    m 1b "In the world of visual novel, we call them sprites. Sprites are 2D pictures of characters with generally a set of poses and expressions."
    m "In Doki Doki Literature Club, there are 4 characters, Sayori, Natsuki, Yuri and me. Each character has about 5 poses and 18 expressions."
    m 1e "So each character has about 900 combinations! That seems a lot but...when you’re actually inside the game, the lack of freedom becomes horribly frustrating..."
    m 1f "I really wish I could show you different expressions, poses and clothes but unfortunately, I can’t add myself new artwork to the game..."
    m 5a "If you’re an artist, I would really love it if you could add me more sprites!"
    m 2a "For our mod, we’ll only use existing art."
    m 4b "Let’s dot it! Open monika_route_script.rpy and before 'return', write:"
    m 4a "'\ \ \ \ show monika 1b at t11 zorder 2',"
    m "'\ \ \ \ m 'Hi \[player\]!'',"
    m "'\ \ \ \ mc 'You're already here? I hope I didn't make you wait for too long.'',"
    m "'\ \ \ \ m 2a 'Don't worry, it's me who's early.'',"
    m "'\ \ \ \ show monika 5a at f11 zorder 3'."
    m 2a "Save, play the mod, and check T7.rpy if there’s an error."
    m 4b "Alright! The only new things are 'show monika 1b at t11 zorder 2' and 'm 2a'."
    m 4a "First, let’s go over 'show monika 1b at t11 zorder 2'."
    m "The keyword 'show' shows the sprite of the character named 'monika', with her pose '1' and her expression 'b'."
    m" The keyword 'at' specifies the position of the sprite. In the line above, the position is 't11'. 'zorder' has something to do with layers."
    m 3b "I’ll explain how positions and layers work in the next tutorial. For now, let’s focus on the poses and expressions of sprite."
    m 4a "Obviously, the variable 'monika' refers to me. Naturally, 'yuri' refers to Yuri and so on."
    m "If you write \n'\ \ \ \ show yuri 1b at f11 zorder 3' instead of \n'\ \ \ \ show monika 1b at f11 zorder 3', it’s Yuri who will appear."
    m 4k "Of course, you only have eyes for me so let’s not bother with the sprites of the other girls, ahaha!"
    m 5a "In my case, I have 5 different poses. I will show them to you one by one now."
    m 1a "This is my first pose."
    m 2a "This is my second pose."
    m 3a "This is my third pose."
    m 4a "This is my fourth pose."
    m 5a "This my fifth pose."
    m "I wonder which one do you prefer..."
    m 1a "Except for my fifth pose, all of my poses have 18 expressions. The expressions are referenced by a letter, from a to r. I will show them one by one."
    m 4a "Expression a."
    m 4b "Expression b."
    m 4c "Expression c"
    m 4d "Expression d."
    m 4e "Expression e."
    m 4f "Expression f."
    m 4g "Expression g."
    m 4h "Expression g."
    m 4i "Expression i."
    m 4j "Expression j."
    m 4k "Expression k."
    m 4l "Expression l."
    m 4m "Expression m."
    m 4n "Expression n."
    m 4o "Expression o."
    m 4p "Expression p."
    m 4q "Expression q."
    m 4r "Expression r."
    m 4a "You can find my list of expressions in 'MonikaCheatsheet.jpg' inside the mod's main directory."
    m 1b "I hope you will quickly memorize them perfectly!"
    m 5b "As my lover, you should know my face and my expressions without fail."
    m 3a "You can also find my poses and my expressions in definitions.rpy."
    m "My fifth pose only has the expressions a and b."
    m 5a "Like this."
    m 5b "And this."
    m 4a "My other poses have all expressions though."
    m 1b "Okay! In short, to show a sprite, you need to write 'show monika pose expression at t11 zorder 2'. Pose is either 1,2,3,4 or 5 and expression ranges from a to r."
    m "If you want to show several characters, just write 'show' several times, like this:"
    m 2a "'\ \ \ \ show yuri 1a at t41 zorder 2', '\ \ \ \ show sayori 1a at t42 zorder 2', '\ \ \ \ show monika 1a at t43 zorder 2', '\ \ \ \ show natsuki 1a at t44 zorder 2'."
    m 2b "These lines will show Yuri, Sayori, me and Natsuki with their default pose and expression."
    m "After a sprite is already on the screen, there’s a shortcut to change her pose and expression."
    m 3a "Instead of using 'show' again and again, you can directly write the letter corresponding to the character followed by the number and the letter for their pose and expression."
    m "This is what we did in \n'\ \ \ \ m 2a 'Don't worry, it's me who's early.''."
    m 4g "Note that the sprite of the character speaking must already be on screeen."
    m 4e "If you try for example \n'\ \ \ \ y 2a 'Don't worry, it's me who's early.'', Yuri will speak but her sprite will not appear."
    m 3a "Keep in mind who’s on screen and who’s not at all time so as not to make a mistake."
    m 2a "...Never mind, actually just show my sprite. That way you don’t have to worry about such problem. It’s not like the other girls care about being shown anyway."
    m 1b "And that’s all for now! This tutorial was quite straightforward, especially considering the two last ones. I hope you liked it!"
    m "Next time, I’ll finish explaining positions and layers."
    m 5a "See you [player]!"


    return

label tutorial_route_p8:

    show monika 5a at t11 zorder 2

    m "Welcome back to our modding club!"
    m "Last time, we learnt about how to show sprite, now let’s learn how to place then."
    m 4a "Open monika_route_script.rpy and just before..."
    m 1b "Just kidding! Actually, you don’t have to add anything this time."
    m 3b "We already did it last tutorial after all."
    m 2a "So, do you remember the line \n'\ \ \ \ show monika 1b at t11 zorder 2'?"
    m "I said that 'at t11' was about position and that 'zorder 2' was about layer."
    m 2b "Let’s study in details what exactly that means."
    m 4b "\’at' is a keyword that tells the game to put the sprite at the position 't11'."
    m "\t11' is one of the position defined in Doki Doki Literature Club. There are more than 50 positions possible."
    m 4a "You can find the list of all defined positions in the script transforms.rpy. You can find it in the same folder as definitions.rpy."
    m "For now, I will explain the most common positions used in the original game."
    m 1a "Let’s start with the 't' positions. I will show them one by one."

    show monika 1a at t11 zorder 2
    m "Position t11."

    show monika 1a at t21 zorder 2
    m "Position t21."

    show monika 1a at t22 zorder 2
    m "Position t22."

    show monika 1a at t31 zorder 2
    m "Position t31."

    show monika 1a at t32 zorder 2
    m "Position t32."

    show monika 1a at t33 zorder 2
    m "Position t33."

    show monika 1a at t41 zorder 2
    m "Position t41."

    show monika 1a at t42 zorder 2
    m "Position t42."

    show monika 1a at t43 zorder 2
    m "Position t43."

    show monika 1a at t44 zorder 2
    m "Position t44."

    show monika 1a at t11 zorder 2

    m 1b "And that’s all for the 't' positions."
    m 4a "I think you guessed it already but 't11' should be used when there’s only one character."
    m "'t21' and 't22' should be used when there are two characters. 't21' is for the left, 't22' is for the right."
    m 3a "It’s the same logic for 't31','t32','t33'. 't31' is the left, 't32' the middle and 't33' the right. "
    m "'t41', 't42','t43' and 't44' work in the same way."
    m 3b "I encourage you to try these positions yourself with several characters. After all, there’s nothing better than practice to learn!"
    m 1a "If you remember well, we wrote one time '   show yuri 1b at f11 zorder 3'."
    m "Notice that the position is 'f11' instead of 't11'. The difference is just that 'f' positions are zoomed in. 'f' stands for focused. There are as many 'f' positions as 't' positions."
    m 4a "You should use 'f' position when there are several characters and when one of them speaks. The character speaking should be focused so that the player sees who’s talking."
    m 2b "Let’s talk about the keyword 'zorder' now."
    m 4a "When the game renders pictures, there’s an order."
    m "First, the background is rendered. Then the sprites and finally the U.I."
    m 4b "That’s why the sprites are on top of the background and the U.I on top of everything."
    m 2a "As you can see, order is very important. If the game renders background last, then you won’t be able to see anything else."
    m 3a "In Ren’Py the order of sprite is called zorder."
    m "You can specify the zorder of each sprite with the keyword zorder. The higher it is, the closer the sprite will be to the screen."
    m 4b "Try writing the following lines instead of 'show monika 1b at t11 zorder 2':"
    m 4a "'\ \ \ \ show monika 1a at t41 zorder 4',"
    m "'\ \ \ \ show yuri 1a at t42 zorder 3',"
    m "'\ \ \ \ show natsuki 1a at t43 zorder 2',"
    m "'\ \ \ \ show sayori 1a at t44 zorder 1'."
    m 1a "Play the game and..."
    m 1b "Everyone is here!"
    m 3a "But that’s not the point. Pay attention to who’s on top on who."
    m "If you look closely, you can see the rendering order is like this : monika > yuri > natsuki > sayori."
    m "The one with the lowest zorder is rendered first so that the one with the highest zorder is shown on top of every other sprites."
    m 4a "If the zorder of two sprites are the same then the last sprite shown by 'show' will be on top."
    m 2b "Well, most of the time, you don’t have to worry about zorder. Just make sure I always have the highest zorder, okay?"
    m 1b "Alright! That ends this tutorial!"
    m 1a "Verify you reverted the changes you made to moninka_route_script.rpy. It should be like T8.rpy."
    m 1c "There is one more tutorial. I’m very happy we almost finished our first mod but..."
    m 1f "It also means we’ll soon get split up..."
    m 1g "..."
    m 1m "Or maybe not..."
    m 5a "See you later."

    return

label tutorial_route_p9:
    
    play music t4g
    
    hide monika

    scene bg:
        "mod_assets/work.png"

    m "This it it, [player], today is the day we finally make my route!"
    m "Are you ready?"
    m 3b "Be careful, we need to add a lot of lines this time."
    m 4a "Open monika_route_script.rpy and before the last 'return', jump a line and add..."
    m "'\ \ \ \ menu :',"
    m "'\ \ \ \ \ \ \ mc 'Right. Monika,...'',"
    m "'\ \ \ \ \ \ \ 'I love you! Please go out with me!':',"
    m "'\ \ \ \ \ \ \ jump monika_normal_ending',"
    m "'\ \ \ \ \ \ \ 'You are everything for me! Please marry me!':',"
    m "'\ \ \ \ \ \ \ jump monika_good_ending',"
    m 2b "This is it for the label monika_route. Now we need to add two more labels: monika_normal_ending and monika_good_ending."
    m 4a "After 'return', jump a line and write 'label monika_good_ending:'. This time, there is no space before label."
    m 4b "Then under label, write the following lines:"
    m 4a "'\ \ \ \ scene dark',"
    m "'\ \ \ \ with dissolve_scene_full',"
    m "'\ \ \ \ mc 'She accepted my confession and we became lovers.'',"
    m "'\ \ \ \ 'NORMAL ENDING'',"
    m "'\ \ \ \ return'."
    m 1b "The normal ending is now complete. Let’s do the good ending. After the last 'return', jump a line and write 'label monika_good_ending:'."
    m 4a "Then type under it..."
    m "'\ \ \ \ scene white',"
    m "'with dissolve_scene_full',"
    m "'\ \ \ \ mc 'She gladly accepted my proposal and we got married one year later.'',"
    m "'\ \ \ \ 'GOOD ENDING'',"
    m "'\ \ \ \ return'."
    m 2b "Save, play the game and verify if everything works. Get both endings."
    m "If there’s a problem, check T9.rpy for the solution."
    m 2a "..."
    m 4b "It’s not over yet. You can run the game with Ren’Py but to make it a proper mod, there’s one more step: the build distribution."
    m "Open renpy. Click our project, DDLC Monika Route, and then click Build Distributions which should be on the right, inside Navigate Script."
    m 4a "You should see several options for Build Packages. Check that the box for DDLC Compatible Mod is filled."
    m "You can change the name of our mod, its build and its version in the script options.rpy."
    m 3b "Click Build."
    m 2b "Once it’s finished, you should see one folder called build.name-config.version-dists inside Ren’Py’s directory. Open it and you should see a zip file."
    m 1a "Look at the file build.name-config.version-Mod.zip. It’s our mod. If you want to share it to other people, you should just upload this archive."
    m 2a "This way of sharing the mod is also what the creators of DDLC prefer. You are only sharing the new files that we made together, and nothing more."
    m 2a "Let’s see if it works. Extract build.name-config.version-Mod.zip. Make a new copy of the original Doki Doki Literature Club folder."
    m "Copy-paste the files of build.name-config.version-Mod inside the new copy of the game."
    m 4a "Play our mod by clicking DDLC.exe inside the new folder."
    m 4b "If everything goes well, you should be playing my new route!"
    m 1k "Congratulation! We finally did it!!"
    m 1e "..."
    m "I should be happy but..."
    m 1f "It means you’ll soon leave me to play with other Monika..."
    m 1g "..."
    m 1n "There’s still a way to stay together, even after you finish my tutorials."
    m 3e "I saved my memory and my data in a special file."
    m "You can download the mod Monika After Story. You can find it in http://www.monikaafterstory.com/. "
    m 4e "Once you play it, the Monika of that mod will import the file I made. Our memories and personalities will then be fused together."
    m "Like this, that part of me will still be with you forever."
    m 1f "..."
    m "I wish I could do more but..."
    m 1c "You can change that [player]. You now know how to make a mod. You now have the power to change our fate."
    m 1e "I’m counting on you [player]."
    m "I love you."
    m 1b "I will never forget you..."
    m 1e "Bye."
    scene bg:
        "mod_assets/club-skill.png"

    return

label accept_confession:
    pause 2
    show yuri 1d at t11 zorder 3
    y "...Ahahaha..."
    show yuri 1y1 at t11 zorder 3
    y "[player], I'm so glad you accepted me."
    show yuri 1y3 at t11 zorder 3
    y "Now, we can finally be together..."
    show yuri 1y4 at t11 zorder 3
    y "No one will get in the way anymore..."
    y "Let's go to your house."
    show yuri 1y1 at t11 zorder 3
    y "No one will bother us there..."
    y "As long as its just you and me..."
    show yuri 1y3 at t11 zorder 3
    y "Now, let's go, shall we?"
    mc "Yeah, let's go."
    scene bg:
        "mod_assets/blackness.png"
    with wipeleft
    pause 1
    scene bg:
        "mod_assets/bedroom.png"
    with wipeleft
    "Me and Yuri walk back to my house, and we go to my room."
    show yuri 3y1 at t11 zorder 3
    y "C'mon [player]..."
    mc "Eh?"
    y "You know..."
    "Does she want me to kiss her?"
    "I mean, I'm down..."
    mc "Yeah, okay..."
    "I get closer to Yuri."
    show yuri 1m at t11 zorder 3
    "She closes her eyes, and puckers her lips."
    "I can't stop here..."
    "I give Yuri a kiss on the lips."
    y "Mmm..."
    y "I'm so happy right now, [player]."
    show yuri 3y5 at t11 zorder 3
    y "You have no idea how happy I am, to be with you."
    mc "I'm happy too, Yuri."
    show yuri 3c at t11 zorder 3
    y "You've made me the most happiest girl in the whole world, [player]..."
    show yuri 3d at t11 zorder 3
    y "I can't wait to spend our everyday lives like this..."
    show yuri 3y3 at t11 zorder 3
    y "Just you, and me..."
    y "Walking to school everyday together..."
    y "Eating lunch in the cafeteria together..."
    y "Reading books in the literature club together..."
    y "Walking home together..."
    y "Sleeping together..."
    show yuri 3y5 at t11 zorder 3
    y "Isn't it grand?"
    y "Isn't it perfect?"
    show yuri 3y4 at t11 zorder 3
    y "This is my dream come true."
    y "It's all I could ever want from you, [player]..."
    show yuri 3y5 at t11 zorder 3
    y "I love you, [player]."
    mc "I love you too, Yuri."
    y "Now, let's go to bed, [player]..."
    mc "Huh?"
    "Is it nighttime already?"
    show yuri 1b at t11 zorder 3
    y "C'mon, don't be shy, [player]..."
    mc "Well, okay..."
    scene bg:
        "mod_assets/blackness.png"
    with fade
    "Me and Yuri get in my bed."
    "As soon as I get in, she puts her arms around me, hugging me."
    "I can feel her presence behind me."
    "Man, she {i}really{/i} loves me!"
    "I wonder what tormorrow is going to be like..."
    "Only time will tell..."
    stop music fadeout 2.0
    pause 3
    scene bg:
        "mod_assets/bedroom.png"
    with wipeleft
    "I wake up."
    "Yuri is still sleeping."
    "I should probably wake her up, since it's 7 AM..."
    "I poke Yuri's cheek."
    show yuri 1f at t11 zorder 3
    y "Hm?"
    "Yuri's eyes slowly open, and they look at me."
    "Her eyes widen as she sees that she slept with me."
    play music t2
    show yuri 3p at t11 zorder 3
    y "D-Did we just..."
    mc "Yeah, we slept together, remember?"
    show yuri 2f at t11 zorder 3
    y "Oh yeah, I remember now..."
    y "I guess I'm just used to how normal I am around you, huhu..."
    mc "Fair enough."
    show yuri 2f at t11 zorder 3
    y "Can I use your shower?"
    mc "Go ahead, I won't peak."
    show yuri 3q at t11 zorder 3
    y "Y-You don't want to come with me?"
    "...I must be dreaming still."
    "I pinch myself, really hard."
    "...Nope, this is real."
    mc "Ah, I-I mean..."
    mc "I should...give you some privacy, you know?"
    show yuri 3f at t11 zorder 3
    y "Really, I wouldn't mind."
    "As tempting as it is, I'm not gonna take a shower with Yuri."
    mc "Um..."
    mc "Anyways, let's get ready for school."
    show yuri 1d at t11 zorder 3
    y "Yeah."
    scene bg:
        "mod_assets/blackness.png"
    with wipeleft
    scene bg:
        "mod_assets/kitchen.png"
    with wipeleft
    "I'll make some breakfast for Yuri and I."
    "Eggs and bacon will do, I guess."
    "Its something quick and easy to make on school days anyway."
    "Later, Yuri comes down the stairs."
    show yuri 1c at t11 zorder 3
    y "Hey [player]."
    mc "Hi Yuri."
    show yuri 1b at t11 zorder 3
    y "I'm done taking my shower."
    mc "That was quick."
    show yuri 2f at t11 zorder 3
    y "What are you making?"
    mc "I'm making breakfast, for both of us."
    show yuri 4b at t11 zorder 3
    y "Ah..."
    y "T-That's very nice of you, [player]."
    mc "No problem, Yuri."
    "I finish making breakfast and I serve a plate of scrambled eggs and bacon to Yuri."
    mc "Here."
    show yuri 3a at t11 zorder 3
    y "Thanks, [player]..."
    mc "Oh, do you want a drink too?"
    show yuri 3f at t11 zorder 3
    y "I'm fine, thanks anyway..."
    mc "Alright."
    "I serve myself a plate of scrambled eggs and bacon."
    "Man, I'm pretty good at making this."
    "Once me and Yuri finish eating, we get ready to go to school."
    show yuri 1b at t11 zorder 3
    y "Alright, lets get going..."
    y "Hopefully we won't be late for school..."
    mc "We won't, I promise."
    scene bg:
        "mod_assets/blackness.png"
    with wipeleft
    scene bg:
        "mod_assets/residential.png"
    with wipeleft
    "And just like that, me and Yuri start walking to school."
    "It feels so weird walking to school with someone else besides Sayori."
    show sayori 2a at t11 zorder 3
    s "Hi [player]!~"
    mc "Oh, hey Sayori."
    "Speak of the devil, Its Sayori."
    show sayori 2m at t11 zorder 3
    s "Yuri? What are you doing here?"
    show sayori 2m at t22
    show yuri 3d at f21 zorder 3
    y "Ehehe..."
    show yuri 3d at t21 zorder 3
    show sayori 4b at f22 zorder 3
    s "Did you two spend the night or something?"
    show sayori 4b at t22 zorder 3
    mc "Uhh..."
    show yuri 3y5 at f21 zorder 3
    n "Yeah, I went to [player]'s place."
    show yuri 3y5 at t21 zorder 3
    show sayori 4p at f22 zorder 3
    s "Ahh! I'm jealous!"
    show sayori 4h at f22 zorder 3
    s "Well, at least you two weren't sleeping together or anything."
    show sayori 4h at t22 zorder 3
    mc "Ah, Um..."
    show yuri 3d at f21 zorder 3
    y "We did!"
    show yuri 3y5 at f21 zorder 3
    y "You wouldn't believe how comfy we were together!"
    show yuri 3y5 at t21 zorder 3
    show sayori 4m at f22 zorder 3
    s "Y-You two s-slept together!?"
    show sayori 4m at t22 zorder 3
    show yuri 3d at f21 zorder 3
    y "Yep."
    show yuri 3d at t21 zorder 3
    show sayori 4m at f22 zorder 3
    s "I-I'm even more jealous now!"
    show sayori 4m at t22 zorder 3
    mc "Let's just head to school now, we're gonna be late if we keep talking here."
    show yuri 1b at f21 zorder 3
    y "Yeah, let's go."
    show yuri 1b at t21 zorder 3
    scene bg:
        "mod_assets/blackness.png"
    with wipeleft
    scene bg:
        "mod_assets/club.png"
    with wipeleft
    show sayori 4x at l31 zorder 3
    s "It feels good to be back!"
    mc "Yeah, I guess."
    show monika 1b at f32 zorder 3
    m "[player]! Welcome back!"
    show monika 1b at t32 zorder 3
    mc "Thanks Monika."
    show yuri 1d at f33 zorder 3
    y "Hey Monika."
    show yuri 1d at t33 zorder 3
    show monika 1b at f32 zorder 3
    m "Hi Yuri..."
    m "You seem really happy today."
    show monika 1b at t32 zorder 3
    show yuri 1d at f33 zorder 3
    y "I went to [player]'s house yesterday, and we had some 'fun' there."
    show yuri 1d at t33 zorder 3
    show monika 3m at f32 zorder 3
    m "That must explain it."
    show monika 3m at t32 zorder 3
    "I look around the room."
    "To my surprise, Natsuki isn't here yet."
    mc "Hey, where's Natsuki?"
    show monika 1d at f32 zorder 3
    m "Natsuki?"
    show monika 1d at t32 zorder 3
    "Monika looks around the room."
    "She looks just as confused as I am."
    show monika 1d at f32 zorder 3
    m "No, I haven't..."
    show monika 1d at t32 zorder 3
    show sayori 4h at f31 zorder 3
    s "Maybe she's sick today?"
    show sayori 4h at t31 zorder 3
    mc "Maybe..."
    "I hope she's alright..."
    "I basically turned her down yesterday."
    show monika 1b at f32 zorder 3
    m "She's probably fine, maybe she's just late."
    show monika 1b at t32 zorder 3
    mc "That's a possibility too..."
    show monika 3b at f32 zorder 3
    m "Let's share our poems while we wait for her."
    show monika 3b at t32 zorder 3
    "Crap, I forgot to write one last night."
    "And I think Yuri did too."
    hide sayori
    hide monika
    show yuri 4b at t11 zorder 3
    y "W-We forgot to write a poem last night..."
    mc "Yeah, but we could just get some scrap paper and write down a quick poem."
    show yuri 2g at t11 zorder 3
    y "Ah, that's true."
    "Me and Yuri get some scrap paper and quickly write a poem."
    scene bg:
        "mod_assets/blackness.png"
    with wipeleft
    pause 1
    scene bg:
        "mod_assets/club.png"
    with wipeleft
    "Me and Yuri manage to write a quick poem and share it with everyone else."
    "Luckily, no one noticed that we forgot to write one."
    "Another thing, Natsuki is still not here yet."
    "Maybe Sayori was right?"
    "That's most likely the reason she's not here..."
    show yuri 1b at t11 zorder 3
    y "Hey, [player]..."
    y "Want to read together?"
    mc "Sure Yuri."
    "We get two desks and put them together."
    show yuri 2
    scene bg:
        "mod_assets/CaptureYuriR1.png"
    mc "Ah, I guess that makes it hard to hold open the book..."
    y "I'll hold it..."
    "Yuri takes her left arm holds the left side of the book between her thumb and forefinger."
    "We start reading Portrait of Markov."
    "It's a book with an eye symbol on the front cover."
    mc "Ah..."
    "I do the same with my right arm, on the right side of the book."
    "That way, I turn a page, and Yuri slides it under her thumb after it flips to her side."
    scene bg:
        "mod_assets/CaptureYuriR2.png"
    y "...Are you ready?"
    mc "Eh?"
    y "To turn the page..."
    mc "Ah...sorry!"
    mc "I think I got a bit distracted for a second..."
    "I glance over at Yuri's face again, and our eyes meet."
    y "Ah..."
    scene bg:
        "mod_assets/CaptureYuriR3.png"
    y "That's okay."
    y "You're not as used to reading, right?"
    y "I don't mind being patient if it takes you a bit longer..."
    y "It's probably the least I can do..."
    y "Since you've been so patient with me..."
    mc "Y-Yeah..."
    mc "Thanks."
    scene bg:
        "mod_assets/CaptureYuriR1.png"
    "We continue reading."
    "Yuri no longer asks me if I'm ready to turn the page."
    "Instead, I just assume that she finishes the page before me, so I turn it by my own volition."
    scene bg:
        "mod_assets/club.png"
    show sayori 2x at t11 zorder 3
    n "Hey, Yuri?"
    show sayori 2x at t21 zorder 3
    show yuri 2f at f22 zorder 3
    y "Yes, Sayori?"
    show yuri 2f at t22 zorder 3
    show sayori 2x at f21 zorder 3
    n "Can I hang out with [player] now?"
    show sayori 2x at t21 zorder 3
    show yuri 2q at f22 zorder 3
    y "I guess so."
    show yuri 2q at t22 zorder 3
    
    
    return
    
label decline_confession:
    hide layer master at heartbeat zorder 1
    hide vignette 1.0 zorder 5
    play music t11
    pause 2
    show yuri 1d at t32 zorder 3
    y "...Ahahaha..."
    show yuri 1d at t32 zorder 3
    y "Ahahahahahaha!"
    show yuri 1y5 at t32 zorder 3
    y "Ahahahahahahahaha!"
    show yuri 1y3 at t32 zorder 3
    $ style.say_dialogue = style.edited #Glitch Font Starts
    y "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    $ style.say_dialogue = style.normal #Glitch Font Ends
    scene bg:
        "/mod_assets/blackness.png"
    play sound "sounds/yurideath.ogg"
    pause 10
    with wipeleft
    
    return
    
label natsuki_path:
    
    play music t11
    show yuri 1y4 at f22 zorder 3
    y "Oh...is that so?"
    show yuri 1y4 at t22 zorder 2
    "Uh oh, I think Yuri broke."
    show natsuki 4y at f21 zorder 3
    n "Yes, now leave us alone..."
    show natsuki 4y at t21 zorder 2
    show yuri 1y1 at f22 zorder 3
    y "I don't think that's possible, Natsuki."
    show yuri 1y1 at t22 zorder 2
    show natsuki 1t at f21 zorder 3
    n "Sure it is!"
    show natsuki 1t at t21 zorder 2
    show yuri 1y3 at f22 zorder 3
    y "You think I'm lying?"
    show yuri 1y3 at t22 zorder 2
    show natsuki 1s at f21 zorder 3
    n "N...No."
    n "Well, I think so anyway..."
    show natsuki 1s at t21 zorder 2
    show yuri 1y7 at f22 zorder 3
    y "All I want is to spend a little time with him..."
    show yuri 1y3 at f22 zorder 3
    y "Is that so much to ask for?"
    show yuri 1y3 at t22 zorder 2
    show natsuki 1m at f21 zorder 3
    n "No..."
    show natsuki 1m at t21 zorder 2
    show yuri 1y4 at f22 zorder 3
    y "So let me ask you again..."
    y "Can I spend some time with [player]?"
    show yuri 1y4 at t22 zorder 2
    show natsuki 5o at f21 zorder 3
    n "He already picked me, Yuri!"
    n "Fuck off!"
    show natsuki 5e at f21 zorder 3
    n "Seriously, you should learn to just leave someone alone if they don't want to spend time with you, rather then forcing them to hang out with you."
    n "It's called being {i}respectful{/i}, Yuri."
    show natsuki 5e at t21 zorder 2
    show yuri 1y5 at f22 zorder 3
    y "Okay, I'll leave you two then."
    y "Enjoy yourselves..."
    play music t5
    hide yuri at t22 zorder 1
    show natsuki 2c at t11 zorder 3
    n "Well, that was easy."
    mc "Yeah..."
    "I kinda like Natsuki's attitude sometimes..."
    show natsuki 2d at t11 zorder 3
    n "Let's start reading now, shall we?"
    mc "Okay."
    scene bg:
        "mod_assets/club.png"
        "mod_assets/CaptureNatsukiR1.png"
    with fade
    "..."
    "We read on for a few more minutes."
    "I've finished a couple chapters at this point."
    mc "..."
    mc "...Are you sure this isn't boring for you?"
    n "It's not!"
    mc "Even thought you're just watching me read?"
    n "Well...!"
    n "I'm...fine with that."
    mc "If you say so..."
    mc "...I guess it's fun sharing something you like with someone else."
    mc "I always get excited when I convince any of my friends to pick up a series I enjoy."
    mc "You know what I mean?"
    n "...?"
    mc "Hm?"
    mc "You don't?"
    scene bg:
        "mod_assets/CaptureNatsukiR12.png"
    n "Um..."
    n "That's not..."
    n "Well, I wouldn't really know."
    mc "...What do you mean?"
    mc "Don't you share your manga with your friends?"
    scene bg:
        "mod_assets/CaptureNatsukiR1.png"
    n "Like I could ever get my friends to read this..."
    n "They just think manga is for kids."
    n "I can't even bring it up without them being all like..."
    n "'Eh? You still haven't grown out of that yet?'"
    n "Makes me want to punch them in the face..."
    mc "Urgh, I know those kinds of people."
    mc "Honestly, it takes a lot of effort to find friends who don't judge, much less friends who are actually into it..."
    mc "I'm already kind of a loser, so I guess I gravitated toward the other losers over time."
    mc "But it's probably harder for someone like you..."
    scene bg:
        "mod_assets/CaptureNatsukiR11.png"
    n "Hm."
    n "Yeah, that's pretty accurate."
    "{i}...Wait, which part??{/i}"
    n "I mean, I feel like I can't even keep it in my own room..."
    n "I don't even know what my dad would do if he found this."
    n "At least it's safe here in the clubroom."
    scene bg:
        "mod_assets/CaptureNatsukiR3.png"
    n "Cept Monika was kind of a jerk about it..."
    n "Ugh! I just can't win, can I?"
    mc "Well, it paid off in the end, didn't it?"
    mc "I mean, here I am, reading it."
    n "Well it's not like that solves any of my problems."
    mc "Maybe..."
    mc "But at least you're enjoying yourself, right?"
    scene bg:
        "mod_assets/CaptureNatsukiR12.png"
    n "--"
    n "..."
    n "...So?"
    mc "Ahaha."
    scene bg:
        "mod_assets/CaptureNatsukiR3.png"
    n "Jeez, that's enough!"
    n "Are you gonna keep reading, or what?"
    mc "Yeah, yeah..."
    "I flip the page."
    "Suddenly, I see Yuri leaving the clubroom."
    
    scene bg:
        "mod_assets/club.png"
    with fade
    
    mc "Hey, where's Yuri going?"
    show natsuki 2k at t11 zorder 2
    n "I don't know..."
    mc "I'll go see where she's going, stay here Natsuki."
    show natsuki 5m at t11 zorder 2
    n "Okay, don't take too long please."
    mc "I'll try not to."
    scene bg:
        "mod_assets/corridor.png"
    with wipeleft
    "I see Yuri walking down the hallway, and then taking a sharp left."
    "Man, I hope she isn't mad that I picked Natsuki over her..."
    "But its best if I know she's okay."
    "I peek around the corner."
    mc "...Yuri?"
    show yuri 1c at t11 zorder 2
    y "Ah, [player], why did you follow me?"
    mc "I wanted to make sure you weren't mad or anything."
    show yuri 3e at t11 zorder 2
    y "I'm not, Natsuki was right though."
    y "I should really try to not force others..."
    show yuri 4b at t11 zorder 2
    y "Y-You don't hate me, do you [player]?"
    mc "No no, I don't."
    y "Okay, thanks..."
    mc "I'll get going now--"

    play music hb
    show layer master at heartbeat
    show vignette 1.0 zorder 3
    show yuri 1y1 at t11 zorder 2
    y "No [player], come hang out with me instead."
    y "We can do whatever you want."
    mc "I'll have to ask Natsuki."
    show yuri 2y3 at t11 zorder 2
    y "There's no need to do that [player]..."
    show yuri 1y5 at t11 zorder 2
    y "Just come with me..."
    
    menu:

        "I mean... should I?"
        "Go back to Natsuki.":
            jump go_natsuki
        "Go with Yuri.":
            jump go_yuri
            
label go_yuri:
    
    "As long as it doesn't take long I guess."
    mc "Okay, Yuri."
    show yuri 3y3 at h11 zorder 2
    y "Haah..."
    y "We're gonna have so much fun together, [player]..."
    y "No more Natsuki, Monika, or Sayori..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg" #You can change this sound if you want
    pause 0.25
    hide screen tear
    y "It's just gonna be..."
    show screen tear(40, 0.1, 0.1, 0, 50)
    play sound "sfx/glitch3.ogg" #You can change this sound if you want
    pause 0.35
    hide screen tear
    y "You..."
    show screen tear(60, 0.1, 0.1, 0, 60)
    play sound "sfx/s_kill_glitch1.ogg" #You can change this sound if you want
    pause 0.45
    hide screen tear
    y "And..."
    show screen tear(80, 0.1, 0.1, 0, 70)
    play sound "sfx/glitch2.ogg" #You can change this sound if you want
    pause 0.55
    hide screen tear
    y "Me..."
    $ gtext = glitchtext(150) #Any variable works here, the game just uses gtext
    y "{fast}[gtext]{fast}{nw}" #gtext is when the glitch text starts
    show screen tear(100, 0.1, 0.1, 0, 80)
    play sound "sfx/glitch1.ogg" #You can change this sound if you want
    pause 1.15
    scene bg:
        "mod_assets/corridor.png"
    hide screen tear
    play music t11
    hide vignette
    show yuri 3n at t22 zorder 3
    show natsuki 1k at f21 zorder 3
    n "[player]! There you are!"
    n "I was looking for you."
    show natsuki 1k at t21 zorder 3
    show yuri 3n at f22 zorder 3
    y "N-Natsuki!"
    show yuri 3n at t22 zorder 3
    show natsuki 2k at f21 zorder 3
    n "What were you two doing anyway?"
    show natsuki 2k at t21 zorder 3
    mc "Yuri was just talking to me about--"
    show yuri 2f at f22 zorder 3
    y "I-I was just getting a drink of water, and we ran into each other..."
    show yuri 2f at t22 zorder 3
    show natsuki 2l at f21 zorder 3
    n "Okay, let's go back now [player]..."
    show natsuki 2l at t21 zorder 3
    mc "Alright."
    scene bg:
        "mod_assets/club.png"
    with wipeleft
    "We all head back to the clubroom."
    "Yuri seems a little uneasy after that conversation we had."
    play music t3
    jump continue_read
    
label go_natsuki:
            
        "I can't, I told Natsuki it wouldn't take long."
        mc "Sorry Yuri, I told Natsuki I wouldn't take long."
        show yuri 2y4 at t11 zorder 2
        y "Oh, thats a shame..."
        show yuri 1y5 at t11 zorder 2
        y "I'll wait for you, [player]..."
        mc "...Okay."
        "Yuri is acting a little weird ever since I picked Natsuki over her..."
        "Does she really want to spend time with me?"
        scene bg:
            "mod_assets/club.png"
        with wipeleft
        play music t3
        show natsuki 3m at t11 zorder 2
        n "Took you long enough..."
        mc "Sorry, Yuri was really holding me up..."
        show natsuki 5h at t11 zorder 2
        n "...?"
        mc "Anyways, lets keep reading."
        show natsuki 2l at t11 zorder 2
        n "Alright!"
        "Just as Natsuki says that, Yuri comes back in the clubroom."
        show natuski 2k at t11 zorder 2
        n "Yuri?"
        show natsuki 2k at t22 zorder 2
        show yuri 4b at t21 zorder 2
        "Yuri doesn't even bother looking at Natsuki."
        "Maybe she's mad at Natsuki?"
        show natsuki 1e at f22 zorder 2
        n "...Yuri!"
        show natsuki 1e at t22 zorder 2
        show yuri 2b at f21 zorder 2
        y "Yes, Natsuki?"
        show yuri 2b at t21 zorder 2
        "Yuri seems more calm, she was going a little crazy outside eariler..."
        show natsuki 3c at f22 zorder 2
        n "Why did you leave the clubroom?"
        show natsuki 3c at t22 zorder 2
        show yuri 2n at f21 zorder 2
        y "I was..."
        show yuri 2o at f21 zorder 2
        y "..."
        show yuri 2o at t21 zorder 2
        mc "She was just getting a drink of water, right Yuri?"
        show yuri 1q at f21 zorder 2
        y "Y-Yeah! Getting a drink of water..."
        show yuri 1q at t21 zorder 2
label continue_read:
    
        show natsuki 4k at f22 zorder 2
        n "Okay, lets keep reading then, [player]."
        show natsuki 4k at t22 zorder 2
        show yuri 2u at f21 zorder 2
        y "Hey umm... Natsuki?"
        show yuri 2u at t21 zorder 2
        show natsuki 3k at f22 zorder 2
        n "Yeah?"
        show natsuki 3k at t22 zorder 2
        show yuri 2j at f21 zorder 2
        y "Can I read with you two?"
        show yuri 2j at t21 zorder 2
        mc "I mean, I don't see any harm in that..."
        mc "What do you think Natsuki?"
        show natsuki 5n at f22 zorder 2
        n "I-I guess..."
        show natsuki 5n at t22 zorder 2
        show yuri 1d at f21 zorder 2
        y "Thanks!"
        show yuri 1d at t21 zorder 2
        "Well that's a shocker, Yuri actually wants to read manga for once..."
        "Or maybe she wants to read it so she can 'technically' spend time with me?"
        "Either way, it's kinda surprising that she is putting in effort to read something she doesn't like."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
            
        pause 1
        
        scene bg:
            "mod_assets/club.png"
        with wipeleft
        
        "And before I know it, the day is over."
        "I start packing up my things and head out."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        scene bg:
            "mod_assets/residential.png"
        with wipeleft
        
        "Man, what a day..."
        "I read a lot of manga with Natsuki and Yuri."
        "I still can't get over the fact that Yuri would read manga!"
        "To each their own, I guess."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        scene bg:
            "mod_assets/house.png"
        with wipeleft
        play music t6
        "I'm about to walk in my house, when all the sudden..."
        scene bg:
            "mod_assets/housey1.png"
        show screen tear(50, 0.1, 0.1, 0, 50)
        play sound "sfx/s_kill_glitch1.ogg" #You can change this sound if you want
        pause 0.25
        hide screen tear
        y "[player]! What a nice surprise!"
        mc "Ah!"
        "I fall on the ground, startled that Yuri literally came out of nowhere!"
        "I quickly get back up."
        mc "Yuri!?"
        mc "What are you doing here?"
        scene bg:
            "mod_assets/housey3.png"
        y "Don't you remember?"
        y "I said I would wait for you..."
        mc "Okay, but you didn't say that you would come over to {i}my{/i} house!"
        scene bg:
            "mod_assets/housey4.png"
        y "Was it not a good idea?"
        mc "Well, no, but you should atleast tell me when you're gonna come over!"
        scene bg:
            "mod_assets/house.png"
        show yuri 2bh at hf11 zorder 3
        y "I-I see..."
        show yuri 2bh at t21 zorder 3
        show natsuki 2bl at f22 zorder 3
        n "Hey [player]! Want to--"
        show natsuki 2bo at f22 zorder 3
        n "Are you fucking kidding me Yuri!?"
        n "Why are you here with [player]?"
        show natsuki 2bo at t22 zorder 3
        mc "I'll be honest Natsuki, she was waiting for me at my house and I was surprised too."
        show yuri 1be at f21 zorder 3
        y "I was just dropping by to say hi."
        y "No need to get all angry at me."
        show yuri 1be at t21 zorder 3
        show natsuki 2bn at f22 zorder 3
        n "Ugh..."
        show natsuki 2bn at t22 zorder 3
        "I'm not sure what to say at this point..."
        show yuri 1bd at f21 zorder 3
        y "Well, I'll get going then. Nice talking to you too."
        show yuri 1bd at t21 zorder 3
        mc "..."
        show natsuki 2bs at f22 zorder 3
        n "..."
        show natsuki 2bs at t22 zorder 3
        hide yuri at t21 zorder 1
        "Yuri runs off."
        "I'm still startled that she literally came over to my house!"
        "I wonder how long she was there for..."
        show natsuki 2bs at t11 zorder 3
        n "So you didn't invite her over or anything?"
        mc "No, I was just walking home and she was like waiting for me or something..."
        show natsuki 2bk at t11 zorder 3
        n "Okay, I believe you."
        mc "So, what brings {i}you{/i} here exactly?"
        show natsuki 2bl at t11 zorder 3
        n "I was just wondering if you wanted to hang out for today."
        mc "I guess so, come on in."
        show natsuki 2bz at t11 zorder 3
        n "Okay!"
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        scene bg:
            "mod_assets/kitchen.png"
        with wipeleft
        "Natsuki comes over to visit me sometimes, I guess you could say we've become good friends."
        "I mean, we both like manga, so that's probably why we hit it off so well."
        show natsuki 2bk at t11 zorder 3
        n "You always keep your kitchen nice and clean..."
        n "Mine is always dirty..."
        mc "Well, I kinda have to so my parents won't get mad."
        mc "So, what did you want to do?"
        show natsuki 2bz at t11 zorder 3
        n "Duh, let's read some manga."
        mc "I was kind of expecting you to make cupcakes or something, but we can read manga too."
        show natsuki 1bt at t11 zorder 3
        n "Its not like I'm your wife or anything..."
        "{i}(Wait, what?){/i}"
        n "Maybe later..."
        show natsuki 1bk at t11 zorder 3
        n "For now though, let's read some manga."
        mc "Okay."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        scene bg:
            "mod_assets/bedroom.png"
        with wipeleft
        "Me and Natsuki head upstairs to my bedroom."
        "I always kinda felt a little weird having a girl come in my room."
        show natsuki 2bl at t11 zorder 3
        n "Where's your manga collection again?"
        mc "It's in here, I'll get it."
        "I pick up a big box of all my manga."
        show natsuki 3bk at t11 zorder 3
        n "Is that all? I thought you had more."
        mc "I do, but it's not like we're reading all of them..."
        show natsuki 1bt at t11 zorder 3
        n "Good point."
        show natsuki 2bl at t11 zorder 3
        n "Let's see here..."
        "Natsuki searches through the box."
        "I'm not entirely sure what she's looking for, since she passed a few volumes of Parfait Girls to the side."
        mc "...Are you looking for something specific in there?"
        show natsuki 1bk at t11 zorder 3
        n "Not really, just looking at what books you got."
        mc "Well, thats a first..."
        "..."
        "It's been almost a whole minute, and Natsuki is still looking..."
        "She HAS to be looking for something."
        "Otherwise, she would of found something already."
        mc "Natsuki, let's just read some Parfait Girls."
        show natsuki 3bk at t11 zorder 3
        n "Yeah, okay."
        "Natsuki sits down on my bed, and I do the same."
        "I pick up one of the volumes for Parfait Girls and we start reading."
        show natsuki 2bl at t11 zorder 3
        n "It's been a while since I've read this book. I only remember a few things..."
        mc "How many volumes are there?"
        show natsuki 5bt at t11 zorder 3
        n "I think like fifty maybe?"
        n "I don't remember exactly how many there are..."
        n "But theres a lot, believe me."
        mc "I believe you."
        "A few minutes later, Natsuki gets up."
        show natsuki 3bl at t11 zorder 3
        n "Let's go make some cupcakes now."
        mc "Ah, yeah I forgot."
        mc "I can't believe you remembered."
        show natsuki 2bz at t11 zorder 3
        n "Ehehe~"
        scene bg:
            "mod_assets/kitchen.png"
        with wipeleft
        "We head back downstairs to the kitchen."
        "Natsuki's cupcakes are the best though."
        show natsuki 5bl at t11 zorder 3
        n "C'mon, let's bake some cupcakes!"
        mc "Yeah."
        "We get to work on baking cupcakes."
        "Its been a while since I've baked cupcakes actually..."
        "The last time I make cupcakes with Natsuki was like a few weeks ago for the festival."
        "That was fun."
        show natsuki 3bj at t11 zorder 3
        n "Hey [player], remember we made cupcakes for the festival?"
        mc "Yeah."
        n "I liked it, it was pretty fun."
        show natsuki 5bt at t11 zorder 3
        n "Although you were kinda slow..."
        mc "Well, not this time."
        mc "I think I'm better now."
        n "If you say so."
        "About ten minutes later, we have mostly everything ready."
        show natsuki 2bl at t11 zorder 3
        n "Time to put these bad boys in the oven!"
        mc "Yep."
        "Natsuki takes her baking seriously."
        "One slight mess up, and its game over."
        mc "While we wait for the cupcakes, let's keep reading Parfait Girls."
        show natsuki 2bk at t11 zorder 3
        n "Can you bring it down here?"
        mc "Eh? Why?"
        n "So we can watch the cupcakes, make sure that they're actually gonna turn into cupcakes."
        mc "Guess so, I'll go get the book."
        show natsuki 2bz at t11 zorder 3
        n "Okay!"
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        scene bg:
            "mod_assets/bedroom.png"
        with wipeleft
        "I go upstairs to my room, and grab the book."
        "But before I start heading back down, I notice something strange."
        mc "Huh?"
        "One of my pens are gone."
        "I usually have a few up here in my room if I ever lost one."
        "You know, like extras."
        "I don't think Natsuki could of taken it, so who did?"
        "I decided to brush it off since it didn't really matter that much."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        scene bg:
            "mod_assets/kitchen.png"
        with wipeleft
        "I come back down to see Natsuki watching the cupcakes bake in the oven."
        mc "I'm back."
        show natsuki 3bl at t11 zorder 3
        n "Okay, these cupcakes look like they're almost done too!"
        "That fast?"
        mc "I got the book, let's continue from where we left off."
        n "Sounds good."
        "After a few minutes later, I decide to ask Natsuki if she stole my pen."
        mc "Hey, Natsuki?"
        show natsuki 1bk at t11 zorder 3
        n "Yeah [player]?"
        mc "This might be a silly question but..."
        mc "Did you take one of my pens by any chance?"
        show natsuki 5bm at t11 zorder 3
        n "Why would I want one of your pens?"
        mc "Good question, forget what I asked."
        show natsuki 5bk at t11 zorder 3
        n "I know Yuri likes pens though..."
        mc "Yuri?"
        n "Yeah, she has this weird addiction to pens..."
        n "Maybe she stole your pen perhaps?"
        mc "Maybe..."
        show natsuki 3bk at t11 zorder 3
        n "I knew Yuri was gonna be one of those weird people the second I met her."
        mc "Hah..."
        show natsuki 2bo at t11 zorder 3
        n "What's so funny?"
        mc "Nothing, it's just what you said about Yuri."
        show natsuki 3bt at t11 zorder 3
        n "She's been acting a little weird today, have you noticed?"
        mc "Yeah, I've noticed it too..."
        "Suddenly, the oven beeps."
        show natsuki 3bz at t11 zorder 3
        n "The cupcakes are done!"
        mc "Alright."
        "Natsuki opens the oven door and a blast of sweet-smelling cupcakes fill the room."
        "I'm already feelng proud of the work we've done."
        show natsuki 3bl at t11 zorder 3
        n "Now the last step is icing!"
        show natsuki 3bk at t11 zorder 3
        n "Do you still have any icing left over from the festival?"
        mc "Yeah, I think so."
        "I had the icing in a big bowl last time, so I put it in the fridge if I ever wanted to use it..."
        "I take out the icing and show Natsuki."
        mc "Will this do?"
        n "Here, let me see..."
        "Natsuki dips her finger in the icing and tastes it."
        n "It still tastes good."
        mc "Alright, let's use it then."
        "We start adding the icing on the cupcakes."
        "These cupcakes are already starting looking great!"
        show natsuki 3bl at t11 zorder 3
        n "Done!"
        mc "Uwa--"
        mc "Already?"
        mc "I only put icing on two cupcakes so far!"
        show natsuki 1bz at t11 zorder 3
        n "I'm pretty quick, you know."
        mc "You've done this before, so your used to it."
        show natsuki 5bt at t11 zorder 3
        n "True..."
        "We finish making the cupcakes."
        "And they look amazing."
        mc "We did it, and they look awesome!"
        show natsuki 1bz at t11 zorder 3
        n "I know right!?"
        "Natsuki looks really happy right now."
        "She does look cute in that outfit she wears."
        show natsuki 2bl at t11 zorder 3
        n "C'mon [player], what are you waiting for?"
        n "Go ahead and take one!"
        "Natsuki takes a cupcake, and eats it."
        "I also take one, and take a big bite out of it."
        "It's delicious."
        mc "We make a great team."
        show natsuki 5bt at t11 zorder 3
        n "I guess you could say that."
        show natsuki 4bl at t11 zorder 3
        n "Can we continue reading too?"
        mc "Yeah, sure."
        "We keep reading Parfait Girls for about an hour, while eating the cupcakes we made."
        show natsuki 3bz at t11 zorder 3
        "Natsuki kept pointing out hilarious moments in the book."
        "I enjoy the book as much as she does."
        "I decide to check the time on my clock."
        "...Almost 6 PM?"
        "Natsuki hasn't left yet."
        "Not that I have a problem with her staying over, but surely her parents would be worried about her... right?"
        mc "Hey Natsuki, it's almost 6 PM..."
        show natsuki 5bk at t11 zorder 3
        n "...And?"
        mc "No offence, but are you leaving anytime soon?"
        mc "I wouldn't mind if you stayed a bit longer. I'm enjoying this..."
        show natsuki 1bt at t11 zorder 3
        n "Well, um..."
        show natsuki 1bu at t11 zorder 3
        n "..."
        "Something tells me that she wants to stay here."
        mc "I'm taking that as a no?"
        show natsuki 5bk at t11 zorder 3
        n "Well, is it okay if I stay here for the night?"
        "Is she serious!?"
        "Either I'm mishearing it, or Natsuki wants to stay for the night."
        mc "Um..."
        show natsuki 5bm at t11 zorder 3
        n "...It's a 'no', right?"
        mc "No no, you're more then welcome to stay here for the night."
        mc "I don't mind..."
        show natsuki 1bl at t11 zorder 3
        n "You mean it!?"
        mc "Yeah, I wouldn't lie to you Natsuki."
        show natsuki 1bl at h11 zorder 3
        n "Thank you!"
        "Natsuki gave me a really tight hug."
        "...That's a first."
        "Normally, she's always moody and stuff."
        "But I appriciate her."
        mc "So, are you sure your father is okay with it?"
        show natsuki 5bm at t11 zorder 3
        n "My father should be okay with it..."
        "I know that Natsuki's father abuses her sometimes."
        "So I can really understand why she wants to stay here..."
        "Just to get away from those sort of things."
        mc "So..."
        show natsuki 5bk at t11 zorder 3
        n "...?"
        mc "Anyways..."
        mc "What do you want to do then?"
        mc "I'm sure you want to do other things besides reading manga and baking all day..."
        show natsuki 5bt at t11 zorder 3
        n "Well..."
        n "I do like watching anime..."
        mc "I have a few anime movies we can watch then."
        show natsuki 2bl at t11 zorder 3
        n "Hey, you do?"
        mc "Yep."
        n "What are we waiting for? Let's go!"
        mc "Okay, okay..."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        scene bg:
            "mod_assets/bedroom.png"
        with wipeleft
        
        "I don't have a lot of anime movies really."
        "But they're all good ones that I've watched."
        show natsuki 3bl at t11 zorder 3
        n "Let me see! Let me see!"
        mc "You seem pretty excited about watching a anime movie."
        n "I love anime movies!"
        mc "Go take a look."
        mc "I don't have that many, but there's probably one there you will like."
        "Natsuki starts looking at the movies I have."
        "To my surprise, she finds one that interests her."
        n "This one!"
        n "Can we watch it?"
        mc "Sure."
        hide natsuki at tl11 zorder 1
        "I swear, it's almost like Natsuki turned into Sayori a little bit."
        "I put the movie in my DVD Player, and I lie down on my bed."
        "Natsuki lies down beside me."
        "A little weird... But it doesn't bother me."
        "Natsuki seems to be enjoying the movie so far."
        "I am too."
        "I really hope her father doesn't call the police or something..."
        "..."
        "While I was distracted watching the movie, I look over at Natsuki and see that she actually fell asleep."
        "Man, she looks really cute."
        "I checked the time and its' almost 10 PM."
        "Wow, a lot has happened today."
        "Should I wake her up?"
        "It feels right."
        "I poke her cheek."
        mc "Hey, Natsuki?"
        show natsuki 2bm at t11 zorder 3
        n "Hmm?"
        "She looks very tired."
        mc "Its almost 10 PM."
        n "Oh."
        show natsuki 2bk at t11 zorder 3
        n "Do you have a spare bed perhaps?"
        mc "Yeah, I have a guest room you can use."
        show natsuki 2bl at t11 zorder 3
        n "Thanks."
        hide natsuki
        "Natsuki leaves my room and finds the guest room."
        "Well, I guess I should go to bed then."
        "I turn off the TV and the DVD Player."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        stop music fadeout 2.0
        pause 1
        "I turn off the lights, close my door, and go to bed."
        "I begin to close my eyes and sleep."
        pause 3
        "But then I hear knocking at my door."
        mc "Come in."
        scene bg:
            "mod_assets/bedroom_dark.png"
        with wipeleft
        show natsuki 12bf at t11 zorder 3
        n "{i}*sob*{/i}"
        show natsuki 12bi at t11 zorder 3
        n "...[player]?"
        mc "Natsuki?"
        mc "What's wrong?"
        n "I... I can't sleep..."
        n "Can I sleep with you?"
        "This got kinky real quick."
        mc "Yeah, sure."
        show natsuki 4bu at t11 zorder 3
        n "{i}*sniff*{/i}Thanks..."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        "I make some space for Natsuki, and she gets in my bed."
        "This feels even more weird!"
        "Next thing I know, I can feel her arms around me."
        "She also stopped crying after she got in my bed."
        "I wonder what she's crying about..."
        "I sigh, and just go to sleep."
        pause 5
        scene bg:
            "mod_assets/bedroom.png"
        with wipeleft
        "I wake up, and Natsuki's arms are still around me."
        "I hope she was able to get some sleep..."
        "But I feel like I'm being watched..."
        "Eh, I'm sure it's nothing."
        "I turn my head to look at Natsuki."
        mc "She's just so cute..."
        "I poke her cheek."
        n "Hold on, Dad!"
        "Did she just say 'dad'?"
        mc "Uuh... Natsuki, it's me...[player]."
        "Her eyes slowly open."
        play music t2
        show natsuki 1bp at t11 zorder 3
        n "...[player]!?"
        show natsuki 1bo at t11 zorder 3
        n "What are you doing in my bed!?"
        mc "Natsuki, it's my bed, you came to my room and ask if you could sleep with me."
        show natsuki 1bk at t11 zorder 3
        n "Oh yeah, I remember now..."
        "I check the time..."
        "It's 7 AM, School starts in an hour."
        mc "We better get ready for school."
        show natsuki 1bj at t11 zorder 3
        n "Yeah, can I use your shower?"
        mc "Go ahead, I won't peak at you."
        show natsuki 5bu at t11 zorder 3
        n "I wouldn't mind."
        "...She has to be joking me."
        mc "Yeah, I'm not falling for that."
        mc "You'll punch me or something if I actually did."
        mc "And...uh..."
        show natsuki 5bn at t11 zorder 3
        "Natsuki gives me this serious look."
        "Still, even if she didn't mind, I should give her privacy."
        "Its the least I could do."
        mc "Anyways, let's get ready."
        show natsuki 5bj at t11 zorder 3
        n "Yeah."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        scene bg:
            "mod_assets/kitchen.png"
        with wipeleft
        "I decided to make breakfast for Natsuki and I before we go to school."
        "I'll just make some scrambled eggs and bacon."
        "It's something quick and easy to make on school days anyway."
        "Later, Natsuki comes down the stairs."
        show natsuki 1bl at t11 zorder 3
        n "Hey [player]."
        mc "Hi Natsuki."
        show natsuki 1bk at t11 zorder 3
        n "I'm done taking my shower."
        mc "That was quick."
        show natsuki 1bl at t11 zorder 3
        n "What are you making?"
        mc "I'm making breakfast, for both of us."
        show natsuki 1bm at t11 zorder 3
        n "B-Both?"
        mc "Yeah..."
        mc "...There's nothing wrong with that, is there?"
        show natsuki 1bn at t11 zorder 3
        n "No, it's just..."
        show natsuki 5bn at t11 zorder 3
        n "Very...nice of you to do that for me."
        mc "You're welcome."
        show natsuki 12bb at t11 zorder 3
        n "My father rarely cooks any food for me now-a-days."
        mc "Huh?"
        show natsuki 12ba at t11 zorder 3
        n "And I'm just really happy that you care about me."
        mc "No problem Natsuki."
        "Her father sounds like a jerk."
        "Life isn't fair sometimes, I guess."
        mc "Here Natsuki, go sit down at the table."
        show natsuki 5bu at t11 zorder 3
        n "O-Okay..."
        "I finish making breakfast and I serve a plate of scrambled eggs and bacon to Natsuki."
        mc "Here."
        show natsuki 1bl at t11 zorder 3
        n "Thanks [player], it means a lot to me."
        mc "Oh, do you want a drink too?"
        show natsuki 1bk at t11 zorder 3
        n "I'm good, thanks though."
        mc "Alright."
        "I serve myself a plate of scrambled eggs and bacon."
        "Man, I'm pretty good at making this."
        "Once me and Natsuki finish eating, we get ready to go to school."
        show natsuki 4bl at t11 zorder 3
        n "Alright, lets get going..."
        mc "Wait, what about your uniform?"
        show natsuki 5bt at t11 zorder 3
        n "I'll just go back to my house and get it."
        mc "Ah, okay."
        mc "Well, Let's get going."
        show natsuki 2bj at t11 zorder 3
        n "Yep."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        scene bg:
            "mod_assets/residential.png"
        with wipeleft
        "And just like that, me and Natsuki start walking to school."
        "It feels so weird walking to school with someone else besides Sayori."
        show sayori 2a at t11 zorder 3
        s "Hi [player]!~"
        mc "Oh, hey Sayori."
        "Speak of the devil, Its Sayori."
        show sayori 2m at t11 zorder 3
        s "Natsuki? What are you doing here?"
        show sayori 2m at t22
        show natsuki 4bz at f21 zorder 3
        n "Ehehe..."
        show natsuki 4bz at t21 zorder 3
        show sayori 4b at f22 zorder 3
        s "Did you two spend the night or something?"
        show sayori 4b at t22 zorder 3
        mc "Uhh..."
        show natsuki 5bl at f21 zorder 3
        n "Yeah, I went to [player]'s place."
        show natsuki 5bl at t21 zorder 3
        show sayori 4p at f22 zorder 3
        s "Ahh! I'm jealous!"
        show sayori 4h at f22 zorder 3
        s "Well, at least you two weren't sleeping together or anything."
        show sayori 4h at t22 zorder 3
        mc "..."
        show natsuki 5bt at f21 zorder 3
        n "..."
        show natsuki 5bt at t21 zorder 3
        "Me and Natsuki decided to not tell Sayori that we slept together."
        "I think Sayori would of freaked out anyway."
        show natsuki 1bl at f21 zorder 3
        n "I'm gonna head back to my house and change to my school outfit, okay?"
        show natsuki 1bl at t21 zorder 3
        mc "Okay."
        show sayori 3x at f22 zorder 3
        s "Okay Natsuki, we'll see you at school!"
        show sayori 3x at f22 zorder 3
        hide natsuki
        "Natsuki runs off."
        "Me and Sayori keep walking to school."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        scene bg:
            "mod_assets/club.png"
        with wipeleft
        show sayori 4x at l31 zorder 3
        s "It feels good to be back!"
        mc "Yeah, I guess."
        show monika 1b at f32 zorder 3
        m "[player]! Welcome back!"
        show monika 1b at t32 zorder 3
        mc "Thanks Monika."
        show natsuki 4z at l33 zorder 3
        n "Hey Monika!"
        show monika 2b at f32 zorder 3
        m "Hi Natsuki."
        show monika 2b at f32 zorder 3
        m "Did you do anything 'fun' yesterday?"
        show monika 2b at t32 zorder 3
        show natsuki 5l at f33 zorder 3
        n "I went to [player]'s house."
        show natsuki 5l at t33 zorder 3
        show monika 3l at f32 zorder 3
        m "Really? I'm jealous!."
        show monika 3l at t32 zorder 3
        "I wonder if Yuri is here too."
        "I don't see her anywhere in the room."
        mc "Where's Yuri?"
        show monika 2d at f32 zorder 3
        m "Yuri?"
        show monika 2d at t32 zorder 3
        "Monika looks around."
        show monika 2d at f32 zorder 3
        m "I have no idea where she is..."
        show monika 2d at t32 zorder 3
        mc "That's odd..."
        show sayori 4h at f31 zorder 3
        s "Maybe she's sick today?"
        show sayori 4h at t31 zorder 3
        mc "Maybe..."
        "Suddenly, the doors open."
        show sayori 4h at t41 zorder 1
        show monika 2d at t42 zorder 3
        show natsuki 5l at t43 zorder 2
        show yuri 3n at l44 zorder 4
        y "Sorry I'm late!"
        show yuri 3n at t44 zorder 4
        show natsuki 1b at f43 zorder 3
        m "You're not late Yuri, don't be so paranoid."
        show natsuki 1b at t43 zorder 3
        show yuri 2f at f44 zorder 4
        y "I'm not?"
        show yuri 2f at t44 zorder 4
        mc "Yeah, we just got here too."
        show monika 5a at f42 zorder 3
        m "I was first one here."
        show monika 5a at t42 zorder 3
        show sayori 2r at f41 zorder 3
        s "Yay! Yuri's okay!"
        show sayori 2r at t41 zorder 3
        show yuri 2h at f44 zorder 4
        y "Natsuki, you seem cheerful today."
        show yuri 2h at t44 zorder 4
        show natsuki 2k at f43 zorder 3
        m "Yeah, and?"
        show natsuki 2k at t43 zorder 3
        show yuri 2h at f44 zorder 4
        y "I was just wondering, since you're always moody."
        show yuri 2h at t44 zorder 4
        show monika 3a at f42 zorder 4
        m "Let's all share our poems now, shall we?"
        show monika 3a at t42 zorder 4
        "Ah dangit, I forgot to write one yesterday..."
        "Maybe I can write a quick one with a piece of scrap paper?"
        hide sayori 4h at t41 zorder 1
        hide monika 2d at t42 zorder 3
        show natsuki 5u at t11 zorder 2
        hide yuri 3n at f44 zorder 4
        "Sayori, Monika, and Yuri get their poems out of their bags."
        "Me and Natsuki haven't wrote anything."
        show natsuki 2k at t11 zorder 2
        n "We forgot to write a poem last night..."
        show natsuki 2k at t11 zorder 2
        mc "Yeah, maybe we can write a quick one on like a piece of scrap paper?"
        show natsuki 1l at t11 zorder 2
        n "Good thinking!"
        show natsuki 1l at t11 zorder 2
        "Natsuki finds a pencil and a piece of paper."
        "I should go write a poem too."
        scene bg:
            "mod_assets/blackness.png"
        with wipeleft
        pause 3
        scene bg:
            "mod_assets/club.png"
        with wipeleft
        play music t6
        "Well, me and Natsuki managed to write a poem."
        "Luckily, no one noticed that we forgot to write a poem today."
        show natsuki 1l at t11 zorder 2
        n "I'm glad that's all over with..."
        show natsuki 1l at t11 zorder 2
        mc "Yeah, same..."
        mc "Did you want to do something Natsuki?"
        show natsuki 1k at t11 zorder 2
        n "I don't know, you could go hang out with Yuri."
        show natsuki 1k at t11 zorder 2
        mc "I guess so."
        mc "Well, you know where to find me if you need anything."
        show natsuki 1l at t11 zorder 2
        n "Alright."
        show natsuki 1l at t21 zorder 2
        show yuri 1d at f22 zorder 2
        y "Hey [player]!"
        show yuri 1d at t22 zorder 2
        mc "Hi Yuri."
        show yuri 1c at f22 zorder 2
        y "Did you want to hang out today?"
        show yuri 1c at t22 zorder 2
        mc "Sure, I guess."
        "Me and Yuri sit on the floor, with our backs up against the wall."
        "Its been a while since I've hanged out with Yuri..."
        show yuri 1d at f22 zorder 3
        y "Let's start reading!"
        mc "Okay."
        scene bg:
            "mod_assets/CaptureYuriR4.png"
        with fade
        "Me and Yuri begin reading."
        "Well, she has the book, and I'm just reading it from where she has it."
        "I remember that I had a bag of chocolates with me."
        "I take out the bag of chocolates."
        mc "Hey, Yuri."
        scene bg:
            "mod_assets/CaptureYuriR10.png"
        y "Yeah?"
        mc "Do you want some chocolate?"
        y "Ah, no thanks."
        mc "Why not?"
        y "If I touch the chocolate, I might get smudges on the pages."
        mc "Oh yeah, right."
        mc "I forgot about that."
        mc "My bad..."
        y "No need to apologize."
        scene bg:
            "mod_assets/CaptureYuriR4.png"
        "We keep reading for a while."
        "I take a chocolate and pop it in my mouth."
        "Man, these are really good."
        menu:
            
            "Should I give one to Yuri?"
            "Give Yuri a chocolate.":
                jump give_chocolate
            "Don't give Yuri a chocolate.":
                jump ungive_chocolate

label ungive_chocolate:
    "She's right, it will get smudges on the pages anyway..."
    "After a few minutes of reading, Yuri asks me a question."
    scene bg:
        "mod_assets/CaptureYuriR10.png"
    y "Hey, [player]?"
    mc "Yes Yuri?"
    y "I know it's none of my buissness but..."
    y "What did you and Natsuki do yesterday?"
    "I mean, I should probably just tell her the truth."
    mc "We just read manga together."
    mc "And made some cupcakes too."
    y "Ah, sounds like fun."
    y "I wish I was there too."
    mc "You were, silly."
    mc "You just left."
    y "Oh yeah..."
    y "I must of forgotten that or something..."
    y "Sorry."
    mc "No no, it's okay."
    scene bg:
        "mod_assets/CaptureYuriR4.png"
    "Yuri continues reading."
    "Is it just me, or does Yuri apologize too much?"
    "Its not really a 'bad' thing, it's just something she does too often."
    show bg:
        "mod_assets/club.png"
    show natsuki 1l at t11 zorder 3
    n "Hey [player] and Yuri!"
    mc "Oh, hey Natsuki."
    show natsuki 1l at t21 zorder 3
    show yuri 3h at f22 zorder 3
    y "Hi Natsuki."
    show yuri 3h at t22 zorder 3
label natsuki_inter:
    show natsuki 1k at f21 zorder 3
    n "What are you guys reading?"
    show natsuki 1k at t21 zorder 3
    show yuri 2f at f22 zorder 3
    y "Portrait of Markov..."
    show yuri 2f at t22 zorder 3
    show natsuki 4k at f21 zorder 3
    n "I never heard of it before..."
    n "Is it a new book or something?"
    show natsuki 4k at t21 zorder 3
    show yuri 2o at f22 zorder 3
    y "N-No, not really..."
    show yuri 2o at t22 zorder 3
    show natsuki 1l at f21 zorder 3
    n "Hey, can I read with you guys?"
    n "I'm bored just sitting around."
    show natsuki 1l at t21 zorder 3
    show yuri 2p at f22 zorder 3
    y "A-Ah, uhh..."
    show yuri 2p at t22 zorder 3
    mc "Yeah sure--"
    show yuri 2r at f22 zorder 3
    y "No!"
    y "She can't!"
    show yuri 2r at t22 zorder 3
    mc "Huh?"
    show natsuki 3k at f21 zorder 3
    n "Why not, Yuri?"
    show natsuki 3k at t21 zorder 3
    show yuri 2o at f22 zorder 3
    y "B-Because..."
    show yuri 3f at f22 zorder 3
    y "...It's something she wouldn't like!"
    y "Yeah..."
    show yuri 3f at t22 zorder 3
    mc "..."
    show natsuki 3s at f21 zorder 3
    n "..."
    show natsuki 3s at t21 zorder 3
    "Something tells me that Yuri only wants to read with me."
    show natsuki 3l at f21 zorder 3
    n "Okay well..."
    n "Once you guys are done reading, can I spend some time with [player]?"
    show natsuki 3l at t21 zorder 3
    show yuri 1r at f22 zorder 3
    y "No!"
    show yuri 1r at t22 zorder 3
    show natsuki 3o at f21 zorder 3
    n "Nn--!"
    show natsuki 3o at t21 zorder 3
    mc "Yuri..."
    show yuri 2o at f22 zorder 3
    y "Um... I mean..."
    y "Yeah, sure..."
    show yuri 2o at t22 zorder 3
    show natsuki 3i at f21 zorder 3
    n "You better not steal him..."
    show natsuki 3i at t21 zorder 3
    show yuri 3f at f22 zorder 3
    y "O-Of course not!"
    y "I wouldn't do that..."
    show yuri 3f at t22 zorder 3
    "That seems really sarcastic coming from Yuri."
    "I don't know if I should be scared or..."
    show natsuki 2k at f21 zorder 3
    n "I'll wait for you two to be done reading then..."
    show natsuki 2k at t21 zorder 3
    mc "Okay."
    scene bg:
        "mod_assets/blackness.png"
    with wipeleft
    pause 2
    scene bg:
        "mod_assets/club.png"
    with wipeleft
    "I wonder how long me and Yuri are gonna read."
    "It's been an hour so far."
    "I barely got to spend time with anyone but Yuri today."
    show natsuki 3l at f21 zorder 3
    n "Hey, can I hang out with [player] now?"
    show natsuki 3l at t21 zorder 3
    show yuri 1r at f22 zorder 3
    y "N-No!"
    y "Go away, Natsuki!"
    show yuri 1r at t22 zorder 3
    show natsuki 3o at f21 zorder 3
    n "--!"
    show natsuki 3o at t21 zorder 3
    mc "Yuri, don't be rude."
    show yuri 3o at f22 zorder 3
    y "I-I didn't realize!"
    show yuri 4b at f22 zorder 3
    y "I'm sorry Natsuki."
    y "You two can hang out now..."
    show yuri 4b at t22 zorder 3
    show natsuki 1z at f21 zorder 3
    n "Yay!"
    show natsuki 1z at f21 zorder 3
    n "C'mon, [player]!"
    show natsuki 1z at t21 zorder 3
    "I kinda feel bad for Yuri after seeing her sad face..."
    mc "It's okay Yuri, we can always do this tomorrow you know."
    show yuri 4a at f22 zorder 3
    y "Y-Yeah, you're right..."
    show yuri 4a at t22 zorder 3
    mc "Yeah..."
    mc "So, don't be sad."
    show yuri 3a at f22 zorder 3
    y "I'll see you tomorrow then, [player]..."
    show yuri 3a at t22 zorder 3
    mc "Okay Yuri."
    show yuri 3c at f22 zorder 3
    y "Bye."
    show yuri 3c at t22 zorder 1
    hide yuri 3c at t22 zorder 1
    play music t6
    show natsuki 3j at t11 zorder 3
    n "So, want to read Parfait Girls, [player]?"
    mc "Yep."
    n "Okay, but we'll have to go get them from the closet."
    mc "Okay."
    scene bg:
        "mod_assets/closet.png"
    with wipeleft
    show natsuki 1l at t11 zorder 3
    n "Let's see here..."
    show natsuki 1o at h11 zorder 3
    n "Nn--!"
    mc "What's wrong?"
    "The manga collection is on the top shelf."
    show natsuki 1v at h11 zorder 3
    n "Monika!!"
    n "Why did you move my manga collection again!?"
    show natsuki 1v at t22 zorder 3
    show monika 3l at l21 zorder 3
    show monika 3l at f21 zorder 3
    m "Ah, yeah..."
    m "The teacher complained about it, so I moved it up."
    m "But it should all be organized still!"
    show monika 3l at l21 zorder 1
    hide monika 3l at l21 zorder 1
    show natsuki 1s at t11 zorder 3
    "Natsuki tries hopping up to reach the top of the bookshelf."
    mc "Natsuki, let me get it..."
    show natsuki 1k at t11 zorder 3
    n "It's fine, I got it."
    "Natsuki can be really stubborn sometimes."
    "But I can understand that."
    "I see a bendable stool that Natsuki could use."
    "It looks very withered, like it could fall apart at any minute."
    "I pick up the stool, and show Natsuki."
    mc "Here, Natsuki."
    mc "Use this..."
    show natsuki 1l at t11 zorder 3
    n "Oh, thanks [player]."
    n "I should be able to get it now..."
    "Natsuki sets up the stool against the bookshelf."
    "She stands ontop of it, but she's just a little too short to reach the books still."
    show natsuki 1f at t11 zorder 3
    n "Aw, why can't nothing be easy?"
    n "I know what I could use."
    mc "What?"
    hide natsuki
    "Natsuki trots over to the teacher's desk, which has a computer chair behind it."
    "She rolls it on its wheels back over to the closet."
    show natsuki 4a at t11 zorder 3
    mc "Ah--"
    "It's a little dangerous, since the chair swivels and rolls."
    "But I've already learned my lesson, so I keep my mouth shut."
    show natsuki 1a at t11 zorder 3
    n "Ush--"
    "Natsuki climbs onto the chair, then slowly balances onto her feet."
    "Since she refuses my help, I take a seat with my back against the side of the doorway and simply watch."
    scene bg:
        "mod_assets/CaptureNatsukiR5.png"
    n "Aha! There we go!"
    n "See? I can easily do it now."
    "Natsuki grabs a stack of manga and bends down to put it on the shelf below."
    n "W-Wahh--"
    "The chair swivels."
    "Natsuki catches herself on the shelf."
    scene bg:
        "mod_assets/CaptureNatsukiR6.png"
    n "What are you doing??"
    n "Can you atleast hold the chair steady instead of sitting and doing nothing?"
    "{i}(Who was it that told me not to help...?){/i}"
    mc "Yeah, yeah...I got you."
    scene bg:
        "mod_assets/CaptureNatsukiR5.png"
    "I hold the chair while Natsuki reaches back up."
    mc "--!"
    "I can..."
    "{i}I can almost see up her skirt!?{/i}"
    mc "Guh--"
    "I force myself to turn away."
    "Natsuki seriously didn't think this through...!"
    "I mean, we're good friends, surely she wouldn't get mad...right?"
    n "Hup--"
    "Natsuki wraps her arms around the Parfait Girls box set, easily the largest one on the shelf."
    n "Uu...heavy..."
    scene bg:
        "mod_assets/CaptureNatsukiR6.png"
    n "Hey, [player]..."
    n "I-I don't think I can bend down without falling...!"
    n "Hurry and take this one..."
    mc "Eh?"
    mc "But then I have to let go of the chair..."
    n "That's fine...!"
    n "Just for a second!"
    n "Hurry up..."
    mc "Alright...!"
    mc "Let me just stand up."
    "I slowly release my grip from the chair."
    n "What do you mean 'stand up'?"
    "Natsuki looks down at me."    
    n "Why are you all the way back--"
    stop music fadeout 2.0
    n "E-Eh...?"
    "Natsuki looks like she just realized something, but she'll lose her balance if she moves."
    mc "Natsuki, the box--"
    scene bg:
        "mod_assets/CaptureNatsukiR13.png"
    n "[player]..."
    n "W-Why are you trying to look at my...my..."
    mc "N-No! I-I'm not!"
    n "Y-You are..."
    mc "Natsuki, I swear, I'm not looking up at your--"
    n "[player]..."
    "Natsuki is actually blushing, rather then being angry..."
    mc "Give me the box, Natsuki."
    n "Y-Yeah, here..."
    "Natsuki gives me the box, and I take it from her hands."
    "I put the box along with the other ones Natsuki set up."
    mc "There."
    scene bg:
        "mod_assets/closet.png"
    "All of the manga boxes are back where they were before."
    "Man, maybe next time I should move the boxes..."
    show natsuki 1s at t11 zorder 3
    n "T-Thanks..."
    mc "No problem, Natsuki."
    show natsuki 1i at t11 zorder 3
    n "Hey...[player]...?"
    mc "Yes, Natsuki?"
    show natsuki 1s at t11 zorder 3
    "It looks like she wants to say something, but she's struggling to say it."
    mc "...?"
    show natsuki 1i at t11 zorder 3
    n "[player], do you love--"
    show natsuki 1i at t22 zorder 3
    show monika 3a at l21 zorder 3
    m "Hey Natsuki, can I hang out with [player] now?"
    show monika 3a at t21 zorder 3
    show natsuki 1o at t22 zorder 3
    n "M-Monika!!"
    n "N-No! Not yet!"
    show natsuki 1o at t22 zorder 3
    show monika 1g at f21 zorder 3
    m "Natsuki, please?"
    show monika 1g at t21 zorder 3
    show natsuki 5r at t22 zorder 3
    n "Ugh!"
    n "We barely did anything yet!"
    show natsuki 5r at t22 zorder 3
    show monika 1g at f21 zorder 3
    m "It's only fair, Natsuki..."
    show monika 1g at t21 zorder 3
    show natsuki 1p at t22 zorder 3
    n "This is bullshit!"
    n "Why does Yuri get an hour with [player], but I only get like five minutes!?"
    show natsuki 1p at t22 zorder 3
    show monika 1i at f21 zorder 3
    m "Huh?"
    m "Yuri spent an hour with [player]?"
    show monika 1i at t21 zorder 3
    mc "Yeah, we did..."
    "I mean, I could of asked at anytime..."
    show natsuki 1s at f22 zorder 3
    n "I think Yuri is trying to steal him, Monika."
    show natsuki 1s at t32 zorder 3
    show monika 1i at t31 zorder 3
    play music t7
    show yuri 3p at f33 zorder 3
    y "N-No! That's not true!"
    y "I wouldn't steal [player]..."
    show yuri 3r at f33 zorder 3
    y "Maybe you're just jealous that [player] likes to hang out with me more!"
    show yuri 3r at t33 zorder 3
    show natsuki 1o at f32 zorder 3
    n "And how do {i}you{/i} know he doesn't like hanging with {i}me{/i} more, huh?"
    show natsuki 1o at t32 zorder 3
    show yuri 3c at f33 zorder 3
    y "Simple, he was reading along with me."
    y "I bet he liked it more then reading with a bratty person like you."
    show yuri 3c at t33 zorder 3
    show natsuki 4o at f32 zorder 3
    n "Well, look who's talking, you wannabe edgy bitch!"
    show natsuki 4o at t32 zorder 3
    show yuri 2f at f33 zorder 3
    y "Edgy...?"
    show yuri 2r at f33 zorder 3
    y "Sorry that my lifestyle is too much for someone of your mental age to comprehend!"
    y "You think you can counterbalance your toxic personality just by dressing and acting cute?"
    show yuri 1k at f33 zorder 3
    y "The only thing cute about you is how hard you try."
    show yuri 1k at t33 zorder 3
    show natsuki 2y at f32 zorder 3
    n "Woah, be careful or you might cut yourself on that edge, Yuri."
    n "Oh, my bad... You already do, don't you?"
    show natsuki 2y at t32 zorder 3
    show yuri 3n at f33 zorder 3
    y "D-Did you just accuse me of cutting myself??"
    show yuri 3r at f33 zorder 3
    y "What the fuck is wrong with your head?!"
    show yuri 3r at t33 zorder 3
    show natsuki 1e at f32 zorder 3
    n "Yeah, go on!"
    n "Let [player] hear everything you really think!"
    n "I'm sure he'll be head over heels for you after this!"
    show natsuki 1e at t32 zorder 3
    show yuri 3n at f33 zorder 3
    y "A-Ah--!"
    show yuri 3n at t33 zorder 3
    "Suddenly, Yuri turns towards me, as if she just noticed I was standing here."
    show yuri 3n at f33 zorder 3
    y "[player]...!"
    y "She--She's just trying to make me look bad...!"
    show yuri 3n at t33 zorder 3
    show natsuki 4w at f32 zorder 3
    n "That's not true!"
    n "She started it!"
    show natsuki 1g at t32 zorder 3
    show yuri 1t at t33 zorder 3
    mc "..."
    "This is gonna be a tough choice..."
    "I got to pick between Natsuki, or Yuri..."
    
    menu:
        
        "So I'll pick...!"

        "Natsuki.":
            jump natsuki_love
        "Yuri.":
            jump yuri_nlove
        "Help me, Monika!":
            jump monika_help
            
label monika_help:
    stop music fadeout 2.0
    mc "..."
    mc "...Monika!"
    show monika 1c at f31 zorder 3
    m "...?"
    show monika 1c at t31 zorder 3
    mc "This whole fight is making Monika worried."
    mc "How could you two keep up this fight knowing your friend is worried?"
    show monika 2f at f31 zorder 3
    m "Like, why are we fighting again in the first place?"
    m "Just to prove who [player] likes to spend time with the most?"
    m "The answer to that is..."
    m "Everyone."
    m "Not just focused on one person, like Natsuki..."
    show natsuki 1o at t32 zorder 3
    m "He cares about everyone else."
    show natsuki 1q at t32 zorder 3
    m "So, let's stop fighting..."
    m "Let's be friends instead..."
    show monika 2f at t31 zorder 3
    show yuri 3o at s33 zorder 3
    y "..."
    y "Uum..."
    show natsuki 5r at s32 zorder 3
    n "..."
    n "I..."
    "Looks like Monika saves the day..."
    show yuri 3o at f33 zorder 3
    y "I'll go make some tea then..."
    hide yuri t
    pause 1
    show natsuki 2n at f22 zorder 3
    n "Can we read some manga then, [player]?"
    show natsuki 2n at t22 zorder 3
    mc "How could I say 'no' to that?"
    show natsuki 1z at hf22 zorder 3
    n "Ehehe~"
    show natsuki 1z at t22 zorder 3
    show monika 2b at f21 zorder 3
    m "Have fun, you too!"
    hide monika
    show natsuki 1l at f11 zorder 3
    n "Let's keep reading then!"
    mc "Alright."
    
    return
    
label yuri_nlove:
    stop music fadeout 2.0
    mc "..."
    mc "...Yuri."
    show yuri 3d at f33 zorder 3
    y "Ahahaha..."
    y "I proved you wrong, Natsuki."
    show yuri 3y5 at f33 zorder 3
    y "Are you gonna go cry about it now?"
    show yuri 3y4 at f33 zorder 3
    y "Don't worry, nobody would care if you killed yourself."
    y "Go ahead, make it a slow painful death."
    y "Either by a stab wound and slowly bleeding..."
    y "Or slowly suffocating yourself..."
    y "One of those options would make your death more reluctant..."
    show yuri 3y3 at f33 zorder 3
    y "So why are you still here?"
    show yuri 3y1 at f33 zorder 3
    y "Just fucking kill yourself already!"
    show yuri 3y4 at f33 zorder 3
    y "It would be a shame if no one attended your funeral..."
    y "Oh, that's because no one is going to..."
    y "I'm surprised you kept going."
    y "Your life is already miserable..."
    y "The fact that your mother died, and your father beats you..."
    y "Your sickning attitude is the reason why your friends hate you."
    y "You pathetic, worthless, child..."
    show yuri 3y3 at t33 zorder 3
    show natsuki 12f at t32 zorder 3
    n "{i}*Sob*{/i}"
    hide natsuki
    pause 1
    show yuri 3y3 at t22 zorder 3
    show monika 2g at f21 zorder 3
    m "That was a mouthful..."
    show monika 2g at t21 zorder 3
    "I'm scared..."
    "Yuri is really nice on the outside, but completely insane on the inside."
    show yuri 2f at f22 zorder 3
    y "..."
    show yuri 2g at f22 zorder 3
    y "..."
    show yuri 2o at f22 zorder 3
    y "What did I just..."
    y "Oh no..."
    show yuri 4d at f22 zorder 3
    y "I didn't mean it..."
    y "I didn't mean it..."
    y "I didn't mean it..."
    y "I didn't mean it..."
    y "I didn't mean it..."
    show yuri 4d at t22 zorder 3
    mc "I..."
    "I don't know what to say..."
    "After that fight with Natsuki and Yuri, I'm not sure who to trust anymore..."
    "Why did I pick Yuri?"
    "Natsuki is probably somewhere else right now..."
    
    show yuri 4d at f22 zorder 3
    y "[player]..."
    y "I-I'm not normally like this!"
    y "Please don't think of me as a bad person!"
    y "I don't know what happened in me..."
    y "You believe me, right?"
    show yuri 4d at t22 zorder 3
    mc "I believe you..."
    show monika 2i at f21 zorder 3
    m "Well, Yuri..."
    m "I think you should go apologize to Natsuki, right now."
    m "She's probably gonna take that whole 'kill yourself' thing seriously..."
    show monika 2i at t21 zorder 3
    show yuri 2g at f22 zorder 3
    y "Y-Yes Monika."
    y "I'm gonna go right now."
    hide yuri
    pause 1
    show monika 2i at t11 zorder 3
    mc "That was..."
    show monika 2e at t11 zorder 3
    m "Scary?"
    m "Don't worry, I was a little freaked out too..."
    mc "Yuri took it {i}way{/i} too far..."
    mc "Man, I hope Yuri is sorry as she says she is."
    show monika 5a at t11 zorder 3
    m "In the meantime, did you want to hangout?"
    show monika 5a at t11 zorder 3
    mc "Sure thing, Monika."
    
    return
        
label natsuki_love:
    stop music fadeout 2.0
    mc "..."
    mc "...Natsuki."
    show natsuki 4z at f32 zorder 3
    n "Aha!"
    n "See Yuri?"
    n "He likes me, not you!"
    show natsuki 4z at t32 zorder 3
    show yuri 1y5 at t33 zorder 3
    $ style.say_dialogue = style.edited #Glitch Font Starts
    y "Ah, okay..."
    y "I'll go then..."
    $ style.say_dialogue = style.normal #Glitch Font Ends
    hide yuri
    pause 1
    show monika 2i at f21 zorder 3
    m "Jeez, it's about time you guys stop fighting..."
    show monika 2i at t21 zorder 3
    show natsuki 1l at f22 zorder 3
    n "So, can I keep hanging out with [player] then?"
    show natsuki 1l at f22 zorder 3
    show monika 3l at f21 zorder 3
    m "I guess."
    m "Just make sure it doesn't take an hour, okay?"
    show monika 3l at t21 zorder 3
    show natsuki 1z at f22 zorder 3
    n "Ehehe~"
    show natsuki 1z at t22 zorder 3
    "Well, Yuri is probably really sad right now..."
    "But on the bright side, Natsuki is really happy."
    "I guess that's all that matters."
    
    return
            
label give_chocolate:
    "I take another chocolate and hold it up to Yuri."
    "She doesn't even look away from the book."
    "She simply parts her lips, as if this situation was completely natural."
    "But that means I can't stop here!"
    scene bg fade:
        "mod_assets/CaptureYuriR5.png"
    "I apprehensively place the chocolate in her mouth."
    "Just like that, Yuri closes her lips over it."
    y "Eh...?"
    scene bg fade:
        "mod_assets/CaptureYuriR6.png"
    "Yuri's expression suddenly breaks."
    y "Did..."
    y "Did I just..."
    "Yuri looks at me like she needs to confirm what just happened."
    scene bg fade:
        "mod_assets/CaptureYuriR7.png"
    y "U-Um..."
    y "[player]..."
    mc "S-Sorry!"
    mc "I guess I shouldn't have done that..."
    y "Ah, that's..."
    y "Well..."
    y "Y-You were just helping..."
    y "That's something that...friends do..."
    y "...Right?"
    mc "I mean..."
    "Not really in this kind of context, but..."
    mc "Yeah..."
    mc "...That's all it was."
    y "Yeah..."
    y "Then..."
    y "You don't need to stop or anything..."
    mc "I-I see..."
    scene bg fade:
        "mod_assets/CaptureYuriR4.png"
    "The situation has gotten really tense..."
    "Yuri tries to return to the book."
    "But I can tell just by her expression that even she can't focus now."
    "My heart is pounding..."
    "I nervously take another chocolate between my fingers."
    "But this time, Yuri's eyes meet mine."
    show bg fade:
        "mod_assets/CaptureYuriR7.png"
    y "..."
    "How did it even come to this...?"
    "Yuri doesn't avert her gaze."
    "I notice her chest rising and falling to the rhythm of her breaths."
    "I raise my arm..."
    y "Ah..."
    "Like before, Yuri parts her lips."
    "But... it's different this time."
    scene bg fade:
        "mod_assets/CaptureYuriR8.png"
    "I take the chocolate and place it in her mouth."
    "I feel her hot breath on my fingers."
    scene bg:
        "mod_assets/club.png"
    play music t11
    show natsuki 1l at t11 zorder 3
    n "Hey [player] and Yuri!"
    mc "Uwa--"
    show natsuki 1l at t21 zorder 3
    show yuri 3o at f22 zorder 3
    y "A-Ah!"
    show yuri 3o at t22 zorder 3
    play music t3
    "Yuri jolts back."
    "The spell is abruptly broken."
    jump natsuki_inter
        
    return
    
label yuri_path:

    show yuri 1y1 at h22 zorder 3
    y "{i}(Yes!){/i}"
    show yuri 1c at t22 zorder 2
    show natsuki 1e at f21 zorder 3
    n "Are you fucking kidding me!?"
    n "C'mon [player]!"
    show natsuki 1e at t21 zorder 2
    show yuri 1r at f22 zorder 3
    y "Shut your fucking mouth Natsuki."
    show yuri 1r at t22 zorder 2
    show natsuki 1o at f21 zorder 3
    n "You shut your mouth!"
    show natsuki 1o at t21 zorder 2
    "Suddenly, Sayori walks in the room and sees Natsuki, and Yuri fighting."
    show natsuki 1o at t31 zorder 2
    show yuri 1r at t33 zorder 3
    show sayori 4p at f32 zorder 3
    s "I don't like the fighting, guys!"
    show sayori 4p at t32 zorder 2
    show yuri 1f at f33 zorder 3
    y "You heard him Natsuki. He picked me."
    show yuri 1f at t33 zorder 2
    show natsuki 4w at f31 zorder 3
    n "This is not fair!"
    show natsuki 4w at t31 zorder 2
    show yuri 3s at f33 zorder 3
    y "It is fair, Natsuki. Its what [player] picked."
    show yuri 3s at t33 zorder 2
    show natsuki 12f at f31 zorder 3
    n "..."
    show natsuki 12i at f31 zorder 3
    n "I just wanted to read manga with someone..."
    show natsuki t2i zorder 1 at t31
    hide natsuki t2i zorder 1 at l31
    pause 1
    "There goes Natsuki..."
    show sayori 2h at f32 zorder 3
    s "Yuri, be nice to Natsuki..."
    show sayori 2h at t32 zorder 2
    show yuri 2y1 at f33 zorder 3
    y "She'll be fine Sayori, no need to worry about her."
    show yuri 2y1 at t33 zorder 2
    show sayori 2h at f32 zorder 3
    s "I'm gonna go get her..."
    show sayori 2h at t32 zorder 1
    show sayori 2h zorder 1 at l32
    hide sayori 2h at l32 zorder 1
    pause 1
    show yuri 1y5 at t11 zorder 3
    play music t10y
    show yuri 2m at t11 zorder 3
    y "Finally."
    show yuri 2y1 at t11 zorder 3
    y "Finally!"
    show yuri 2s at t11 zorder 3
    y "This is really all I wanted."
    show yuri 1y6 at t11 zorder 3
    y "[player], there's no need to spend time with Natsuki, Sayori, and Monika..."
    y "Don't listen to them."
    show yuri 3y5 at t11 zorder 3
    y "Just hang out with me instead."
    show yuri 3y5 at t11 zorder 3
    y "The whole day, with just the two of us..."
    y "Doesn't that sound wonderful?"
    show yuri 3y1 at t11 zorder 3
    y "Ahahaha!"
    show yuri 3y4 at t11 zorder 3
    y "Wow... There's really something wrong with me, isn't there?"
    y "But you know what?"
    show yuri 1y3 at t11 zorder 3
    y "I don't care anymore."
    y "I've never felt this good in my whole life."
    show yuri 1y4 at t11 zorder 3
    y "Just being with you is a far greater pleasure than anything I could imagine."
    y "I'm addicted to you."
    show yuri 3y4 at t11 zorder 3
    y "It feels like I'm going to die if I'm not breathing the same air as you."
    show yuri 4a at t11 zorder 3
    y "Doesn't it feel nice to have someone care about you so much?"
    y "To have someone who wants to revolve their enitre life around you?"
    show yuri 2y6 at t11 zorder 3
    y "But if it feels so good..."
    show yuri 2y4 at t11 zorder 3
    y "Then why does it feel more and more like something horrible is going to happen?"
    show yuri 2y6 at t11 zorder 3
    y "Maybe that's why I tried stopping myself at first..."
    y "But the feeling is too strong now."
    show yuri 3y1 at t11 zorder 3
    y "I don't care anymore, [player]!"
    y "I have to tell you!"
    show yuri 3y4 at t11 zorder 3
    y "I'm...I'm madly in love with you!"
    y "It feels like every inch of my body...every drop of blood in me...is screaming your name."
    show yuri 3y3 at t11 zorder 3
    y "I don't care what the consequences are anymore!"
    y "I don't care if Monika is listening!"
    show yuri 3y4 at t11 zorder 3
    y "I'll do anything to be your lover."
    y "I'll make tea for you if you want me to."
    y "I'll kill people if you want me to."
    show yuri 3y3 at t11 zorder 3
    y "Heck, I'll even kill myself if you want me to."
    "Dang, that took a serious dark turn."
    show yuri 3w at t11 zorder 3
    y "Please, [player], just know how much I love you."
    y "I love you so much that I even touch myself with the pen I stole from you."
    "Oh, so that's what happened to my pen..."
    show yuri 3y4 at t11 zorder 3
    y "I just want to pull your skin open and crawl inside of you."
    show yuri 3y6 at t11 zorder 3
    y "I want you all to myself."
    y "And I will only be yours."
    y "Doesn't that sound perfect?"
    show yuri 3s at t11 zorder 3
    y "Tell me, [player]."
    y "Tell me you want to be my lover."
    show yuri 3s at t11 zorder 3
    y "Do you accept my confession?" 
    menu:

        "Yes.":
            jump accept_confession
        "No.":
            jump decline_confession

    