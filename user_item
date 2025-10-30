user_system/user_item.py
class User: # represents users in our review system

  # stores all usernames 
  all_usernames = []

  def __init__(self, username): # creates a new user with a given username
    self._username = username 
    self._saved_reviews = [] 
  
  @classmethod
  def create_user(cls): # creates a new username
  # while loop used to make sure user ends up eventually entering a valid input  
    while True:
      username_input = input("Enter a username: ")
      clean_username = username_input.strip()

      # ensures that the username is not empty, must have atleast 1 character
      if not clean_username:
        print("Username cannot be empty, please try again.\n") 
      elif clean_username in cls.all_usernames:
      #ensures that the username is not already in use
        print("{clean_username} is already taken, please choose another.\n")
      else:
        # once the username is verified as a valid username, the user is created
        new_user = cls(clean_username)
        cls.all_usernames.append(clean_username)
        print(f"Username: {clean_username} \nYour account has successfully been created.\n")
        return new_user

  @property
  def username(self): # returns the user's username (read-only)
    return self._username
  
  def save_review(self, media_title, review_descrip, rating): #saves a review to the user's list
    review_entry = {"title": media_title.strip(), "review": review_descrip.strip(), "rating": rating}
    self._saved_reviews.append(review_entry)
  
  def view_saved(self): #shows all the reviews the user has saved
    if not self._saved_reviews:
      return "User had not saved any reviews yet."
    # for nice and organized layout of info
    result = f"Saved Reviews for user:\n"
    result += "-" * 30 + "\n"
    for review in self._saved_reviews:
      result += f"Title: {review['title']}\n"
      result += f"Review: {review['review']}\n"
      result += f"Rating: {review['rating']}\n"
      result += "-" * 30 + "\n"
    return result
  
  def search_reviews(self, keyword): # allows user to search through saved reviews using a keyword
    key_search = [] 
    for review in self._saved_reviews:
      if keyword.lower() in review['review'].lower() or keyword.lower() in review['title'].lower():
        key_search.append(review)
    if not key_search:
      return f"No reviews found containing '{keyword}'.\n"
    return key_search 

  def __str__(self): # quick summary of the user 
    return f"User: {self._username} \nSaved Reviews: {len(self._saved_reviews)}\n"

  
  def __repr__(self): # for debugging
    return f"User(username = {self._username}, saved_reviews = {self._saved_reviews})\n"

  git add user_system/user_system.py
git commit -m "Add UserItem class with validation, encapsulation, and Project 1 integration"
git push origin feature/useritem-class
