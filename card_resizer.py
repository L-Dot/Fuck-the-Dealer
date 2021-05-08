from PIL import Image
import os

# Resizes the cards in the card_deck directory to smaller versions
def card_resizer(max_pix, prefix, dir):
    cards = [file for file in os.listdir('card_deck') if file.endswith(('jpeg', 'png', 'jpg'))]
    for card in cards:
        img = Image.open('card_deck\\'+card)
        img.thumbnail((max_pix,max_pix))
        img.save(f"{dir}\\{prefix}{card}", optimize=True, quality=40)

card_resizer(70, '', 'small_deck')
card_resizer(300, '', 'medium_deck')