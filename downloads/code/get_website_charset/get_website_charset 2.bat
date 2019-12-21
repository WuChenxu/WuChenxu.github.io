@echo off
set bat_file_name=%~n0

set file_suffix=.py

set file_name=%bat_file_name%%file_suffix%

python %file_name%
pause