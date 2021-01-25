import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} connected to Discord")

@client.event
async def on_member_remove(member):
    print("Someone left")
    member_name = str(member)
    member_name = member_name[:member_name.index("#")]
    embed = discord.Embed(title=f"{member_name} Left!", description=f"We're sorry to say good bye, hope"
                                                                                   f" we will see you soon"
                                                                                   f" {member.mention}")
    channel = client.get_channel(802143961031507968)
    await channel.send(embed=embed)

@client.event
async def on_member_join(member):
    member_name = str(member)
    member_name = member_name[:member_name.index("#")]
    print("Someone joined")
    channel = client.get_channel(797412497589927937)
    embed = discord.Embed(title=f"Welcome {member_name}",
                          description=f"Welcome {member_name}, hope you will have a nice"
                                      " time will you're here")
    await channel.send(embed=embed)


@client.event
async def on_message(message):
    message_content = str(message.content)
    restricted_words = ['fuck', 'dick', 'ass', 'motherfucker', 'pussy', 'moron', 'bitch']

    for restricted_word in restricted_words:
        if restricted_word in message_content.lower():
            embed = discord.Embed(title="Message Removal", description=f"Hey {message.author.mention}, I wanted to let"
                                                                       f" you know you know that your message has been"
                                                                       f" removed because of use of inappropriate words"
                                                                       f". If you think that this was a mistake please"
                                                                       f" contact the administrators of the server.")
            await message.author.send(embed=embed)
            await message.delete()

    else:
        if message_content.startswith("!"):
            if message_content == "!hello":
                await message.channel.send(f"Hey {message.author.mention}")
            elif message_content == "!my_messages":
                no_of_messages = 0
                async for msg in client.get_channel(message.channel.id).history():
                    if msg.author == message.author:
                        print(msg.content)
                        no_of_messages += 1
                embed = discord.Embed(title="Number of Messages", description=f"Hey {message.author.mention}, "
                                                                              f"According to our records you have sent a"
                                                                              f" total of {no_of_messages} to this channel")
                await message.channel.send(embed=embed)
            if message_content == "!latest_events":
                events_channel = client.get_channel(802144608464404520)
                async for msg in events_channel.history():
                    if msg.embeds:
                        await message.channel.send(embed=msg.embeds[0])
                        break
                    else:
                        await message.channel.send(msg.content)
                        break

client.run("ODAyNDU1NzIxMjQ0MzYwNzI1.YAvfIA.OGZv2fkku8Z88Ny_bQ6XL6pmmXM")
