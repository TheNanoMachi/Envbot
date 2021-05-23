import os
import discord
import random

key = 'TOKEN'

messagesSent = 0

# def get_hash(hashValue):
#   response = requests.get("http://api.hashify.net/hash/md4/hex?value="+hashValue)
#   print(response)
#   return response



def messageCheck(server):
  f = open("messagerecord.txt", "rt+")
  for i in f:
    value = i.split()
    print(i)
    if server == value[1]:
      f.close()
      return value[0]
    else:
      f.write("0 "+ server + "\n")
      f.close()
      return 0
    

def format_array(array):
  output = ''
  for i in range(len(array)):
    output += array[i]
    output += "\n"
  return output

EnvironmentalFacts = {
  "generalFacts": [
    "The cows ‘destroy’ the environment",
    "The Earth has a lot of water",
    "Humans only use 1% of all available water",
    "About 10 million trees are down every year to make toilet paper",
    "Paper from trees can be recycled 6 times",
    "Aluminium can be recycled forever",
    "The earth is about 1 million years old, with more than 1 million species going extinct",
    "Earthquakes are explained as part of the planet’s natural geography, and they are very hard to predict.",
    "Fungi plays a highly vital role in the environment",
    "Elephants are unique humans!!",
    "Bats are not blind",
    "The combined weight of ants on the planet makes them heavier than all human beings. ",
    "Glass does not decompose easily and is categorized as one of the human made longest-lasting materials",
    "Plastic does not decompose easily either",
    "Greenhouse gasses are good",
    "Americans are the world's number one trash-producing nation, accounting for 30% of the world’s waste.",
    "Garbage Island really exists.",
    "Beef is harmful to the environment",
    "Recycling one glass bottle saves enough energy to power a normal light bulb for about four hours",
    "There are about 27 oil spills daily, somewhere in the world. "
  ],
  "species": [
    "Up to 1 million species face extinction due to human activity",
    "Around 8.7 million species exist",
    "An endangered species is one whose numbers are so small that it is at risk of extinction.",
    "A species is defined as endangered or threatened when it suffers from these factors: damage to its habitat for recreational, or entertainment purposes; disease or predation of the species; and hazards to the continued life of the species.",
    "A species is declared extinct after many years of not being spotted. Because it takes so long to define an entire species as extinct, it is probable that there are many species already gone that we are unaware of.",
    "Extinction is a natural phenomenon, it occurs at a natural “background” rate of about one to five species per year. Scientists estimate we’re now losing species at 1,000 to 10,000 times the “background” rate, with dozens going extinct every day.",
    "As many as 30 to 50 percent of all species are possibly heading toward extinction by mid-century.",
    "99% of currently threatened species are at risk from human activities, primarily those driving habitat loss, introduction of exotic species, and global warming.",
    "Freshwater ecosystems are home to more than 100,000 known species of plants and animals, and are now one of the most endangered habitats in the world as a result of human development, pollution, and climate change.",
    "Wildlife population sizes dropped by 68% between 1970 and 2018.",
    "Species are dying off 1,000 times more frequently today than during the 60 million years before the arrival of humans.",
    "100 million hectares of tropical forest were lost between 1980 and 2000.",
    "Four in 10 (39.4%) plants are at risk of dying out.",
    "Over 40% of all insects could disappear within decades.",
    "One species of jellyfish is immortal. It can revert back to its child state after having become sexually mature, and therefore never dies.",
    "The golden Toad is the first species to go extinct due to climate change.",
    "Invasive Species are plants and animals transported from one country or region to another and introduced into the wild.",
    "Over-hunting and Over-collecting has impacted many endangered species, wreaking havoc on ecosystems and eliminating entire species forever.",
    "A keystone species is a plant or animal that plays a crucial role in how an ecosystem functions",
    "An indicator species is a plant or animal species humans focus on to gather information about an ecosystem."
  ],
  "Climate": [
    "The global temperature on an average has increased by 0.6 to 1 degree Celsius till 20th century",
    "The united States constitutes 5% of the world population and contributes to 22% of the world’s carbon emission. ",
    "Around 15% of the carbon released in the environment is due to deforestation and change in the use of land. ",
    "Vehicles like cars and trucks contribute to 20% of carbon emissions in the United states.",
    "Air conditions and heating elements consume 50% of electricity in America",
    "Hurricanes, Droughts, and coral deaths are a few of the natural disasters caused due to climate change. ",
    "The hottest years have been experienced from 1990 till 1997. The warmest years have been since 2005.",
    "Climate change enhances the spread of pests that causes life-threatening diseases like malaria, dengue, lyme diseases, etc. ",
    "Land use change and deforestation contributes to 15% of carbon emission every year. "
    "The number of climate change related incidents has increased fourfold between 1980 and 2010.",
    "A separate budget of US$ 40 million has been allotted for climate change research since 1990.",
    "Due to the greenhouse effect, the average temperature of the earth is 15 degrees rather than -18 degrees without the greenhouse effect.",
    "Carbon dioxide constitutes only 3.6 % of total greenhouse gases, out of which 0.12% is attributed to human activities.",
    "Carbon dioxide is not the only contributing gas to climate change. Other gases like methane and nitrous oxide are far more dangerous than carbon dioxide alone."
    "n 2003, around 70,000 deaths occurred in Europe alone due to diseases caused by rising temperatures.",
    "Climate change can have serious health impacts such as heat stress, extreme cold, which can cause major deaths due to heart diseases.",
    "Due to water shortages, the transportation of water will cause it to contaminate and make it even more deadly by spreading diseases.",
    "Over the next 20 years, global warming is expected to increase by 0.2 degrees per decade.",
    "Above 600000 deaths occur worldwide every year due to climate change. 95% of these deaths take place in developing countries.",
    "Climate change can have serious health impacts such as heat stress, extreme cold, which can cause major deaths due to heart diseases."
  ],
  "Ocean": [
    "The majority of life on Earth is aquatic."
    "Our oceans cover more than 70 per cent of the Earth’s surface.",
    "Less than five per cent of the planet’s oceans have been explored.",
    "The world’s longest mountain chain is underwater.",
    "There are more historic artefacts under the sea than in all of the world’s museums.",
    "We still only know a fraction of the marine species in our oceans.",
    "Over 70 per cent of our planet’s oxygen is produced by the ocean.",
    "It’s possible to find rivers and lakes beneath the ocean.",
    "Around 50 per cent of the US lies beneath the ocean.",
    "The Pacific Ocean is the world’s largest ocean and contains around 25,000 islands",
    "There's around 20 million tons of gold dispersed throughout the oceans. ",
    "The Antarctic Ice Sheet is larger than the entire Continental United States.",
    "The Pacific is wider than the moon.",
    "One iceberg could supply a million people with drinking water for five years.",
    "Water at the bottom of the ocean is incredibly hot.",
    "The planet's biggest waterfall is in the ocean.",
    "The loudest ocean sound came from an icequake.",
    "More people have been to the moon than to the Mariana Trench.",
    "Sea ice is drinkable.",
    "Most of Earth's volcanic activity happens in the ocean."
  ],
  "Quotes": [
    "I only feel angry when I see waste. When I see people throwing away things we could use - Mother Teresa",
    "The Earth is what we all have in common - Wendell Berry",
    "Progress is impossible without change, and those who cannot change their minds cannot change anything - George bernard Shaw",
    "Time spent among trees is never time wasted - Anonymous",
    "He that plants trees loves other besides himself - Thomas Fuller",
    "Never doubt that a small group of thoughtful, committed citizens can change the world; indeed, it is the only thing that ever has - Margaret Mead",
    "One that of the first conditions of happiness is that the link between man and nature shall not be broken - Leo Tolstoy",
    "The environment is where we all meet; where all have a mutant interest; it is the one thing all of us share -Lady Bird Johnson",
    "Nature is painting for us, day after day, pictures of infinite beauty - John Ruskin",
    "Like music and art, love of nature is a common language that can transcend political or social boundaries -Jimmy Carter.",
    "Nothing is more beautiful than the loveliness of the woods before sunrise - George Washington Carver",
    "What’s the use of a fine house if you haven’t got a tolerable planet to put it on - Henry David Thoreau",
    "Environmentally friendly cars will soon cease to be an option … they will become a necessity. - Fujio Cho, Honorary Chairman of Toyota Motors",
    "To me a lush carpet of pine needles or spongy grass is more welcome than the most luxurious Persian rug. - Helen Keller",
    "The earth is a fine place and worth fighting for - Earnest Hemingway",
    "The proper use of science is not to conquer nature but to live in it - Barry commoner.",
    "We have forgotten how to be good guests, how to walk lightly on the earth as its other creatures do - Barbara Ward",
    "A healthy ecology is the basis for a healthy economy - Terry Tempest Williams",
    "Sustainability is the right thing to do, it’s the smart thing to do, it’s the profitable thing to do - Lady Bird Johnson",
    "You cannot escape the responsibility of tomorrow by evading it today. - Abraham Lincon"
  ],
  "humans": [
    "An increased population results in more clear-cutting, resulting in severely damaged ecosystems.",
    "Humans tend to depend on high usage of fossil fuels and coal for energy. ",
    "Significant use of fossil fuels (such as oil and coal) results in large amounts of carbon dioxide into the air, threatening the extinction of thousands of species.",
    "Humanity is continuously polluting indispensable resources like air, water, and soil which requires millions of years to replenish.",
    "Humanity is continuously polluting indispensable resources like air, water, and soil which requires millions of years to replenish.",
    "Human overpopulation is one of the major ecological issues the world is facing.",
    "Many garbage patches exist in the oceans. The largest one covers more than 1.6 million square kilometers.",
    "Human use of pesticides and antibiotics have created super germs and plants, organisms with the ability to resist most drugs.",
    "Release of carbon dioxide has caused the oceans to become more and more acidic, killing coral reefs and shelled organisms.",
    "Humans have released more than 5.25 trillion pieces of garbage into the ocean.",
    "Red and brown tides, periods where algae grows rapidly, are caused by fertilizer leaking into the oceans.",
    "One-third of assessed fisheries are beyond their capacity.",
    "18 million acres of trees are clear-cut each year.",
    "Acid rain is caused by factories polluting the air.",
    "The ozone layer is being destroyed by human activity.",
    "Poaching is killing many endangered animals, and bringing them close to the point of extinction.",
    "Mercury accumulation in fish eventually comes back to bite as humans eat the fish.",
    "Three million people die each year because of air pollution.",
    "Light pollution is disrupting the natural activity of many organisms.",
    "Many rivers have run dry due to industrial activity."
  ],
  "improve": [
    "Reuse, Reduce, and Recycle.",
    "Save electricity by turning off appliances when not needed.",
    "Buy from ecologically friendly brands.",
    "Reduce carbon footprint by walking or biking if possible, instead of driving.",
    "Don’t waste water by opening the tap when you are not using it. ",
    "Cut down use of pesticides and herbicides, keep greenspace chemical free. ",
    "Plant more trees, or get plants and plant them in your backyard.",
    "Don’t buy clothes if you don’t need them.",
    "Donate to conservation efforts.",
    "Transition to digital files instead of paper.",
    "Donate to environmental charities such as the WWF.",
    "Volunteer for a wildlife or environmental organization.",
    "Don’t use plastic straws if you don’t need them.",
    "Reduce meat consumption.",
    "Don’t use plastic bags while going grocery shopping, use a fabric bag instead.",
    "If you have to drive, try mass transit or carpooling.",
    "Plant pollinator-friendly plants.",
    "Don’t spray pesticides or overuse fertilizers.",
    "Compost things.",
    "Shop organically by supporting local farmers.",
    "Purchase reusable bottles and containers instead of using single-use plastic bottles."
  ],
  "images": [
    "https://www.eartheclipse.com/wp-content/uploads/2016/02/environmental-pollution.jpg",
    "https://st.depositphotos.com/1488495/3840/v/600/depositphotos_38404195-stock-illustration-conserve-the-earth-environmental-pollution.jpg",
    "https://www.tutorialspoint.com/environmental_studies/images/pollutants.jpg",
    "https://i.pinimg.com/originals/ec/95/f0/ec95f01417267b3c05a198e16dcbf741.png",
    "https://static.vecteezy.com/system/resources/previews/000/368/716/non_2x/vector-deforestation-scene-at-daytime.jpg",
    "https://www.counterfire.org/images/stories/mar2018/madagascar-deforestation-lg.jpg",
    "https://thumbs-prod.si-cdn.com/qn4AI9OgMpkIMPe_99j_zaUmgTc=/fit-in/1600x0/https://public-media.si-cdn.com/filer/fa/8d/fa8d22e3-9b93-426c-bb3e-a0b8c28d122f/12685861633_1708f2dbff_o1.jpg",
    "https://i.guim.co.uk/img/media/27974093ba1227c5e6ba29794f15a8c72266c447/0_68_2048_1229/master/2048.jpg?width=445&quality=45&auto=format&fit=max&dpr=2&s=9ed032b527c4217b2df8020ce836b682",
    "https://www.ucsusa.org/sites/default/files/styles/original/public/images/1200-corndrought.jpg?itok=EAJuxQvZ",
    "https://img.lovepik.com/photo/40020/0061.jpg_wh300.jpg",
    "https://i.pinimg.com/736x/ba/3c/e7/ba3ce7e2bd8cb6cac3c95a0c0943acec.jpg",
    "https://www.imperial.ac.uk/ImageCropToolT4/imageTool/uploaded-images/newseventsimage_1614176492477_mainnews2012_x1.jpg",
    "https://lh3.googleusercontent.com/proxy/wMwoAippYPzGruQsUDdzS3VKC6HPgxwa0CunC35YqXihbPvQTAs1b1DX_nKegBFpEc3Kwusa6MMuAIe2SaUpWWcen7onDnDGxw",
    "https://image.freepik.com/free-vector/pollution-earth-with-dirty-smoke-from-factory-buildings_1639-11884.jpg",
    "https://e360.yale.edu/assets/site/GettyImages-1165944572_Mumbai-flooding_web.jpg",
    "https://i.pinimg.com/originals/48/ee/13/48ee1307af4f9b6b0ead7c3930c432f7.jpg",
    "https://thumbs.dreamstime.com/b/problem-recycling-garbage-household-waste-environmental-clogging-moscow-russia-may-big-city-container-littered-183213954.jpg",
    "https://i.pinimg.com/originals/0b/32/8a/0b328a4ca0ad1b793814c469db8f46a9.jpg",
    "https://images-na.ssl-images-amazon.com/images/I/41GslLz2SjL.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFKylEuqOYtCNT1kPoSPbMpH9B6UaLYPAXG3bFFkRlDzqcuTP5pp-k3SWDEip767GW9Z4&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqc0b4QS0aoOL13bA8hklgPqjCZSYjJ56PdubYu9noMJ83IAFpAcdAiEZhdnxa5oRs-6w&usqp=CAU",
    "https://image.freepik.com/free-vector/save-planet-concept-with-cute-smiling-earth_23-2148519535.jpg",
    "https://static.vecteezy.com/system/resources/previews/002/084/011/original/cute-earth-mascot-character-save-earth-cartoon-icon-illustration-free-vector.jpg",
    "https://i.ibb.co/wMdVMfn/image.png "
  ]
}

commands = ['$test', '$commands', '$description', '$fact', '$species', '$climate', '$ocean', '$quotes', '$trees', '$image', '$checkmessages', '$humanactivity', '$improve']

treesPlanted = 0

Client = discord.Client()

@Client.event
async def on_ready():
  print("we have logged in as {0.user}.format(Client)")

@Client.event
async def on_message(message):
  global messagesSent
  f = open("messagerecord.txt", 'rt+')

  if message.author == Client.user:
    return

  if message.content.startswith('$description'):
    await message.channel.send("Welcome to Envbot, a discord bot designed to help raise awareness on, and help, the environment. Try $commands to check out our commands! \n \n We have a tree-planting program. Every 1000 messages a server types, we will plant a tree. Check out the messages you've sent with $checkmessags!")

  if message.content.startswith('$test'):
    await message.channel.send("testing")
  
  if message.content.startswith('$fact'):
    await message.channel.send(EnvironmentalFacts['generalFacts'][random.randint(0, len(EnvironmentalFacts['generalFacts'])-1)])
    
  if message.content.startswith('$species'):
    await message.channel.send(EnvironmentalFacts['species'][random.randint(0, len(EnvironmentalFacts['species'])-1)])
  
  if message.content.startswith('$climate'):
    await message.channel.send(EnvironmentalFacts['Climate'][random.randint(0, len(EnvironmentalFacts['Climate'])-1)])
  
  if message.content.startswith('$trees'):
    await message.channel.send(messageCheck(str(message.guild)))
  
  if message.content.startswith('$ocean'):
    await message.channel.send(EnvironmentalFacts['Ocean'][random.randint(0, len(EnvironmentalFacts['Ocean'])-1)])

  if message.content.startswith('$quotes'):
    await message.channel.send(EnvironmentalFacts['Quotes'][random.randint(0, len(EnvironmentalFacts['Quotes'])-1)])

  if message.content.startswith('$humanactivity'):
    await message.channel.send(EnvironmentalFacts['humans'][random.randint(0, len(EnvironmentalFacts['humans'])-1)])

  if message.content.startswith('$images'):
    await message.channel.send(EnvironmentalFacts['images'][random.randint(0, len(EnvironmentalFacts['images'])-1)])

  if message.content.startswith('$improve'):
    await message.channel.send(EnvironmentalFacts['improve'][random.randint(0, len(EnvironmentalFacts['improve'])-1)])

  if message.content.startswith('$planted'):
    await message.channel.send("You have planted "+str(treesPlanted)+" trees.")

  if message.content.startswith('$server'):
    await message.channel.send("You are in "+str(message.guild))

  
  for i in f:
    value = i.split()
    if value[1] == str(message.guild):
      print(value[0])
      i.replace(value[0], str(int(value[0])+1))

  if not message.content.startswith('$'):
    messagesSent += 1
  
  if message.content.startswith("$checkmessages"):
    await message.channel.send("Server has typed "+str(messageCheck(str(message.guild)))+ " messages.")
  
  if message.content.startswith("$commands"):
    await message.channel.send(format_array(commands))
  
  f.close()
  
  

Client.run(os.getenv(key))