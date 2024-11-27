# adfs_login
use this python script to simulate interaction between ADFS and browser to login to ADFS server and get saml response


# usage:

python adsf_login.py

# information needed:

User Name: (AD FS user login name)
Password: (AD FS user password)
Relying Party Name: (AD FS configured Relying Party display name. The script will use this name to search for the id for the relying party to login)
IDP Domain Name: (AD FS server domain name)

The SAML will be printed out in console. Please also note that there might have warngings about server SSL certificate verification before the SAML data.
