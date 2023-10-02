bumpversion alpha
git push
git push --tags
python setup.py sdist bdist_wheel
twine upload dist/*
