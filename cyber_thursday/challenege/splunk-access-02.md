# Splunk Challenge: Access Control Adventure!

###  Welcome to the Splunk Challenge! Get ready for an exciting journey where you'll onboard logs, set hostnames, extract fields, and configure access control to ensure users only see their own data. Follow the steps below to complete the challenge.

## Challenge Steps
Onboard access-02.log into the main Index
- Ingest the access-02.log file into the main index to get started with the data.

Set Hostnames
- Assign hostnames to your log files for easy identification:
- Set the hostname for access-01.log to olinesecurity.
- Set the hostname for access-02.log to newWorldRecords.

Extract Access Log Fields
- Ensure that all relevant fields from the access logs are extracted. This includes IP addresses, usernames, timestamps, HTTP methods, URLs, status codes, response sizes, referrers, user agents, and operating systems.
Configure Access Control

Implement access control so that users from different hostnames can only see their own data:

- Users from newWorldRecords should only see events from their host.
- Users from olinesecurity should only see records from their host.

Logs Directory
- The logs you need to ingest will be provided in the logs directory on Git.

## Good Luck!
Dive into the challenge and showcase your Splunk skills. Make sure to have fun and enjoy the process of becoming a Splunk Access Control Master!