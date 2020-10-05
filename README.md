# Video Tutorials
1. [Create a simple message forwarding telegram bot](https://www.youtube.com/watch?v=nnERUAHO2PY&list=PLfn8j7KfZQVtp3hYPf0ZuLX1LRVcVkf4J)
2. [Make combination specific whitelist and blacklist words](https://www.youtube.com/watch?v=hOfEydh2e6E&list=PLfn8j7KfZQVtp3hYPf0ZuLX1LRVcVkf4J)

## Installation

1. Clone the project
```bash
git clone https://github.com/Ak4zh/conflux-clone
```
2. Change directory to the project directory ```cd conflux-clone```
3. Install the requirements ```pip install -r requirements.txt```

4. Create a new file ```.env``` inside the project directory.
5. Now add your API_ID and API_HASH obtained from https://my.telegram.org/apps
```
TELEGRAM_API_ID=your-api-id
TELEGRAM_API_HASH=your-api-hash
```
6. Now make changes in ```settings.py``` file as per your requirements.
 
## Usage
Start the bot:
```python main.py```

If the is the first time you are running the bot it will ask you to enter your phone number and login code to generate a session for your account. All subsequent logins will run without the need to login again.
