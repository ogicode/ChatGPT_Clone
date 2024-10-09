from flask import Flask, render_template, request, jsonify
from openai import OpenAI

# Initialize Flask app
app = Flask(__name__)

# Set your OpenAI API key
client = OpenAI()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("question", "")
    if not user_message:
        return jsonify({"response": "No question provided."})

    try:
        # Call the OpenAI API using your specified method
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        answer = completion.choices[0].message.content.strip()
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"response": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
