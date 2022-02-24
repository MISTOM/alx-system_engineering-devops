# Postmortem

![Developer Typo Funny](https://raw.githubusercontent.com/MISTOM/alx-system_engineering-devops/887d68037191d251d0c033d73b5775f60f11b759/0x19-postmortem/HowCanWeBeThisRubbish.gif)

## Issue Summary
On Tuesday 22/02/2022 at approximately 07:32:16 GMT an error ocurred in an isolated container running Apache Web Server and MySQL with the purpose of displaying a Holberton Wordpress site. GET requests demonstrated that users received Error Code 500 (Internal Server Error). The root of the outage was determined, at 07:58:23 GMT, to be a Typografical error regarding a file with extension `.php` presenting itself with extension `.phpp`.

## Timeline
7:32 am: Encountered that the website was returning a 500 status code.

7:34 am: `ps auxf` was utilized to verify running processes on `Apache2` and `MySQL`. `ps auxf` found processes to be running as expected, indicating an error with PHP/WordPress.

7:37 am: On `sites-available` in `/etc/apache2/` was able to determine that the web server provided content from `DocumentRoot /var/www/html/`.

7:41 am: Enabled debug mode in `/var/www/html/wp-config.php` to therefore `curl` website again.

7:43 am: Website `curl` showed a missing file `/var/www/html/wp-includes/class-wp-locale.phpp` required in `/var/www/html/wp-settings.php` for which it was quickly notices a typo for the file extension.

7:46 am: Fixed typographical error `.phpp` extension on the file to `.php` extension.

7:47 am: Realized a test `curl` on the website after the update. No further issues were reported.

7:58 am: Redeacted a Pupet manifest that allowed the automation of the typo error fix for other remaining servers.

## Root cause and resolution
The root cause of the incident in question was in fact a typographical error in which `/var/www/html/wp-settings.php` when tyring to load the file `/var/www/html/wp-includes/class-wp-locale.phpp` indicated that said file was non-existent. The file extension `.phpp` was supposed to be `.php`. Once the typo was corrected, tested and comfirmed to function accordingly a Puppet manifest was made to automate the fix on remaining servers affected if any.

## Corrective and preventative measures
Testing is imperative in order to prevent such incidents and more importantly diminish errors that require unnesesary work such as a typographical error. Nevertheless reviewing code and monitoring servers for a time period are also good ways to correct and prevent these types of ocurrences and at the same time focus on more hard to detect situations. Also fire Bob! It was his fault! (Theres no actual Bob and no Bobs were harmed during the making of this task.)
<img src="https://i.kym-cdn.com/photos/images/original/001/050/209/b01.png">
