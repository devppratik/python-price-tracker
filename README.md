# Python Price Tracker

A Simple Python Script to Track Product Prices.

The script uses Beautiful-Soup, smtplib and request modules to track prices and send Emails when prices go below your desired price. The modules can be installed using the command: *pip install module_name*

The scripts used are a bit different for Flipkart and Amazon as they have different HTML structures.

#### *The products urls used were random from my respective search history*

### Important Notes:

    • To use the script, Two-Factor-Authenication in Google Account needs to be enabled. 
    • Generate a App Password from your Google Account 
                Refer : https://support.google.com/mail/answer/185833?hl=en-GB
    • Replace the URL and desired price according to your needs.
    • Replace the User-Agent with your browser user agent. Find it by searching for "My User Agent" 
    • The mail_1, mail_2 variables needs to be replaced  with the mail id you wish to use. 
    • The passwd needs to replaced with the generated app password
