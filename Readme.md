## Use Github actions to store new tech deals every 48 hours

#### The repository does following to automate
- Makes use of Flask server to create an endpoint to trigger deployment using repository_dispatch event.
- Flask  server uses POST request to trigger repository_dispatch event. LINK_REPO : https://github.com/dineshpabbi10/send_github_action
- Send GET request to FLASK server's /sendAction endpoint to trigger deployment . NOTE: Needs GITHUB TOKEN and PASSWORD in OS env (for request auth) for server to trigger action
- Github action on triggering uses selenium to fetch tech deals in Canada and commits the deals table in deals.md file 

### Running every 48 hours
- Used Cronhub to send request to deployed flask server every 48 hours , triggering workflow.
- Sends request to <domain>/sendAction?password=<password set in deployment os env>
