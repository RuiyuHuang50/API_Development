# Flask Learning Project

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Flask Server
```bash
python server_flask.py
```
Server will start at: `http://localhost:3000`

### 3. Test the API

#### Option A: Use Python Client
```bash
python client.py
```

#### Option B: Use Web Interface
Open `test_client.html` in your browser, or visit the server directly at `http://localhost:3000`

#### Option C: Use curl commands
```bash
# Get API info
curl http://localhost:3000/

# Get sample data
curl http://localhost:3000/input

# Submit data
curl -X POST http://localhost:3000/submit \
  -H "Content-Type: application/json" \
  -d '{"name": "test", "value": 123}'

# Get all users
curl http://localhost:3000/users

# Get specific user
curl http://localhost:3000/users/1

# Create new user
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com"}'

# Update user
curl -X PUT http://localhost:3000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated", "email": "john.new@example.com"}'

# Delete user
curl -X DELETE http://localhost:3000/users/2
```

## 📚 API Endpoints

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| GET | `/` | API documentation | `curl http://localhost:3000/` |
| GET | `/input` | Get sample data | `curl http://localhost:3000/input` |
| POST | `/submit` | Submit data | `curl -X POST ... /submit` |
| GET | `/users` | Get all users | `curl http://localhost:3000/users` |
| GET | `/users/<id>` | Get user by ID | `curl http://localhost:3000/users/1` |
| POST | `/users` | Create new user | `curl -X POST ... /users` |
| PUT | `/users/<id>` | Update user | `curl -X PUT ... /users/1` |
| DELETE | `/users/<id>` | Delete user | `curl -X DELETE ... /users/1` |

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
