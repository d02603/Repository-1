from flask import Flask, request, jsonify
import openai

# 🔹 Вставь свой API-ключ OpenAI
API_KEY = os.getenv("OPENAI_API_KEY")

# Создаём сервер Flask
app = Flask(__name__)

@app.route("/v1/chat/completions", methods=["POST"])
def chat():
    data = request.json
    data["model"] = "gpt-4o-mini"  # 🔹 Принудительно подменяем модель

    # Отправляем запрос в OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=data["messages"],
        api_key=API_KEY
    )

    return jsonify(response)

if __name__ == "__main__":
    app.run(port=5001)  # Запускаем сервер на локальном порту
