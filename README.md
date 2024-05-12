# coronavacuna

⚠️ This project has been archived and it is no longer maintained.

A simple [personal project](https://miguelangelcolmenero.eu/proyectos/coronavacuna/) which retrieves the data of the vaccinated people in Spain from [Our World In Data](https://ourworldindata.org/covid-vaccinations) and displays it on a simple manner.

## coronavacuna_scrapper.py
This Python script scrapes the vaccinations data from Our World In Data and generates a JSON file with the data retrieved. It runs four times a day.

## index.html
This is the index page of the website where it is hosted. A script in JavaScript retrieves the data from the JSON file and displays the data. Previously a countdown with the time to end the [Alarm State](https://en.wikipedia.org/wiki/State_of_alarm_(Spain)) in Spain was placed, but since the Alarm State prescribed it was removed.

## dataSpain.json
This is a sample of the file generated from the Python scrapper.
