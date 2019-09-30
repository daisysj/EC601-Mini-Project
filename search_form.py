from wtforms import Form, StringField
 
class TweetSearchForm(Form):
    search = StringField('')