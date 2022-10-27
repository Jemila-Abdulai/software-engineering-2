set -e

BUMP=1

if [[ -z $1 ]]
then
  echo Missing first argument: part to bump, "major", "minor" or "patch"
  BUMP=0
fi

if [ "1" == "$BUMP" ]
then
  # go to the root of the repo
  cd $(dirname "$0")/../

  # bump the version
  python -m bumpversion $1 --config-file VERSION.cfg
  VERSION=$(python util/what-version-are-we.py)
  git tag -a $VERSION -m "Bump to $VERSION"
fi
