from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import config
import openai

openai.api_key = config.OPENAI_API_KEY

app = Flask(__name__, static_folder=config.UPLOAD_FOLDER)

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route('/some-page', methods=["GET", "POST"])
def somePage():
    return render_template('some-page.html', **locals())

@app.route('/discover-careers', methods=["GET", "POST"])
def discoverCareers():
    return render_template('discover-careers.html', **locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)

@app.route("/chat", methods=["POST"])
def chat():
    input_text = request.json.get("input", "")
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    output_text = response.choices[0].text.strip()
    return jsonify({"output": output_text})