import requests
import simplejson
import os
import argparse

#Parse the arguments passed into the script, move this to its own script
parser = argparse.ArgumentParser()
parser.add_argument("name",type=str,help="The name of the new GitHub Repository.")
parser.add_argument("description",type=str,help="A description for the new GitHub Repository.")
parser.add_argument("-t", "--token",type=str,help="The GitHub User's Token. If no token is provided then an attempt at pulling the value from the user's environment variables is made.")
parser.add_argument("-u", "--url",type=str,help="The URL with more info about the repository.")
parser.add_argument("-p", "--private",type=bool,help="True to create repository as private. Default is false.")
parser.add_argument("-i", "--issues",type=bool,help="True to enable issues in repository. Default is true.")
parser.add_argument("-w", "--wiki",type=bool,help="True to enable a wiki for the repository. Default is true.")
parser.add_argument("-d", "--downloads",type=bool,help="True to enable repository downloads. Default is true.")
parser.add_argument("-m", "--teamid",type=int,help="Id of the team that is granted access to the repository. Only valid when creating repo in an organization.")
parser.add_argument("-a", "--autoinit",type=bool,help="True to create an initial commit with an empty README. Default is false.")
parser.add_argument("-g", "--gitignore",type=str,help="The language or platform of the .gitignore template to apply. Use name of the template without extension.")
parser.add_argument("-l", "--license",type=str,help="The license template to apply to repository. Use the name fo the license template without the extension.")
args = parser.parse_args()

if args.token is not None:
    t=args.token
else:
    t = os.environ['gitT'] 

#move the data instantiation and population to its own script
data = {}
data['name']=args.name
data['description']=args.description
if args.url is not None:
    data['homepage']=args.url
if args.private is not None:
    data['private']=args.private
if args.issues is not None:
    data['has_issues']=args.issues
if args.wiki is not None:
    data['has_wiki']=args.wiki
if args.downloads is not None:
    data['has_downloads']=args.downloads
if args.teamid is not None:
    data['team_id']=args.teamid
if args.autoinit is not None:
    data['auto_init']=args.autoinit
if args.gitignore is not None:
    data['gitignore_template']=args.gitignore
if args.license is not None:
    data['license_template']=args.license

#move the request to its own script
r = requests.post('https://api.github.com/user/repos?access_token='+t, json = data)
c = r.content
#move the parsing and building of string from response to its own script
j = simplejson.loads(c)
idUrl = {}

for item in j.items():
    if item[0]=="id":
        idUrl[item[0]] = item[1]
    elif item[0]=="git_url":
        idUrl[item[0]] = item[1]

#printing of string build from response stays
if len(idUrl) > 0:
    print ("{}".format(str(idUrl)))
else:
    print ("Error: Please review the response \n {}".format(j))
