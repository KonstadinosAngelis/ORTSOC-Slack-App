# ORTSOC-Slack-App (How to set up Autostart)
## 1. Test your bot manually first

Make sure the bot runs normally:
```
cd YOUR_PROJECT_FILE_PATH
source .venv/bin/activate
python app.py
```

## 2. Save the project directory filepath (Where app.py is)
Run the command `pwd` to get the path of the project, and set that aside for the next step

## 3. Edit the service file
1. Using your preferred text editor (vim/nano/etc) create the file `slackbot.service` in the `/etc/systemd/system` directory.
2. Paste in the following template:
```
[Unit]
Description=ORTSOC-Slack-App
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=[YOUR_PROJECT_FILE_PATH]

Environment="PATH=[YOUR_PROJECT_FILE_PATH]/.venv/bin"
ExecStart=[YOUR_PROJECT_FILE_PATH]/.venv/bin/python3 [YOUR_PROJECT_FILE_PATH]/app.py

Restart=always
RestartSec=10

StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```
3. Replace all 4 instances of `[YOUR_PROJECT_FILE_PATH]` with the path you saved in Step #2

## 4. Manage systemctl
1. Run: `sudo systemctl daemon-reload`
    1. (Note: Re-Run this command every time you edit the `slackbot.service` file as well )
2. Run: `sudo systemctl start slackbot.service` 
    1. Check it worked: `sudo systemctl status slackbot.service`
3. Enable auto-start at boot: `sudo systemctl enable slackbot.service`

## 5. Troubleshooting 
If you run into any issues with the service the following commands can shine light on what went wrong:
`journalctl -u slackbot.service -f`
`journalctl -u slackbot.service -b`

---
# Useful Commands

**Whenever you create or edit a service:**
`sudo systemctl daemon-reload`

**Start/Stop/Restart the service**
`sudo systemctl start slackbot.service `
`sudo systemctl stop slackbot.service`
`sudo systemctl restart slackbot.service `

**Check status**
`sudo systemctl status slackbot.service`

**Enable auto-start at boot / Disable auto-start at boot**
`sudo systemctl enable slackbot.service`
`sudo systemctl disable slackbot`

**View logs**
`journalctl -u slackbot.service -f `

**Troubleshooting**
`journalctl -u slackbot.service -f`
`journalctl -u slackbot.service -b`
