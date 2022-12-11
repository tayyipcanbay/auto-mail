# auto-mail

1) For the mail HTML edit mail.html before start the program.

2) For the attachments add all of the attachments to the attachments folder before start the program.

3) Add all the receivers to mail_list.txt file. Add a new line for every single address.

4) When you start it you have to give your mail address as an input.

5) After the mail address we need Application Password <a href="https://yandex.com/support/id/authorization/app-passwords.html">Here is the tutorial</a>

6) After you create it give as an input to program.

-------------------------------------------------
YOU CAN TRACK THE PROGRESS FROM THE TERMINAL
-------------------------------------------------



# Using another mail service

For using another mail service you just have to edit ```host``` and ```port``` from the ```init()``` function. For example

  ```
    server = smtplib.SMTP ('host.address.com', 587)
  ```
