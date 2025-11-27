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

from PIL import Image, ImageDraw, ImageFont
import random
import os
from instagrapi import Client
import re

# ===========================
#   Fonts
# ===========================
POPPINS_FONT = "fonts/Poppins-Bold.ttf"
NOTO_EMOJI_FONT = "fonts/NotoColorEmoji-Regular.ttf"

font_size = 60
font_poppins = ImageFont.truetype(POPPINS_FONT, font_size)
font_emoji = ImageFont.truetype(NOTO_EMOJI_FONT, font_size)

# ===========================
#   Instagram Login
# ===========================
SESSION_FILE = "session.json"
cl = Client()

if os.path.exists(SESSION_FILE):
    cl.load_settings(SESSION_FILE)
    cl.private_request("accounts/current_user/?edit=true")
    print("🔐 Logged in using existing session")
else:
    USERNAME = os.getenv("INSTAGRAM_USERNAME")
    PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)
    print("✅ New session saved!")

# ===========================
#   Quotes and Hashtags
# ===========================
quotes = [
    "Stay positive, work hard, make it happen. 💪✨",
    "Dream big, hustle harder. 🚀🔥",
    "Good vibes only. 🌸😎",
    "Believe you can and you're halfway there. 🌟💖",
]

hashtags = ["#motivation", "#inspiration", "#success", "#positivity"]

quote = random.choice(quotes)
caption = f"{quote}\n\n{' '.join(random.sample(hashtags, 4))}"

# ===========================
#   Create Image
# ===========================
WIDTH, HEIGHT = 1080, 1080
img = Image.new("RGB", (WIDTH, HEIGHT), color="black")
draw = ImageDraw.Draw(img)

# ===========================
#   Function to separate text and emojis
# ===========================
def split_text_emoji(text):
    """Split a string into list of tuples: (char, font)"""
    result = []
    for char in text:
        if re.match(r'[\U0001F300-\U0001FAFF\u2600-\u26FF]', char):
            # Emoji range
            result.append((char, font_emoji))
        else:
            result.append((char, font_poppins))
    return result

# ===========================
#   Draw text with mixed fonts
# ===========================
x, y = 50, HEIGHT // 2 - 100
spacing = 5

for char, font in split_text_emoji(quote):
    draw.text((x, y), char, font=font, fill="white")
    # Advance x by character width
    x += font.getlength(char) + spacing

# ===========================
#   Save & Upload
# ===========================
post_image = "post_with_quote.jpg"
img.save(post_image)
print(f"📸 Post image created with quote: {quote}")

cl.photo_upload(post_image, caption=caption)
print("✅ Uploaded post to Instagram with caption")

cl.dump_settings(SESSION_FILE)
print("🔄 Session updated and saved")
