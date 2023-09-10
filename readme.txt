Greetings to the GDSC Team! My name is Prithu Paresh (2022A4PS1795H) and this is my submission for the inductions of GDSC.
The project name is Hello and it has one django app called home.

Steps to run the project
1. Clone the project from github, at https://github.com/sawbl4de/Baba-s_Archive.
2. Install the dependencies needed from the requirements.txt file.
3. Start the development server in your Terminal and you can now run the project on localhost.

The superuser login for the admin site is:
Username - prithu
Password - prithu2205

Ordinary user login for the main site is:
Username - rohan
Password - 1122334455
Alternatively, you could create a new user using the Sign Up option.

Some changes I know I could have made:
1. When Login fails due to invalid credentials, I have a django message flashing on the screen saying "Invalid Credentials. 
    Please try again.". I had to use messages.success to achieve this, because messages.error wasn't working for some reason.
2. Same with the other error messages, I tried to use messages.error for them but couldn't.
3. When I pull data from my home_poems table in my PostgreSQL, the data is being retrieved correctly, but I am unable to 
    display the poem content correctly. The line breaks (new lines) are not showing up on the site, even though the poem 
    content has been entered correctly in the database.
4. I had added a footer in my base.html file, and I extended base.html in my index.html file. My index.html file has a carousel,
    and the footer was overlapping it. No other pages had an issue, but I have removed the footer anyway. I tried hiding the 
    footer only on the index.html page using CSS styling, but I couldn't figure out how to.
