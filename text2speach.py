from gtts import gTTS
import os
text = """It is He Who has made the earth a bed for you and the sky a canopy;
 and it is He Who sends down rain from above for the growth of every kind of food products 
for your sustenance. So, 
when you know this, you should not set up equals to rank with Allah """
lang = 'en'
myobj = gTTS(text=text,lang=lang,slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")
