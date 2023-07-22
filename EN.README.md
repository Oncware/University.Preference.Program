This program, written in Python based on the tkinter framework, allows users to store information about universities and departments, add rankings and notes. Due to the program's lack of connection to a specific database or API, the entered information is collected from the user.

This program consists of 3 main pages:

Schools: On this page, users can add a university to the list by entering university, city, department, ranking, old ranking, and notes. They can also delete an existing university from the list.
Wishlist: On this page, users can add a university to the wish list or remove it from the list.
Presentation Days: On this page, users can record university presentation days. This information includes city, university, date, and notes.
The main functions of the program are as follows:

add_to_list: This function takes the information entered by the user and adds it to the data.
add_to_wishlist: This function adds a university selected by the user to the wish list.
delete: This function removes a university selected by the user from the data list.
delete_wishlist: This function removes a university selected by the user from the wish list.
load_listbox: This function loads and sorts the lists.
save_data, save_wishlist and save_presentation_days: These functions save the data, wish list, and presentation days to a json file.
load: This function loads the data, wish list, and presentation days from a json file. If the file cannot be found, it creates empty lists.
on_double_click: This function is called when the user double-clicks an item. It loads the selected university's information into the input fields.
edit_score: This function allows the user to edit the old ranking of a university.
add_to_presentation_days: This function takes the information entered by the user and adds it to the presentation days list.
This program provides a simple interface for users to manage and monitor their university and department preferences. Users can list universities and departments, add them to the wish list, track presentation days, and plan accordingly.




