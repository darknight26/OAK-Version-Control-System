# OAK


OAK is a student-developed version control system project at NITK. It provides local version control capabilities without the need for installation.

## Getting Started

To access the OAK project, you can clone the repository to your local machine using the following command:

```
git clone https://github.com/darknight26/git-proj.git
```

Once you have the code on your local machine, you can navigate to the project directory.

## Running OAK

OAK can be run directly from the command line or terminal. Here are the available commands:

```
oak init                # Initialize a new OAK repository
oak add <file>          # Add a file to the repository
oak commit "message" # Commit changes to the repository
oak log                 # Display commit history
oak status              # Show the current status of the repository
```

# OAK: A Version Control System
Oak is a python-based version control system, useful for understanding basic git internals. Our aim is to make a simpler version of Git, one that focuses on local files and repositories.
The commands we have defined are similar to Git's in terms of functionality.

## Oak Internals
Oak's internal data representation is inspired from Git, but differs in 3 main ways:
* Git compresses file contents stored before further processing, while Oak doesn't.
* Git stores metadata such as file creation\modification time, Author name, user ID, hardware device ID, file access permissions, while Oak doesn't.
* Git stores and manipulates data at the binary bite level, while Oak stores and manipulates data in the usual ASCII form.

We chose to differ from Git it the above ways as Oak is meant to be a demonstrator to basic Git internal principles, so the user can browse through Oak's source code
while exploring the .oak folder where data is stored in a readable form. The reason we don't store metadata for now is that Oak was meant to handle local files and repositories,
hence the lack of need for storing user and device IDs, file permissions etc.

## Oak Functions
We have implemented the following functions as of now:
* init : initializes an empty repository.
* commit: commits the files present in the staging area at the time of commit.
* log: display's commit history and relevant details.
* short log: similar to log, but display's information in a concise form.
* add: given files/directories, adds them into the index (staging area).
* restore: given a filename/directory name, commitID, the function restores the file/directory to its state in the mentioned commit.

## Functions yet to be Implemented:
* reset and revert
* oakignore
* diff
* branch
* merge

## Recommended reading:
* FreeCodeCamp blog on ['A Visual Guide to Git Internals - Objects, Branches, and How to Create a Repo From Scratch'](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/#:~:text=In%20git%20%2C%20the%20contents%20of,creation%20time%20remains%20the%20same) by Omer Rosenbaum.
* [Git Internals](https://github.com/pluralsight/git-internals-pdf) by Scott Chacon.
* [Git from the bottom up](https://jwiegley.github.io/git-from-the-bottom-up/) by John Wiegley.
* Building Git by James Coglan (a detailed study).
