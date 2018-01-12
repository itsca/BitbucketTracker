# A tracker file used to log all contributions I do at work to the company's bitbucket and show them on my stats.

I was having a hard time losing my Github stats because I do most of my contributions at work to their private bitbucket account now so I came up with this idea, probably not the best solution but the best I could think about with the time I had.

## Getting Started

It consists of 2 parts, one is the git hook that must be located in the hooks folder of the project you wish to track, and the other is a script and a tracker that live somewhere in your system and are global to all projects you wish to track.

### Prerequisites

A repository with the tracker.txt and githubLogger.py files that will track all your private repositories.

### Installing

- Clone or download the template branch of this repo.

- Create a repository to track all your repositories with the tracker.txt and githubLogger.py.

- Add the absolute path of your tracker.txt on the pre-push file to where your tracker is located.

```
os.chdir("PATH_TO_YOUR_TRACKER.TXT_FILE")

```

- Add the pre-push file to the hooks folder of the project you wish to track, you have to o this for all projects you want to be tracked.

- Change your name and anything else you wish on the tracker.txt it will always add new logs to the end of the file.

- Next time you make a push in the tracked repository it will add the log to your tracker.txt and push it to Github (remember to set the tracker repo to push with your personal account).


## Built With

* [python] - The hook and loggerFile

## Authors

* **Javier Escalante**
* **Angel Echavarría**
