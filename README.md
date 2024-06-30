**Tech stack:** Python, Django Rest Framework, Sqlite3

**User Credentials**

Ops user: username: ops, password: G13pics007@

Client user: username:ehson, password: G13pics007@

**Endpoints**

Account Management:-

Signup: /api/accounts/signup/ - POST

Login: /api/accounts/login/ - POST

File Operations:-

 Upload File: /api/files/upload/ - POST

 Generate Download Link: /api/files/{file_id}/download-link/ - GET

 Download File: /api/files/{file_id}/download/ - GET

 List Files: /api/files/ - GET

**Features Implemented**

1. Client user: sign up, log in, list all files, get an encrypted download link and download from the encrypted link.
2. Ops user: login, upload file
3. Ops user cannot perform client user's operations and vice versa
4. Download url encryption
5. Only pptx,docx, and xlsx type files are allowed to be uploaded
   
**Note** Sample Postman dump is provided as postman_dump.json

**Tests**: I have  tested features using Postman collections

**Deployment**: I  refrained from using environment variables for storing confidential keys and rather has manually defined it in configuration to make it easier to execute and test.In Production level deployment this should be avoided. I plan to deploy it on pythonanywhere.com(already 2 web apps, 2 Rest API deployed)  which is extremely useful tool and provides CI/CD to automate maintenance.
