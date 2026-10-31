# ORTSOC-Slack-App
Slack app that acts as a connector for Kibana - Development / Deployment Instructions included

Sources: https://www.elastic.co/docs/reference/kibana/connectors-kibana/slack-action-type
https://www.elastic.co/guide/en/workplace-search/current/workplace-search-slack-connector.html
https://www.elastic.co/docs/deploy-manage/manage-connectors

## Slack App Basics
App Name - ORTSOC Log Source Alerts 
Collaborators - Konnor, Alex

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

### Webhook for #all-cs428group1
https://hooks.slack.com/services/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
