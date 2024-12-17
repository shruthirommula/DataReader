from app import initialize_app

app = initialize_app()
if __name__=='__main__':
    app.run(debug=True) 
#Data Reader (Microservice 3 - Redis to Log)
import redis
import json
import time

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
    data = redis_client.lpop('market_data')
    if data:
        print(f"Market Data: {json.loads(data)}")
    time.sleep(1)
