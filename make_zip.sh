#/bin/sh

ZIP=pomodoro.zip

rm -f $ZIP
zip -r $ZIP pomodoro
zip $ZIP __main__.py
zip -d $ZIP "pomodoro/__pycache__/*.pyc"
zip -d $ZIP "pomodoro/__pycache__/"