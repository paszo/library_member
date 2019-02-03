{
'name': 'Library Members and Borrowing',
'description': 'User library cards for people to borrow books',
'author': 'Daniel Reis',
'data': [
    'views/book_view.xml',
    'security/library_security.xml',
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/member_view.xml',
],
'depends': ['library_app'],
'application': False,
}
