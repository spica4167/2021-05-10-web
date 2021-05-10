from flask import Flask, request, render_template , redirect, url_for #flask, request, render_template, redirect를 사용한다. java.util.~~과 비슷한역활
app = Flask(__name__)

@app.route('/kakao')
def dsa():
    return redirect("https://daum.net/") #redirect를 이용한 다음으로 연결.

@app.route('/url_test')
def url_test():
    return redirect(url_for('nsa')) #이동시 404 not found 오류발생. 정의된것이 없음.

@app.route('/move/<site>')
def move_site(site): #파라미터의 값이 무엇이냐에 따라 네이버나 다음이 실행이된다.
    if site == 'nsa':
        return redirect(url_for('nsa'))
    elif site == 'dsa':
        return redirect(url_for('dsa'))
    else :
        return '없는 페이지'

@app.route('/nsa')
def nsa():
   return redirect("https://naver.com/")
   # return render_template("nsa.html") #스크립트 동작시 네이버로 자동연결. / nsa.html에서 location.href="/dsa"로 변경해주면 다음으로 연결된다.

@app.route('/')
def hello():
    return 'Hello World!'

        #로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
     return render_template('login.html') #login.html을 보여달라 요청.
    else:
        id = request.form['id']
        pw = request.form['pw']
    #id 와 pw가 임의로 정한 값이랑 비교해서 참이다 거짓이다
    if id == 'abc' and pw == '1234':
        return "반갑습니다 {}님.".format(id)
    else:
        return "아이디 또는 패스워드를 확인 하세요."

@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL을 확인하여 주세요.", 404 #플라스크 기본 404명령어를 내가 원하는것으로 변경.
if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('dsa')) # das로 지정된 링크를 가져와서 실행, das에 해당한 링크를 그대로 가져와서 실행하게됨.
    app.run(debug=True) #이것으로 인해 env 환경에서 python app.py로 실행이 가능하다.