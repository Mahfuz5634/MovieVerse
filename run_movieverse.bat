@echo off
title MovieVerse - Film Recommendation Engine
echo ========================================================
echo Launching MovieVerse Recommendation System
echo ========================================================
echo.
cd /d "%~dp0"
"..\venv\Scripts\streamlit.exe" run app.py
pause
