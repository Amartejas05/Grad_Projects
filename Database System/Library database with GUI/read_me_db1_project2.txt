QUERIES:
	SELECT * FROM LIBRARY.employee ;
	SELECT * FROM LIBRARY.books ;
	SELECT * FROM LIBRARY.catalog ;
	select * from library.issue;
	select * from library.members;


Functionalities:

1. Any new member that has to be added to the members database. One has to fill up the membership form.
2. Any New Employee who has to join the library or as an professor will fill the employee form.

MEMBER_LOGIN:

1.member who wants to login has to enter credentials.
2.after successful login he can view books.
3.if he wants to rent the book. He will type the ISBN number in the box given next to request books and click the submit button.
4.he will be notified with a pop-up to contact ref_librarian.
5.while returning the book he under goes the same procedure as requisition.
6.If he wants to extend the membership then he do that by clicking the extend button which automatically renews the issue date.

EMPLOYEE LOGIN:

1.employee who wants to login has to enter credentials.
2.after successful login he can view books, get the description of books, weekly_report.
3. He can get the list of due dates of everyone who have borrowed the books with their member_ID.
4.If any new book has to be added to catalog then he can add the book by adding the details of the books.

Assumptions:

1.reference librarian can do all the functions related to books.
2.other have no access to get weekly report or insert new book.
3.One who is a professor has to fill employee form to show that he is directly added to the membership database.
4.triggers will be indicated as pop-up window when they click on the appropriate buttons.


Note:
1. We have not used any data file to load data. We doing it dynamically.
2. We have not used triggers instead used buttons to notify the member about his due date or membership extension.
 





