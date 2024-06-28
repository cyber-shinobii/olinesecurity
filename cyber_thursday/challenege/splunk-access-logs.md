# Welcome to the Splunk Log Adventure!
#### Objective: Your mission is to onboard a set of access logs available on GitHub into Splunk. Extract specific fields from each log event and complete various challenges to earn points!

## Instructions:
Download the Access Logs:
- Visit our GitHub repository to download the access logs.

Ingest Logs into Splunk
- Choose your method of ingestion. You get cool points for onboarding data via backend.

Ensure the logs are indexed into the main index with a sourcetype of access.

Extract Essential Fields:
- Extract the following fields from each log event:
- IP Address
- User
- Date and Time
- HTTP Method
- Path
- HTTP Version
- HTTP Response Code
- Byte Response Size
- Referrer URL
- Browser
- Operating System

## Complete Challenges:
### Earn points for each challenge completed!
- Most Active User: Identify the user who accessed the site the most.
- Unique Users: Count how many different users have accessed the site.
- Top IPs: Determine which IP addresses are most frequently accessing the site.
- Popular Operating Systems: Find out which operating systems are used the most by visitors.

### Scoring:
- Each correctly extracted field: 10 points.
- Finding the most active user: 50 points.
- Counting unique users: 30 points.
- Identifying top IPs: 20 points.
- Discovering popular operating systems: 40 points.
- Extra Cool Points: Upload data via backend for bonus points!

## Submit Your Findings:

Once you've completed the challenges, submit your results and total points earned to see where you stand!

## Tips:
Use Splunk's search and reporting capabilities to extract and analyze data.

Explore SPL (Splunk Processing Language) commands to refine your searches.
Have fun exploring and mastering Splunk while uncovering insights from real access logs!

Let the Splunk Log Adventure begin! Good luck!