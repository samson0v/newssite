# Test Task (News Site)
Wrote on:
 - HTML5
 - CSS3
 - Python
 - Django 3.0
 - PostgreSQL
 - Mailgun(Email backend)
 ## Start Up
 - Clone GitHub repository 
  >**ProTip** You can do it by this link github.com/samson0v/newssite
 - Make virual enviroment
 >**Pro Tip** In terminal use the command: virtualenv -p python3 . (Make sure you are in outside folder)
 - Download all pip packages
 >**Pro Tip** You can find all packages in requirements.txt file in GitHub repository 
 - Make migrations
 - Run server
 ## Quick guide
 When you open the site you come up to the catalog news.
 https://photos.app.goo.gl/8obpjZbK7an8Tvpm8
 Let`s go to the header. It include:
 - Logo
 - Login Button
 - Sign Up Button
 >**If You Are At Once** If you the first time on the site and want to craete news, you must create a new account. To do this, click on Sign Up Button.
 
>**If You Have An Account** If you have an account, click on Login Button.
 
 At the center you can see News Feed. 
 
**Create an account**
To create an account click on Sign Up Button and you will go to Sign Up Form.
https://photos.app.goo.gl/EuipEjrRjcWXMBZ1A
The Sign Up Form have the next field **(all field are requirement)**:
 - First Name
 - Last Name
 - Birthdate
 - Username
 - Email
 - Password
 - Re Password
 - Sign Up Button
 If you feel all field, click on Sign Up Button. The next step is to confirm your account. You will receive a letter on your email.
 >**ADVICE** Make sure you write on right email

 Next step it is see the letter and click on the link to confirm your account.
 https://photos.app.goo.gl/vtDQaUBADB5XZ7m77
Congratulations, you have the account. 

**Sign In Account**
To login to your account, click on the Login Button and you will see Login Form.
https://photos.app.goo.gl/Km1gLg5TvL9iLTde9
The Login Form have the next field **(all field are requirement)**:
 - Email
 - Password
 - Login Button

**Create a news**
To create a news click on Add News Button and will see Add News Form.
https://photos.app.goo.gl/B7AHtu72i1K82VcC7
The Add News Form have the next fields **(all field are requirement)**:
 - Title
 - Text
 - Image
 - Add News Button

After all click on the Add News Button and your news will go to moderate mode. 
>**ProTip** If you are user, your news will be moderate every time  you add them.
>If you are editor, your news woun`t be moderate.
>If you are administrator, your news woun`t be moderate.

**If You Are Admonistrator**
You can go to the Admin Panel by follow the link below
https://newssiteplaneks.herokuapp.com/admin/
and you will see Login Form https://photos.app.goo.gl/nF4Y518tz3bfaiVb9.
On the next page you can see the next information https://photos.app.goo.gl/HKwC2iSMNqXfobZn7
When you click on the Group, you can add/edit/delete user groups and add/delete there permission. (see first link below)
When you click on the User, you can add/edit/delete user and edit there groups and permission. (see second link below)
When you click on the Newss, you can add/edit/delete them and add/edit/delete comments and moderate them. (see third link below)
1. https://photos.app.goo.gl/8VJR6MBPzdVjHppa6
2. https://photos.app.goo.gl/ifmjTKgH7FBu69n28
3. https://photos.app.goo.gl/SumH6pYasbK45NTp6
4. https://photos.app.goo.gl/ufXmJXm2BQuoqTr56

## For Developers
**Email Backend**
To send email, you must to do:
 1. In settings.py change EMAIL_HOST_USER and EMAIL_HOST_PASSWORD fields.
 2. If you want to send html template email, in users/templates/Email.html
change it if you want custom html template.
3. And in users/views.py change send_simple_message() function with your own arguments.
>**ProTip** If you want to send text email, change "html" raw to "text" raw in send_simple_message() function.
