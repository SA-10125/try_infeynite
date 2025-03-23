8# try_infeynite
 
## Overview:

Our team of three secured 4th place at InFeynite, an 18-hour hackathon hosted by the  ECE department at PES University, Electronic City campus where we developed a secure encrypted channel of communication utilising several open-source encryption algorithms such as XChaCha, ECC and LSB steganography.
Proud to have worked with an incredible team: Vinaayak G Dasika and Madhav Vinod.

## My role:
Built the backend for the website to send secure messages. This included:

    1. Creating models in django such as 
(i) Users that can sign up using username, password and email ID. 
(ii) ID cards connected to each user that hold unique User ID
(iii) Pouches of two that holds 2 User ID'S and certain keys. (created only once first message is to be sent bw two users.)
(iv) Messages containing sender, reciever, subject and message.

    2. Making pages and methods to send the messages. (backend)

    3. Integrating the encryption method.

    4. Rendering frontend.

## To run:

Aftee downloading dependencies, to run, download folder and go to directory containing manage.py in cmd, then 'manage.py runserver' .