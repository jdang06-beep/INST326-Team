# Data Persistence – Media Review Library

The Media Review Library application includes a full data persistence layer to ensure that all media records, user reviews, and workflow outputs are reliably maintained between sessions. Because this system functions as a real library management tool rather than a single-use script, persistence is a core design requirement. The system supports saving and loading state, importing datasets, exporting reports, and handling errors gracefully.

---

## 1. Saving and Loading System State

The application automatically saves the entire system state—media items, metadata, user reviews, and ratings—to a persistent JSON file. JSON was selected because it:

- supports nested structures (e.g., media → reviews),
- is human-readable and easy to debug,
- works naturally with Python,
- does not require an external database server.

Whenever users add new media, update reviews, or modify the library, the system writes these changes to a file such as `media_library.json`. On startup, the program loads this file to restore the library exactly as it was, allowing users to continue where they left off. This behavior aligns the system with real-world Information Science applications that maintain long-term records.

---

## 2. Data Import

The Media Review Library supports data import from standard formats such as CSV and JSON. This allows users or instructors to begin with an existing dataset rather than manually entering media. Imported data may include:

- Titles  
- Creators (author, director, artist)  
- Release years  
- Genres or categories  
- Descriptions or other metadata  

The system validates the incoming file structure and converts each entry into a standardized media object. This demonstrates core IS principles of integrating external data sources into a unified system.

---

## 3. Data Export and Reporting

The application can export data in widely compatible formats. Users can generate:

- library summaries  
- review or rating reports  
- filtered item lists (e.g., by genre or rating)  
- processed datasets  

Exports are created in formats such as CSV, JSON, or text files and saved to an `exports/` directory. This supports reuse of the library’s data in analytics tools, spreadsheets, or external applications.

---

## 4. Error Handling and Data Integrity

To ensure reliability, the persistence layer includes robust error handling:

- Detects missing or unreadable save files  
- Creates a new persistence file if none exists  
- Catches JSON decoding errors (corrupted/malformed files)  
- Validates structure before importing CSV/JSON data  
- Provides clear user messages for failed imports or exports  
- Handles file permissions or I/O issues gracefully  

These safeguards prevent crashes and ensure that users do not lose progress, even when encountering invalid files or unexpected storage conditions.

---

## Summary

The Media Review Library’s data persistence design provides a professional-level, fully functional system. Users can:

- permanently store media items  
- retain user reviews and ratings  
- import datasets from standard file formats  
- export reports and summaries  
- rely on the system to recover safely from errors  

These capabilities fulfill the capstone requirement of creating a reliable, persistent Information Science application that supports real workflows end-to-end.
