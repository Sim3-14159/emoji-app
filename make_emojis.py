import regex
import emoji
import re
from PIL import Image, ImageFont
from pilmoji import Pilmoji
import os

# --- Pillow Compatibility Fix ---
if not hasattr(Image, "Resampling"):
    class Resampling:
        LANCZOS = Image.ANTIALIAS
    Image.Resampling = Resampling


def crop_transparent(image):
    """Crop the transparent edges of an RGBA image."""
    bbox = image.getbbox()  # returns (left, upper, right, lower)
    if bbox:
        return image.crop(bbox)
    return image  # no content? return as is


def emoji_to_image(emoji_char, font_size=128, output_filename="emoji.png"):
    # create a blank image
    image = Image.new("RGBA", (font_size * 2, font_size * 2), (0, 0, 0, 0))
    
    fallback_font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size
    )
    
    with Pilmoji(image) as pilmoji:
        pilmoji.text((0, 0), emoji_char, font_size=font_size, font=fallback_font)
    
    # crop the transparent borders
    image = crop_transparent(image)
    
    image.save(f"{PATH}/emojis/{output_filename}")
    print(f"Saved {emoji_char} as \033[33m{output_filename}\033[0m" +
          f" in \033[32m{PATH}/emojis/\033[0m")


PATH = os.path.dirname(os.path.abspath(__file__))


# --- Read concatenated emojis ---
f = open(f"{PATH}/emojis.txt", "r", encoding="utf-8")
all_emojis = f.read().strip()
f.close()

# split into grapheme clusters (handles multi-codepoint emojis)
emoji_list = regex.findall(r'\X', all_emojis)

# --- Generate PNGs ---
for char in emoji_list:
    if not char.strip():
        continue
    # get emoji name
    name = emoji.demojize(char).strip(":")
    # sanitize filename
    safe_name = re.sub(r"[^\w\-]", "_", name)
    # generate image
    emoji_to_image(char, 128, safe_name + ".png")
