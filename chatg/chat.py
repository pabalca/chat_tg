import openai
import os


# OpenAI API key
chat_key = os.getenv("CHAT_TOKEN")
openai.api_key = chat_key


def question(question_text):
    # send the question to the ChatGPT model and get the response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    answer = response.choices[0].text.strip()
    return answer

    # format the response as a code block
    # formatted_answer = f"```python\n{answer}\n```"

    # send the formatted answer to the Telegram chat
    # bot.send_message(chat_id=chat_id, text=formatted_answer, parse_mode=telegram.ParseMode.MARKDOWN)
