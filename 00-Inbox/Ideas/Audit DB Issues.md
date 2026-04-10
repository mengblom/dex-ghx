I wanted to continue a conversation that started in Daniel's office last week regarding Audit DB, how we use it, why it is under so much pressure, and opportunities for improvements.

In a nutshell, here is what I understand:
- The vast majority of the volume and load comes from the Activity collection.
- On average we write ~188M documents per day
- Most of the time, most of those documents are never read, only when somebody views the Audit Trail in the Document Flows dashboard is the data actually read.
- Due to the volume, we only keep 3 days worth of data in Mongo. I.e. every day we also delete 188M documents - the data is archived to S3 at this point.
- If someone tries to view something that is older than 3 days, we automatically rehydrate that data back from S3 storage.

So some questions arises:
1. Why does this data need to live in Mongo at all?
	- Is it every queried in any way other than "all activities that belong to this document"?
	- Why can't the application load this data straight from S3?
2. If for some reason the data does have to live in Mongo when it is displayed, or if it is difficult to change the app to read from S3:
	- Why do we need to keep the last 3 days worth of data in Mongo - why not rely on the rehydration mechanism we already have and move data from S3 -> Mongo only when somebody wants to view it?