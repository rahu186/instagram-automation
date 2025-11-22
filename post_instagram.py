from instagrapi import Client
from generate_reel import create_reel
from PIL import Image, ImageDraw, ImageFont
import os
import random

# --- Instagram session-based login ---
SESSION_FILE = "session.json"

cl = Client()
if os.path.exists(SESSION_FILE):
    cl.load_settings(SESSION_FILE)
    cl.login(None, None)  # Login using session
else:
    USERNAME = os.getenv("INSTAGRAM_USERNAME")
    PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)  # Save session for future runs

# --- Images and quotes ---
images_folder = "images"
all_images = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not all_images:
    raise Exception("No images found in 'images/' folder!")

quotes = [
    "Stay positive, work hard, make it happen.",
    "Dream big, hustle harder.",
    "Good vibes only.",
    "Believe you can and you're halfway there.",
    "Success is no accident."
]

hashtags = ["#motivation", "#dailyquotes", "#inspiration", "#automation", "#fun"]

# --- Function to write quote on image ---
def write_quote_on_image(image_path, quote, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font_size = max(20, image.size[0] // 15)
    font = ImageFont.load_default()

    # Pillow >=10 fix for text size
    bbox = draw.textbbox((0, 0), quote, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Position text at bottom center
    x = (image.width - text_width) // 2
    y = image.height - text_height - 20

    draw.text((x, y), quote, font=font, fill="white")
    image.save(output_path)

# --- Post ---
post_image_orig = os.path.join(images_folder, random.choice(all_images))
post_image = "post_with_quote.jpg"
quote_post = random.choice(quotes)
write_quote_on_image(post_image_orig, quote_post, post_image)
caption_post = f"{quote_post}\n{' '.join(random.sample(hashtags, 3))}"
cl.photo_upload(post_image, caption=caption_post)
print(f"Posted image with quote: {quote_post}")

# --- Reel ---
reel_image_orig = os.path.join(images_folder, random.choice(all_images))
reel_image = "reel_with_quote.jpg"
quote_reel = random.choice(quotes)
write_quote_on_image(reel_image_orig, quote_reel, reel_image)
reel_video = "reel_video.mp4"
create_reel(reel_image, reel_video)
caption_reel = f"{quote_reel}\n{' '.join(random.sample(hashtags, 3))}"
cl.video_upload(reel_video, caption=caption_reel)
print(f"Uploaded reel with quote: {quote_reel}")
