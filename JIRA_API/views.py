from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
import json
from django.views.decorators.csrf import csrf_exempt
import random
from jira import JIRA

# Create your views here.
@api_view(["POST"])
def get_data(request):
    if request.method == "POST":
        data = request.data 
        print(data)
        server = data.get("server", None)
        email = data.get("email", None)
        api_token = data.get("api_token", None)
        creds = {"server" : server, "email" : email, "api_token" : api_token}
        project = data.get("project", None)
        sprint = data.get("sprint", None)
        filters = {"project" : project, "sprint" : sprint}
        card_data_dic = fetch_data(creds, filters=filters)
        json_res = json.dumps(card_data_dic)
        print(card_data_dic)
        return HttpResponse(json_res)
    
        
        # if email is not None and api_token is not None:
        #     card_data = CredsModel.objects.get(id = id)
        #     serializer = CardDataSerializer(card_data)
        #     json_data = JSONRenderer().render(serializer.data)
        #     return HttpResponse(json_data)
        # else:
        #     json_data = {"message" : "ID is not valid"}
        #     json_data = json.dumps(json_data)
        #     return HttpResponse(json_data)
            
            
# test = {"server" : "https://bhavin-sangani.atlassian.net", "email" : "100bhavinsangani@gmail.com", "api_token" : "ATATT3xFfGF0e96g8_XM84jCNf0XClY0D6f4-mq5cX7199h4ndX5-1U7pMZtQnsGubv_zU4YZCxgN8xHirfi6enBUcjlxtKKNvVntaUiU7BT4KMSzsvTU_JTiXbArxIT7MdP77iZxLyHqOFQRsQM5OJbH3ekh2RG-qLo4frZQgFq9Ni5KKU81ZU=2D44418E", "project" : "Data Automation", "sprint" : "DA Sprint 1"}
            
def fetch_data(cred, filters = {}):
    
    server = cred['server']
    email_id = cred["email"]
    auth_token = cred["api_token"]
    
    jiraOptions = {'server': server}

    # Get a JIRA client instance, pass,
    # Authentication parameters
    # and the Server name.
    # emailID = your emailID
    # token = token you receive after registration
    jira = JIRA(options=jiraOptions, basic_auth=(
    email_id, auth_token))
    
    fields = jira.fields()
    fields_dic = {}
    for field in fields:
        fields_dic[field['name']] = field['id']
    # print(fields_dic)

    
    
    # Search all issues mentioned against a project name.
    issue_dic = {"Issue_Type":[], "Project":[],"Time_Spent":[],"Status":[], "Story_Points":[], "Last_Viewed":[], "Sprint":[], "Priority":[],
             "Assignee":[], "Issue_Key":[], "Description":[], "Summary":[], "Reporter":[]}
    
    jql_str = ""
    for i, filter in enumerate(filters.items()):
        if i == 0 and filter[1] != None:
            jql_str += f"\'{filter[0]}\'= \'{filter[1]}\'"
        elif filter[1] != None:
            jql_str += f" and \'{filter[0]}\'= \'{filter[1]}\'"

    print(jql_str)
    
    valid = True
    try:
        for singleIssue in jira.search_issues(jql_str=jql_str):
            break 
    except:
        valid = False
        
    if valid == False:
        return {"msg" : "Invalid Information Passed."}
    for singleIssue in jira.search_issues(jql_str=jql_str):
	# print(singleIssue.fields.
        # print(getattr(singleIssue.fields, fields_dic["Story Points"]))
        try:
            Issue_Type = getattr(singleIssue.fields, fields_dic["Issue Type"]).name
        except:
            Issue_Type = None
        try:
            Project = getattr(singleIssue.fields, fields_dic["Project"]).name
        except:
            Project = None
        try:
            Time_Spent = getattr(singleIssue.fields, fields_dic["Time Spent"])
        except:
            Time_Spent = 0
        try:
            Status = getattr(singleIssue.fields, fields_dic["Status"]).name
        except:
            Status = "Backlog"
        try:
            Story_Points = getattr(singleIssue.fields, fields_dic["Story Points"])
        except:
            Story_Points = 0
        try:
            Last_Viewed = getattr(singleIssue.fields, fields_dic["Last Viewed"])
        except:
            Last_Viewed = None
        try:
            Sprint = getattr(singleIssue.fields, fields_dic["Sprint"])[0].name
        except:
            Sprint = None
        try:
            Priority = getattr(singleIssue.fields, fields_dic["Priority"]).name
        except:
            Priority = None
        try:
            Assignee = getattr(singleIssue.fields, fields_dic["Assignee"]).displayName
        except:
            Assignee = None
        try:
            Issue_Key = singleIssue.key
        except:
            Issue_Key = None
        try:
            Description = getattr(singleIssue.fields, fields_dic["Description"])
        except:
            Description = None
        try:
            Summary = getattr(singleIssue.fields, fields_dic["Summary"])
        except:
            Summary = None
        try:
            Reporter = getattr(singleIssue.fields, fields_dic["Reporter"]).displayName
        except:
            Reporter = None
        issue_dic["Issue_Type"].append(Issue_Type)
        issue_dic["Project"].append(Project)
        issue_dic["Time_Spent"].append(Time_Spent)
        issue_dic["Status"].append(Status)
        issue_dic["Story_Points"].append(Story_Points)
        issue_dic["Last_Viewed"].append(Last_Viewed)
        issue_dic["Sprint"].append(Sprint)
        issue_dic["Priority"].append(Priority)
        issue_dic["Assignee"].append(Assignee)
        issue_dic["Description"].append(Description)
        issue_dic["Summary"].append(Summary)
        issue_dic["Reporter"].append(Reporter)
        issue_dic["Issue_Key"].append(Issue_Key)
        
    # issue_df = pd.DataFrame(issue_dic)

    return issue_dic
    
            
            
    