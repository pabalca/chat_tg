# telegram chat
- chatgpt conversation mode
- get price of tokens
- generate bitcoin key based on input secret

chat.service : systemd unit
```
[Unit]
Description=Chatgpt Telegram Bot
After=network.target

[Service]
Type=simple
User=pabs
Environment=TG_TOKEN=<input yours>
Environment=CHAT_TOKEN=<input yours>

WorkingDirectory=/opt/apps/chatg/chatg
ExecStart=/opt/apps/chatg/venv/bin/python /opt/apps/chatg/chatg/cli.py
Restart=always

[Install]
WantedBy=multi-user.target
```

[@telegram_bot](https://t.me/pabs_alerts_bot)
