# Phonebook
Developed a comprehensive Phonebook application using Django, providing a user-friendly interface for managing contacts efficiently. Phonebook is a simple Django app to manage contacts (first name, last name, mail, phone, mobile phone)

# Technologies Used
HTML: Used for structuring the web pages.<br>
CSS: Employed for styling and layout.<br>
Django: For Backend <br>

# Quick Start
1. Add 'phonebook' to your INSTALLED_APPS setting like this::
```bash
   INSTALLED_APPS = (
   ...
   'phonebook',
 )
```
2. Include the phonebook URLconf in your project urls.py like this:
```bash
  url(r'^phonebook/', include('phonebook.urls')),
```
3. Run 'python manage.py' syncdb to create the phonebook models.
4. Start the development server and visit 'http://127.0.0.1:8000/phonebook/' to start phonebook.

# TODO
```bash
  - Create, edit, delete groups on contacts
```

# Screenshots
<img width="960" alt="image" src="https://github.com/mhdasif123/Phonebook/assets/97513284/7d8b9d99-b463-44c0-a25e-2496c4328631">
