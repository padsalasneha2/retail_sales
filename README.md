# Retail Sales Data Analyzer

A menu-driven, Python-based tool that loads retail sales data (CSV or Excel), cleans it, calculates key
business metrics, filters and aggregates records, and visualises sales trends using Matplotlib and Seaborn.

---

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Objectives](#2-objectives)
3. [Features](#3-features)
4. [Concepts Demonstrated](#4-concepts-demonstrated)
5. [Technologies Used](#5-technologies-used)
6. [Project Structure](#6-project-structure)
7. [Dataset Description](#7-dataset-description)
8. [Setup Instructions](#8-setup-instructions)
9. [How to Run](#9-how-to-run)
10. [Menu Guide](#10-menu-guide)
11. [Code Design (OOP)](#11-code-design-oop)
12. [Data Cleaning Logic](#12-data-cleaning-logic)
13. [Visualizations](#13-visualizations)
14. [Sample Output](#14-sample-output)
15. [Error Handling and Edge Cases](#15-error-handling-and-edge-cases)
16. [Testing](#16-testing)
17. [Future Improvements](#17-future-improvements)
18. [Author](#18-author)

---

## 1. Project Overview
Retail businesses generate a large amount of sales data every day. Reading this data manually is slow
and error-prone. The **Retail Sales Data Analyzer** automates this process. The user supplies a sales
file, and the program validates it, cleans it, computes metrics and draws charts, all from a simple
console menu.

The project is written in a modular, object-oriented style. All functionality lives inside one class,
`RetailAnalyzer`, and each task is a separate, reusable method.

## 2. Objectives
- Read retail sales data from a CSV or Excel file and validate it.
- Clean the data by handling missing and invalid values.
- Calculate total sales, average sales, the most popular product and other metrics.
- Filter the data by category, product or date range.
- Aggregate sales by product, category and date.
- Visualise trends using a bar chart, a line graph and a heatmap.
- Demonstrate control structures, arrays, OOP, NumPy, Pandas, Matplotlib and Seaborn in one project.

## 3. Features
| # | Feature | Description |
|---|---------|-------------|
| 1 | Load Dataset | Accepts `.csv`, `.xlsx` and `.xls` files and checks that all required columns exist |
| 2 | Explore Dataset | Shows first 5 rows, last 5 rows, dataset info, statistical summary and missing values |
| 3 | Sales Metrics | Total, average, maximum and minimum sales, total quantity, most popular product, sales percentage |
| 4 | Filter Data | Filter by category, by product or by a date range |
| 5 | Aggregate Data | Total sales grouped by product, category and date |
| 6 | Bar Chart | Total sales by product category |
| 7 | Line Graph | Sales trend over time |
| 8 | Heatmap | Correlation between price, quantity sold and total sales |
| 9 | Summary Report | One-page summary of records, products, categories and sales |
| 10 | Exit | Closes the program |

## 4. Concepts Demonstrated
| Topic | Where it is used |
|-------|------------------|
| **Control Structures** | `if / elif / else` chains for file-type checks and menu choices; `while True` loop for the main menu; `for` loop to verify required columns |
| **Arrays** | Required column names are kept in a list and checked with a loop; sales and quantity are converted to NumPy arrays |
| **OOP** | `RetailAnalyzer` class with a constructor, instance data (`self.data`) and reusable methods |
| **NumPy** | `np.sum`, `np.mean`, `np.max`, `np.min` and vectorised sales percentage `(sales / total_sales) * 100` |
| **Pandas** | `read_csv`, `read_excel`, `to_datetime`, `to_numeric`, `fillna`, `groupby`, `transform`, `dropna`, boolean filtering |
| **Matplotlib** | Figure size, titles, axis labels, tick rotation, `tight_layout`, `show` |
| **Seaborn** | `barplot`, `lineplot` and `heatmap` for cleaner and more attractive charts |

## 5. Technologies Used
- Python 3.8 or higher
- pandas
- numpy
- matplotlib
- seaborn
- openpyxl (needed only to read `.xlsx` files)

## 6. Project Structure
```
Retail-Sales-Data-Analyzer/
|
|-- retail_analyzer.py    # Main program (class + menu)
|-- retail_sales.csv      # Sample dataset used for testing
|-- README.md             # Project documentation
```

## 7. Dataset Description
The sample file `retail_sales.csv` was generated with the help of AI, as the project brief allows.

| Item | Details |
|------|---------|
| Records | 300 rows |
| Date range | 2025-01-01 to 2025-12-31 |
| Products | 10 (Laptop, Smartphone, Headphones, T-Shirt, Jeans, Jacket, Rice Bag, Cooking Oil, Notebook, Pen Pack) |
| Categories | Electronics, Clothing, Grocery, Stationery |

**Columns**

| Column | Type | Description |
|--------|------|-------------|
| `Date` | Date (YYYY-MM-DD) | Date of the sale |
| `Product` | Text | Name of the product |
| `Category` | Text | Product category |
| `Price` | Number | Price per unit |
| `Quantity Sold` | Number | Units sold |
| `Total Sales` | Number | Price x Quantity Sold |

The dataset contains a few intentionally missing values (in `Price`, `Quantity Sold` and `Category`)
so that the data cleaning step can be demonstrated and tested.

## 8. Setup Instructions
1. **Install Python** (3.8 or higher) from https://www.python.org and tick *Add Python to PATH*.
2. **Download or clone** this repository:
   ```bash
   git clone <your-repository-link>
   cd Retail-Sales-Data-Analyzer
   ```
3. **Install the required libraries:**
   ```bash
   pip install pandas numpy matplotlib seaborn openpyxl
   ```
4. Make sure `retail_analyzer.py` and `retail_sales.csv` are in the **same folder**.

## 9. How to Run
```bash
python retail_analyzer.py
```
Then:
1. Choose **1** (Load Dataset).
2. Press **Enter** to use the default file `retail_sales.csv`, or type the path of another CSV/Excel file.
3. Use options **2 to 9** to explore, analyse and visualise the data.
4. Choose **10** to exit.

> The data must be loaded (option 1) before any other option is used. Otherwise the program shows
> "Please load dataset first!".

## 10. Menu Guide
```
======================================
       RETAIL SALES DATA ANALYZER
======================================
1. Load Dataset
2. Explore Dataset
3. Calculate Sales Metrics
4. Filter Data
5. Aggregate Sales Data
6. Bar Chart
7. Line Graph
8. Heatmap
9. Display Summary Report
10. Exit
```
**Example workflow**

1. **Input validation:** the user enters (or accepts) the file name. The program checks the file type.
2. **Data loading:** `load_data()` reads the file and verifies all six required columns.
3. **Cleaning:** `clean_data()` runs automatically after loading.
4. **Analysis:** `calculate_metrics()` computes total sales, average sales and the most popular product.
5. **Filtering:** `filter_data()` lets the user narrow the data by category, product or dates.
6. **Visualisation:** the bar chart, line graph and heatmap show trends and relationships.

## 11. Code Design (OOP)
All logic is encapsulated inside the `RetailAnalyzer` class. The dataset is held in `self.data`.

| Method | Purpose |
|--------|---------|
| `__init__()` | Creates an empty DataFrame to hold the data |
| `load_data(file_path)` | Reads CSV/Excel with Pandas, validates the file type and required columns |
| `clean_data()` | Fixes data types, fills missing values, removes invalid rows, recalculates Total Sales |
| `explore_data()` | Sub-menu to view head, tail, info, statistics and missing values |
| `calculate_metrics()` | NumPy-based calculation of sales metrics and sales percentage |
| `filter_data()` | Filters by category, product or date range based on user input |
| `aggregate_data()` | Groups total sales by product, category and date |
| `bar_chart()` | Seaborn bar chart of sales by category |
| `line_graph()` | Seaborn line graph of sales over time |
| `heatmap()` | Seaborn heatmap of the correlation matrix |
| `display_summary()` | Prints the overall summary report |

`main()` contains the menu loop and calls these methods. The line `if __name__ == "__main__":`
makes sure the program runs only when the file is executed directly.

## 12. Data Cleaning Logic
The `clean_data()` method follows these steps in order:

1. **Convert data types:** `Date` to datetime; `Price`, `Quantity Sold` and `Total Sales` to numbers
   (invalid entries become `NaN` through `errors="coerce"`).
2. **Fill text gaps:** missing `Product` or `Category` is set to `"Unknown"`.
3. **Fill missing Price:** use the **median price of the same product**; if still empty, use the overall median.
4. **Fill missing Quantity Sold:** use the **median quantity of the same product**; if still empty, use the overall median.
5. **Remove invalid rows:** drop rows with an invalid `Date`, `Price` or `Quantity Sold`, and rows with negative values.
6. **Recalculate Total Sales:** `Total Sales = Price x Quantity Sold`, which keeps the column consistent.

The median is used instead of the mean because it is not affected by extreme values.

## 13. Visualizations
All charts include a title and labelled axes.

| Chart | Library | Insight |
|-------|---------|---------|
| Bar Chart | Seaborn `barplot` | Which category earns the most total sales |
| Line Graph | Seaborn `lineplot` | How sales change over time |
| Heatmap | Seaborn `heatmap` | How price, quantity sold and total sales relate to each other |

## 14. Sample Output
Output after loading the sample dataset and choosing **9 (Summary Report)**:
```
========== RETAIL SALES SUMMARY ==========
Total Records: 300
Total Products: 10
Total Categories: 5
Total Sales: 21116665.01
Average Sales: 70388.88

Category Wise Sales:
Clothing         997376.05
Electronics    19812431.44
Grocery          257953.45
Stationery        35601.45
Unknown           13302.62

Most Popular Product:
T-Shirt
==========================================
```
The `Unknown` category appears because two rows in the sample file have no category. The
cleaning step labels them as `Unknown` instead of deleting them.

## 15. Error Handling and Edge Cases
| Situation | How the program responds |
|-----------|--------------------------|
| File does not exist | "File not found! Please check file name." |
| Unsupported file type (for example `.txt`) | "Please enter CSV or Excel file!" |
| Required column missing | "Missing column: <name>", and the data is discarded |
| Menu option used before loading | "Please load dataset first!" |
| Invalid menu choice | "Invalid Choice! Please Try Again!" |
| Wrong date format in filter | "Invalid date format!" |
| Start date later than end date | "Start date must be before end date!" |
| Filter returns nothing | "No records found!" |
| Total sales equal to zero | "Total Sales is zero!" (avoids division by zero) |
| Any other unexpected problem | Caught by `try / except` and printed, so the program does not crash |

## 16. Testing
The program was tested with:
- The sample dataset, which has missing values, to check the cleaning step.
- Every menu option from 1 to 10.
- Wrong file names and wrong file types.
- Invalid and reversed dates in the date-range filter.
- Selecting options before loading the data.

## 17. Future Improvements
- Export the cleaned data and the summary report to a new CSV or PDF file.
- Add monthly and yearly growth-rate analysis.
- Save charts as image files.
- Build a graphical interface (Tkinter) or a web dashboard (Streamlit).
- Add sales forecasting with a simple machine learning model.

## 18. Author
- **Name:** sneha padsal
- **Submission:** Practical Exam, Retail Sales Data Analyzer
