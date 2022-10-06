# Notes on how to use Docker

## Rough Notes on Commands

```
# Move to the Git Repo
$ cd /path/to/software-engineering-2
```
Then to start building:
```
$ docker build -t test1 -f .\Docker\Dockerfile .
```
Run the container:
```
$ docker run -it test1
```
... which will allow one to enter the container at the `ENTRYPOINT` (which is a bash shell, whacking you in at `/` as `root`)

To run the container in the background, please enter:
```
$ docker container create test1
$ 5370e25a407835e225fa68074d318837d491e91f219da638f5eba33d10ee0307    # <container id example>
$ docker container start 5370e25a407835e225fa68074d318837d491e91f219da638f5eba33d10ee0307
```

To then enter a running container: 
```
$ docker exec -it 5370e25a407835e225fa68074d318837d491e91f219da638f5eba33d10ee0307 bash
```
... if the container doesn't do so there is a chance that the container isn't running, which is normal if a persistent process isn't running (if no processes, Docker will just exit the container).

## Syntax of the `docker build` command

`docker build -t test1 -f .\Docker\Dockerfile .`

### Table explaining the above

| Term                  | What it is                                   |
|-----------------------|----------------------------------------------|
| `docker`              | Docker command                               |
| `build`               | Build command                                |
| `-t`                  | Tag flag                                     |
| `test1`               | Tag name (user defined)                      |
| `-f`                  | Filename flag (for Dockerfile)               |
| `.\Docker\Dockerfile` | Path to Dockerfile to use (from current dir) |
| `.`                   | Build context (relative or absolute path)    |

Please note that the Path I provide here is a Windows path, Mac and Linux users will want `/`s.

We want to make sure that the build context is the parent directory of the project, or this doesn't work and Docker complains that it can't do the `COPY` line(s).

i.e.
```
pwd
C:\Users\SamReece\Desktop\UoEx\Year 4\Software Engineering 2\COURSEWORK\software-engineering-2\
```
... we use `.` as the build context (relative path)
OR
... we can use the absolute path as the build context (not shown as my path has spaces which makes life more difficult).

Note - when using the relative path, keep an eye on your cwd!

# Building the Image