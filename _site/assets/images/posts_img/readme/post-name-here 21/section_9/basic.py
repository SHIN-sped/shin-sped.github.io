from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField("What Breed are you?")
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    breed = None  # Initialize breed here

    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''
    
    return render_template('index.html', form=form, breed=breed)

if __name__ == '__main__':
    app.run(debug=True)
    
# Flask가 여전히 index.html 템플릿을 렌더링하려고 시도하고 있지만 찾을 수 없는 것 같습니다. "TemplateNotFound: index.html" 오류 메시지는 Flask가 'index.html' 템플릿 파일을 찾을 수 없음을 나타냅니다.

# 다음 사항을 확인하십시오.

# index.html 파일이 올바른 디렉토리에 있는지 다시 확인하세요.
# 파일 이름이 실제로 'index.html'(모두 소문자)이고 파일 확장자가 '.html'인지 확인하세요.
# index.html 파일이 Flask 애플리케이션(basic.py)이 있는 동일한 디렉터리에 있는지 확인하세요.
# 여전히 문제가 발생하는 경우 프로젝트의 디렉터리 구조, index.html 파일 위치, Flask 애플리케이션 실행 방법에 대한 자세한 정보를 제공해 주세요. 이렇게 하면 보다 구체적인 지원을 제공하는 데 도움이 됩니다.