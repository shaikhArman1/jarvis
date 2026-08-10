# Jarvis - Python Voice Assistant

## Overview
Jarvis is a Python-based voice assistant that performs basic tasks through voice commands. It can open applications, search the web, play music, and respond to user queries.

This project was built to explore how voice-based systems work and to understand automation using Python.

---

## Features
- Voice command recognition
- Text-to-speech responses
- Open websites and applications
- Play music from YouTube
- Perform basic web searches
- Execute simple system commands

---

## Tech Stack
- Python
- SpeechRecognition
- pyttsx3 (Text-to-Speech)
- pywhatkit
- OS & webbrowser modules

---

## How It Works
1. Listens to user input via microphone  
2. Converts speech to text using SpeechRecognition  
3. Processes the command using Python logic  
4. Executes the task (e.g., open browser, play music)  
5. Responds using text-to-speech  

---

<!-- commit-log: 2026-02-06T18:15:08 - refactor: move config values to constants file -->

<!-- commit-log: 2026-02-11T17:52:28 - fix: resolve import ordering and circular dependency -->

<!-- commit-log: 2026-02-12T21:18:34 - docs: add README section for local setup -->

<!-- commit-log: 2026-02-15T12:26:40 - docs: update inline comments and docstrings -->

<!-- commit-log: 2026-02-18T17:40:15 - chore: remove unused imports and dead code -->

<!-- commit-log: 2026-02-23T15:06:45 - fix: resolve import ordering and circular dependency -->

<!-- commit-log: 2026-02-24T21:40:02 - refactor: rename variables for clarity -->

<!-- commit-log: 2026-02-26T18:12:55 - test: add unit tests for core functions -->

<!-- commit-log: 2026-03-02T21:30:30 - fix: correct file path handling on Windows systems -->

<!-- commit-log: 2026-03-04T22:17:13 - fix: resolve import ordering and circular dependency -->

<!-- commit-log: 2026-03-08T09:54:46 - refactor: extract helper functions for better modularity -->

<!-- commit-log: 2026-03-11T20:35:46 - perf: cache repeated API calls to reduce latency -->

<!-- commit-log: 2026-03-16T14:53:23 - feat: add input validation and error handling -->

<!-- commit-log: 2026-03-17T19:34:00 - fix: adjust threshold values based on testing -->

<!-- commit-log: 2026-03-21T13:09:43 - chore: remove unused imports and dead code -->

<!-- commit-log: 2026-03-24T18:56:45 - fix: handle None types in response parser -->

<!-- commit-log: 2026-03-25T12:21:41 - feat: add input validation and error handling -->

<!-- commit-log: 2026-03-30T15:54:19 - fix: adjust threshold values based on testing -->

<!-- commit-log: 2026-04-22T14:47:41 - refactor: rename variables for clarity -->

<!-- commit-log: 2026-04-23T09:03:15 - refactor: move config values to constants file -->

<!-- commit-log: 2026-04-23T12:18:58 - perf: cache repeated API calls to reduce latency -->

<!-- commit-log: 2026-04-23T18:49:52 - refactor: rename variables for clarity -->

<!-- commit-log: 2026-04-23T20:48:11 - fix: correct file path handling on Windows systems -->

<!-- commit-log: 2026-04-23T21:23:53 - perf: cache repeated API calls to reduce latency -->

<!-- commit-log: 2026-04-30T14:42:14 - feat: add input validation and error handling -->

<!-- commit-log: 2026-05-13T09:44:35 - fix: correct file path handling on Windows systems -->

<!-- commit-log: 2026-05-13T11:10:34 - fix: adjust threshold values based on testing -->

<!-- commit-log: 2026-05-13T15:34:57 - refactor: extract helper functions for better modularity -->

<!-- commit-log: 2026-05-13T18:44:41 - fix: resolve edge case in data processing pipeline -->

<!-- commit-log: 2026-05-13T19:05:06 - feat: add logging to main processing module -->

<!-- commit-log: 2026-05-13T20:55:29 - fix: resolve import ordering and circular dependency -->

<!-- commit-log: 2026-05-14T09:31:31 - perf: optimize loop logic to reduce processing time -->

<!-- commit-log: 2026-05-17T15:14:20 - chore: update requirements.txt with pinned versions -->

<!-- commit-log: 2026-05-18T10:22:37 - perf: optimize loop logic to reduce processing time -->

<!-- commit-log: 2026-05-18T12:20:40 - fix: adjust threshold values based on testing -->

<!-- commit-log: 2026-05-18T17:44:04 - docs: update inline comments and docstrings -->

<!-- commit-log: 2026-05-18T17:06:20 - feat: add retry logic for network requests -->

<!-- commit-log: 2026-05-18T21:10:04 - refactor: extract helper functions for better modularity -->

<!-- commit-log: 2026-06-11T10:12:28 - refactor: move config values to constants file -->

<!-- commit-log: 2026-07-03T10:03:15 - fix: resolve edge case in data processing pipeline -->

<!-- commit-log: 2026-07-03T19:51:10 - test: add unit tests for core functions -->

<!-- commit-log: 2026-07-08T19:47:33 - fix: handle None types in response parser -->

<!-- commit-log: 2026-07-20T11:39:16 - chore: update requirements.txt with pinned versions -->

<!-- commit-log: 2026-07-20T11:10:08 - fix: adjust threshold values based on testing -->

<!-- commit-log: 2026-07-20T12:36:13 - fix: resolve edge case in data processing pipeline -->

<!-- commit-log: 2026-07-20T17:22:21 - feat: add logging to main processing module -->

<!-- commit-log: 2026-07-20T17:19:29 - fix: resolve import ordering and circular dependency -->

<!-- commit-log: 2026-07-20T18:12:58 - feat: add logging to main processing module -->

<!-- commit-log: 2026-07-20T18:08:12 - test: add unit tests for core functions -->

<!-- commit-log: 2026-07-20T20:34:42 - chore: remove unused imports and dead code -->

<!-- commit-log: 2026-07-20T20:42:18 - refactor: rename variables for clarity -->

<!-- commit-log: 2026-07-20T20:52:33 - refactor: rename variables for clarity -->

<!-- commit-log: 2026-07-20T21:17:30 - docs: add README section for local setup -->

<!-- commit-log: 2026-07-22T09:54:21 - fix: handle None types in response parser -->

<!-- commit-log: 2026-07-22T12:16:05 - refactor: extract helper functions for better modularity -->

<!-- commit-log: 2026-07-22T20:57:17 - fix: handle None types in response parser -->

<!-- commit-log: 2026-07-22T20:02:36 - perf: cache repeated API calls to reduce latency -->

<!-- commit-log: 2026-07-22T21:57:52 - feat: add input validation and error handling -->

<!-- commit-log: 2026-07-23T18:28:01 - feat: add input validation and error handling -->

<!-- commit-log: 2026-08-10T10:39:33 - chore: remove unused imports and dead code -->

<!-- commit-log: 2026-08-10T12:40:28 - feat: add retry logic for network requests -->

<!-- commit-log: 2026-08-10T16:39:22 - feat: add logging to main processing module -->

<!-- commit-log: 2026-08-10T16:58:28 - docs: update inline comments and docstrings -->

<!-- commit-log: 2026-08-10T18:26:10 - fix: correct file path handling on Windows systems -->

<!-- commit-log: 2026-08-10T22:16:41 - docs: add README section for local setup -->
