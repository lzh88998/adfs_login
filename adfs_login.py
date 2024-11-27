import os
import base64
import requests
import getpass
import re
from bs4 import BeautifulSoup
from requests_ntlm import HttpNtlmAuth

os.environ['PYTHONWARNINGS'] = 'ignore'

username=input("User Name:")
password=getpass.getpass()
relying_party_name=input("Relying Party Name:")

idp_domain=input("IDP Domain Name:")

idp_adfs_login_page="/adfs/ls/IdpInitiatedSignOn.aspx?loginToRp=zzhli"
idp_entry_url="https://"+idp_domain+idp_adfs_login_page

session=requests.Session()
response=session.get(idp_entry_url, verify=False)

x=re.match("[\\w|\\W]*<form [^>]*id=\"loginForm\"[^>]*action=\"([^\"]*)\"", response.text)

#print(x.group(1))

idp_login_url=x.group(1)

data={"UserName":username, "Password":password, "AuthMethod":"FormsAuthentication"}
response=session.post("https://"+idp_domain+idp_login_url, data, verify=False)

x=re.match("[\\w|\\W]*<form [^>]*id=\"idpForm\"[^>]*action=\"([^\"]*)\"", response.text)

#print(x.group(1))

idp_post_url=x.group(1)

x=re.match("[\\w|\\W]*<option value=\"([^\"]*)\">"+relying_party_name+"</option>", response.text)

#print(x.group(1))

relying_party_id=x.group(1)

idp_data={"SignInOtherSite":"SignInOtherSite","RelyingParty":relying_party_id, "SignInGo":"Sign in", "SingleSignOut":"SingleSignOut"}

response=session.post("https://"+idp_domain+idp_post_url, idp_data, verify=False)

x=re.match("[\\w|\\W]*<input[^>]*name=\"SAMLResponse\"[^>]*value=\"([^\"]*)\"", response.text)

print(x.group(1))

username="###################"
password="###################"

del username
del password


