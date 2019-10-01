# Fall 2019 EC602-Mini-Project: PoppyTweets

## Jing Song U65712216 & Zhou Fang U03663101

### Our application "PoppyTweets" is designed for cinema owners and it is aimed to help them gain more profit and more popularity among customers. The application provides users with sentiment analysis of customers' tweets, which we retrieve tweet feeds from Twitter API and pass the related tweets to Google Natural Language API for further analysis. The users would be able to directly tell how positive or negative customers' tweets are about a specific movie, so that they could change their movie showing schedule accordingly.

## PoppyTweets' MVP:
###     “I, as a cinema owner, should be able to tell which movie that is currently showing receives the most positive feedback from our customers.”
### i.e. The user should be able to see the sentiment analysis of tweets on a specific movie that is shown at a specific movie theater<br/>

## Architecture:
<img src="https://github.com/daisysj/EC601-Mini-Project/blob/master/architecture_1.png"/>
<img src="https://github.com/daisysj/EC601-Mini-Project/blob/master/architecture_2.png"/>
<img src="https://github.com/daisysj/EC601-Mini-Project/blob/master/architecture_3.png"/>

## Contents:

 ### 1. [User Stories](https://github.com/daisysj/EC601-Mini-Project/blob/master/EC601%20Mini%20Project%201_%20User%20Stories.pdf)
 
 ### 2. [Architecture graph 1](https://github.com/daisysj/EC601-Mini-Project/blob/master/architecture_1.png)

 ### 3. [Architecture graph 2](https://github.com/daisysj/EC601-Mini-Project/blob/master/architecture_2.png)

 ### 4. [Architecture graph 3](https://github.com/daisysj/EC601-Mini-Project/blob/master/architecture_3.png)

 ### 5. [twitter_search.py](https://github.com/daisysj/EC601-Mini-Project/blob/master/twitter_search.py): handles Twitter API call within the terminal
 
 ### 6. [raw_twitter_search.py](https://github.com/daisysj/EC601-Mini-Project/blob/master/raw_twitter_search.py): handles Twitter API with flask
 
 ### 7. [google_NLapi.py](https://github.com/daisysj/EC601-Mini-Project/blob/master/google_NLapi.py): handles Google Natural Language API call

 ### 8. [app.py](https://github.com/daisysj/EC601-Mini-Project/blob/master/app.py): flask running main python function
 
 ### 9. [search_form.py](https://github.com/daisysj/EC601-Mini-Project/blob/master/search_form.py): flask homepage search form
 
 ### 10. [sample_twitter_apicall_results.txt](https://github.com/daisysj/EC601-Mini-Project/blob/master/sample_twitter_apicall_results.txt): a sample Twitter API call return before parsing
 
 ### 11. [templates](https://github.com/daisysj/EC601-Mini-Project/tree/master/templates): flask html templates

 ### 12. [Testing Documentation](https://github.com/daisysj/EC601-Mini-Project/blob/master/Testing%20Document.pdf)<br/><br/>

 ## How to run the project:
 ### Within Terminal: python twitter_search.py
 ### Flask Local Host Web Browser: python -m flask run<br/><br/>

 ## How we made it:
 ### API Calls: Twitter and Google Natural Language APIs offer a quite detailed description of how to make use of their APIs and there are many tutorials online to help us make the API call successfully. The main idea was to understand what we should pass to the API and what kind of object we should expect to receive. What we should pass is usually the API keys, tokens and query strings. For these, we have to read carefully through the API documentation to find the exact format. What we receive from the API is usually an json object, and we could parse it easily by referencing them with specific indexes. 
 ### Twitter to Google: After we got the results from Twitter API, we need to pass those tweets texts to Google Natural Language API. The way to make it is to call the python function what deals with Google API from the python file that handles Twitter API, so that we could pass whatever we want as a text to Google Natural Language API.
 ### Returns: What users want probably would not be two numbers, one representing the average sentiment score and the other representing the sentiment magnitude, what they want is more diret. So we develop a score scale system for the users, so that they could directly tell how positive is the sentiment, "quite" or "relatively", very suitable for users who are not good at Math.<br/><br/>
 
 
 ## Lesson Learned:
 ### What I really enjoyed was to see how our plan became the reality, and I think that is the fun part of project design. Though what we imagined would be quite different from what we were actually capable to make, doing the project is very satifying. 
 ### APIs such as Twitter and Google Natural Language have a quite well-built system and documentations already, so that we could access them with ease. However, there are many other softwares and platforms out there which have not had such a complete API system, so we could expect some difficulties to cope with them in the future.
 ### What we could do better next time is to build a more interactive user interface. Most users prefer simple and easy-understanding interfaces, and that should be one of the goals for every software ever made. Besides, there are a lot of potential functions and possibilities we could develop for our user interface, so that users could find what they need all on one page and access different functions more easily. 
 ### Cybersecurity is really a big problem, and we should never push our tokens and keys to github. People who wonder around the Internect are not always good, so we should pay extra attention to protecting personal information. Especially for Twitter API, exposing the keys could even lead to the disclose of other people's personal information, becuase we could retreive their account information. tention to protecting personal information. Especially for Twitter API, exposing the keys could even lead to the disclose of other people's personal information, becuase we could retreive their account information. While we are getting what we want from the API, we should always be mindful of the security problem.

