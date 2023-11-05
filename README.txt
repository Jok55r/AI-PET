FULL GUIDE ON THIS APP:


SETUP:
you will need to change 'Secret.txt' file with your character ai TOKEN on the first line and your current CHAT on the second

here is how to find both:
1. token
    -go to developer tab in character.ai browser and find 'Application' menu
    -open Local Storage -> https://beta.character.ai -> char_token
    -copy the full value without ' or " to the 'Secret.txt' in the first line
2. chat
    -open any character you want
    -click at the url and copy the value between '...char=' and '&source=...'
    -paste it as the second line in 'Secret.txt'
3. done
    you're good to go
    
DO NOT SHARE THE TOKEN TO OTHER PEOPLE, YOU MIGHT GET IN TROUBLE!
'Secret.txt' IS STORED LOCALLY AND NO ONE EXCEPT YOU WILL HAVE ACCESS TO IT


SETTINGS:
there is a 'settings.txt' file that's, of course, managing the settings of the app

this is the order of settings:
1. line:
    this is prefix for '_talking' and '_idle' which MUST BE .JPG
    these images needs to be stored in 'Resources'
    for example if you type 'char' the program will show 'char_talking.jpg' and 'char_idle.jpg'
2. line:
    Y/N if you want this horrible text-to-speech to be enabled
