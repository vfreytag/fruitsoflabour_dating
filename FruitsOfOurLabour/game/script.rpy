# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mf = Character("Mae")
define rd = Character("Red Delicious")



image mae happy:
    "mae happy2"
    pause 1.0
    "mae happy1"
    pause 0.2
    "mae happy2"
    pause 2.0
    repeat



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_room1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mae sad
    show gala stock img at left
    # These display lines of dialogue.

    mf "I'm sad."

    mf "My partner of undefined gender cheated on me with my best friend and now I'm all alone in this world..."

    mf "What should I do????"

    menu:
        "Make a wish":
            $ made_wish = True
            show mae happy

            mf "Oh my god!!! Apples"
            show apples at right
            hide mae happy
            show rd_neutral
            rd "Hey bro"
            hide rd_neutral
            show mae happy
            mf "wow... i love apples"
        "Do not make a wish":
            return

    # This ends the game.

    return
