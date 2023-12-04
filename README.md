# PFW_ChatBot (Please keep this readme updated)

CS59000-03 Group Project for Course

## Motivation:
> Purdue Fort Wayne doesn't have a chatbot right now. The current process is to communicate/post queries to relevant people using existing coimmunication channels. This leads usually to ask a lot of FAQs, which becomes repetative at some point.

## Goal:
> * The current idea is to design this chatbot in the scope of PFW CS Department only.
> * Good enough performance.
> * Quick response with even quicker turn around time.
> * Should be accurate.

## Tech Stack:
> * Python
> * Flask
> * React
> * PaLM API
> * Playwright
> * JSON

## Creators:
> * @sanidhyaRsharma
> * @staticowl
> * @knsspsj19
> * @dannypz97

## Prerequisites:
> 1. keyboard-0.13.5 (from pip)
> 2. Python (>=3.10)

## Installation:
> 1. Clone the repository
> 2. Two ways to install backend dependencies the program, after you go to the backend directory.
>> 1. Run `python3 app.py -s` in the terminal. This will trigger the setup script which will install all the dependencies required.
>> 2. Or you can run `pip3 install -r requirements.txt` to install all the dependencies.
> 3. For the frontend, go to the frontend directory and run `npm install` to install all the dependencies.

## Usage:
> 1. Run the backend:
>> 1. First Time Users, collect the data using `python3 app.py -sc` in the terminal. This will collect the data from the URLs mentioned in the `urls.txt` file.
>> 2. Run the program using `python3 app.py` in the terminal. This will start the backend of the program.
> 2. Run the frontend using `npm start` in the terminal.

And Voilà! You should be able to access the chatbot in localhost.

## Important Instructions:
> * Have used `esc` as a default escape button for any and every operation in the program.

## Features:
> * PaLM API is currently being used for the chatbot.
> * The chatbot is currently trained on the data collected from the URLs mentioned in the `urls.txt` file.
> * The chatbot currently only supports the following topics:
>> * Courses
>> * Faculty
>> * Research
>> * Credits
>> * Contact
> * It also produces a confidence score for the response it gives.
> * In case the chatbot doesn't know anything in particular, it will redirect you to the relevant person to contact.

## Tasks:
>* Feel free to add any task you think is important.

| Task                          | SubTask             | Assigned to            | Current Status | 
|-------------------------------|---------------------|------------------------|----------------|
| Approval Procedure            | -                   | All                    | [x]            |
| Requirements                  | -                   | All                    | [x]            |
| Design                        | Auto Install        | @staticowl             | [x]            |
| Backend                       | Flask Backbone      | @dannypz97             | [x]            |
| Backend                       | Setup APIs          | @dannypz97             | [x]            |
| FrontEnd                      | React               | @sanidhyaRsharma       | [x]            |
| Integrate Front-end back-end  | React               | @sanidhyaRsharma       | [x]            |
| Integrate Back-end with model | Flask               | @dannypz97             | [x]            |
| Model                         | Model Type Finalize | @knsspsj19, @staticowl | [x]            |
| Model                         | PreProcessing       | @knsspsj19, @staticowl | [x]            |
| API                           | Context             | @dannypz97             | [x]            |
| Data                          | Scraping URL List   | All                    | [x]            |
| Convert UI to Modal           | Move Chat component | @sanidhyaRsharma       | [x]            |
| Setting up login/signup       | Login               | @sanidhyaRsharma       | [x]            |
| Setting up login/signup       | Sign Up             | @sanidhyaRsharma       | [x]            |
| Data Collection               | Scrapping Config    | @staticowl             | [x]            |
