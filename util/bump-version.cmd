@echo off

set REPO_ROOT=%0/../
echo %1

if %1 == "" echo Missing first argument: part to bump, "major", "minor" or "patch" && exit

cd REPO_ROOT

python -m bumpversion %1 --config-file VERSION.cfg --tag --commit
