# software-engineering-2

This repository is a _monorepo_ containing all the code for Software Engineering 2 module.

# TOC

  - [software-engineering-2](#software-engineering-2)
  - [TOC](#toc)
    - [Assignment Brief](#assignment-brief)
    - [How we work](#how-we-work)
      - [Pull Requests](#pull-requests)

## Assignment Brief

[Click here for the assignment brief](https://vle.exeter.ac.uk/pluginfile.php/3353859/mod_resource/content/0/ECM3440%20Assessment%202022.pdf)

## How we work

 - Weekly Thursday standups and bi-weekly sprints to discuss progress or any blockers
 - Sprint meetings will be used to review and retrospectives to discuss what went well, backlog,etc
 - Log of initial allocation of work
 - Project will be split up into phases to decide internal deadlines and to allocate tasks
 - A DevOps approach of continuous and iterative delivery will be followed for each phase

### Bumping the Repo Version and Tagging
First, in your new branch, you need to update the version of the repository with `./util/bump-version.sh patch`. `patch` can be `patch`, `minor` or `major`.

_When your Pull Request is merged_, you should checkout `master` and make sure it is up to date. You can then run `./util/create-tag.sh`. This will push the new version as a tag, the workflow `.github/workflows/docker.yml` will run and push the new tag to Dockerhub.

### Rolling back
For some reason, you have some code that has been merged into master that does not work. To roll it back you do the following
 - Run `util/rollback.sh <tag>`. This will create a new branch called `rollback-<tag>` and check it out. This branch will be reverted to the tag you passed into `rollback.sh`. (NOTE: Any tags already in master will not be affected by this process)
 - Commit, push and merge this branch into `master`
 - If there was a tag created with the rubbish code in it, you will need to delete the tag from `master` with `git push --delete origin <rubbish-tag> && git tag -d <rubbish-tag>`. This will remove the tag from the remote and local

The final two steps are not automatic because you are deleting code and we believe this should be a manual process, not an automatic one. Removing code should be a deliberate action, not an accidental one.

### Code Conventions
 - 2 space tabs for python code
 - Else, follow PEP8 conventions

### Pull Requests

To commit code, we will operate a branch and PR system. 

 - Create a branch from `master`
 - Make your changes in a branch
 - Pull from `master` before committing
 - Create a PR
 - Seek someone to review

#### In your Pull Request

Include:
 - Issue number
 - Summary of changes
 - How tested (in brief)
## Repository map
This is a monorepo, a repository containing multiple different (but related) codebases

 - `/sensors/CounterFit` - simulates an IoT sensor
 - `/sensors/soil-moisture-sensor` - Python application, simulates an IoT sensor
 - `/dashboard` - React application, dashboard to monitor the sensors
 - `/util` - any utility scripts live here

### Contributing

There are a couple different source trees in this monorepo, each with their own specifics.

#### Dashboard

##### Setup
You will need `nodejs` 16 installed, found here https://nodejs.org/en/

FYI: All commands executed for the dashboard need to be run while under the `dashboard` directory. This is due to how `npm` detects the location of the `package.json` file. Since this is a `monorepo`, I thought it would be best to keep the source trees as separate as possible.

To install the required dependencies, execute the following
```
npm install
```

The (ESLint VSCode Extension)[https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint] will be helpful if you plan on making `nodejs` changes

##### Development
To run the dashboard for development, you should run
```
npm run start:dev
```

This will start the backend server with `nodemon`, which will pick up file changes to the source tree and reload the server if they are made. This will also start a `webpack-dev-server`, which will do the same as `nodemon` but for the UI. The result is a running dashboard website whose code can be changed and without the need to manually reload the server.

##### Testing
To test the Dashboard, run
```
npm run test
```

This will automatically run the NodeJS `eslint` linter, you can run this separately with
```
npm run lint
```

##### Production
Before the Dashboard can be run in production mode, a webpack build must be run with
```
npm run build
```

To start the production web server, run
```
npm run start
```

This will serve the UI frontend from the `dist` directory, statically.

#### Sensors
##### Setup
You will also need `python` 3.10 installed, found here https://www.python.org/downloads/

To install the python dependencies you will need to run
```
python -m pip install -r requirements.txt
```

If you use VSCode, there are some recommended settings and extensions to speed up development:
 1. (Python VSCode Extension)[https://marketplace.visualstudio.com/items?itemName=ms-python.python]
 3. Change your `Python > Formatting: Provider` to `black`
 4. Set `Editor: Format on Save` to true, so that the Python formatting provider we just set will auto-format the file according to `black`'s formatting rules everytime you save
 5. Set `Python > Linting: Flake8 Enabled` to true

#### Testing and linting
To test the sensors, run
```
cd sensors
python -m pytest
```

To lint the sensors, run
```
cd sensors
python -m flake8
```

### Deployment

 TODO

Talk about Kubernetes configuration here ...

## Docker

For notes on how to use Docker in our project, please [see this link](./docs/Docker_README.md)