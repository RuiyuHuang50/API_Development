import requests
import json

BASE_URL = 'http://localhost:3000'

def make_request(method, endpoint, data=None):
    """Helper function to make requests with error handling"""
    url = f"{BASE_URL}{endpoint}"
    try:
        if method.upper() == 'GET':
            response = requests.get(url)
        elif method.upper() == 'POST':
            response = requests.post(url, json=data)
        elif method.upper() == 'PUT':
            response = requests.put(url, json=data)
        elif method.upper() == 'DELETE':
            response = requests.delete(url)
        
        print(f"\n{method.upper()} {endpoint}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response
        
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection failed. Make sure Flask server is running!")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_all_endpoints():
    """Test all Flask endpoints"""
    print("🚀 Testing Flask API Endpoints")
    print("=" * 50)
    
    # Test home
    make_request('GET', '/')
    
    # Test original endpoints
    make_request('GET', '/input')
    make_request('POST', '/submit', {"name": "example", "value": 456})
    
    # Test user endpoints
    make_request('GET', '/users')
    make_request('GET', '/users/1')
    
    # Create new user
    new_user = {"name": "Charlie", "email": "charlie@example.com"}
    make_request('POST', '/users', new_user)
    
    # Update user
    update_data = {"name": "Charlie Updated", "email": "charlie.new@example.com"}
    make_request('PUT', '/users/3', update_data)
    
    # Get updated users list
    make_request('GET', '/users')
    
    # Delete user
    make_request('DELETE', '/users/2')
    
    # Final users list
    make_request('GET', '/users')
    
    # Test non-existent endpoint
    make_request('GET', '/nonexistent')

if __name__ == "__main__":
    test_all_endpoints()