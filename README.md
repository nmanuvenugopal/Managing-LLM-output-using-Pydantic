# Managing-LLM-output-using-Pydantic
Managing LLM output using Pydantic

This project aims to screen tweets for political and offensive language using Pydantic for data validation and LangChain for language model processing. The primary goal is to identify and 
filter tweets containing political references or offensive language, ensuring strict validation rules through Pydantic.

### Explanation
1. Imports: Necessary libraries are imported, including Pydantic for data validation and LangChain for handling language model tasks.
2. Example Tweets: A list of example tweets is provided, each containing an ID, text, and date.
3. Pydantic Model: A Pydantic model Tweet is defined with two fields: isPolitical and isOffensive. The Config class enforces strict validation by forbidding extra fields.
4. LLM and Parser: A language model llm is initialized using the ChatOpenAI model, and a JSON parser is set up to parse the output into the Tweet Pydantic model.
5. Tweet Screening Function: The check_tweet function processes each tweet by creating a prompt and feeding it to the LLM. The LLM's output is parsed and printed.
6. Tweet Iteration: The script iterates through each raw tweet, invoking the check_tweet function to screen them for political and offensive content.

### Output
![image](https://github.com/user-attachments/assets/c8eef7a5-44ef-4bef-ae31-4eb0bcee5cd4)

### Reference
Controlling Large Language Model output with Pydantic - Matt Chinnock (Medium article)

