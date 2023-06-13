# mcstatus
Minecraft Status Bot for Discord written in Python
## Installation

1. Clone the repository:
```bash
git clone https://github.com/Spectroxx/mcstatus.git
```
2. Change Directory
```bash
cd mcstatus/
```
3. Install the required dependencies using pip:
```bash
pip3 install -r requirements.txt
```
## Configuration

1. Edit the `config.json` file with the following structure:
```json
{
  "token": "YOUR_DISCORD_BOT_TOKEN",
  "server_ip": "YOUR_MINECRAFT_SERVER_IP",
  "server_name": "YOUR_SERVER_NAME",
  "channel_id": "YOUR_DISCORD_CHANNEL_ID"
}
```
## Usage
To start the bot, run the following command:
```bash
python3 mcstatus.py
```

## Features
-   Fetches the Minecraft server status using the mcsrvstat.us API.
-   Displays the server's online/offline status and player count in a Discord embedded message.
-   Retrieves the list of online players and displays their names.

## Links
[License](https://github.com/Spectroxx/mcstatus/blob/main/LICENSE)<br>
[mcsrvstat.us API](https://api.mcsrvstat.us/)
