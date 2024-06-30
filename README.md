**User Credentials**

Ops user: username:ops, password: G13pics007@
Client user: username:ehson, password: G13pics007@

**Endpoints**

Account Management
Signup: /api/accounts/signup/ - POST

Login: /api/accounts/login/ - POST

File Operations
Upload File: /api/files/upload/ - POST

Generate Download Link: /api/files/{file_id}/download-link/ - GET

Download File: /api/files/{file_id}/download/ - GET

List Files: /api/files/ - GET

**Features Implemented**

1. Client user: singup, login, list all files, get encrypted download link, download from the enrypted link.
2. Ops user: login, upload file
3. Ops user cannot perform client users operations and vice versa
4. Download url encryption
5. Only pptx,docx, and xlsx type file are allowed to be uploaded
   
