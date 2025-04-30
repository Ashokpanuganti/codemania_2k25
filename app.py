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

    # Internship
    elif "internship" in user_message or "internship opportunities" in user_message:
        response = (
            "Sri Indu College has strong industry partnerships and offers a variety of internship opportunities. "
            "You can check the internship opportunities on the placement portal or contact the placement office for more details."
        )

    # Programming languages
    elif "programming languages" in user_message or "learn programming" in user_message:
        response = (
            "Here are some popular programming languages to learn:\n"
            "1. Python - Great for beginners and used in data science, AI, web development.\n"
            "2. JavaScript - For web development, front-end and back-end.\n"
            "3. Java - Widely used in enterprise applications.\n"
            "4. C++ - Used in system programming, game development.\n"
            "5. Ruby - Known for web development using the Ruby on Rails framework.\n"
            "Which one would you like to know more about?"
        )

    # Learn Python
    elif "learn python" in user_message:
        response = (
            "Python is an easy-to-learn programming language with a simple syntax. It's widely used in web development, data science, AI, "
            "automation, and more. Here are some topics to get started:\n"
            "1. Variables and Data Types\n"
            "2. Functions\n"
            "3. Loops and Conditionals\n"
            "4. Object-Oriented Programming\n"
            "5. Libraries like NumPy, Pandas, and Matplotlib"
        )

    # Learn C++
    elif "learn c++" in user_message:
        response = (
            "C++ is a powerful language used for system programming, game development, and applications requiring high-performance.\n"
            "Start learning C++ by focusing on:\n"
            "1. Basic Syntax\n"
            "2. Variables and Data Types\n"
            "3. Functions and Recursion\n"
            "4. Object-Oriented Programming\n"
            "5. Pointers and Memory Management"
        )

    # Learn JavaScript
    elif "learn javascript" in user_message:
        response = (
            "JavaScript is essential for web development, both on the client-side and server-side (using Node.js).\n"
            "Here are topics to get started with:\n"
            "1. Variables and Data Types\n"
            "2. Functions and Scope\n"
            "3. DOM Manipulation\n"
            "4. Asynchronous JavaScript (Promises, Async/Await)\n"
            "5. Frameworks like React, Angular, and Vue"
        )

    # Learn Java
    elif "learn java" in user_message:
        response = (
            "Java is widely used in large-scale systems, Android development, and web applications.\n"
            "Key topics to learn:\n"
            "1. Basic Syntax\n"
            "2. OOP Concepts (Classes, Objects, Inheritance)\n"
            "3. Collections Framework\n"
            "4. Exception Handling\n"
            "5. Android Development"
        )

    # System-related questions
    elif "operating system" in user_message or "os" in user_message:
        response = (
            "An operating system (OS) manages hardware resources and provides services for software applications.\n"
            "Some key concepts to understand are:\n"
            "1. Process Management\n"
            "2. Memory Management\n"
            "3. File Systems\n"
            "4. Virtual Memory\n"
            "5. OS Types: Windows, Linux, MacOS"
        )

    # Networking basics
    elif "networking" in user_message:
        response = (
            "Networking is the practice of connecting computers to share resources. Key concepts include:\n"
            "1. IP Addressing\n"
            "2. Routing and Switching\n"
            "3. Protocols (TCP/IP, HTTP, FTP)\n"
            "4. Network Topologies\n"
            "5. DNS and DHCP"
        )

    # Economy basics
    elif "economy" in user_message or "economic concepts" in user_message:
        response = (
            "Some key economic concepts include:\n"
            "1. Supply and Demand\n"
            "2. Inflation\n"
            "3. Fiscal Policy and Monetary Policy\n"
            "4. Gross Domestic Product (GDP)\n"
            "5. International Trade and Exchange Rates"
        )

    # Stock Market
    elif "stock market" in user_message or "investing" in user_message:
        response = (
            "The stock market allows individuals and institutions to buy and sell shares of companies.\n"
            "Some basic concepts:\n"
            "1. Stocks, Bonds, and Mutual Funds\n"
            "2. Bull and Bear Markets\n"
            "3. Dividends\n"
            "4. Stock Valuation (P/E Ratio)\n"
            "5. Risk and Portfolio Management"
        )

    # General Knowledge or trivia questions
    elif "general knowledge" in user_message or "trivia" in user_message:
        response = (
            "Here's a fun general knowledge fact:\n"
            "Did you know that the Eiffel Tower can be 15 cm taller during the summer due to the expansion of iron?"
        )

    # Default response if the question is not recognized
    else:
        response = (
            "I'm here to help with your academic questions! You can ask me about courses, deadlines, department news, or anything related to your college life."
        )

        # Software Development
    if "software development" in user_message:
        response = (
            "Software development is the process of designing, coding, testing, and maintaining software applications. "
            "It involves multiple stages including requirement gathering, designing, coding, testing, deployment, and maintenance."
        )
    
    # Software Design
    elif "software design" in user_message:
        response = (
            "Software design is the process of defining the architecture, components, interfaces, and other characteristics of a system. "
            "It aims to create software that is scalable, maintainable, and meets user needs."
        )

    # Programming Languages for Software Development
    elif "programming languages for software development" in user_message:
        response = (
            "Some popular programming languages for software development include:\n"
            "1. Python - Great for rapid prototyping and backend development.\n"
            "2. JavaScript - Widely used for web development (frontend and backend).\n"
            "3. Java - For enterprise-level applications.\n"
            "4. C++ - For high-performance applications and system programming.\n"
            "5. C# - Used for Windows-based applications and game development (Unity)."
        )

    # Frontend Development
    elif "frontend development" in user_message:
        response = (
            "Frontend development involves creating the user-facing part of a web application. Common tools include HTML, CSS, JavaScript, and frameworks like React, Angular, and Vue.js."
        )

    # Backend Development
    elif "backend development" in user_message:
        response = (
            "Backend development refers to the server-side of a web application. Common backend technologies include Node.js, Django (Python), Ruby on Rails, and Spring Boot (Java)."
        )

    # Full Stack Development
    elif "full stack development" in user_message:
        response = (
            "Full stack development refers to working on both the frontend and backend of a web application. A full-stack developer has knowledge of both client-side (React, HTML, CSS) and server-side (Node.js, Express, Django) technologies."
        )

    # DevOps
    elif "devops" in user_message:
        response = (
            "DevOps is a combination of software development (Dev) and IT operations (Ops). It aims to shorten the software development lifecycle and deliver high-quality software by automating processes like testing, integration, and deployment."
        )

    # Agile Software Development
    elif "agile development" in user_message:
        response = (
            "Agile is an iterative approach to software development where requirements and solutions evolve through collaboration. Popular Agile methodologies include Scrum and Kanban."
        )

    # Scrum Framework
    elif "scrum framework" in user_message:
        response = (
            "Scrum is an Agile framework used for managing software development. It involves roles like Scrum Master and Product Owner and processes such as sprints, stand-ups, and retrospectives."
        )

    # Version Control (Git)
    elif "version control" in user_message or "git" in user_message:
        response = (
            "Version control is a system that helps track changes to source code over time. Git is the most widely used version control system, enabling developers to collaborate efficiently on coding projects."
        )

    # GitHub
    elif "github" in user_message:
        response = (
            "GitHub is a web-based platform for version control using Git. It allows multiple developers to work on the same codebase, manage repositories, and collaborate through pull requests and issues."
        )

    # Software Testing
    elif "software testing" in user_message:
        response = (
            "Software testing is the process of evaluating a software application to find bugs and ensure that it behaves as expected. Common types include unit testing, integration testing, system testing, and acceptance testing."
        )

    # Unit Testing
    elif "unit testing" in user_message:
        response = (
            "Unit testing involves testing individual components or functions of a software application to ensure they work correctly. Popular frameworks include JUnit (Java), pytest (Python), and Mocha (JavaScript)."
        )

    # Debugging
    elif "debugging" in user_message:
        response = (
            "Debugging is the process of identifying and fixing errors (bugs) in a program. Tools like Visual Studio Code, IntelliJ IDEA, and PyCharm offer built-in debuggers to help developers pinpoint issues."
        )

    # CI/CD
    elif "ci/cd" in user_message:
        response = (
            "Continuous Integration (CI) and Continuous Deployment (CD) are practices used to automate the process of integrating code and deploying software. Popular CI/CD tools include Jenkins, Travis CI, and GitLab CI."
        )

    # Software Architecture
    elif "software architecture" in user_message:
        response = (
            "Software architecture refers to the high-level structuring of a software system. It involves decisions about components, interactions, data flow, and design patterns like MVC and Microservices."
        )

    # Microservices
    elif "microservices" in user_message:
        response = (
            "Microservices is an architectural style that structures an application as a collection of loosely coupled services, each responsible for a specific business function. It allows for better scalability and maintainability."
        )

    # Monolithic Architecture
    elif "monolithic architecture" in user_message:
        response = (
            "Monolithic architecture refers to building a software application as a single, unified unit. While it's easier to develop initially, it can be harder to scale and maintain as the application grows."
        )

    # RESTful API
    elif "restful api" in user_message:
        response = (
            "RESTful APIs are web services that follow REST principles for communication. They use standard HTTP methods like GET, POST, PUT, DELETE and typically return data in JSON format."
        )

    # Web Frameworks
    elif "web frameworks" in user_message:
        response = (
            "Web frameworks are libraries that provide pre-built functionality for creating web applications. Some popular frameworks include:\n"
            "1. Django (Python)\n"
            "2. Flask (Python)\n"
            "3. Express (Node.js)\n"
            "4. Ruby on Rails (Ruby)\n"
            "5. Spring (Java)"
        )

    # Cloud Computing
    elif "cloud computing" in user_message:
        response = (
            "Cloud computing is the delivery of computing services like servers, storage, databases, and software over the internet. Popular cloud platforms include AWS, Microsoft Azure, and Google Cloud Platform."
        )

    # Docker
    elif "docker" in user_message:
        response = (
            "Docker is a platform for developing, shipping, and running applications in containers. Containers allow developers to package an application and its dependencies into a standardized unit for deployment."
        )

    # Kubernetes
    elif "kubernetes" in user_message:
        response = (
            "Kubernetes is an open-source container orchestration platform for automating the deployment, scaling, and management of containerized applications."
        )

    # Design Patterns
    elif "design patterns" in user_message:
        response = (
            "Design patterns are reusable solutions to common software design problems. Some well-known patterns include Singleton, Factory, Observer, and Strategy."
        )

    # Data Structures
    elif "data structures" in user_message:
        response = (
            "Data structures are ways of organizing and storing data for efficient access and modification. Some common data structures are Arrays, Linked Lists, Stacks, Queues, Trees, and Graphs."
        )

    # Algorithms
    elif "algorithms" in user_message:
        response = (
            "Algorithms are step-by-step procedures or formulas for solving problems. Some fundamental algorithms include sorting (like QuickSort and MergeSort), searching (like Binary Search), and graph algorithms (like Dijkstra's)."
        )

    # Code Review
    elif "code review" in user_message:
        response = (
            "Code review is the practice of having someone other than the author review code to find bugs, ensure adherence to coding standards, and suggest improvements."
        )

    # Software Documentation
    elif "software documentation" in user_message:
        response = (
            "Software documentation includes all written material that describes how software works and how to use it. It can include user manuals, API documentation, and inline code comments."
        )

    # Database Management
    elif "database management" in user_message:
        response = (
            "Database management refers to the administration of databases for efficient data storage, retrieval, and manipulation. Some popular DBMS include MySQL, PostgreSQL, MongoDB, and Oracle."
        )

    # SQL Queries
    elif "sql queries" in user_message:
        response = (
            "SQL (Structured Query Language) is used to interact with databases. Some basic SQL queries include SELECT, INSERT, UPDATE, DELETE, and JOIN."
        )

    # Big Data
    elif "big data" in user_message:
        response = (
            "Big data refers to datasets that are too large or complex to be handled by traditional data processing tools. Technologies like Hadoop and Apache Spark are used for big data processing."
        )

    # Data Science Tools
    elif "data science tools" in user_message:
        response = (
            "Popular tools for data science include:\n"
            "1. Python (with libraries like Pandas, NumPy, Matplotlib)\n"
            "2. R\n"
            "3. Jupyter Notebooks\n"
            "4. Tableau\n"
            "5. SQL"
        )

    # Artificial Intelligence
    elif "artificial intelligence" in user_message:
        response = (
            "Artificial Intelligence (AI) involves creating machines or software that can simulate human intelligence. Key areas include machine learning, natural language processing, and robotics."
        )

    # Machine Learning
    elif "machine learning" in user_message:
        response = (
            "Machine Learning is a subset of AI that focuses on the development of algorithms that can learn and make predictions from data. Popular algorithms include Linear Regression, Decision Trees, and Neural Networks."
        )

    # Deep Learning
    elif "deep learning" in user_message:
        response = (
            "Deep Learning is a subset of machine learning that uses artificial neural networks to model complex patterns in large datasets. It is used in applications like image recognition and natural language processing."
        )

    # Testing Frameworks
    elif "testing frameworks" in user_message:
        response = (
            "Some popular testing frameworks are:\n"
            "1. JUnit (Java)\n"
            "2. pytest (Python)\n"
            "3. Mocha (JavaScript)\n"
            "4. Selenium (Web Testing)"
        )

    # Software Deployment
    elif "software deployment" in user_message:
        response = (
            "Software deployment is the process of releasing software to users. This may include packaging, installation, and configuration of the application on user systems."
        )

    # Software Maintenance
    elif "software maintenance" in user_message:
        response = (
            "Software maintenance refers to the process of updating software to fix bugs, improve performance, or add new features after the software has been deployed."
        )

    # Cloud Services
    elif "cloud services" in user_message:
        response = (
            "Cloud services are resources like computing power, storage, and software available over the internet. Some major cloud service providers are AWS, Microsoft Azure, and Google Cloud Platform."
        )

    # Virtualization
    elif "virtualization" in user_message:
        response = (
            "Virtualization is the process of creating virtual versions of physical resources, like servers, storage, or networks, to optimize resource usage."
        )

    else:
        response = (
            "I can help with software-related questions like programming languages, development frameworks, version control, testing, and much more. Just ask!"
        )


    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
