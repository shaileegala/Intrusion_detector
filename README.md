# Intrusion detector 
Machine learning password intrusion detection application that will detect if an unauthorised user is trying to log in.
The decision is made by analysing a typing fingerprint which is generate by difference in key press timings between 
characters in the password. A T-Distribution Test is used to make a decision against the sample and population

Language: python3.6
DB: MySQL

Step 1: Sign Up
Step 2: Log In yourself. You should get an alert saying 'OK'
Step 3: Give your username and password to your friend and ask them to log in. 
        You should get an alert saying 'Intrusion Detected'. 
        The reason being that although the password matches, your way of typing does not match your friend.