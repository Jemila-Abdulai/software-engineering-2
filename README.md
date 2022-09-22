# software-engineering-2

# TOC

  - [software-engineering-2](#software-engineering-2)
  - [TOC](#toc)
    - [How we work](#how-we-work)
      - [Pull Requests](#pull-requests)

## How we work

- Weekly Thursday standups and bi-weekly sprints to discuss progress or any blockers
- Log of initial allocation of work
- Project will be split up into phases to decide internal deadlines and to allocate tasks
- A DevOps approach of continuous and iterative delivery will be followed for each phase

### Contributing

#### Environment and Initial setup
You will need `nodejs` 16 installed, found here https://nodejs.org/en/
You will also need `python` 3.10 installed, found here https://www.python.org/downloads/

To install the python dependencies you will need to run
```
python -m pip install -r requirements.txt
```

To install the nodejs dependencies you will need to run
```
npm install
```

If you use VSCode, there are some recommended settings and extensions to speed up development:
 1. (Python VSCode Extension)[https://marketplace.visualstudio.com/items?itemName=ms-python.python]
 2. (ESLint VSCode Extension)[https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint] if you plan on making `nodejs` changes
 3. Change your `Python > Formatting: Provider` to `black`
 4. Set `Editor: Format on Save` to true, so that the Python formatting provider we just set will auto-format the file according to `black`'s formatting rules everytime you save
 5. Set `Python > Linting: Flake8 Enabled` to true

#### Repository map
 - `/sensors/CounterFit` - Desc. TODO
 - `/sensors/soil-moisture-sensor` - Python application, simulates an IoT sensor
 - `/dashboard` - React application, dashboard to monitor the sensors
 - `/scripts` - any utility scripts live here

Due to our usage of NodeJS and React for the sensor dashboard, there is a `package.json` file at the root of this repository.
The `package.json` allows you to define a number of named scripts for automation, run with `npm run <script-name>`. We use these to automate tasks which require multiple steps to speed up development.
Although not all of these tasks are directly related to the dashboard, this automation tool is generally useful.

#### Testing


#### Deployment



#### Pull Requests

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

