import discord
from discord.ext import commands


async def ismoderator(ctx) -> bool:
    for role in ctx.message.author.roles:
        if role.name == "moderator":
            return True
        else:
            continue
    return False

class Challenge:
    def __init__(self):
        self.people = 0
    def update(self):
        self.people += 1
    def reset(self):
        self.people = 0
challenge = Challenge() 
   
        
client = commands.Bot(command_prefix="C")

@client.event
async def on_ready():
    print("Bot good to go")



@client.command()
async def Hello(ctx):
    await ctx.send("Hi")
    

@client.command()
async def submitCode(ctx,*,code):
    submission = ctx.author.name+':'+" "+str(code)+'\n'
    with open('Submissions.txt','a',encoding='utf-8') as  submissions:
        submissions.write(submission)
        challenge.update()
        await ctx.send('code submitted')
@client.command()
async def view_submissions(ctx):
    moderator = await ismoderator(ctx)
    if moderator:
       with open('Submissions.txt','r',encoding='utf-8')as challenge_submissions:
           read_submissions = challenge_submissions.read()
           await ctx.send(read_submissions)
    else:
       await ctx.send("you do not have the permissions required to  use this command")


client.run()

