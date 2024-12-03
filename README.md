##  Mental Health Chatbot Documentation
**This documentation provides a detailed explanation of the Python, HTML, CSS and JavaScript code for the Mental Health Chatbot developed by me.**
**The chatbot is built using Python, Flask, and ChatterBot, and it is designed to offer basic mental health support and mindfulness guidance.**


# AIM
The Mental Health Chatbot aims to provide users with support for common mental health challenges, mindfulness techniques, and crisis resources. It uses pre-trained conversational data to simulate helpful responses and includes additional custom responses for mental health contexts.


# Problems this Mental Health Chatbot will solve
**(1) People faced with limited barriers to seeking mental health support such as lack of insurance, long waitlists, or social stigma.**
**(2) Individuals struggling with mental health conditions who find it challenging to monitor and manage their symptoms**
**(3) People already already bedeviled by mental issues requiring immediate support and guidance for their absolute safety**
**(4) Individuals with mental health conditions that has led to them to habitually living a life of loneliness, social withdrawal, and emotional disconnection from life**


# Benefits to users:
1. Convenient and accessible support: This chatbot provides users with easy access to mental health support, whenever and wherever they need it.
2. Personalized support and guidance: By leveraging AI and machine learning, this chatbot will immensely offer tailored advice, resources, and support to users based on their specific needs and concerns.
3. Improved symptom management: This chatbot can help users track their symptoms, identify patterns, and develop strategies for managing their mental health.
4. Reduced feelings of loneliness and isolation: By providing a supportive and non-judgmental space, this chatbot will help users feel more connected and less alone in their struggles.
5. Crisis intervention and support: In times of crisis, this chatbot can offer immediate support, guidance, and resources to help users ensure their safety and well-being.
6. Anonymity and confidentiality: This chatbot will provide users with a safe and confidential space to discuss their mental health concerns, without fear of judgment or repercussions.
7. Scalability and reach: By leveraging technology, this chatbot can reach a wider audience, including those in remote or underserved areas, and provide support to a larger number of users.


# Features

**Chatbot Conversation:**
    => Responds to user messages with predefined responses or dynamically using ChatterBot's BestMatch logic.

**Mindfulness Prompts:**
    => Offers mindfulness exercises on request.

**Crisis Resources:**
    => Shares contact information for mental health crisis resources.

**Web Interface:**
    => Interactive web page for users to chat with the bot.


## My Python Code Explanation


## (1) Imports

`from chatterbot import ChatBot`
`from chatterbot.trainers import ListTrainer`
`from flask import Flask, render_template, request`
`import random`

**(a) ChatterBot and ListTrainer: Used to create and train the chatbot.**
**(b) Flask: Framework for creating the web application.**
**(c) random: Generates random mindfulness prompts.**

## (2) Flask Application Setup

`app = Flask(__name__)`

**Initializes the Flask web application.**

## (3) ChatBot Initialization

`bot = ChatBot(`
    `"chatbot",`
    `read_only=True,`
    `logic_adapters=[`
        `{`
            `"import_path": "chatterbot.logic.BestMatch",`
            `"default_response": "Sorry, I don't have an answer.",`
            `"maximum_similarity_threshold": 0.9`
        `}`
    `]`
`)`

**(a) ChatBot: Creates a chatbot instance named "chatbot".**
**(b) read_only: Ensures the bot does not learn during conversations.**
**(c) logic_adapters:**
    Configures the bot to use the BestMatch logic adapter to find the closest matching response.
    Sets a default response if no match is found.
    Limits response similarity with a threshold of 0.9.


## (4) Training the Chatbot

`trainer = ListTrainer(bot)`
`trainer.train(mental_health_data)`

**(a) ListTrainer: Trains the bot using the custom mental_health_data dataset.**
**(b) mental_health_data: Contains predefined question-response pairs relevant to mental health.**


## (5) Additional Features

**(a) Mindfulness Prompts**
    => A list of mindfulness tips to provide when requested.

`MINDFULNESS_PROMPTS = [`
    `"Take a deep breath and exhale slowly. Repeat 3 times.",`
    `"Close your eyes and list 3 things you are grateful for today.",`
    `"Focus on your surroundings. What can you see, hear, and feel right now?"`
`]`


**(b) Crisis Resources**
    => A list of mindfulness tips to provide when requested.

`CRISIS_RESOURCES = [`
    `{"name": "National Suicide Prevention Lifeline", "contact": "1-800-273-8255"},`
    `{"name": "Crisis Text Line", "contact": "Text HOME to 741741"},`
    `{"name": "SAMHSA Helpline", "contact": "1-800-662-4357"}`
`]`


## (6) Flask Routes

## (I) Main Page
    **Serves the index.html file as the main web page.**

`@app.route("/")`
`def main():`
    `return render_template("index.html")`

## (II) Chatbot Response
    **Handles user messages sent from the web interface and returns a bot response.**

`@app.route("/get")`
`def get_chatbot_response():`
    `userText = request.args.get('userMessage')`
    `return str(bot.get_response(userText))`



## Mental Health Chatbot - HTML, CSS, and JavaScript
This project also included a Mental Health Chatbot Web Interface designed to provide a user-friendly interaction platform for mental health support. The chatbot displays a minimalistic interface where users can send messages and receive responses in a styled conversation-like format. The HTML, CSS, and JavaScript code combines structure, design, and interactivity.

## HTML
    **The HTML structure provides the basic layout for the chatbot interface.**

`<!DOCTYPE html>`
`<html lang="en">`

**Code Explanation:**
    Declares the document type as HTML5.
    Specifies the language attribute (lang="en") to indicate the content is in English.

`<head>`
    `<meta charset="UTF-8">`
    `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
    `<title>Home Page</title>`

**Code Explanation:**
    Sets the character encoding to UTF-8 for supporting various characters.
    Ensures responsive design on different devices with viewport meta tag.
    Defines the page title as "Home Page.

`<script src="https://code.jquery.com/jquery-3.7.1.js" integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4=" crossorigin="anonymous"></script>`
    **Includes jQuery library for simplified DOM manipulation and AJAX requests.**


``<style>``

**/* Inline CSS for styling */**
    **Contains CSS styles for chatbot appearance, layout, and design.**


`<h1>`
    MENTAL HEALTH AI
`</h1>`

**Displays the main heading centered at the top.**


`<div>`
    `<div id="chatbox">`
        `<p class="botText">`
            `<span>Hi there!</span>`
        `</p>`
    `</div>`
    `<div id="userInput">`
        `<input id="textInput" type="text" name="userMessage" placeholder="Type your Message....."/>`
        `<input id="buttonInput" type="submit" value="Send"/>`
    `</div>`
`</div>`

**div#chatbox: A container for the chatbot conversation.**
    Contains the default bot greeting: "Hi there!"

**div#userInput: Holds user input elements:**
    
    **(a) input#textInput: A text box for user input.**
    **(b) input#buttonInput: A button to send messages.**
    

## The CSS provides styling for the chatbot layout.

`body {`
    `font-family: sans-serif;`
`}`

**Sets the font for the webpage to sans-serif.**


`#chatbox {`
    `margin-left: auto;`
    `margin-right: auto;`
    `width: 40%;`
    `margin-top: 50px;`
`}`

**(a) Centers the chatbot conversation box horizontally.**
**(b) Sets the width to 40% of the viewport and adds a top margin.**


`.botText {`
    `font-family: monospace;`
    `font-size: 16px;`
    `text-align: left;`
    `line-height: 25px;`
    `color: blue;`
`}`

**Defines styles for bot messages with a blue monospace font.**


`#userInput {`
    `margin-left: auto;`
    `margin-right: auto;`
    `width: 80%;`
    `text-align: center;`
    `margin-top: 50px;`
`}`

**Centers the input area horizontally with a width of 80%.**


`#textInput {`
    `border-bottom: 3px solid green;`
    `font-family: sans-serif;`
    `font-size: 16px;`
`}`

**Styles the input text box with a green underline and a font size of 16px.**


`#buttonInput {`
    `padding: 5px;`
    `font-family: monospace;`
    `font-size: 16px;`
`}`

**Adds padding and styles for the "Send" button.**


## JavaScript handles chatbot interaction, including message handling and AJAX calls.


# javascript

`function typeBotResponse(text, container) {`
    `let index = 0;`
    `function type() {`
        `if (index < text.length) {`
            `container.innerHTML += text.charAt(index);`
            `index++;`
            `setTimeout(type, 50); // Adjust typing speed here`
        `}`
    `}`
    `type();`
`}`

**Simulates typing effect for bot responses by gradually adding characters to a container.**


`function getUserResponse() {`
    `var userText = $('#textInput').val();`
    `var userHTML = "<p class='userText'><span>" + userText + "</span></p>";`
    `$('#textInput').val(""); // Clears the input box.`
    `$('#chatbox').append(userHTML); // Appends user's message to the chatbox.`
    `document.getElementById("userInput").scrollIntoView({ block: 'start', behavior: 'smooth' });`

**Retrieves user input and displays it in the chatbox.**


    `var botHTML = "<p class='botText'><span class='typingIndicator'></span></p>";`
    `$('#chatbox').append(botHTML);`

**Adds a typing indicator before the bot responds.**


    `$.get("/get", { userMessage: userText }).done(function (data) {`
        `var botTextContainer = document.querySelector(".typingIndicator");`
        `botTextContainer.innerHTML = ""; // Clear typing indicator`
        `typeBotResponse(data, botTextContainer); // Apply typing effect`
    `});`
`}`

**Sends the user's input to the server via an AJAX GET request.**
**Displays the bot's response with a typing effect.**


`$("#textInput").keypress(function (e) {`
    `if (e.which == 13) { // Checks for Enter key.`
        `getUserResponse();`
    `}`
`});`

`$('#buttonInput').click(function () {`
    `getUserResponse();`
`});`

**Allows users to send messages using the Enter key or the "Send" button.**

## Features
**(1) Responsive Design: Adjusts well to various screen sizes.**
**(2) Interactive Chat: Real-time interaction with a chatbot.**
**(3) Typing Indicator: Simulates a real-time conversation.**
**(4) AJAX Integration: Communicates seamlessly with a Python Flask backend.**

## Dependencies
**jQuery 3.7.1: For DOM manipulation and AJAX requests.**

## Install dependencies:

**pip install flask chatterbot chatterbot_corpus**

## Versions used
**Flask==1.1.2**
**ChatterBot==1.0.8**

## All the above code is running on Python 3.8.0 64-bit
