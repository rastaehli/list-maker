
# Design for web application page content and navigation

# /index (default address) redirects to /home
# /home displays /categories and /latest
# /categories returns list of all "category" items
# /latest returns list of most recently modified "type" items
# a "category" x links to /category/{x}
# /category/{x} returns a list of "types" in category x
# a "type" links to /type/{x}
# /type/{x} returns the definition of a checklist type x
# all views include /home and /login links at the top
# /login displays user/password fields and "login" button
# "login" button validates credentials and redisplays /login with error if invalid
# "login" button sets "loggedIn" session state if login is valid
# when state is "loggedIn" all views display "logout" button
# "logout" button removes "loggedIn" state
# when "loggedIn", home includes "addItem" link above latest items list
# when "loggedIn", /type/{x} displays "edit" and "delete" links
# "addItem" links to /type/edit
# /type/edit diplays form with "title", "description", "category", input fields and an "save" button.  The category input offers a dropdown with a list of existing categories.
# the "save" button creates the checklist type, or updates it if an existing type was being edited. 
# the "edit" button links to /type/edit with the content of the existing type to edit.
# the "delete" button links to the "deleteConfirmation" form with "yes" and "cancel" buttons
# the "cancel" button returns to the previous page
# the "confirm deletion" button deletes the type before returing to the previous page

