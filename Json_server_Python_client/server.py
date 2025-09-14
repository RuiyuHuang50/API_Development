import requests 
INPUT_URL ="http://localhost:3000/input"
SUBMIT_URL ="http://localhost:3000/submitResults"

def run():
    r = requests.get(INPUT_URL)
    r.raise_for_status()
    data = r.json()
    print("got input:", data)

    #do some processing
    result ={"answer": (data.get("value", 0)+sum(data.get("items",[])))}
    resp = requests.post(SUBMIT_URL, json = result)
    print("submit status", resp.status_code, resp.text)
    print("submit status", resp.status_code, resp.text)
if __name__ == "__main__":
    run()
