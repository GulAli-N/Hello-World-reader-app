# Hello-World-reader-app

### What was the challenge? 

This 'Hello World' challenge involved the creation of a reader app using python code whose function was to:

1. write verbose log data in the local file system
2. use ansible to retrieve an environment variable stored in another file
3. verify the environment variable is present and record this in the log file

The data in the log file needed to be accessed by filebeat and connected to an Elasticsearch index that should then be able to create a dashboard in kibana where a visualisation of the data log can be created and stored.

The python code for the Hello World reader app was created using Visual Studio, a GitHub repository was also set up for version control and the app code pushed to the repository.  

It was also necessary to install ansible as the reader app was run using a playbook. Following this, filebeat was installed in the Hello World directory. This created a filebeat directory containing the resources to run filebeat including a configuration template file called filebeat.yml which required specific changes to ensure filebeat would run as required.   

### How I expected the challenge to go. 

- This challenge was great fun as we had some research to carry out and were let loose on the internet. I expected the challenge to be more complicated than it actually turned out to be. I expected the main premise of the challenge was to be able to utilise tools interdependently including python, ansible, terraform and filebeat, all of them operated from a terminal window. Once set in motion the next stage was to use ElasticSearch to create an index which could be used in a Kibana dashboard to create data visualisations. 

### What went well? 

- The teamwork was amazing, I saved alot of time researching when I eventually reached out for clues as to where answers may be found, such as with ElasticSearch and Kibana.  Installation of the various resources was also much easier than anticipated. 

### What didn't go as planned? 

- I struggled particularly with the filebeat.yml template as there were many factors that had to be tweaked. Also some idiosyncracies to deal with such as code/copy pasted from guidance websites that raised errors when running the file, solved by physically re-typing the identical code manually, a tip from another team member.
The filebeat.yml template file settings were also a challenge and I needed assistance from team members to get it set correctly. The use of terraform was also not completely understood and it was not implemented in the final solution. I also didn't manage to get the app to print the contents of the environment variable to the terminal. 

### Possible improvements for future challenges.

- It is important not to go too far down the rabbit hole when researching, the internet is a vast resource and many times it became clear that my research was not yielding results as fast as anticipated. Asking for help early can save alot of time.

