from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request
import random


# Initializing the Flask web application.
app = Flask(__name__)


# Initializing the chatbot
bot = ChatBot(
    "chatbot",
    read_only=True,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Sorry, I don't have an answer.",
            "maximum_similarity_threshold": 0.9
        }
    ]
)


# Custom training data for mental health support
mental_health_data = [
    "I feel stressed",
    "I'm sorry to hear that. Remember to take breaks and breathe deeply. Would you like some mindfulness tips?",
    "stressed",
    "I'm sorry to hear that. Remember to take breaks and breathe deeply. Would you like some mindfulness tips?",
    "I am feeling anxious",
    "Anxiety can be tough. Focus on the present moment and take deep breaths. Let me know if you need exercises.",
    "I feel depressed",
    "I'm really sorry you're feeling this way. It's important to talk to someone you trust, or consider reaching out to a professional.",
    "I need help",
    "I'm here to help. If it's serious, please reach out to a crisis helpline.",
    "I'm feeling overwhelmed",
    "It's okay to feel overwhelmed. Take things one step at a time, and be sure to ask for support if you need it.",
    "I'm so sad",
    "I'm really sorry you're feeling this way. It's okay to talk about it. Would you like some resources or coping strategies?",
    "I'm struggling with my mental health",
    "You're not alone. Seeking help from a counselor or therapist can be a great way to start working through challenges.",
    "I feel anxious about the future",
    "It's normal to feel anxious about the future. Try focusing on the present moment and setting small goals.",
    "I'm feeling down",
    "I'm sorry you're feeling down. Taking a moment to focus on your breathing and check in with yourself can help.",
    "Can you help with mindfulness?",
    "Sure! Try this: Take a deep breath in for 4 seconds, hold it for 7 seconds, and breathe out slowly for 8 seconds. Repeat this 3 times.",
    "I need some coping strategies",
    "Some helpful strategies include deep breathing, journaling, and reaching out to a friend or a professional for support.",
    "I'm feeling hopeless",
    "It's important to reach out to a mental health professional. You don't have to go through this alone.",
    "What are some crisis resources?",
    "Here are some resources:\n- National Suicide Prevention Lifeline: 1-800-273-8255\n- Crisis Text Line: Text HOME to 741741\n- SAMHSA Helpline: 1-800-662-4357",
    "I feel like giving up",
    "I'm really sorry you're feeling this way. Please reach out to someone you trust or a mental health professional. You matter.",
    "I'm afraid of social situations",
    "It's okay to feel anxious in social settings. Consider practicing grounding techniques, like deep breathing, to stay calm.",
    "I can't sleep",
    "Having trouble sleeping is common. Try relaxation exercises like progressive muscle relaxation before bed to calm your mind.",
    "I'm constantly worrying",
    "It's natural to worry, but try focusing on what you can control in the present moment. Deep breathing can help reduce anxiety.",
    "I'm afraid I'll never get better",
    "It's hard when things feel like they won't improve, but with time, support, and effort, many people find their way to healing.",
    "I don't know how to cope",
    "There are many ways to cope, such as mindfulness, talking to a therapist, engaging in physical activity, or simply taking things one day at a time.",
    "I feel numb",
    "Feeling numb can be a sign of emotional overwhelm. It might help to talk with someone you trust about what you're experiencing.",
    "I can't focus",
    "It's okay if you're having trouble focusing. Take breaks, practice deep breathing, and prioritize self-care.",
    "I feel disconnected from others",
    "It's important to feel connected to others. Try reaching out to a trusted friend, or consider joining a support group.",
    "How do I deal with panic attacks?",
    "During a panic attack, try deep breathing, grounding techniques, or focusing on your senses to calm down. Remember, the attack will pass.",
    "I don't feel like doing anything",
    "When you're feeling unmotivated, start small. Even a small task can give you a sense of accomplishment. Please be kind to yourself.",
    "I don't know how to talk to a therapist",
    "Talking to a therapist is a big step, and it's okay to feel unsure. You can start by sharing what brought you there, or just talk about your day.",
    "Can you suggest a relaxation technique?",
    "Try progressive muscle relaxation. Start with your toes and work your way up to your head, tensing each muscle group for 5 seconds, then releasing.",
    "I feel like I'm failing",
    "It's tough to feel like you're failing, but everyone has setbacks. Be compassionate with yourself, and reach out for support if you need it.",
    "I don't know how to manage my emotions",
    "Managing emotions can be hard. Start by acknowledging how you feel, and try journaling or expressing your emotions through art or music.",
    "What can I do if I feel lonely?",
    "Loneliness can be difficult. Try reaching out to friends, family, or even online communities for support. You don't have to be alone.",
    "How do I calm my racing thoughts?",
    "To calm racing thoughts, try grounding techniques like focusing on your breath, counting backwards, or using a mantra.",
    "I don't know how to get started with therapy",
    "Finding a therapist can feel overwhelming. Start by looking for local providers or using online platforms. Therapy is a helpful resource for many.",
    "I feel like I don't belong",
    "Feeling like you don't belong can be painful. Remember, you are worthy, and there are communities where you can feel accepted and understood.",
    "What is mindfulness?",
    "Mindfulness is focusing on the present moment without judgment. You can practice it through deep breathing, meditation, or simply paying attention to your senses.",
    "I feel like I'm stuck in a rut",
    "It's normal to feel stuck sometimes. Break your routine, set new small goals, or try engaging in activities that bring you joy.",
    "How can I stay positive during tough times?",
    "During tough times, it helps to focus on small victories, express gratitude, and connect with loved ones. Remember, it's okay to not feel positive all the time.",
]


# Training the chatbot with mental health data
trainer = ListTrainer(bot)
trainer.train(mental_health_data)


# Mindfulness prompts
MINDFULNESS_PROMPTS = [
    "Take a deep breath and exhale slowly. Repeat 3 times.",
    "Close your eyes and list 3 things you are grateful for today.",
    "Focus on your surroundings. What can you see, hear, and feel right now?",
]


# Crisis resources (for when the user asks about help)
CRISIS_RESOURCES = [
    {"name": "National Suicide Prevention Lifeline", "contact": "1-800-273-8255"},
    {"name": "Crisis Text Line", "contact": "Text HOME to 741741"},
    {"name": "SAMHSA Helpline", "contact": "1-800-662-4357"},
]


# Function to handle chatbot conversation
def chat_with_bot():
    print("Welcome to the Mental Health Support Bot. Type 'exit' to quit.")
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'exit':
            break

        # Respond to specific keywords
        if "mindfulness" in user_message.lower():
            response = random.choice(MINDFULNESS_PROMPTS)
        elif "crisis" in user_message.lower() or "help" in user_message.lower():
            response = (
                "It sounds like you may need immediate assistance. Here are some resources:\n" +
                "\n".join([f"{res['name']}: {res['contact']}" for res in CRISIS_RESOURCES])
            )
        else:
            # Default response using ChatterBot
            response = bot.get_response(user_message).text

        print(f"MentalHealthBot: {response}")


# Serving the index.html file as the main web page.
@app.route("/")
def main():
    return render_template("index.html")


# Handling user messages sent from the web interface and returning a bot response.
@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)