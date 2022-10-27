TAG=$1

if [[ -n $TAG ]]; then
  git checkout -b rollback-$TAG
  git revert $TAG
else
  echo "Missing argument: TAG"
fi

crap code is now in main

on a branch
git revert to a tag which isn't broken, most recent
merge the branch
delete the new crap tag from master