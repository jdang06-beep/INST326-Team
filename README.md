
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

## **Usage Examples for Key Functions**

### 🧹 Clean Review Text
```python
from src.media_utils import clean_review_text

text = "Amazing show!!! <3 #mustwatch"
print(clean_review_text(text))
# Output: "amazing show mustwatch"





























