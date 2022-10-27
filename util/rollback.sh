TAG=$1

if [[ -n $TAG ]]; then
  git checkout -b rollback-$TAG
  git revert $TAG
else
  echo "Missing argument: TAG"
fi
