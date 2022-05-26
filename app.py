import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        name = request.form["name"]
        role = request.form["role"]
        field = request.form["field"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_prompt(name, role, field),
            temperature=0.6,
            max_tokens=1000
        )

        return render_template("index.html", result=response.choices[0].text)

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(name, role, field):
    return """Write a verbose academic letter of recommendation.

Name: Paige
Role: Psychology Fellowship
Field: Developmental Psychology
Letter: I am writing to strongly support Paige's application for the fellowship. I have known her since Fall 2020 when she enrolled in my developmental psychology class. \n Paige has produced very thoughtful work in my course, engaging with the readings in both personal and analytical ways. She did not shy away from difficult and complex topics and often has been a wonderful source of critical thinking in our discussions, offering nuanced perspectives and asking questions that prompted the group members to think more thoroughly through their stated positions.

Name: Annie
Role: Graduate Program
Field: Neuroimaging
Letter: I am writing to strongly recommend Annie for admission in your program. Annie joined our lab as an undergraduate research assistant last year after taking a neuroscience class with my graduate student. In short, Annie has been a superstar. She has not been involved in data collection but has been deeply involved in multimodal neuroimaging data analysis and will be second author of a poster at a conference based on her work this spring. She would be an excellent addition to any team.

Name: {}
Role: {}
Field: {}
Letter:""".format(
        name.capitalize(),
        role.capitalize(),
        field.capitalize()
    )
