from django.shortcuts import render_to_response, redirect, render
from rest_framework import status, request
import json
from rest_framework.views import APIView
from rest_framework.response import Response

from .ParseNLP import parse_nlp
from .Bot import Bot
Pybot=Bot()
verification='IWATM1SH14f3IjyAgSQLjvcu'

def _event_handler(event_type, slack_event):
    team_id = slack_event["team_id"]
    if event_type == "message" and slack_event["event"].get("user") != None:
        user_id = slack_event["event"].get("user")
        message = slack_event["event"].get("text")
        a, resp = parse_nlp(message)
        # if a==1:
        verification.send_response(team_id,user_id,resp)
        # elif a==2:
        #     verification.show_schedule(team_id,user_id)
        # elif a==3:
        #     verification.meeting_setup(team_id, user_id)
        Pybot.send_response(team_id, user_id)
    if event_type == "team_join" and slack_event["event"].get("user") != None:
        data = {
             "members" : []
        }
        data["members"].append(slack_event["event"].get("user"))
        # verification.prepar_userlist(data)
        # Welcome message
        return Response("Welcome message updates with shared message",200)
    message = "You have not added an event handler for the %s" % event_type
    return Response(message, 200, {"X-Slack-No-Retry": 1})

class Listen(APIView):
    def post(self, request):
        slack_event = request.data
        # ============= Slack URL Verification ============ #
        if "challenge" in slack_event:
            return Response(slack_event["challenge"], 200, {"content_type":
                                                                 "application/json"
                                                                 })
        # ============ Slack Token Verification =========== #
        if verification != slack_event.get("token"):
            message = "Invalid Slack verification token: %s \npyBot has: \
                       %s\n\n" % (slack_event["token"], verification)
            Response(message, 403, {"X-Slack-No-Retry": 1})

        # ====== Process Incoming Events from Slack ======= #
        if "event" in slack_event:
            event_type = slack_event["event"]["type"]
            print("==========================slack events==========================")
            print(slack_event)  #['channel'] == 'D9Q50NRQT':
            return _event_handler(event_type, slack_event)
        print("[NO EVENT IN SLACK REQUEST] These are not the droids\
                             you're looking for.", 404, {"X-Slack-No-Retry": 1})

# class Install(APIView):
#     def get(self,request):
#         client_id = Pybot.oauth["client_id"]
#         scope = Pybot.oauth["scope"]
#         return render(request,"install.html", client_id=client_id, scope=scope)
#
# class Thanks(APIView):
#     def post(self, request):
#         print("here~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         code_arg = request.args.get('code')
#         u_id = (json.loads(Pybot.auth(code_arg)))["a"]
#         print(u_id, type(u_id))
#         print("here``````````````````````````````")
#         t = "ADMINUSERS" + u_id
#         print(t)
#         Pybot.read_userlist()
#         urll = "http://localhost:8090/login/"+t
#         return redirect(urll)
#         # return render_template("thanks.html")
#         #return "Successful"
#         #return redirect('https://robotic-augury-200612.firebaseapp.com/onboarding.html')
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
# class Success(APIView):
#     def post(self, request):
#         print("id is: ",id)
#         return render(request, "thanks.html")
#
#     def index(request):
#         return "You reached here."







