from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)
app.secret_key = "여기는 플래그 자리였습니다. 코드를 잘 해독하여 풀어보세요."

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''

    if request.method == 'POST':
        user_input = request.form['input']
        try:
            # 사용자 입력을 템플릿 문자열로 평가
            result = render_template_string(user_input)
        except Exception as e:
            result = str(e)

    return render_template('ssti_first.html', result=result)

@app.route('/ssti', methods=['GET', 'POST'])
def ssti():
    result = ''

    if request.method == 'POST':
        user_input = request.form['input']
        try:
            # 사용자 입력을 템플릿 문자열로 평가
            result = render_template_string(user_input)
        except Exception as e:
            result = str(e)

    return render_template('ssti_index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
