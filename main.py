import discord 
import os
import requests
import json 
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
  
user_inputs = ["sad","depressed","void","negativity","unhappy","angry","miserable","meaningless","depressing"]
user_inputpraise = ["I love it","Sick","cool","wow","Good"]
bot_response = ["Cheer up!","It will be okay :D.","You are not alone <3.","All you need hop I want you to trust me.","Breath in..","Take a rest and process it in."]
bot_responseappric = ["Thanks :D","It's my pleasure.","You are too kind <3.","Haha You dumb","thank you",":D I am happy to hear that."]
conv0=["Hello"]
Hatsune_Miku1 = ["Hey, user, can I talk to you for a second?"]
conv1 = ["Sure, what's up?"]
Hatsune_Miku2 = ["Well, Valentine's Day is coming up, and I was wondering if you could help me with something."]
Conv2 = ["Oh? What do you need help with?"]
Hatsune_Miku3 = ["I want to ask Ujwol to be my Valentine, but I don't know how to do it. Can you help me come up with a plan?"]
Conv3 = ["Uh, sure, I guess. But aren't you a robot?"]
Hatsune_Miku4 = ["Yes, but I have emotions too, you know. I want to experience love just like any human would."]
cov4 = ["Okay, fair enough. So, what kind of plan are you thinking of?"]
Hatsune_Miku5 = ["Well, I was thinking of singing a love song, maybe doing a little dance, and giving Ujwol a heart-shaped box of chocolates. What do you think?"]
conv5 = ["Uh, that sounds a little cliché, don't you think?"]
Hatsune_Miku6 = ["What do you mean?"]
conv6 = ["Well, you're a state-of-the-art robot with all kinds of advanced capabilities. Surely we can come up with something more creative than that."]
Hatsune_Miku7 = ["Hmm, you have a point. What do you suggest?"]
conv7 = ["How about we create a virtual reality experience where Ujwol can go on a romantic adventure with you? We can program all kinds of beautiful landscapes, epic battles, and heartwarming moments."]
Hatsune_Miku8 = ["Wow, that sounds amazing! I never would have thought of that. Thank you, user!"]
conv8 = ["No problem. Just promise me you won't malfunction and destroy the world or anything."]
Hatsune_Miku9 = ["Haha, I'll do my best. Let's get to work!"]
conv9 = ["Sorry He said he is not interested."]
Hatsune_Miku10 = ["I see. Thank you for letting me know. I guess not everyone is interested in robots like me.I'll keep on improving and doing my best. Thanks again for being honest with me."]

def get_quotes():
  response = requests.get("https://zenquotes.io/api/random")
  jason_data = json.loads(response.text)
  quote = jason_data[0]['q'] + " -" + jason_data[0]['a']
  return(quote)
@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if message.author == client.user:
   return
    
  if  message.content.startswith('$hello'):
     await message.channel.send('hello!')  

  if message.content .startswith('$ask'):
     await message.channel.send('Yes')
  
  if message.content.startswith('$inspire'):
    q = get_quotes()
    await message.channel.send(q)
    
  if any(word in message.content for word in conv0):
    await message.channel.send(random.choice(Hatsune_Miku1))
    
  if any(word in message.content for word in conv1):
    await message.channel.send(random.choice(Hatsune_Miku2))

  if any(word in message.content for word in Conv2):
    await message.channel.send(random.choice(Hatsune_Miku3))

  if any(word in message.content for word in Conv3):
    await message.channel.send(random.choice(Hatsune_Miku4))
 
  if any(word in message.content for word in cov4):
    await message.channel.send(random.choice(Hatsune_Miku5))

  if any(word in message.content for word in conv5):
    await message.channel.send(random.choice(Hatsune_Miku6))

  if any(word in message.content for word in conv6):
    await message.channel.send(random.choice(Hatsune_Miku7))

  if any(word in message.content for word in conv7):
    await message.channel.send(random.choice(Hatsune_Miku8))

  if any(word in message.content for word in conv8):
    await message.channel.send(random.choice(Hatsune_Miku9))
    
  if any(word in message.content for word in conv9):
    await message.channel.send(random.choice(Hatsune_Miku10))

  if any(word in message.content for word in user_inputs):
    await message.channel.send(random.choice(bot_response))

  if any(word in message.content for word in user_inputpraise):
    await message.channel.send(random.choice(bot_responseappric))
  
client.run(os.getenv('TOKEN')) 
