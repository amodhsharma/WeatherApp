# Html file and API calls
This application uses an API key ( privately generated through https://openweathermap.org/ ) and a API url ( public ). To ensure the safety of my accounts, I have passed the html file ( originally index.html ) as index_template.txt ( a txt file of the html file ) through a python script ( generated through ChatGPT ). Which takes the URL and Key through the terminal ( terminal of my preferred IDE - VS code ). this inturn generates an index.html file that I have stored in the gitignore file. ensuring safety.

# Files

The files of html code, txt, css and python are all accessible through the github repository. 

> Remember to generate a gitignore file and route the index.html file there.
> 
# Terminal Use
> Remember to use the git command " git rm --cached index.html " in the terminal to clear the tracking history of the index.html ( user specific ) file by git.
> 
> One can also use the vix terminal ( if one is using a macintosh system ) to do the same. 
> 
# Prompt for generating the txt file, python script and bash code ( for running in the terminal ) from GPT 
"I have an index.html where I want to put a private api key and url. Create a python script which takes it those as arguments and generates an index.html file with the arguments formatted in the correct place"
