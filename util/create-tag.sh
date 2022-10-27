  VERSION=$(python util/what-version-are-we.py)
  git tag -a $VERSION -m "Bump to $VERSION"
  git push origin $VERSION