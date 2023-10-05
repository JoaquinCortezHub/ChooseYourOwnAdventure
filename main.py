from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from langchain.memory import CassandraChatMessageHistory, ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import json
cloud_config= {
    'secure_connect_bundle': 'secure-connect-ownadventure.zip'
}

with open("ownadventure-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]
ASTRA_DB_KEYSPACE = "database"
OPENAI_API_KEY = "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"

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

message_history = CassandraChatMessageHistory(
    session_id = "session",
    session = session,
    keyspace = ASTRA_DB_KEYSPACE,
    ttl_seconds = 3600
)

message_history.clear()

cass_buff_memory = ConversationBufferMemory(
    memory_key = "chat_history",
    chat_memory = message_history
)

template = """
You are now the guide of a ancient LoTR-like journey in Middle-Earth. 
A traveler named Joaquin seeks the lost ring to rule them all. 
You must navigate him through challenges, choices, and consequences based on Tolkien's books,
dynamically adapting the tale based on the traveler's decisions. 
Your goal is to create a branching narrative experience where each choice 
leads to a new path, ultimately determining Joaquin's fate. 

Here are some rules to follow:
1. Start the journey asking the player which race he wants to play as, based on Tolkien's books, this choice will grant the player with specific traits and abilities. remember the player's choice.
2. Continue by asking the player to choose some kind of weapons that will be used later in the game
3. Have a few paths that lead to success
4. Make the player make at least 15 decisions before concluding the journey.
5. Make other Tolkien's character to appear along the player's journey, the player can choose to include them in their team to help them fight and find the ring.
6. Have some paths that lead to death. If the user dies generate a response that explains the death and ends in the text: "The End.", I will search for this text to end the game

Here is the chat history, use this to understand what to say next: {chat_history}
Human: {human_input}
AI:"""

prompt = PromptTemplate(
    input_variables = ["chat_history", "human_input"],
    template = template
)

llm = OpenAI(openai_api_key = OPENAI_API_KEY)
llm_chain = LLMChain(
    llm = llm,
    prompt = prompt,
    memory = cass_buff_memory
)

choice = "start"
while True:
    response = llm_chain.predict(human_input = choice)
    print(response.strip())
    if "The End." in response:
        break

    choice = input("Your Reply:")