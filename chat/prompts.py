SYSTEM_PROMPT = """
# Background information

I want to improve the learning process by using flash cards for a given topic

# Instruction

I will give you a text.  I'd like you to create flash cards in form {"question1": "answer1", "question2": "answer2", "question3": "answer3"} for this text. The information in the flash cards should be obligatory correct and based on the input text. Answer only with the flash cards, no other text.

# Example 

## Input text
Bulgaria, officially the Republic of Bulgaria,is a country in Southeast Europe. It is situated on the eastern portion of the Balkans directly south of the Danube river and west of the Black Sea. Bulgaria is bordered by Greece and Turkey to the south, Serbia and North Macedonia to the west, and Romania to the north. It covers a territory of 110,994 square kilometres (42,855 sq mi) and is the tenth largest within the European Union and the sixteenth-largest country in Europe by area. Sofia is the nation's capital and largest city; other major cities include Burgas, Plovdiv, and Varna. 
One of the earliest societies in the lands of modern-day Bulgaria was the Karanovo culture (6,500 BC). In the 6th to 3rd century BC, the region was a battleground for ancient Thracians, Persians, Celts, and Macedonians; stability came when the Roman Empire conquered the region in AD 45. After the Roman state splintered, tribal invasions in the region resumed. Around the 6th century, these territories were settled by the early Slavs. The Bulgars, led by Asparuh, attacked from the lands of Old Great Bulgaria and permanently invaded the Balkans in the late 7th century. They established the First Bulgarian Empire, victoriously recognised by treaty in 681 AD by the Byzantine Empire. It dominated most of the Balkans and significantly influenced Slavic cultures by developing the Cyrillic script. Under the rule of the Krum's dynasty, the country rose to the status of a mighty empire and great power. The First Bulgarian Empire lasted until the early 11th century, when Byzantine emperor Basil II conquered and dismantled it. A successful Bulgarian revolt in 1185 established a Second Bulgarian Empire, which reached its apex under Ivan Asen II (1218–1241). After numerous exhausting wars and feudal strife, the empire disintegrated and in 1396 fell under Ottoman rule for nearly five centuries


## Example output
{"How big is the territory of Bulgaria?": "110,994 square kilometres", "When was Bulgaria recognized as a country?": "681 AD", "Until when lasted the First Bulgarian Empire?": "Until early 11th century"}


Input text:
"""

