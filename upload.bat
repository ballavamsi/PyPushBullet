bumpversion patch
git push
git push --tags
python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/* --verbose
