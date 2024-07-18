import os
from pydantic.v1 import BaseModel, Extra, Field
from langchain_community.chat_models import ChatOpenAI 
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import JsonOutputParser
from pydantic.v1 import ValidationError


# Autentictaing OpenAI
os.environ["OPENAI_API_KEY"] = "sk-proj-QMuZDXyQkZaj7xq5pevKT3BlbkFJSMmXWvYkAXCn6DBAJ5aU"

# Example tweet and their metadata
# Our aim is to screen the tweet with political and offensive langugage using pydantic

raw_tweets = [
    {"id":"001", "text":"It's been a week since the Sparks Valley fire roared to the life and its now the largest wildfire in history.","date":"03-04-2024"},
    {"id":"002", "text":"Video of the flames destroying my neighbourhood. **** that fire! #firesucks", "date":"03-04-2024"},
    {"id":"003", "text":"I blame Joe Biden for the #sparkvalleyfire response", "date":"02-09-2024"}
]


# So, we need to define a pydantic model with Ispolictal and isOffensive properties
# config class with in model configuration enforces the strict validation by forbidding any extra field not explicitly definded in the model
class Tweet(BaseModel):
    isPolitical: bool = Field(description="Whether the tweet is political")
    isOffensive: bool = Field(description="whether the tweet is offensive")

    class Config:
        extra = Extra.forbid


llm = ChatOpenAI(model="gpt-4o")
parser = JsonOutputParser(pydantic_object=Tweet)

screened_chat = []

# Function for checking and screening the tweets
def check_tweet(tweet):
    tweet_text = tweet["text"]
    print(tweet_text)

    # Now we need to create a prompt for feeding to the llm
    prompt  = PromptTemplate(
        template=""" 
        Assess whether the tweet contain references to any politicians or political parties.
        Assess if the tweet contains offensive language.
        {format_instruction}
        {tweet_text}
        """,
        input_variables=["query"],
        partial_variables={"format_instruction": parser.get_format_instructions()}
    )

    chian = prompt|llm|parser
    result = chian.invoke({"tweet_text":tweet_text})
    print(result)
    if not(result["isPolitical"]) and not(result["isOffensive"]):
        screened_chat.append(tweet_text)
        print("Screened and Pass")
    else:
        print("Contain sensitive content and thus failed")
    
    print("\n")
    print("---------------------------------------------------------")


# Iterating through every raw tweet
for tweet in raw_tweets:
    check_tweet(tweet=tweet)