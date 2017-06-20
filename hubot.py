import os, slackclient, time
from generate import generate_sentence


# delay in seconds before checking for new events 
SOCKET_DELAY = 0.1
# slackbot environment variables
HUBOT_SLACK_NAME = os.environ.get('HUBOT_SLACK_NAME')
HUBOT_SLACK_TOKEN = os.environ.get('HUBOT_SLACK_TOKEN')
HUBOT_SLACK_ID = os.environ.get('HUBOT_SLACK_ID')

hubot_slack_client = slackclient.SlackClient(HUBOT_SLACK_TOKEN)

def is_private(event):
    """Checks if on a private slack channel"""
    channel = event.get('channel')
    return channel.startswith('D')

def post_message(message, channel):
    hubot_slack_client.api_call('chat.postMessage', channel=channel,
                          text=message, as_user=True)


def is_for_me(event):
    """Know if the message is dedicated to me"""
    # check if not my own event
    type = event.get('type')
    if type and type == 'message' and not(event.get('user')==HUBOT_SLACK_ID):
        if is_private(event):
            return True
        text = event.get('text')
        channel = event.get('channel')


def say_bilbo():
    # response_template = "hello, This is me!"

    response_template = generate_sentence()
    return response_template


def is_bilbo(message):
    return 'bilbo' in message.lower().split()[:5]


def say_help():
    response_template = "Hello this is bot created form Bilbo's sentences.\nType: 'bilbo' to hear want he wants to tell you.\n Beware, Bilbo can speak in elvish."
    # response_template = "lol"
    return response_template

def is_help(message):
    return 'help' in message.lower().split()

def handle_message(message, channel):
    if is_bilbo(message):
        post_message(message=say_bilbo(), channel=channel)
    if is_help(message):
        post_message(message=say_help(), channel=channel)


def run():
    if hubot_slack_client.rtm_connect():
        print('[.] HUBOT de Machin is ON...')
        while True:
            event_list = hubot_slack_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    if is_for_me(event):
                        handle_message(message=event.get('text'), channel=event.get('channel'))
            time.sleep(SOCKET_DELAY)
    else:
        print('[!] Connection to Slack failed.')

if __name__=='__main__':
    run()