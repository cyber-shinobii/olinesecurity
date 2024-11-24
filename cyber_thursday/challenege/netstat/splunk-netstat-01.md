Welcome to the Splunk Netstat Log Challenge!

Objective: Your mission is to onboard a set of Netstat logs into Splunk, extract key fields from each log event, and complete various challenges to earn points!

Instructions:

Download the Netstat Logs:

	•	Get your hands on the Netstat logs (you can simulate this data or use logs from your system).
	•	These logs should be formatted similarly to the output of the netstat command, which includes columns like Foreign, Local, PID/Program, Proto, Recv-Q, Send-Q, and State.

Ingest Logs into Splunk:

	•	Choose your method of ingestion. For bonus points, use backend ingestion (via a forwarder or another method).
	•	Ensure that the logs are indexed into the main index with a sourcetype of netstat_log.

Extract Essential Fields:

	•	Extract the following key fields from each Netstat log event:
	•	Foreign: The foreign address and port number.
	•	Local: The local address and port number.
	•	PID/Program: The process ID and associated program name (e.g., 1234/mongod).
	•	Proto: The protocol used (e.g., TCP, UDP).
	•	Recv-Q: The number of bytes in the receive queue.
	•	Send-Q: The number of bytes in the send queue.
	•	State: The current state of the connection (e.g., ESTABLISHED, TIME_WAIT).

Complete Challenges:

Earn points for each challenge completed!

	•	Top Proto: Find which protocol (TCP or UDP) is used the most in your logs.
	•	Active Connections: Determine how many connections are currently in the ESTABLISHED state.
	•	Top Ports: Identify the most common local and foreign ports used in the logs.
	•	Most Active Program: Find which program has the most open connections based on the PID/Program field.
	•	Bytes In Queue: Calculate the total number of bytes in the Recv-Q and Send-Q columns combined.

Scoring:

	•	Each correctly extracted field: 10 points.
	•	Identifying the top protocol: 30 points.
	•	Counting active connections (ESTABLISHED state): 50 points.
	•	Identifying the most common ports: 20 points.
	•	Finding the most active program: 40 points.
	•	Calculating total bytes in queues: 40 points.
	•	Extra Cool Points: Upload data via backend for bonus points!