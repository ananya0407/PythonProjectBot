from slackclient import SlackClient
from .message import Message

class Bot(object):

    def __init__(self):

        super(Bot, self).__init__()
        self.name = "meetingbot"
        self.emoji = ":robot_face:"
        self.oauth = {"client_id": '329716265793.351740552772',  # os.environ.get("CLIENT_ID"),
                      "client_secret": 'd1fa556b13db1311aaaa10ec422fcbf7',  # os.environ.get("CLIENT_SECRET"),
                      "scope": "bot,commands,users.profile:read,chat:write:bot"}
        self.verification = 'IWATM1SH14f3IjyAgSQLjvcu'  # os.environ.get("VERIFICATION_TOKEN")
        self.client = SlackClient("")
        self.messages = {}

    def open_dm(self, user_id):

        print("user_id")
        new_dm = self.client.api_call("im.open",
                                      user=user_id)
        print("=============new dm==================")
        # print new_dm
        print(new_dm["ok"])
        dm_id = new_dm["channel"]["id"]
        return dm_id


    def send_response(self, team_id, user_id):

        # print authed_teams
        # if not team_id in authed_teams:
        #     print "not authorised"
        # else:
        # self.client = SlackClient(authed_teams[team_id]["bot_token"])
        print("-----------",user_id)
        print(">>>>>>>>>>",team_id)
        print(team_id)
        self.client = SlackClient('xoxb-351275082976-U3Pjstlu6FSBcsPmbLcdBWYT')
        if self.messages.get(team_id):
            self.messages[team_id].update({user_id: Message()})
        else:
            self.messages[team_id] = {user_id: Message()}
        message_obj = self.messages[team_id][user_id]
        message_obj.channel = self.open_dm(user_id)
        # message_obj.create_attachments()
        post_message = self.client.api_call("chat.postMessage",
                                            channel=message_obj.channel,
                                            text="thank you"  # message_obj.text
                                            )

        timestamp = post_message["ts"]
        message_obj.timestamp = timestamp