from flask import Flask
from flask import flash, render_template, request, redirect, url_for
from search_form import TweetSearchForm
import raw_twitter_search as raw_search
import google_NLapi as google_analyze
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/', methods=['GET', 'POST'])
def home():
    search = TweetSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('homepage.html', form=search)
 
@app.route('/results')
def search_results(search):
    global results
    search_string = search.data['search'] 
    if search_string == "":
        flash('Please type in key words to start searching!')
        return redirect('/')
    
    results = raw_search.get_raw_tweets(search_string)

    if not results:
        flash('No results found!')
        return redirect('/')

    else:
        # display results
        return render_template('display_twitter.html', results=results)

@app.route("/analysis")
def analyze_results():
    analysis = ""
    score = 0
    mag = 0
    for i in results:
        sentis = google_analyze.analyze_sentiment(i.text)
        score = score + sentis[0]
        mag = mag + sentis[1]

    score = score / len(results)
    mag = mag / len(results)

    analysis = "The average sentiment score is: " + str(score)
    analysis = analysis + "; The average sentiment magnitude is: " + str(mag)

    if (score <= -0.5):
        analysis = analysis +  "; The sentiment is quite negative"
    elif ((score > -0.5) & (score < 0)):
        analysis = analysis + "; The sentiment is relatively negative"
    elif ((score < 0.5) & (score >= 0)):
        analysis = analysis + "; The sentiment is relatively positive"
    elif (score >= 0.5):
        analysis = analysis + "; The sentiment is quite positive"
    
    return render_template('display_google.html', analysis = analysis)

if __name__ == '__main__':
    
    sess.init_app(app)
    app.debug = True
    app.run()