# ORTSOC-Slack-App
Slack app that acts as a connector for Kibana - Development / Deployment Instructions included

## Setup

#### Create Your Slack App (If you don't have one)
1. Open [https://api.slack.com/apps/new](https://api.slack.com/apps/new) and choose "From an app manifest"
2. Choose the workspace you want to install the application to
3. Copy the contents of [manifest.json](./manifest.json) into the text box that says `*Paste your manifest code here*` (within the JSON tab) and click *Next*
4. Review the configuration and click *Create*
5. Click *Install to Workspace* and *Allow* on the screen that follows. You'll then be redirected to the App Configuration dashboard.

#### Environment Variables
Before you can run the app, you'll need to store some environment variables from the app you just created

1. Open up [env.example](./env.example)
2. Go to your Slack apps configuration page [link](https://api.slack.com/apps), click *OAuth & Permissions* in the left hand menu, then copy the Bot User OAuth Token (starts with xoxb-). You will store this as `SLACK_BOT_TOKEN`.
3. Click *Basic Information* from the left hand menu and follow the steps in the *App-Level Tokens* section to create an app-level token with the `connections:write scope` (starts with xapp-), copy this token and store it as `SLACK_APP_TOKEN`.
4. IMPORTANT: Rename `env.example` to just `.env` - You can use a command like `cp env.example .env` or the GUI

#### Dependencies 
```
# Python 3.7+ required
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
```

#### Starting the app
```
python3 app.py
```

## Development

#### Linting
```
# Run ruff from root directory for linting
ruff check

# Run ruff from root directory for code formatting
ruff format
```

#### Testing
```zsh
# Run pytest from root directory for unit testing
pytest .
```

## Project Structure

### `manifest.json`

`manifest.json` is a configuration file for the settings of the Slack app set on the web portal. It gives the app a pre-defined configuration.

### `app.py`

`app.py` is the entry point for the application and is the file you'll run to start the server.

### `/listeners`

Every incoming request is routed to a "listener". Inside this directory, each listener is grouped based on the Slack Platform feature used. [Reference](https://docs.slack.dev/reference/)

### Slack app Scope (Permissions)
```
Commands - Add shortcuts and/or slash commands that people can use
Channels:history - View messages and other content in public channels that your Slack app has been added to
Used by the message.channels event
Chat:write- Send messages as @your_slack_app
Im:write - Start direct messages with people
Im:write.topic - Set the description in direct messages
Im:read - View basic information about direct messages that your Slack app has been added to
```

### Slack app Events (Events the bot can react to)
```
App_home_opened - User clicked into your App Home
Message.channels - A message was posted to a channel
Im_close - You closed a DM
Im_created - A DM was created
Im_open - You opened a DM
message.im - A message was posted in a direct message channel
```
