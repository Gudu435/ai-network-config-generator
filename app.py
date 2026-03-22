from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_config(user_input):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a Cisco network engineer. Output only CLI commands. No explanation."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    return response.choices[0].message.content


def is_safe(config):
    blocked = ["reload", "erase", "format", "delete", "write erase"]
    return not any(word in config.lower() for word in blocked)


@app.route("/", methods=["GET", "POST"])
def index():
    output = None

    if request.method == "POST":
        user_input = request.form["user_input"]
        config = generate_config(user_input)

        if is_safe(config):
            output = config
        else:
            output = "❌ Unsafe configuration detected!"

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
