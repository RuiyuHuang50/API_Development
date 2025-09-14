import requests
import json

BASE_URL = 'http://localhost:3000'

def simple_test():
    """Simple test for beginners"""
    print("🧪 Simple Flask API Test")
    print("=" * 30)
    
    try:
        # Test 1: Get sample data
        print("\n1. Getting sample data...")
        response = requests.get(f'{BASE_URL}/input')
        print(f"   Status: {response.status_code}")
        print(f"   Data: {response.json()}")
        
        # Test 2: Submit some data
        print("\n2. Submitting data...")
        data = {"name": "Simple Test", "value": 100}
        response = requests.post(f'{BASE_URL}/submit', json=data)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        
        # Test 3: Get users
        print("\n3. Getting users...")
        response = requests.get(f'{BASE_URL}/users')
        print(f"   Status: {response.status_code}")
        users_data = response.json()
        print(f"   Found {users_data['count']} users")
        for user in users_data['users']:
            print(f"     - {user['name']} ({user['email']})")
            
        print("\n✅ All tests passed!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Flask server!")
        print("   Make sure to run: python server_flask.py")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    simple_test()
