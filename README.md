# ZsskTicketsToGoogleCalendar

- parser.py používa PyPDF2 a vytiahne dátumy, časy a stanice začiatku a konca z .pdf lístka (na mobilový .png nefunguje !!!)

- zapisovanie do Google kalendára sa deje v calendar_writer.py, ktorý ale aby fungoval treba mať na Google Cloud Console projekt (for record - u mňa sa volá calendar project), v ňom mať pridané Google Calendar API, vytvorený  OAuth 2.0 Client IDs (treba mat v projekte ulozene ako credentials.json, z coho sa pri prvom volani zgeneruje token.json) a keďže mi to nešlo, tak som aj sama seba pridala ako testera, a potom to už behalo. 
