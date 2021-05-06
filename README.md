# Webfortune
Final project for DevOps

To run you will need python, pytest and docker to install everything else that is needed.

# How to install
First you will use git clone to obtain all the neccessary files. Then the next thing is building a docker image
and then running it. To build the docker image type 'docker build -t <directory name> . the dot is needed and
directory name is name of dirrectory that the Dockerfile, appserver.py, and requirements.txt are in.

# How to run
To run the file go to the web address of your commputer and with the port number you use in the run command
for example (since 8 is my favorite number) suppose you use docker run -dp 8888:5000 webfortune this assumes
that webfortune is what you called the docker image. This will run on port 8888 so if you go to the address
and type in 8888 after the : then it will take you to the web app. To access the other pages type after the /
fortune/ will take you to fortune. /cowsay/'insert message here' inside the tick marks would be ones message
will bring you to the cow with your message. The last one is /cowfortune/ which will take you to a page 
where the cow is telling you the fortune instead of it being user defined. 
