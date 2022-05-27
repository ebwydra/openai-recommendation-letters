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
            #engine="davinci:ft-personal-2022-05-26-22-42-44",
            prompt=generate_prompt(name, role, field),
            temperature=0.6,
            max_tokens=2000,
            frequency_penalty=1
        )

        return render_template("index.html", result=response.choices[0].text.split('\n'))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(name, role, field):
    return """Write an academic letter of recommendation.

Name: Emily Stone
Role: Postdoctoral Associate
Field: Developmental Psychology
Letter: It is my pleasure to write in strong support of the application of Emily Stone for the postdoctoral position in your lab. Emily defended her dissertation and completed her doctoral degree this month. I have had the pleasure of being Emily’s primary mentor throughout her graduate training. Emily sailed through our doctoral training program with flying colors, receiving the highest grades and very top marks on her qualifying exams. In short, Emily is a superb, highly motivated, and talented student, and one of the most promising young scientists I have mentored in the past 35 years.  She is dedicated to an academic research career in developmental science, and I have no doubt that she has the motivation, skills, and ability to succeed.\n\nEmily has an impressive array of advanced quantitative skills! She has completed our department’s quantitative minor and enjoys working with large data sets. She has an exceptionally strong knowledge base in advanced quantitative methods.  In particular, she is skilled in correlation/regression approaches, structural equation modeling, including growth curve modeling of longitudinal data, mediation and moderation, and methods for estimating missing data.\n\nOn a personal level, Emily is a pleasure to work with.  She is enthusiastic, positive, and constructive and enjoys interacting with others at all levels, faculty, students, and colleagues, alike. Emily has surmounted hardships, both financial and personal, to create educational opportunities and a career path for herself.  She comes from a challenging background and is the first in her family to attend and graduate from college and obtain a graduate degree. She knows the importance of fostering a sense of inclusiveness firsthand, appreciates diversity, and is committed to fostering equity and opportunities for students of all backgrounds.\n\nEmily has a clear and strong passion for conducting research to uncover the origins and developmental pathways to outcomes including language and social-emotional functioning in typical and atypical development. She has the talent, skills, and the drive necessary to succeed and to make important contributions to this field.  In sum, I enthusiastically and without reservation recommend Emily Stone for your postdoctoral position. She is a truly exceptional young scientist with a very promising career ahead.  Please let me know if you need any additional information.

Name: Kendall Brown
Role: Postgraduate Fellowship
Field: Psychology
Letter: I’m extremely pleased to recommend Kendall Brown for a fellowship in developmental psychopathology and social neuroscience. Kendall was a student in three of my classes. In addition, Kendall served as my prefect (i.e., TA) last fall for my introductory psychology course.\n\nKendall did extremely well in all three classes, earning A’s in every one. She is an excellent writer, and her work reflects an agile, thoughtful mind in operation. In the two discussion-based classes she was a thoughtful and consistent contributor, and was always prepared for class. Because of her superior performance, I asked her to be the teaching assistant for my introductory psychology course.\n\nThe feedback I received from students about Kendall after the course was quite positive. They noted that she was extremely helpful during review sessions, and they liked her positive approach. I think she has great potential to become a professor, should she choose the academic path.\n\nStudent comments on Kendall’s performance as a teaching assistant support my own observations and impressions. I find Kendall to be open, positive, empathic, and warm in all of her interactions. She leaves a room with more positive energy in it than when she entered.\n\nOne last comment concerns an aspect of a student that I suspect rarely gets mentioned in letters of recommendation, but should, in my opinion. Kendall is a member of the women’s softball team. Not only does she have considerable experience being part of a team, but she plays in a sport that involves a high rate of failure and often means performing under painfully cold conditions. In short, she’s tough and can handle adversity.\n\nIn summary, I have really high regard for Kendall Brown. She’s a bright and capable student, a conscientious worker, and a truly decent human being. I enthusiastically recommend her for this fellowship

Name: Mohammed Assad
Role: Research Assistant
Field: Computer Science
Letter: I am pleased to write a letter of recommendation for Mohammed Assad. I highly recommend Mohammed to your organization for the position of research assistant.\n\nI have known Mohammed for the past four semesters as he has taken the following courses that I teach: Intermediate Programming, Data Structures and Analytics, and Ethics in Artificial Intelligence. As his professor, I have had an opportunity to observe his participation and interaction in class and to evaluate Mohammed’s knowledge of the subject matter. In short, he is an outstanding student in all respects. Mohammed has proven that through hard work, follow-through, and teamwork, he can accomplish tasks in a courteous and timely manner.\n\nMohammed is well equipped to grow from challenges that he is presented with. His strong programming skills, passion for social justice, and ability to relate to others prepare him beautifully for work in your organization. In summary, I strongly endorse making Mohammed Assad a member of your team. Please do not hesitate to contact me if I can provide any further information in support of Mohammed’s application.

Name: Ian Harris
Role: Residency
Field: Medicine
Letter: It is my pleasure to write in support of the application of Mr. Ian Harris for your residency program. I have been an educator for decades with considerable experience with national organizations. I worked closely with Mr. Harris during his third-year clerkship as well as during his acting internship.  As is evident from his CV, Mr. Harris has excelled throughout his career with many notable accomplishments which I will not repeat here. I will focus on my experiences with Mr. Harris, primarily those related to his clinical abilities and which demonstrate the qualities necessary for your residency: excellent knowledge, clinical skills, patient care, and leadership. I have observed Mr. Harris in both the inpatient and outpatient setting, taught him in class, and overseen his performance during his clerkship and acting internship.\n\nIn addition to considerable intellect and exemplary performances on standardized examinations, Mr. Harris is a warm, engaging individual who teaches others by example, is inclusive, and consistently exhibits curiosity and motivation to learn. He comes prepared for all types of learning situations, having researched the relevant topics so that he can provide quality care as well as participate actively in class and clinical supervision. Mr. Harris is articulate, well‐read, and able to utilize his knowledge effectively in the clinical setting.  In addition to prioritizing his own learning, Mr. Harris considers the needs of others. On multiple occasions, he has arrived in clinic with handouts on relevant clinical topics tailored for the rest of the medical team.  He has been described as one of the best students to rotate on our service by our residents and several attending physicians.  A colleague was so impressed by Mr. Harris’ knowledge and skills that she invited him to give a presentation during Grand Rounds. His presentation was outstanding – comprehensive in scope yet presented efficiently and effectively. On his own time, Mr. Harris designed a well‐conceived, thorough study protocol on risk factors for readmission within 30 days to our inpatient service.\n\nIn conclusion, I am happy to give Mr. Harris my highest recommendation for your residency program. In my experience, he is in the top 10% of all medical students with whom I have worked over the past 20 years. If you have any additional questions or require further information, please do not hesitate to contact me.

Name: Divya Agarwal
Role: Medical School
Field: Developmental Neuroscience
Letter: It is my great pleasure to write a letter of recommendation for Divya Agarwal.  I have known Divya for over one year.  My impressions of her are based on the comparison between Divya and 20-some other research assistants and research fellows who have worked in my lab over the past decade.  This reference group consists of highly selected, bright, and motivated post-baccalaureate individuals who typically spend two years working with our group before pursuing graduate studies in psychology or medicine.  Divya distinguishes herself from this group as a highly talented and driven person with strong computational skills and deep dedication to improving lives of individuals with developmental disabilities through translational research.\n\nDivya's position requires great technical and clinical skills, as well as ability to work with a highly interdisciplinary team of researchers across several departments.  Divya has excelled on all fronts, as she moves seamlessly from handling concerned parents and their distressed children, to interfacing with clinicians, and to designing new experimental procedures and improving our eye tracking data pre-processing pipeline.\n\nDivya learned very quickly how to run multi-software (MATLAB, Python, Perl, R) pipelines and has become the lead fellow on several quality control (QC) and pre-processing data pipelines.  It usually takes about a year to obtain the level of proficiency that Divya demonstrated after only a few months. Even after being shown something like a new bit of R or SQL syntax just once, she can quickly apply it in novel situations. She has mastered the art of reporting QC results and has developed great skill in troubleshooting any obstacle that comes her way. Divya is also a strong communicator and translates difficult concepts well to colleagues.\n\nDivya shows great promise for a successful career in medicine and in research aimed at improving care and ultimately quality of life of patients. I recommend Divya for your program with the greatest enthusiasm and no hesitation.  It has been a great pleasure to see her grow as a person and to crystallize her professional interests.  Please do not hesitate to contact me directly with any further questions.

Name: {}
Role: {}
Field: {}
Letter:
""".format(
        name.capitalize(),
        role.capitalize(),
        field.capitalize()
    )
