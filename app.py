from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    print("Received message:", data.get("message"))  # Add this line for debugging
    user_message = data.get("message", "").lower()

    # Course-related questions
    if "course" in user_message or "subjects" in user_message:
        response = (
            "Your enrolled courses this semester are:\n"
            "1. Data Structures\n"
            "2. Operating Systems\n"
            "3. Artificial Intelligence\n"
            "4. Cloud Computing\n"
            "Check your student portal for detailed schedules and syllabus."
        )

    # Deadline or exam-related questions
    elif "deadline" in user_message or "exam" in user_message or "assignment" in user_message:
        response = (
            "The upcoming deadlines are:\n"
            "- Assignment submission: May 5\n"
            "- Internal Exams: May 15–18\n"
            "- End Semester Exams: June 1\n"
            "Make sure to submit your assignments before the due dates!"
        )

    # Department news or updates
    elif "news" in user_message or "update" in user_message:
        response = (
            "📢 Department News:\n"
            "1. Tech Fest 'Innovate 2025' on May 15\n"
            "2. Guest Lecture on AI Trends on May 10\n"
            "3. Final Year Project Demos on May 20\n"
            "Stay updated with the latest department activities!"
        )

    # About Sri Indu College
    elif "sri indu" in user_message or "college" in user_message or "about" in user_message:
        response = (
            "Sri Indu College of Engineering & Technology is located in Hyderabad, "
            "offering a wide range of engineering, technology, and management courses. "
            "The college is known for its academic excellence and has strong industry collaborations."
        )

    # Introduction about the assistant
    elif "who are you" in user_message or "introduction" in user_message or "help" in user_message:
        response = (
            "Hi! I'm your AI-powered Student Assistant 👩‍💻. I'm here to help with academic queries, "
            "exam deadlines, college information, and more. Just ask me anything related to your studies!"
        )

    # Faculty-related queries
    elif "faculty" in user_message or "professor" in user_message:
        response = (
            "The faculty at Sri Indu College consists of highly qualified professors with expertise in various fields "
            "such as Data Science, AI, Cloud Computing, and more. You can view detailed faculty profiles on the student portal."
        )

    # Fee-related questions
    elif "fee" in user_message or "tuition" in user_message:
        response = (
            "The tuition fee structure varies based on the course and year of study. You can check the fee details on the "
            "student portal or contact the administration office for more information."
        )

    # Hostel-related questions
    elif "hostel" in user_message or "accommodation" in user_message:
        response = (
            "Sri Indu College provides hostel accommodation for both male and female students. "
            "You can apply for hostel facilities through the student portal. Rooms are available on a first-come, first-served basis."
        )

    # Library-related questions
    elif "library" in user_message or "books" in user_message:
        response = (
            "The college library is open from 8 AM to 8 PM. It has a vast collection of academic and reference books, "
            "as well as online journal access. You can also access e-books and digital resources through the library portal."
        )

    # Placement-related questions
    elif "placement" in user_message or "recruitment" in user_message:
        response = (
            "The placement cell at Sri Indu College facilitates internships and job placements for students in top companies. "
            "You can view placement records and upcoming recruitment drives on the student portal."
        )

    # Exam-related questions (specific)
    elif "exam schedule" in user_message or "exam dates" in user_message:
        response = (
            "The internal exams are scheduled from May 15 to May 18, and the end semester exams will begin from June 1. "
            "Stay tuned for the detailed exam timetable on the portal."
        )

    # About student support services
    elif "support" in user_message or "counseling" in user_message:
        response = (
            "The college provides student support services including academic counseling, mental health counseling, and career guidance. "
            "You can book an appointment through the student support portal."
        )

    # Scholarship-related questions
    elif "scholarship" in user_message or "financial aid" in user_message:
        response = (
            "The college offers various scholarships based on merit and financial need. You can apply for scholarships through the "
            "student portal. Details are available in the scholarship section."
        )

    # Questions about extracurricular activities
    elif "extracurricular" in user_message or "activities" in user_message or "sports" in user_message:
        response = (
            "Sri Indu College offers a range of extracurricular activities such as sports, cultural events, and clubs. "
            "You can check the extracurricular calendar on the student portal for upcoming events."
        )

    # Hostel fee-related questions
    elif "hostel fee" in user_message or "accommodation fee" in user_message:
        response = (
            "Hostel fees vary depending on the type of accommodation chosen. For details, you can check the hostel section on the "
            "student portal or contact the hostel office."
        )

    # Internships
    elif "internship" in user_message or "internship opportunities" in user_message:
        response = (
            "Sri Indu College has strong industry partnerships and offers a variety of internship opportunities. "
            "You can check the internship opportunities on the placement portal or contact the placement office for more details."
        )

    # Research opportunities
    elif "research" in user_message or "research opportunities" in user_message:
        response = (
            "The college encourages students to participate in research projects and offers various research opportunities in fields like AI, Data Science, and Engineering. "
            "You can check with your department for ongoing research initiatives."
        )

    # Infrastructure-related questions
    elif "infrastructure" in user_message or "facilities" in user_message:
        response = (
            "Sri Indu College has state-of-the-art infrastructure, including modern classrooms, laboratories, sports facilities, and Wi-Fi-enabled campus. "
            "The campus also has dedicated spaces for coding labs, robotics, and innovation centers."
        )

    # How to contact the college
    elif "contact" in user_message or "contact details" in user_message:
        response = (
            "You can contact the college at: \n"
            "Phone: +91 123 456 7890\n"
            "Email: info@sriindu.edu\n"
            "Address: Sri Indu College, Hyderabad, Telangana, India"
        )

    # General FAQs about the college
    elif "faq" in user_message or "frequently asked questions" in user_message:
        response = (
            "You can find a list of frequently asked questions on the college website. "
            "It covers topics such as admissions, fee structure, scholarship options, and campus life."
        )

    # Default response if the question is not recognized
    else:
        response = (
            "I'm here to help with your academic questions! You can ask me about courses, deadlines, department news, or anything related to your college life."
        )

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
