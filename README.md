# gst
A gamified group studying web application, so you can compete with friends to study the most. Studying has never been ~~so much~~ fun!

## How to run 
(PowerShell commands)
1. `.\.venv\Scripts\activate` 
2. `py manage.py migrate --run-syncdb`
3. `py manage.py runserver`
4. `cd .\frontend`
5. `npx vite`

## API endpoints
See test.rest for example API requests (For most requests, X-CSRFTOKENS and Authorization headers will need changing - sign up and log in to get a CSRF token and auth token)

- `api/auth/create` - Create a new user (email, password)
- `api/auth/profile` - Retrieve information about the user making the request
- `api/auth/login` - Create new authentication session and retrieve auth and CSRF tokens for this new session
- `api/auth/logout` - Delete current authentication session
- `api/auth/logoutall` - Delete all authentication sessions for user making the request
- `api/group/create` - Create a new group and add the founding member to the group
- `api/group/get-info` - Retrieve the name and description of a group
- `api/group/set-info` - Update the name and description of a group
- `api/group/join` - Add the user making the request to a certain group
- `api/group/leave` - Remove the user making the request from a certain group
- `api/group/leaderboard` - Retrieve a list of all members of a group, ordered by their study duration
- `api/study/start` - Start the study timer for the user making the request
- `api/study/end` - Stop the study timer for the user making the request and update their study duration
- `api/mygroups` - Retrieve a list of all the groups which the user making the request is a member of

## Planned changes & enhancements
- Further flesh out frontend
- Invalidate study timers which exceed some threshold (8h?) to avoid egregious cheating
- Add more functionality wrt group management - group admin, kick a user from a group, invite a user to a group
