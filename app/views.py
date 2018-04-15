from flask import Flask, render_template, flash, redirect, url_for
from . import app

'''
Index view - Displays a list of categories and most recent items
'''
@app.route('/')
def showCategories():
    return render_template('categories.html', categories=['test1', 'test2'])

'''
Category view - Displays a list of all items in the selected category
'''
@app.route('/category/<int:category_id>')
@app.route('/category/<int:category_id>.<format>')
def showCategory(category_id, format='html'):
    return "display items in a category"

'''
Add a new item to the selected category
'''
@app.route('/category/<int:category_id>/items/new', methods=['GET', 'POST'])
def newItem():
    return "Create a new item in the category"

'''
Edit the selected item
'''
@app.route('/category/<int:category_id>/items/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem():
    return "Edit an item"

'''
Delete the selected item
'''
@app.route('/category/<int:category_id>/items/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem():
    return "Delete an item"

'''
JSON endpoint to a list of categories
'''
@app.route('/JSON')
def showCategoriesJSON():
    return "JSON endpoint for category listing"

'''
JSON endpoint to a list of items in a category
'''
@app.route('/category/<int:category_id>/items/JSON')
def showCategoryJSON():
    return "JSON endpoint for items in category"

'''
JSON endpoint to a specific item
'''
@app.route('/category/<int:category_id>/items/<int:item_id>/JSON')
def showItemJSON():
    return "JSON endpoint to specific item"