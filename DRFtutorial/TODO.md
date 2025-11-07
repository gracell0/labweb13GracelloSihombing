# TODO List for Making HTML Usable and Connected to API

## 1. Update CORS Settings
- [ ] Update DRFtutorial/DRFtutorial/settings.py to allow local origins for CORS

## 2. Modify HTML JavaScript for API Integration
- [ ] Update perpustakaan.html to fetch books from /basic/ API on page load
- [ ] Modify addBook() function to send POST request to /basic/ with form data and image upload
- [ ] Modify deleteBook() function to send DELETE request to /basic/<id>/
- [ ] Update displayBooks() to use API data structure

## 3. Test Integration
- [ ] Run Django server (python manage.py runserver)
- [ ] Open perpustakaan.html in browser and verify CRUD operations work
- [ ] Test search and filter functionality with API
