from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("meme.PNG")
afbeelding = Image.open("meme.PNG")

breedte = str(afbeelding.width)
hoogte = str(afbeelding.height)

lettertype = ImageFont.truetype("impact", 40)

tekengebied = ImageDraw.Draw(achtergrond)

tekst = "Teacher: what comes after 69?\nMe: 70\nTeacher: why did you write 'Nice'"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

achtergrond.show()

achtergrond.save("meme_met_tekst.jpg")
