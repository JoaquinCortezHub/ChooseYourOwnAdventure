# Choose Your Own Adventure 🗺️
Python terminal choose your own adventure-like game inspired in LoTR
## Idea 💡
The idea for this project cem from Tech With Tim's [Python AI Choose Your Own Adventure Game](https://www.youtube.com/watch?v=nhYcTh6vw9A) video. 
I decided to follow this project to learn more about how APIs work and to recreate this childhood classic game. I just modified the LLM's prompt
to make the AI give prompts related to "The Lord of The Rings" series.
## Installation & Usage 🛠️
To run this project correctly you should:
1. Go to the [Datastax](https://www.datastax.com) website and create a new vector database.
  - Make sure to select **Python** as your **driver** and follow the database setup guide.
  - you** must** download your Datastax secret bundle and token in the **same directory as your project**.
2. Go to the [OpenAI platfrom](https://platform.openai.com) website and get your API key.
3. you need to install these packages using pip:
  - cassio
  - langchain
  - openai
  - tiktoken
4. You need to import these to properly run the game:
  - from langchain.memory import CassandraChatMessageHistory, ConversationBufferMemory
  - from langchain.llms import OpenAI
  - from langchain.chains import LLMChain
  - from langchain.prompts import PromptTemplate
## Prompting the AI 🤖
You'll find a space in the code where the prompt for the AI is, change this to your liking to instruct the AI on how to act and what to include
in the game.
> [!Warning]
> DO NOT delete the last instruction where it tells the AI to finish the game with a **"The End."** text. This will break the code.

You can give the AI as many rules as you like to make the game more or less specific and accurate.
## Help & Support

