
import glob
import openai
from gpt import GPT
from gpt import Example
import pandas as pd
import json
from pandas import json_normalize
import time

# configure GPT
openai.api_key = "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"
gpt = GPT(engine="text-davinci-002",
          temperature=0.5,
          output_prefix="Output: \n\n",
          max_tokens=100)

df = pd.read_csv('/Users/maximushan/Desktop/MLLU/headlines.csv',delimiter='@', header = 0)
responses = []
print("running")
#gpt.add_example(Example("Replace this sentence with slang: Trump's Scottish Golf Resort Pays Women Significantly Less Than Men: Report", "Trump's Scottish Golf Resort Pays Women Like Trash Compared to Men: Report"))
#gpt.add_example(Example("Replace this sentence with slang: The New York Knicks get embaressed in 23 point loss.", "The New York Knicks get rekt."))
#gpt.add_example(Example("Replace this sentence withS slang: Samantha Bee's Parents Think America Is Basically A War Zone", "Samantha Bee's Parents Think America Is Basically Pew Pew and Boom Boom"))
#gpt.add_example(Example("Replace this sentence with slang: North Korea Still Open To Talks After Trump Cancels Summit", "North Korea Still Open To Talks After Trump Yeets from Summit"))
#gpt.add_example(Example("Replace this sentence with slang: Justworks Postpones IPO, Citing Market Conditions", "Justworks just put their IPO on the back burner due to stiff market conditions"))
#gpt.add_example(Example("Replace this sentence with slang: Chevron Rakes in $15.6 Billion in Annual Profits as Oil Prices Climb", "Chevron makes bank"))
#gpt.add_example(Example("Replace this sentence with slang: Tailgating in the Time of Inflation", "Inflation sucks! Let's go tailgate!"))
#gpt.add_example(Example("Replace this sentence with slang: Australia Takes the Initiative in the Pacific", "Australia's been stepping up their game in the Pacific lately."))
#gpt.add_example(Example("Replace this sentence with slang: Investors Begin to Get Picky on Manager Selection", "Investors Begin to Get Fussy on Manager Selection"))
#gpt.add_example(Example("Replace this sentence with slang: The Left Defends the Legacy of Redlining", "lefties be defending they shit"))
#gpt.add_example(Example("Replace this sentence with slang: How to Quit Your Job Gracefully", "How to Quit Your Job Without Burning Bridges"))
#gpt.add_example(Example("Replace this sentence with slang: The Filibuster Helps Nobody, and That Means You", "That filibuster's ain't helpin' nobody."))


print("examples loaded")

for example in df['Prompt']:
    prompt = "Replace this sentence with slang: " + example
    output = gpt.get_top_reply(prompt)
    print(prompt + ": " + output)
    responses.append(output)
#df['Responses'] = responses
df2 = pd.DataFrame(responses, columns=['Prompt'])
fileNameOutput = "/Users/maximushan/Desktop/MLLU/data" + str(time.time())
df.to_csv(fileNameOutput+'.csv')
df2 = df2.replace(r'\n',' ', regex=True) 
df2.to_csv(fileNameOutput+'responses.csv')



# Inferences
# prompt = "sort list in python"
# output = gpt.get_top_reply(prompt)
# print(prompt, ":", output)
# print("----------------------------------------")

# prompt = "Code weather api in python"
# output = gpt.get_top_reply(prompt)
# print(prompt, ":", output)
# print("----------------------------------------")

# prompt = "What is 876+89"
# output = gpt.get_top_reply(prompt)
# print(prompt, ":", output)
# print("----------------------------------------")