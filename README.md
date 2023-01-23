# ZsskTicketsToGoogleCalendar

- repo obsahuje skripty, ktore sparsuju .pdf subor s listkom na vlak od Zssk a pridaju danu cestu ako event do google kalendara

- parser.py používa PyPDF2 a vytiahne dátumy, časy a stanice začiatku a konca z .pdf lístka (na mobilový .png nefunguje !!!)

- zapisovanie do Google kalendára sa deje v calendar_writer.py, ktorý ale aby fungoval treba mať na Google Cloud Console projekt (for record - u mňa sa volá calendar project), v ňom mať pridané Google Calendar API, vytvorený  OAuth 2.0 Client IDs (treba mat v projekte ulozene ako credentials.json, z coho sa pri prvom volani zgeneruje token.json) a keďže mi to nešlo, tak som aj sama seba pridala ako testera, a potom to už behalo. 

# troubleshooting

- obcas sa stane, ze API prestane spolupracovat, vtedy je dobre vymazat token.json a pri spusteni a autentifikacii do kalendara sa zgeneruje novy



TODOs:
- zrusit vyrabanie textaku
- vyrezat z pdfka QRkod
- posielat QR kod do kalendara (https://developers.google.com/calendar/api/v3/reference/events) - nie je take straight forward - musel by sa nahravat do Drivu (https://www.projectpro.io/recipes/upload-files-to-google-drive-using-python), pricom treba drive API...
- medzinarodne cesty
- matchovat rozumnym regexom
