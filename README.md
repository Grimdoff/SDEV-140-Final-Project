# SDEV-140-Final-Project
The orginal scope of my project proved too much. I have since scaled it back. The goal was to create a program that only took a waitlist order and allowed staff to modify it. I dropped the survey section and the ordering section as I learned about databases too late to program and troubleshoot those sections. I also scrapped most of my orginial code as I was having calling a dictionary between functions. Instead I opted for a database appoarch which seems to work fairly well. The program works as intended though there is a section of code that I have commented out due to me not being able to get it to work in time.

Currently there is no safe guards in terms of input validation other than a box expecting a string or an integer. Overflow is an issue as well as bad actors using the entry boxes as a way to maliciously enter code into the system.

Things to fix in the future should I attempt this project again:

1. A better looking gui. While the current one works as intended, it is by no means pretty or ready for a business end
2. Add a more robust input validation to deter attacks on the system. Preventing special characters from being entered, limiting the length of how many characters can be entered/how many characters are expected to be entered.
3. Rewriting how window generation takes places so that there is only one parent window and many children windows instead of them all being parent windows.
