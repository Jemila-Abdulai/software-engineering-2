TAG=$1

if [[ -n $TAG ]]; then
  if [[ "" -ne $(git tag -l "$TAG") ]]; then
    git revert $TAG
  else
    echo "Tag not found"
  fi
else
  echo "Missing argument: TAG"
fi