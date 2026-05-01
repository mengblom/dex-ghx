This is a draft email (or Slack message) to my leadership team on Q2 focus areas.

Team,

A couple of weeks ago we talked about the updated org topology, and problems we are aiming to solve (break the monolith, getting to autonomous teams).

- We have a lot of work to do, but as we talked about, first and foremost we need to work aggressively towards a more decoupled architecture, autonomous teams, and standalone SDLC and deployments 
- It is time to get busy - we need to make progress towards this with everything we do. 
- I want each team to start defining exactly what they own and are responsible for. This may or may not be obvious depending on the team. When you come across uncertainty or ambiguity, let's work together to clear it up.
- Over the next couple of weeks I am going to want to meet with each team to talk this through, so please start thinking about:
	- Your domain - what is in and what is out?
	- How is your domain tightly coupled to "the monolith" or anything else? Is the code base part of the "all" repo, or a different repo shared with other apps/services? Does it have hard dependencies - direct service calls to other services, shared databases etc.
	- What prevents you from deploying the apps and services in your domain independently?