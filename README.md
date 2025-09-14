# Flask API Learning Project

## 🌐 Live Demo
**Try the interactive API tester: [https://ruiyuhuang50.github.io/API_Development/](https://ruiyuhuang50.github.io/API_Development/)**

> ⚠️ **Important**: The live demo is for **demonstration purposes only**. The buttons won't work on the live site because GitHub Pages only hosts static files and cannot run the Flask server. To test the actual API functionality, you need to run the Flask server locally (see instructions below).

## 🚀 Quick Start (Required for API Testing)

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/RuiyuHuang50/API_Development.git
   cd API_Development
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask server**
   ```bash
   python server_flask.py
   ```

4. **Access the application**
   - API endpoints: `http://localhost:3000`
   - Interactive tester: Open `index.html` in your browser or visit `http://localhost:3000/test`

```bash
# Get API info
curl http://localhost:3000/


## 📖 API Endpoints

### Core Endpoints
- `GET /` - API information and available endpoints
- `GET /input` - Sample data endpoint
- `POST /submit` - Submit data with JSON payload

### User Management (CRUD)
- `GET /users` - Get all users
- `GET /users/<id>` - Get user by ID
- `POST /users` - Create new user
- `PUT /users/<id>` - Update existing user
- `DELETE /users/<id>` - Delete user

### Example Requests

**Create User:**
```bash
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

**Get All Users:**
```bash
curl http://localhost:3000/users
```

## 🧪 Testing Options

### Option 1: Web Interface (Recommended)
1. Run the Flask server: `python server_flask.py`
2. Open `index.html` in your browser
3. Use the interactive buttons to test all endpoints

### Option 2: Python Client
```bash
python client.py
```

### Option 3: Simple Python Client
```bash
python simple_client.py
```

### Option 4: Manual Testing
Use curl, Postman, or any HTTP client with the endpoints above.

## 📁 Project Structure

```
API_Development/
├── server_flask.py          # Main Flask application
├── client.py                # Comprehensive Python test client
├── simple_client.py         # Simplified test client
├── index.html              # Interactive web-based API tester
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔧 Configuration

The server runs on `http://localhost:3000` by default. To change the port:

```python
if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Change port here
```

## 📚 Learning Topics Covered

- Flask application setup and routing
- HTTP methods (GET, POST, PUT, DELETE)
- Request/response handling with JSON
- CORS configuration for cross-origin requests
- Error handling and HTTP status codes
- REST API design principles
- Client-server communication
- API testing strategies (Python clients, web interface)
- Interactive web-based API testing

## 🌟 Features

- **Complete CRUD operations** for user management
- **Multiple testing interfaces** (web, Python clients)
- **Error handling** with proper HTTP status codes
- **CORS support** for cross-origin requests
- **Interactive web interface** for easy API testing
- **Live demo** showcasing the interface design

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new endpoints
- Improve error handling
- Enhance the web interface
- Add authentication features
- Implement database integration
- Add input validation

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed.

## 🆘 Troubleshooting

**"Failed to fetch" error in web interface:**
- Ensure Flask server is running locally (`python server_flask.py`)
- Check that CORS is enabled in the Flask server
- Verify the server is running on `http://localhost:3000`

**"Module not found" error:**
- Install requirements: `pip install -r requirements.txt`

**"Port already in use" error:**
- Change port in `server_flask.py` or kill existing process:
  ```bash
  lsof -ti:3000 | xargs kill -9
  ```

**Buttons not working on live GitHub Pages:**
- This is expected! GitHub Pages only hosts static files
- Clone the repository and run locally for full functionality

## 📞 Support

For questions about Flask development, check the official documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

---

*🔥 Built with Flask for learning REST API development*

**Live Demo**: [https://ruiyuhuang50.github.io/API_Development/](https://ruiyuhuang50.github.io/API_Development/) | **Local Setup Required for Full Functionality**
```

## 📚 API Endpoints


| Method | Endpoint      | Description       | Example                              |
| ------ | ------------- | ----------------- | ------------------------------------ |
| GET    | `/`           | API documentation | `curl http://localhost:3000/`        |
| GET    | `/input`      | Get sample data   | `curl http://localhost:3000/input`   |
| POST   | `/submit`     | Submit data       | `curl -X POST ... /submit`           |
| GET    | `/users`      | Get all users     | `curl http://localhost:3000/users`   |
| GET    | `/users/<id>` | Get user by ID    | `curl http://localhost:3000/users/1` |
| POST   | `/users`      | Create new user   | `curl -X POST ... /users`            |
| PUT    | `/users/<id>` | Update user       | `curl -X PUT ... /users/1`           |
| DELETE | `/users/<id>` | Delete user       | `curl -X DELETE ... /users/1`        |

## 🎯 Learning Objectives

### 1. HTTP Methods

- **GET**: Retrieve data
- **POST**: Create new resources
- **PUT**: Update existing resources
- **DELETE**: Remove resources

### 2. Status Codes

- **200**: Success
- **201**: Created
- **400**: Bad Request
- **404**: Not Found
- **500**: Internal Server Error

### 3. JSON Handling

- Sending JSON data in requests
- Receiving JSON responses
- Parsing and validating JSON

### 4. Error Handling

- Try-catch blocks
- HTTP error responses
- Connection error handling

### 5. REST API Design

- Resource-based URLs
- Proper HTTP methods
- Consistent response format

## 📁 File Structure

```
Flask/
├── server_flask.py      # Main Flask application
├── client.py           # Python test client
├── test_client.html    # Web-based test interface
├── requirements.txt    # Python dependencies
└── README.md          # This documentation
```

## 🔧 Code Examples

### Creating a Simple Route

```python
@app.route("/hello")
def hello():
    return jsonify({"message": "Hello, World!"})
```

### Handling POST Data

```python
@app.route("/api/data", methods=["POST"])
def handle_data():
    data = request.get_json()
    # Process data here
    return jsonify({"status": "success"})
```

### Error Handling

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404
```

## 🐛 Troubleshooting

### Common Issues

1. **"Connection refused"**

   - Make sure Flask server is running
   - Check if port 3000 is available
2. **"Module not found"**

   - Install requirements: `pip install -r requirements.txt`
3. **"Method not allowed"**

   - Check HTTP method (GET vs POST)
   - Verify endpoint accepts the method
4. **JSON parsing errors**

   - Ensure Content-Type is `application/json`
   - Validate JSON format

## 🚀 Next Steps

1. Add database integration (SQLite, PostgreSQL)
2. Implement authentication and authorization
3. Add input validation and sanitization
4. Deploy to cloud platforms (Heroku, AWS, etc.)
5. Add unit tests and documentation
6. Implement rate limiting and caching
