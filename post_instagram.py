# from instagrapi import Client
# from generate_reel import create_reel
# from PIL import Image, ImageDraw, ImageFont
# import os
# import random

# # ===========================
# #   SESSION-BASED INSTAGRAM LOGIN
# # ===========================
# SESSION_FILE = "session.json"
# cl = Client()

# try:
#     if os.path.exists(SESSION_FILE):
#         print("🔐 Using existing Instagram session...")
#         cl.load_settings(SESSION_FILE)
#         cl.private_request("accounts/current_user/?edit=true")

#     else:
#         print("🔑 Logging in first time...")
#         USERNAME = os.getenv("INSTAGRAM_USERNAME")
#         PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

#         if not USERNAME or not PASSWORD:
#             raise Exception("Instagram credentials missing in GitHub secrets.")

#         cl.login(USERNAME, PASSWORD)
#         cl.dump_settings(SESSION_FILE)
#         print("✅ Session saved!")
# except Exception as e:
#     print("❌ Login failed:", e)
#     raise

# # ===========================
# #   IMAGE & QUOTE SETUP
# # ===========================
# images_folder = "images"
# all_images = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# if not all_images:
#     raise Exception("No images found in 'images/' folder!")

# quotes = [
#     "Stay positive, work hard, make it happen.",
#     "Dream big, hustle harder.",
#     "Good vibes only.",
#     "Believe you can and you're halfway there.",
#     "Success is no accident.",
#     "Every day is a new beginning.",
#     "Push yourself because no one else will.",
#     "Let your dreams be bigger than your fears."
# ]

# hashtags = [
#     "#motivation", "#inspiration", "#success", "#positivity",
#     "#dailyquotes", "#quotes", "#lifestyle", "#hustle"
# ]

# # ===========================
# #   FUNCTION: WRITE QUOTE ON IMAGE
# # ===========================
# def write_quote_on_image(image_path, quote, output_path):
#     image = Image.open(image_path).convert("RGB")
#     draw = ImageDraw.Draw(image)

#     # Auto-size font based on width
#     font_size = max(40, image.size[0] // 18)
#     font = ImageFont.load_default()

#     # Pillow 10+ method
#     bbox = draw.textbbox((0, 0), quote, font=font)
#     text_width = bbox[2] - bbox[0]
#     text_height = bbox[3] - bbox[1]

#     x = (image.width - text_width) // 2
#     y = image.height - text_height - 40

#     # Text border for better visibility
#     for ox in [-2, 2]:
#         for oy in [-2, 2]:
#             draw.text((x + ox, y + oy), quote, font=font, fill="black")

#     draw.text((x, y), quote, font=font, fill="white")
#     image.save(output_path)

# # ===========================
# #   POST IMAGE LOGIC
# # ===========================
# post_image_orig = os.path.join(images_folder, random.choice(all_images))
# post_image = "post_with_quote.jpg"
# quote_post = random.choice(quotes)

# write_quote_on_image(post_image_orig, quote_post, post_image)
# caption_post = f"{quote_post}\n\n{' '.join(random.sample(hashtags, 4))}"

# cl.photo_upload(post_image, caption=caption_post)
# print(f"📸 Posted Image with Quote: {quote_post}")

# # ===========================
# #   REEL LOGIC
# # ===========================
# reel_image_orig = os.path.join(images_folder, random.choice(all_images))
# reel_image = "reel_with_quote.jpg"
# quote_reel = random.choice(quotes)

# write_quote_on_image(reel_image_orig, quote_reel, reel_image)
# reel_video = "reel_video.mp4"
# create_reel(reel_image, reel_video)

# caption_reel = f"{quote_reel}\n\n{' '.join(random.sample(hashtags, 4))}"

# cl.video_upload(reel_video, caption=caption_reel)
# print(f"🎥 Uploaded Reel with Quote: {quote_reel}")

# # ===========================
# #   UPDATE SESSION
# # ===========================
# cl.dump_settings(SESSION_FILE)
# print("🔄 Session updated and saved.")

# from PIL import Image, ImageDraw, ImageFont
# import random
# import os
# from instagrapi import Client
# import re

# # ===========================
# #   Fonts
# # ===========================
# POPPINS_FONT = "fonts/Poppins-Bold.ttf"
# NOTO_EMOJI_FONT = "fonts/NotoColorEmoji-Regular.ttf"

# font_size = 60
# font_poppins = ImageFont.truetype(POPPINS_FONT, font_size)
# font_emoji = ImageFont.truetype(NOTO_EMOJI_FONT, font_size)

# # ===========================
# #   Instagram Login
# # ===========================
# SESSION_FILE = "session.json"
# cl = Client()

# if os.path.exists(SESSION_FILE):
#     cl.load_settings(SESSION_FILE)
#     cl.private_request("accounts/current_user/?edit=true")
#     print("🔐 Logged in using existing session")
# else:
#     USERNAME = os.getenv("INSTAGRAM_USERNAME")
#     PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
#     cl.login(USERNAME, PASSWORD)
#     cl.dump_settings(SESSION_FILE)
#     print("✅ New session saved!")

# # ===========================
# #   Quotes and Hashtags
# # ===========================
# quotes = [
#     "Stay positive, work hard, make it happen. 💪✨",
#     "Dream big, hustle harder. 🚀🔥",
#     "Good vibes only. 🌸😎",
#     "Believe you can and you're halfway there. 🌟💖",
# ]

# hashtags = ["#motivation", "#inspiration", "#success", "#positivity"]

# quote = random.choice(quotes)
# caption = f"{quote}\n\n{' '.join(random.sample(hashtags, 4))}"

# # ===========================
# #   Create Image
# # ===========================
# WIDTH, HEIGHT = 1080, 1080
# img = Image.new("RGB", (WIDTH, HEIGHT), color="black")
# draw = ImageDraw.Draw(img)

# # ===========================
# #   Function to separate text and emojis
# # ===========================
# def split_text_emoji(text):
#     """Split a string into list of tuples: (char, font)"""
#     result = []
#     for char in text:
#         if re.match(r'[\U0001F300-\U0001FAFF\u2600-\u26FF]', char):
#             # Emoji range
#             result.append((char, font_emoji))
#         else:
#             result.append((char, font_poppins))
#     return result

# # ===========================
# #   Draw text with mixed fonts
# # ===========================
# x, y = 50, HEIGHT // 2 - 100
# spacing = 5

# for char, font in split_text_emoji(quote):
#     draw.text((x, y), char, font=font, fill="white")
#     # Advance x by character width
#     x += font.getlength(char) + spacing

# # ===========================
# #   Save & Upload
# # ===========================
# post_image = "post_with_quote.jpg"
# img.save(post_image)
# print(f"📸 Post image created with quote: {quote}")

# cl.photo_upload(post_image, caption=caption)
# print("✅ Uploaded post to Instagram with caption")

# cl.dump_settings(SESSION_FILE)
# print("🔄 Session updated and saved")

# from PIL import Image, ImageDraw, ImageFont
# import random
# import os
# from instagrapi import Client
# import re
# import requests

# # ===========================
# # Fonts & Emoji folder
# # ===========================
# POPPINS_FONT = "fonts/Poppins-Bold.ttf"
# font_size = 60
# font_poppins = ImageFont.truetype(POPPINS_FONT, font_size)

# EMOJI_FOLDER = "emoji_pngs"  # folder to store PNG emojis
# EMOJI_SIZE = font_size        # resize emoji to font size
# os.makedirs(EMOJI_FOLDER, exist_ok=True)

# # ===========================
# # Instagram login
# # ===========================
# SESSION_FILE = "session.json"
# cl = Client()

# if os.path.exists(SESSION_FILE):
#     cl.load_settings(SESSION_FILE)
#     cl.private_request("accounts/current_user/?edit=true")
#     print("🔐 Logged in using existing session")
# else:
#     USERNAME = os.getenv("INSTAGRAM_USERNAME")
#     PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
#     cl.login(USERNAME, PASSWORD)
#     cl.dump_settings(SESSION_FILE)
#     print("✅ New session saved!")

# # ===========================
# # Quotes and hashtags
# # ===========================
# quotes = [
#     "Stay positive, work hard, make it happen. 💪✨",
#     "Dream big, hustle harder. 🚀🔥",
#     "Good vibes only. 🌸😎",
#     "Believe you can and you're halfway there. 🌟💖",
# ]

# hashtags = ["#motivation", "#inspiration", "#success", "#positivity"]

# quote = random.choice(quotes)
# caption = f"{quote}\n\n{' '.join(random.sample(hashtags, 4))}"

# # ===========================
# # Download missing emoji PNGs
# # ===========================
# def is_emoji(char):
#     return re.match(r'[\U0001F300-\U0001FAFF\u2600-\u26FF]', char)

# def download_emoji(char):
#     code = f"{ord(char):x}"
#     filename = f"emoji_u{code}.png"
#     path = os.path.join(EMOJI_FOLDER, filename)
#     if not os.path.exists(path):
#         url = f"https://raw.githubusercontent.com/googlefonts/noto-emoji/main/png/128/emoji_u/{filename}"
#         try:
#             r = requests.get(url)
#             if r.status_code == 200:
#                 with open(path, "wb") as f:
#                     f.write(r.content)
#                 print(f"✅ Downloaded {filename}")
#             else:
#                 print(f"⚠ Emoji PNG not found for {char}")
#         except Exception as e:
#             print(f"❌ Error downloading {filename}: {e}")
#     return path if os.path.exists(path) else None

# # ===========================
# # Create image with wrapping
# # ===========================
# WIDTH, HEIGHT = 1080, 1080
# MARGIN = 50
# LINE_SPACING = 20  # space between lines
# img = Image.new("RGB", (WIDTH, HEIGHT), color="black")
# draw = ImageDraw.Draw(img)

# x, y = MARGIN, MARGIN
# spacing = 5  # <--- add this
# line_height = EMOJI_SIZE + 10  # height for each line (text + emojis)

# for char in quote:
#     if is_emoji(char):
#         path = download_emoji(char)
#         if path:
#             emoji_img = Image.open(path).convert("RGBA")
#             emoji_img = emoji_img.resize((EMOJI_SIZE, EMOJI_SIZE), Image.ANTIALIAS)

#             # Wrap line if exceeding WIDTH
#             if x + EMOJI_SIZE > WIDTH - MARGIN:
#                 x = MARGIN
#                 y += line_height + LINE_SPACING

#             img.paste(emoji_img, (x, y), emoji_img)
#             x += EMOJI_SIZE + spacing
#         else:
#             x += EMOJI_SIZE + spacing  # skip missing
#     else:
#         char_width = font_poppins.getlength(char)
#         # Wrap line if exceeding WIDTH
#         if x + char_width > WIDTH - MARGIN:
#             x = MARGIN
#             y += line_height + LINE_SPACING

#         draw.text((x, y), char, font=font_poppins, fill="white")
#         x += char_width + spacing

# # ===========================
# # Save & upload
# # ===========================
# post_image = "post_with_quote.png"
# img.save(post_image)
# print(f"📸 Post image created with quote: {quote}")

# cl.photo_upload(post_image, caption=caption)
# print("✅ Uploaded post to Instagram with caption")

# cl.dump_settings(SESSION_FILE)
# print("🔄 Session updated and saved")

import requests
from instagrapi import Client
import os
import json

# -----------------------
# Stability AI Settings
# -----------------------
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

PROMPT = """
Create a brand-new original one-line motivational quote.
Design a modern Instagram poster (1080x1080), aesthetic and clean,
with the quote beautifully written inside the image.
"""

# -----------------------
# Instagram Login
# -----------------------
SESSION_FILE = "session.json"
cl = Client()

def login_instagram():
    if os.path.exists(SESSION_FILE):
        try:
            cl.load_settings(SESSION_FILE)
            cl.private_request("accounts/current_user/?edit=true")
            print("🔐 Logged in using saved session")
            return
        except Exception as e:
            print("⚠ Saved session failed, logging in fresh:", e)

    USERNAME = os.getenv("INSTAGRAM_USERNAME")
    PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)
    print("✅ Logged in & new session saved")


# -----------------------
# Generate Image using Stability AI
# -----------------------
def generate_ai_post():
    url = "https://api.stability.ai/v2beta/stable-image/generate/ultra"

    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Accept": "image/*",
    }

    data = {
        "prompt": PROMPT,
        "output_format": "png",
    }

    files = {
        "none": (None, "")   # REQUIRED for Ultra to accept multipart/form-data
    }

    print("🎨 Generating AI image...")

    response = requests.post(url, headers=headers, data=data, files=files)

    if response.status_code != 200:
        print("❌ Stability Error:", response.text)
        return None

    with open("daily_post.png", "wb") as f:
        f.write(response.content)

    print("✨ Image saved as daily_post.png")
    return "daily_post.png"


# -----------------------
# Upload to Instagram
# -----------------------
def upload_to_instagram(image_path):
    caption = "✨ Daily Motivation\n#motivation #inspiration #quotes #positivity"
    try:
        cl.photo_upload(image_path, caption)
        print("📤 Successfully uploaded to Instagram!")
    except Exception as e:
        print("❌ Upload error:", e)


# -----------------------
# Main Run
# -----------------------
login_instagram()

image = generate_ai_post()
if image:
    upload_to_instagram(image)

cl.dump_settings(SESSION_FILE)
print("🔄 Session saved again")
