from flask import Flask, render_template, request,redirect
import create,os,datetime
app = Flask(__name__)

# getのときの処理
@app.route('/', methods=['GET'])
def get():
  t_delta = datetime.timedelta(hours=9)
  dt = datetime.datetime.now(datetime.timezone.utc)+t_delta
  data1 =request.args.get('name', '')
  if data1=="":
    return render_template("index.html",d_month=dt.month,d_day=dt.day)
  hyouka1 =request.args.get('j', '')
  hyouka2=request.args.get("k","")
  hyouka3=request.args.get("h","")
  nextn=request.args.get("next","")
  month=request.args.get("month","")
  day=request.args.get("day","")
  jikan=request.args.get("jikan","")
  yokatta=request.args.get("yokatta","")
  mochi=request.args.get("mochi","")
  shuku=request.args.get("shuku","")
  create.main(hyouka1,hyouka2,hyouka3,"response",data1,nextn,month,day,jikan,yokatta,mochi,shuku)
  return redirect('/static/response.png')
@app.route('/')
def aaa():
  t_delta = datetime.timedelta(hours=9)
  dt = datetime.datetime.now(datetime.timezone.utc)+t_delta
  dt_text = f"{dt.month}/{dt.day} {dt.minute}:{dt.second}"
  return render_template("index.html",d_month=dt.month,d_day=dt.day,d_time=dt_text)


# postのときの処理	

app.run("0.0.0.0",port=os.getenv("PORT"))
