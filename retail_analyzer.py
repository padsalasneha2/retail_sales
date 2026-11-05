
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class RetailAnalyzer:

    def __init__(self):
        self.data = pd.DataFrame()

    # 1. Load Dataset
    def load_data(self, file_path):

        try:

            if file_path.lower().endswith(".csv"):
                self.data = pd.read_csv(file_path)

            elif file_path.lower().endswith(".xlsx"):
                self.data = pd.read_excel(file_path)

            elif file_path.lower().endswith(".xls"):
                self.data = pd.read_excel(file_path)

            else:
                print("Please enter CSV or Excel file!")
                return

            required_columns = [
                "Date", "Product", "Category",
                "Price", "Quantity Sold", "Total Sales"
            ]

            for col in required_columns:
                if col not in self.data.columns:
                    print("Missing column:", col)
                    self.data = pd.DataFrame()
                    return

            print("\nDataset loaded successfully!")

            print("\nDataset Information:")
            self.data.info()

            self.clean_data()

        except FileNotFoundError:
            print("File not found! Please check file name.")

        except Exception as e:
            print("Error:", e)

    # 2. Data Cleaning
    def clean_data(self):

        if self.data.empty:
            print("Please load dataset first!")
            return

        self.data["Date"] = pd.to_datetime(
            self.data["Date"], errors="coerce"
        )

        self.data["Price"] = pd.to_numeric(
            self.data["Price"], errors="coerce"
        )

        self.data["Quantity Sold"] = pd.to_numeric(
            self.data["Quantity Sold"], errors="coerce"
        )

        self.data["Total Sales"] = pd.to_numeric(
            self.data["Total Sales"], errors="coerce"
        )

        self.data["Product"] = self.data["Product"].fillna("Unknown")

        self.data["Category"] = self.data["Category"].fillna("Unknown")

        # Fill Missing Price
        self.data["Price"] = self.data.groupby(
            "Product"
        )["Price"].transform(
            lambda x: x.fillna(x.median())
        )

        self.data["Price"] = self.data["Price"].fillna(
            self.data["Price"].median()
        )

        # Fill Missing Quantity
        self.data["Quantity Sold"] = self.data.groupby(
            "Product"
        )["Quantity Sold"].transform(
            lambda x: x.fillna(x.median())
        )

        self.data["Quantity Sold"] = self.data[
            "Quantity Sold"
        ].fillna(self.data["Quantity Sold"].median())

        # Remove Invalid Data
        self.data = self.data.dropna(
            subset=["Date", "Price", "Quantity Sold"]
        )

        self.data = self.data[
            (self.data["Price"] >= 0) &
            (self.data["Quantity Sold"] >= 0)
        ].copy()

        # Calculate Total Sales
        self.data["Total Sales"] = (
            self.data["Price"] * self.data["Quantity Sold"]
        )

        print("\nData cleaned successfully!")

        print("Total Records:", len(self.data))

        print("\nMissing Values:")
        print(self.data.isnull().sum())

    # 3. Explore Dataset
    def explore_data(self):

        if self.data.empty:
            print("Please load dataset first!")
            return

        print("\n1. Display First 5 Rows")
        print("2. Display Last 5 Rows")
        print("3. Dataset Information")
        print("4. Statistical Summary")
        print("5. Check Missing Values")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print(self.data.head())

        elif choice == "2":
            print(self.data.tail())

        elif choice == "3":
            self.data.info()

        elif choice == "4":
            print(self.data.describe())

        elif choice == "5":
            print(self.data.isnull().sum())

        else:
            print("Invalid choice!")

    # 4. Calculate Metrics using NumPy
    def calculate_metrics(self):

        if self.data.empty:
            print("Please load dataset first!")
            return

        sales = self.data["Total Sales"].to_numpy()

        quantity = self.data["Quantity Sold"].to_numpy()

        total_sales = np.sum(sales)

        average_sales = np.mean(sales)

        maximum_sales = np.max(sales)

        minimum_sales = np.min(sales)

        total_quantity = np.sum(quantity)

        popular_product = (
            self.data.groupby("Product")["Quantity Sold"]
            .sum().idxmax()
        )

        print("\n========== SALES METRICS ==========")

        print("Total Sales:", round(total_sales, 2))

        print("Average Sales:", round(average_sales, 2))

        print("Maximum Sales:", maximum_sales)

        print("Minimum Sales:", minimum_sales)

        print("Total Quantity Sold:", total_quantity)

        print("Most Popular Product:", popular_product)

        print("\nSales Percentage:")

        if total_sales != 0:
            percentage = (sales / total_sales) * 100
            print(np.round(percentage, 2))

        else:
            print("Total Sales is zero!")

    # 5. Filter Data
    def filter_data(self):

        if self.data.empty:
            print("Please load dataset first!")
            return

        print("\n1. Filter by Category")
        print("2. Filter by Product")
        print("3. Filter by Date Range")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            category = input("Enter Category: ")

            result = self.data[
                self.data["Category"].str.lower() ==
                category.lower()
            ]

        elif choice == "2":

            product = input("Enter Product: ")

            result = self.data[
                self.data["Product"].str.lower() ==
                product.lower()
            ]

        elif choice == "3":

            start_date = pd.to_datetime(
                input("Enter Start Date (YYYY-MM-DD): "),
                errors="coerce"
            )

            end_date = pd.to_datetime(
                input("Enter End Date (YYYY-MM-DD): "),
                errors="coerce"
            )

            if pd.isna(start_date) or pd.isna(end_date):
                print("Invalid date format!")
                return

            if start_date > end_date:
                print("Start date must be before end date!")
                return

            result = self.data[
                (self.data["Date"] >= start_date) &
                (self.data["Date"] <= end_date)
            ]

        else:
            print("Invalid choice!")
            return

        if result.empty:
            print("No records found!")

        else:
            print("\nFiltered Data:")

            print(result.to_string(index=False))

            print("\nFiltered Total Sales:",
                  result["Total Sales"].sum())

    # 6. Data Aggregation
    def aggregate_data(self):

        if self.data.empty:
            print("Please load dataset first!")
            return

        print("\nSales by Product:")

        print(
            self.data.groupby("Product")["Total Sales"].sum()
        )

        print("\nSales by Category:")

        print(
            self.data.groupby("Category")["Total Sales"].sum()
        )

        print("\nSales by Date:")

        print(
            self.data.groupby("Date")["Total Sales"].sum()
        )

    # 7. Bar Chart using Seaborn
    def bar_chart(self):

        if self.data.empty:
            print("Please load dataset first!")
            return

        sales = self.data.groupby(
            "Category"
        )["Total Sales"].sum().reset_index()

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=sales,
            x="Category",
            y="Total Sales"
        )

        plt.title("Total Sales by Product Category")

        plt.xlabel("Product Category")

        plt.ylabel("Total Sales")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()

    # 8. Line Graph
    def line_graph(self):

        if self.data.empty:
            print("Please load dataset first!")
            return

        sales = self.data.groupby(
            "Date"
        )["Total Sales"].sum().reset_index()

        sales = sales.sort_values("Date")

        plt.figure(figsize=(10, 6))

        sns.lineplot(
            data=sales,
            x="Date",
            y="Total Sales",
            marker="o"
        )

        plt.title("Retail Sales Trend Over Time")

        plt.xlabel("Date")

        plt.ylabel("Total Sales")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()

    # 9. Heatmap using Seaborn
    def heatmap(self):

        if self.data.empty:
            print("Please load dataset first!")
            return

        numeric_data = self.data[
            ["Price", "Quantity Sold", "Total Sales"]
        ]

        correlation = numeric_data.corr()

        plt.figure(figsize=(8, 6))

        sns.heatmap(
            correlation,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            linewidths=0.5
        )

        plt.title("Retail Sales Correlation Heatmap")

        plt.tight_layout()

        plt.show()

    # 10. Summary Report
    def display_summary(self):

        if self.data.empty:
            print("Please load dataset first!")
            return

        print("\n========== RETAIL SALES SUMMARY ==========")

        print("Total Records:", len(self.data))

        print("Total Products:",
              self.data["Product"].nunique())

        print("Total Categories:",
              self.data["Category"].nunique())

        print("Total Sales:",
              round(self.data["Total Sales"].sum(), 2))

        print("Average Sales:",
              round(self.data["Total Sales"].mean(), 2))

        print("\nCategory Wise Sales:")

        print(
            self.data.groupby("Category")["Total Sales"].sum()
        )

        print("\nMost Popular Product:")

        print(
            self.data.groupby("Product")["Quantity Sold"]
            .sum().idxmax()
        )

        print("\n==========================================")


# Main Program
def main():

    analyzer = RetailAnalyzer()

    while True:

        print("\n")

        print("======================================")

        print("       RETAIL SALES DATA ANALYZER")

        print("======================================")

        print("1. Load Dataset")

        print("2. Explore Dataset")

        print("3. Calculate Sales Metrics")

        print("4. Filter Data")

        print("5. Aggregate Sales Data")

        print("6. Bar Chart")

        print("7. Line Graph")

        print("8. Heatmap")

        print("9. Display Summary Report")

        print("10. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":

            file_path = input(
                "Enter CSV or Excel File Path "
                "(default: retail_sales.csv): "
            )

            if file_path.strip() == "":
                file_path = "retail_sales.csv"

            analyzer.load_data(file_path)

        elif choice == "2":
            analyzer.explore_data()

        elif choice == "3":
            analyzer.calculate_metrics()

        elif choice == "4":
            analyzer.filter_data()

        elif choice == "5":
            analyzer.aggregate_data()

        elif choice == "6":
            analyzer.bar_chart()

        elif choice == "7":
            analyzer.line_graph()

        elif choice == "8":
            analyzer.heatmap()

        elif choice == "9":
            analyzer.display_summary()

        elif choice == "10":
            print("\nThank You for Using Retail Sales Data Analyzer! Good byy")
            break

        else:
            print("Invalid Choice! Please Try Again!")


if __name__ == "__main__":
    main()
