TAG=$1

if [[ -n $TAG ]]; then
  git revert $TAG
else
  echo "Missing argument: TAG"
fi