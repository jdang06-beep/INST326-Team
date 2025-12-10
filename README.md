
# Media Review Utility Library

## Project Title and Description
**Media Review Utility Library** is a Python function library designed to manage, analyze, and process media reviews efficiently. It includes utilities for validating reviews,
computing statistics, filtering by tags, anonymizing reviewer names, exporting/importing data, and recommending similar titles. This library provides building blocks for future
object-oriented projects and integrated information systems.

---

## Team Members and Roles
| Name          | Role                                      |
|---------------|-------------------------------------------|
| Lateef Ambali | Function implementation & documentation  |
| Eliab Getachew| Function implementation & code review    |
| Heaven Worku  | Function implementation & testing        |
|.Jolina Dang   | Repository management & documentation    |

---

## Domain Focus and Problem Statement
**Domain:** Information Science – Media Review Management

**Problem Statement:** Managing large collections of media reviews manually is inefficient. Our library solves key problems such as:
- Identifying the most-reviewed items
- Searching reviews by reviewer or tags
- Aggregating ratings and review statistics
- Exporting and importing review datasets
- Recommending similar titles for users

---

## **Function Library Overview and Organization**

| Category            | Description                          | Example Functions                                       |
| ------------------- | ------------------------------------ | ------------------------------------------------------- |
| **Validation**      | Ensure data consistency and quality  | `validate_rating()`, `validate_review_data()`           |
| **Cleaning**        | Prepare review text for analysis     | `clean_review_text()`, `remove_stopwords()`             |
| **Analysis**        | Compute statistics and metrics       | `calculate_average_rating()`, `summarize_reviews()`     |
| **Data Management** | Import/export and transform datasets | `export_reviews_to_csv()`, `import_reviews_from_json()` |
| **Recommendation**  | Suggest similar media titles         | `recommend_similar_titles()`                            |


## **Contribution Guidelines for Team Members**

Our team worked together to create this function library by dividing tasks, sharing ideas, and reviewing each other's work. The goal was to make sure everyone contributed meaningfully and understood the code we built.

---

### **🧩 Team Collaboration**
Each person was responsible for adding different functions to the main library while also helping with testing and reviewing.  
We used GitHub to keep our work organized — everyone made updates in their own sections and checked in regularly with the group to make sure everything fit together smoothly.

| **Team Member**   | **Main Responsibilities** |
|--------------------|----------------------------|
| **Lateef Ambali**  | Focused on function creation, writing documentation, and improving readability of the code. |
| **Eliab Getachew** | Reviewed teammates’ code, helped refine algorithms, and worked on improving data accuracy. |
| **Heaven Worku**   | Tested each function, fixed errors, and made sure the outputs were consistent. |
| **Jolina Dang**    | Organized the GitHub repository and helped maintain all documentation and formatting. |

---

### **💬 Communication and Review Process**
We communicated mainly through group chats and GitHub comments to give feedback and make improvements.  
Before adding new code, each person explained what their function was supposed to do and asked for suggestions.  
When someone made a mistake or their code didn’t run properly, we helped debug it together.  

During peer reviews:
- We checked that each function had proper docstrings and examples.  
- We made sure every team member understood their own code and any AI-generated parts they used.  
- We confirmed that all the functions worked well together and didn’t overlap.

---

### **🧠 Documentation and Testing**
We kept all code and notes up to date in the `docs/` folder so anyone could easily understand what each function does.  
Each person tested their own functions and then another teammate’s functions to make sure results were accurate.  
We also made small example scripts in the `examples/` folder to show how our functions could be used in real situations.

## UPDATED DOCUMENTATION PROJECT 2 
For this portion of the project, our team focused on transforming our Project 1 function library into an object-oriented system by designing and implementing core classes. We successfully created the MediaItem class, along with supporting classes like Reviewer, Review, Catalog, and RecommendationEngine, each with proper encapsulation, validation, and documentation. The team collaborated using feature branches, pull requests, and peer reviews to ensure code quality and maintainability. Integration with our existing Project 1 functions allowed methods like title normalization, similarity computation, and tag-based recommendations to work seamlessly. Overall, this phase strengthened our understanding of OOP principles and set a solid foundation for future subclassing and polymorphism in Project 3.
Documentation included:
- **Function names and what they do**  
- **Input and output examples**  
- **Any errors or issues we fixed**  
- **Notes on improvements after code review**
---
## ✅ Running the Test Suite

This project uses Python’s built-in `unittest` framework for all testing.
All tests are located in the `tests/` directory and are divided into:

- Unit Tests  
- Integration Tests  
- System Tests  

### 🔹 Windows (PowerShell)

From the project root:

```powershell
$env:PYTHONPATH = (Get-Location).Path
python -m unittest discover -v tests
---
## **Contribution Guidelines for Team Members**

- **Collaboration:** Everyone on the team should take part in building, testing, and improving the functions. We all share responsibility for making sure the library works smoothly.  
- **Commit Messages:** When pushing changes, write clear and short messages (for example: `add: new rating validation function` or `fix: incorrect average calculation`).  
- **Coding Standards:** Follow **PEP 8** style rules to keep our code clean and easy to read. Use meaningful variable names and add helpful comments when needed.  
- **Testing Requirements:** Every new function should come with at least one test to make sure it runs correctly and doesn’t break anything else.  
- **Code Review:**  
  - Each pull request should be reviewed by at least one teammate before merging.  
  - Give helpful and respectful feedback focused on clarity and function performance.  
- **Documentation:** Whenever a function is added or updated, make sure to update the docstrings and this README file if needed.  
- **Communication:** Use our group chat or GitHub issues to stay in touch, share progress, and avoid working on the same part of the project at the same time.  
- **Respect and Accountability:** Everyone’s ideas and work matter. Be respectful, meet deadlines, and make sure everyone contributes fairly to the final product.  
---
## **Usage Examples for Key Functions**

```python
from media_utils import (
    validate_rating,
    calculate_average_rating,
    filter_by_tag,
    anonymize_reviewer,
    export_reviews_to_csv,
    recommend_similar_titles
)

# **Validate a review rating**
print(validate_rating(4.5))  # Output: True

# **Compute average rating from a list of reviews**
ratings = [5, 4, 3, 4, 5]
print(calculate_average_rating(ratings))  # Output: 4.2

# **Filter reviews by tag**
reviews = [
    {"title": "Inception", "tags": ["Sci-Fi", "Action"]},
    {"title": "Titanic", "tags": ["Romance", "Drama"]}
]
filtered = filter_by_tag(reviews, "Sci-Fi")
print(filtered)  # Returns reviews matching "Sci-Fi"

# **Anonymize reviewer names**
review_data = [{"reviewer": "John Smith", "rating": 5, "text": "Great movie!"}]
anon_reviews = anonymize_reviewer(review_data)
print(anon_reviews)

# **Export reviews to CSV file**
export_reviews_to_csv(review_data, "output/reviews.csv")

# **Recommend similar titles**
database = [
    {"title": "Inception", "tags": ["Sci-Fi", "Thriller"]},
    {"title": "Interstellar", "tags": ["Sci-Fi", "Drama"]},
    {"title": "Titanic", "tags": ["Romance", "Drama"]}
]
recommendations = recommend_similar_titles("Inception", database)
print(recommendations)  # Expected output: ["Interstellar"]
---







