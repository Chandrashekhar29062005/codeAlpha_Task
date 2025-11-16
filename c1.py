import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data
nltk.download('punkt')

# Step 1: Collect FAQs (You can modify this list)
faqs = {
    "What is your name?": "I am an FAQ Chatbot created to answer your questions.",
    "How can I reset my password?": "To reset your password, go to the settings page and click 'Forgot Password'.",
    "What are your working hours?": "We are available 24/7 to assist you.",
    "How do I contact support?": "You can email us at support@example.com.",
    "Where can I find pricing information?": "All pricing details are available on our Pricing page."
}

# Step 2: Preprocess (Tokenize + Vectorize)
questions = list(faqs.keys())
answers = list(faqs.values())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Step 3: Function to find best match
def chatbot_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    confidence = similarity[0][index]
    
    if confidence < 0.3:
        return "Sorry, I couldn't understand that. Please try again."
    else:
        return answers[index]

# Step 4: Chat loop
print("🤖 FAQ Chatbot: Hi! Ask me something (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break
    print("Chatbot:", chatbot_response(user_input))