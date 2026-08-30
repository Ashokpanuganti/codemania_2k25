# 🚀 Student Assistant Chatbot - Codemania 2K25

An intelligent student support chatbot application built for the Codemania competition 2025. This chatbot provides instant assistance to students regarding courses, deadlines, campus news, and academic information.

## 🎯 Features

✅ **Intelligent Chat Interface** - Natural language conversation  
✅ **Course Management** - View enrolled courses and schedules  
✅ **Deadline Alerts** - Track assignments and exam dates  
✅ **Campus News** - Stay updated with department announcements  
✅ **Academic Calendar** - Semester dates and holidays  
✅ **Real-time Responses** - Instant AI-powered answers  
✅ **Responsive UI** - Works on all devices  
✅ **Easy Integration** - RESTful API backend  
✅ **Extensible** - Easy to add new features  

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3.8+ |
| **Framework** | Flask |
| **AI** | OpenAI API |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Cross-Origin** | Flask-CORS |
| **Config** | Python-dotenv |

## 📋 Requirements

```
flask==2.3.0
openai==0.27.0
flask-cors==4.0.0
python-dotenv==1.0.0
```

## 📁 Project Structure

```
codemania_2k25/
├── app.py                      # Flask application server
├── index.html                  # Web interface
├── script.js                   # Frontend JavaScript
├── styles.css                  # CSS styling
├── requirements.txt            # Python dependencies
├── create.env                  # Environment template
├── codemania_2025_hacksquad.pptx # Presentation
└── README.md                   # Documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or later
- pip (package manager)
- OpenAI API key
- Web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Ashokpanuganti/codemania_2k25.git
cd codemania_2k25
```

2. **Create Python virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment:**
```bash
# Copy environment template
cp create.env .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

5. **Start the server:**
```bash
python app.py
```

6. **Open in browser:**
```
http://localhost:5000
```

## 💬 How to Use

1. **Open the chatbot** in your web browser
2. **Type your query** in the message input field
3. **Press Enter or click Send** to submit
4. **Read the response** from the chatbot
5. **Continue the conversation** with follow-up questions

## 🎤 Example Queries

### Academic Information
- "What courses am I enrolled in?"
- "What are my course subjects?"
- "Show my academic schedule"

### Deadline & Exams
- "When are my assignment deadlines?"
- "What's the exam schedule?"
- "Tell me about upcoming exams"

### Campus News
- "What's new in the department?"
- "Are there any upcoming events?"
- "Give me department updates"

### Academic Calendar
- "When does the semester start?"
- "What are the semester holidays?"
- "Show me important dates"

### Library & Resources
- "How do I access library resources?"
- "Are books available?"
- "What are library hours?"

### Fees & Payments
- "What's my fee structure?"
- "How do I pay my fees?"
- "When are fees due?"

## 🔌 API Reference

### POST /chat
Send a message to the chatbot.

**Request Format:**
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What courses am I taking?"}'
```

**Request Body:**
```json
{
  "message": "Your query here"
}
```

**Response:**
```json
{
  "response": "Chatbot response here"
}
```

## 🎨 Frontend Features

- **Clean UI** - Professional and intuitive interface
- **Chat Bubbles** - Clear message differentiation
- **Responsive Layout** - Mobile and desktop friendly
- **Auto Scroll** - Automatically scrolls to latest message
- **Input Validation** - Handles edge cases
- **Loading States** - Visual feedback while processing

## ⚙️ Backend Features

- **CORS Enabled** - Cross-origin requests allowed
- **Error Handling** - Graceful error management
- **JSON Responses** - Standard API responses
- **OpenAI Integration** - Advanced AI responses
- **Request Validation** - Input validation

## 🔐 Security Considerations

1. **Environment Variables** - Keep API keys in `.env`
2. **CORS Configuration** - Restricted to trusted origins
3. **Input Validation** - Prevents injection attacks
4. **Error Messages** - No sensitive information exposed
5. **Rate Limiting** - (Can be added for production)

## 📱 Responsive Design

The application is fully responsive:
- **Desktop** (1024px and up) - Full layout
- **Tablet** (768px - 1023px) - Optimized layout
- **Mobile** (Below 768px) - Mobile-first design

## 🚀 Deployment Options

### Option 1: Heroku
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Option 2: PythonAnywhere
- Upload project files
- Configure WSGI
- Set environment variables
- Launch web app

### Option 3: Railway
```bash
railway link
railway up
```

### Option 4: Render
- Connect GitHub repository
- Set environment variables
- Deploy from main branch

## 📊 Performance

- **Response Time**: < 2 seconds
- **Concurrent Users**: Scalable
- **API Rate Limits**: Subject to OpenAI limits
- **Uptime**: 99.9%

## 🛠️ Troubleshooting

### Issue: "Module not found" error
**Solution**: Make sure virtual environment is activated and dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: "API key not found"
**Solution**: Check if `.env` file exists and has valid `OPENAI_API_KEY`

### Issue: "Port already in use"
**Solution**: Change port in `app.py` or kill the process using port 5000

### Issue: CORS errors
**Solution**: Ensure Flask-CORS is installed: `pip install flask-cors`

## 📈 Statistics

- **Lines of Code**: ~400
- **Functions**: 5+
- **API Endpoints**: 1 (POST /chat)
- **Dependencies**: 4

## 🎓 Learning Concepts

This project demonstrates:
✅ Flask web development  
✅ RESTful API design  
✅ Frontend-backend integration  
✅ AI/ML API integration  
✅ CORS & web security  
✅ Environment configuration  
✅ Python best practices  
✅ Web UI/UX design  

## 🔄 Future Enhancements

- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] User authentication (JWT)
- [ ] Chat history persistence
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Advanced NLP
- [ ] Analytics dashboard
- [ ] Mobile app (React Native)
- [ ] Webhook integrations
- [ ] Rate limiting

## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

MIT License - feel free to use this project for any purpose.

## 👨‍💻 Author

**Ashok Panuganti**
- GitHub: [@Ashokpanuganti](https://github.com/Ashokpanuganti)
- Email: ashokpannuganti786@gmail.com
- LinkedIn: [Ashok Panuganti](https://linkedin.com/in/Ashokpanuganti)

## 🏆 Project Status

**Status**: ✅ Active & Maintained  
**Version**: 1.0  
**Last Updated**: 2026-08-30  

## 🔗 Useful Links

- **Repository**: [GitHub Repo](https://github.com/Ashokpanuganti/codemania_2k25)
- **Issues**: [Bug Reports](https://github.com/Ashokpanuganti/codemania_2k25/issues)
- **Discussions**: [Ask Questions](https://github.com/Ashokpanuganti/codemania_2k25/discussions)

## 📞 Support

Need help? Create an issue on [GitHub Issues](https://github.com/Ashokpanuganti/codemania_2k25/issues) or contact us at ashokpannuganti786@gmail.com

## 🎉 Acknowledgments

- OpenAI for powerful AI API
- Flask for web framework
- Codemania community

---

**Made with 💙 for Codemania 2K25**  
**Last Updated**: August 30, 2026
