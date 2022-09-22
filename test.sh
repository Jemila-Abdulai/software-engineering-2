# tests all applications

cd dashboard && npm run test

cd sensors
python -m flake8
python -m pytest