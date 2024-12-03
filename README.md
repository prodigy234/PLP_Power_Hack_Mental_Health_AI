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


## CSS

**The embedded 'style' block defines the visual appearance of the chatbot**

**

``<style>``

**/* Inline CSS for styling */**
    **Contains CSS styles for chatbot appearance, layout, and design.**


`<h1>`
    MENTAL HEALTH AI
`</h1>`

**Displays the chatbot's title at the top of the page.**


`body { font-family: sans-serif; }` =>
    **Sets the font for the whole page to "sans-serif" for better readability.**

`#chatbox { margin: 50px auto; width: 40%; }` =>
    **Centers the chatbox on the page with:**
        (1) margin: 50px auto; for vertical and horizontal centering.
        (2) width: 40%; sets the chatbox width to 40% of the screen.

`.botText, .userText { ... }` =>
    **Defines styling for messages:**
        (1) Uses a monospace font for a consistent typewriter look.
        (2) Sets font size and line height.

`.botText span` =>
    **Styles bot messages:**
        (1) color: blue; colors text blue.
        (2) text-align: left; aligns text to the left.

`.userText span` =>
    **Styles user messages:**
        (1) color: green; colors text green.
        (2) text-align: right; aligns text to the right.

`#userInput` =>
    **Centers the input area and makes it responsive with:**
        (1) margin: 50px auto; for centering.
        (2) width: 80%; makes it fit most screens.

`#textInput` =>
    **Styles the text input field:**
        (1) border-bottom: 3px solid green; gives a green underline.
        (2) font-size: 16px; width: 80%; makes it readable and responsive.

`#buttonInput` =>
    **Styles the "Send" button:**
        (1) Adds padding for better clickability.
        (2) Sets a matching font size.

`h1`
**Centers the title using text-align: center;.**


## HTML Body
**Defines the visible elements on the page.**

`<h1>MENTAL HEALTH AI</h1>`
    **Displays the chatbot's title at the top of the page.**


`<div id="chatbox">`
    **(1) Initializes the chatbox to display conversation history.**
    **(2) Contains a greeting:**
        `<p class="botText"><span>Hi there!</span></p>`

`<div id="userInput">`
Holds the input area:
    `<input id="textInput" type="text">` : The field where users type messages.
    `<input id="buttonInput" type="submit">` : A button to send messages.



## JavaScript
**Handles interactivity and chatbot functionality.**

## JavaScript handles chatbot interaction, including message handling and AJAX calls.


# javascript

`<script>` => 
    Begins the script section.



function `typeBotResponse(text, container)` => 
    **This function animates the bot's response character by character.**

`let index = 0;` => 
    **Initializes a counter to track the current character position.**

function `type()` =>
    **A nested function to handle the typing effect.**

`if (index < text.length)`
    **Checks if there are characters left to type.**

`if (text.substr(index, 4) === "<br>")`
    **If the next 4 characters represent a line break (<br>), adds it and skips ahead.**

`container.innerH`function getUserResponse() {`
    `var userText = $('#textInput').val();`
    `var userHTML = "<p class='userText'><span>" + userText + "</span></p>";`
    `$('#textInput').val(""); // Clears the input box.`
    `$('#chatbox').append(userHTMTML += text.charAt(index);` =>
    **Adds one character to the container.**

`setTimeout(type, 30);` =>
    **Calls type() again after a short delay for typing effect.**
    **Simulates typing effect for bot responses by gradually adding characters to a container.**


function `getUserResponse()` =>
    Handles user input and bot response.

`var userText = $('#textInput').val();` =>
    **Retrieves the user's input from the text field.**

`if (!userText.trim()) return;`
    `Prevents submission of empty messages.`

`var userHTML = "<p class='userText'><span>" + userText + "</span></p>";` =>
    **Wraps the user's message in HTML for display.**

`$('#textInput').val("");` =>
    **Clears the input field.**

`$('#chatbox').append(userHTML);` =>
    **Adds the user's message to the chatbox.**

`document.getElementById("userInput").scrollIntoView(...);` =>
    **Scrolls the input area into view.**

`var botHTML = "<p class='botText'><span class='typingIndicator'>...</span></p>";` =>
    **Shows a temporary typing indicator in the chatbox.**

`$.get("/get", { userMessage: userText })`
    **Sends the user's message to the /get endpoint via AJAX.**

`.done(function (data) { ... })`
    **Executes once the server responds:** => 
         Clears the typing indicator.
            Calls `typeBotResponse(data, botTextContainer)` to animate the response.


## Event Listeners

`$("#textInput").keypress(function (e) { ... })` => 
    **Listens for the Enter key (key code 13) and triggers** `getUserResponse.`

`$('#buttonInput').click(function () { ... })` =>
    **Listens for the Send button click and triggers getUserResponse.**
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


## Summary

**Frontend: Handles user input, displays messages, and simulates bot typing.**

**Backend Dependency: Relies on the /get endpoint to provide meaningful bot responses.**

**This code creates an interactive chatbot experience with smooth animations and responsive design.**