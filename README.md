# slack-bot
A place for all slack-bots

In order for the slackbot to work you need to create a Slack App and get the webhooks of the channel you want to send messages to / interact with.

## How to call functions in your script
Since the repo is public you can add the following snippet to your code and then use bot as any other library. <br>
`!pip install git+https://github.com/artemdou/slack-bot@main`<br>
`from bot import bot`

## send_slack_message(webhook, message)
inputs: webhook url (str), message (str)<br>
outputs: prints ok if the message was send sucessfully.

