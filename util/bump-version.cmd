

set REPO_ROOT=%~dp0..\

if %1 == "" echo Missing first argument: part to bump, "major", "minor" or "patch" && exit

cd %REPO_ROOT%

python -m bumpversion %1 --config-file VERSION.cfg
VERSION=$(python what-version-are-we.py)
git tag -a $VERSION -m "Bump to $VERSION"