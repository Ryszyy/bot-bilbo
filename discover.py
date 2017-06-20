import os, slackclient

HUBOT_SLACK_NAME = os.environ.get('HUBOT_SLACK_NAME')
HUBOT_SLACK_TOKEN = os.environ.get('HUBOT_SLACK_TOKEN')
# initialize slack client
hubot_slack_client = slackclient.SlackClient(HUBOT_SLACK_TOKEN)
# check if everything is alright
print(HUBOT_SLACK_NAME)
print(HUBOT_SLACK_TOKEN)
is_ok = hubot_slack_client.api_call("users.list").get('ok')
if(is_ok):
    for user in hubot_slack_client.api_call("users.list").get('members'):
        if user.get('name') == HUBOT_SLACK_NAME:
            print(user.get('id'))