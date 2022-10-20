if [ "" == $1 ];
  echo Missing first argument
  echo
  echo Usage:
  echo    bump-version-to.sh new-version-number
  exit 1
fi

# go to the root of the repo
cd $(dirname "$0")/../

# bump the version
python -m bumpversion --config-file VERSION.cfg --tag-name v$1

git push
