import os
import io
import requests
import shutil 
import random
import re
import glob
import time

from io import BytesIO
from requests import get
from telethon.tl.types import InputMessagesFilterPhotos

from TGNRobot import OWNER_ID
from TGNRobot.events import register
from TGNRobot import telethn
from PIL import Image, ImageDraw, ImageFont


LOGO_LINKS            = ["https://telegra.ph/file/66c94adc82e1fcd5ff1d5.jpg",
                         "https://telegra.ph/file/05a88eae0a3d43e7bd014.jpg",
                         "https://telegra.ph/file/9d6c7c817ab2d55886749.jpg",
                         "https://telegra.ph/file/68ec005e8844fe1b0f1a9.jpg",
                         "https://telegra.ph/file/661049ee2c2fa39951a04.jpg",
                         "https://telegra.ph/file/7bf091e53d4711ffde2cf.jpg",
                         "https://telegra.ph/file/7bcd8d6bf0b7b07e8d4af.jpg",
                         "https://telegra.ph/file/74bb73a6f5e0a20a91cca.jpg",
                         "https://telegra.ph/file/1b1ec1309746d2b58a1b9.jpg",
                         "https://telegra.ph/file/b327dea282a1adf95246b.jpg",
                         "https://telegra.ph/file/19116ed25c5050f8ffa5f.jpg",
                         "https://telegra.ph/file/6ea78967e99e991ba15d3.jpg",
                         "https://telegra.ph/file/84c16ab5710329b1979a3.jpg",
                         "https://telegra.ph/file/500d90d3549b1b2027273.jpg",
                         "https://telegra.ph/file/47dde9d76d452cee17499.jpg",
                         "https://telegra.ph/file/3db29ffcaf85d6cc3ba9a.jpg",
                         "https://telegra.ph/file/3a6a70fe84badbdc89b02.jpg",
                         "https://telegra.ph/file/aebefd3f837f46e161f0d.jpg",
                         "https://telegra.ph/file/62693b6a5a6b2339c2207.jpg",
                         "https://telegra.ph/file/b672fdee4593ea67bca22.jpg",
                         "https://telegra.ph/file/9b0f36896be1586e0a807.jpg",
                         "https://telegra.ph/file/29376c68166d073d843fa.jpg",
                         "https://telegra.ph/file/97459559987623dcc6dc1.jpg",
                         ]

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

  if not quew:
     await event.reply('Please Gimmie A Text For The Logo.')
     return
 pesan = await event.reply('Logo In A Process. Please Wait.')
 try:
    text = event.pattern_match.group(1)
    randc = random.choice(LOGO_LINKS)
    img = Image.open(io.BytesIO(requests.get(randc).content))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "black"
    shadowcolor = "blue"
    fnt = glob.glob("./TGNRobot/utils/Logo/*")
    randf = random.choice(fnt)
    font = ImageFont.truetype(randf, 120)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y = ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black")
    fname = "Cutiepii.png"
    img.save(fname, "png")
    await telethn.send_file(event.chat_id, file=fname, caption = f"Made by @SkylerX_Bot")         
    await pesan.delete()
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await event.reply(f'Error, Report @electrobot_support, {e}')
