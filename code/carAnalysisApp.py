import pandas as pd
import tkinter as tk
import logging
from tkinter import filedialog, messagebox
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CarAnalysis:

    def __init__(self, df):
        self.df = df
        self.chart_widgets = []

    def calculate_correlation_heatmap(self):
        correlation_matrix = self.df.corr(numeric_only=True)
        return correlation_matrix

    def get_top_5_car_types(self):
        top_5_car_types = self.df.groupby(['Car Name', 'Type']).agg({'Price': 'mean'}).sort_values("Price", ascending=False).reset_index()[:5]
        return top_5_car_types

    def get_owner_vs_price_data(self):
        owner = self.df['Owner']
        price = self.df['Price']
        owner_vs_price_data = pd.DataFrame({'Owner': owner, 'Price': price})
        return owner_vs_price_data

    def get_distance_vs_price_data(self):
        distance = self.df['Distance']
        price = self.df['Price']
        distance_vs_price_data = pd.DataFrame({'Distance': distance, 'Price': price})
        return distance_vs_price_data

    def get_driving_type_vs_price_data(self):
        drive = self.df['Drive']
        price = self.df['Price']
        driving_type_vs_price_data = pd.DataFrame({'DriveType': drive, 'Price': price})
        return driving_type_vs_price_data


class CarAnalysisApp:

    logging.basicConfig(filename='test.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    def __init__(self, root):
        self.root = root
        self.root.title("Car Analysis App")
        self.analysis_app = None

        self.file_label = tk.Label(root, text="Select CSV file:")
        self.file_label.pack()

        self.browse_button = tk.Button(root, text="Browse", command=self.load_csv)
        self.browse_button.pack()

        self.analysis_label = tk.Label(root, text="Select Analysis Type:")
        self.analysis_label.pack()

        self.analysis_var = tk.StringVar()
        self.analysis_var.set("Correlation Heatmap")

        self.analysis_options = ["Correlation Heatmap", "Top 5 Car Types", "Owner vs. Price Scatter Plot",
                                 "Distance vs. Price Scatter Plot", "Driving Type vs. Price"]
        self.analysis_dropdown = tk.OptionMenu(root, self.analysis_var, *self.analysis_options)
        self.analysis_dropdown.pack()

        self.run_button = tk.Button(root, text="Run Analysis", command=self.run_analysis)
        self.run_button.pack()

    def load_csv(self):
        try:
            file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
            self.df = pd.read_csv(file_path)
            self.analysis_app = CarAnalysis(self.df)
        except Exception as e:
            messagebox.showinfo("Warning", str(e))
            logging.warning(f"An unexpected error occurred: {e}")

    def run_analysis(self):
        if self.analysis_app:
            analysis_type = self.analysis_var.get()

            # Destroy existing chart-related widgets
            for widget in self.analysis_app.chart_widgets:
                widget.destroy()
            self.analysis_app.chart_widgets = []

            if analysis_type == "Correlation Heatmap":
                correlation_matrix = self.analysis_app.calculate_correlation_heatmap()
                self.plot_correlation_heatmap(correlation_matrix)
            elif analysis_type == "Top 5 Car Types":
                top_5_car_types = self.analysis_app.get_top_5_car_types()
                self.display_top_5_car_types(top_5_car_types)
            elif analysis_type == "Owner vs. Price Scatter Plot":
                owner_vs_price_data = self.analysis_app.get_owner_vs_price_data()
                self.plot_owner_vs_price(owner_vs_price_data)
            elif analysis_type == "Distance vs. Price Scatter Plot":
                distance_vs_price_data = self.analysis_app.get_distance_vs_price_data()
                self.plot_distance_vs_price(distance_vs_price_data)
            elif analysis_type == "Driving Type vs. Price":
                driving_type_vs_price_data = self.analysis_app.get_driving_type_vs_price_data()
                self.plot_driving_type_vs_price(driving_type_vs_price_data)
        else:
            messagebox.showinfo("Error", "Please select a CSV file first.")
            logging.error("CSV file not provided.")

    def plot_correlation_heatmap(self, correlation_matrix):
        try:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
            ax.set_title('Correlation Heatmap')
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            self.analysis_app.chart_widgets.append(canvas.get_tk_widget())
            canvas.get_tk_widget().pack()
        except Exception as e:
            messagebox.showinfo("Error", str(e))
            logging.error(f"An unexpected error occurred: {e}")

    def display_top_5_car_types(self, top_5_car_types):
        try:
            result_string = top_5_car_types.to_string(index=False)
            label = tk.Label(self.root, text=result_string, justify=tk.LEFT)
            self.analysis_app.chart_widgets.append(label)
            label.pack()
        except Exception as e:
            messagebox.showinfo("Error", str(e))
            logging.error(f"An unexpected error occurred: {e}")

    def plot_owner_vs_price(self, owner_vs_price_data):
        try:
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(x='Owner', y='Price', data=owner_vs_price_data, ax=ax)
            ax.set_xlabel('Owner')
            ax.set_ylabel('Price')
            ax.set_title('Owner vs. Price Bar Plot')
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            self.analysis_app.chart_widgets.append(canvas.get_tk_widget())
            canvas.get_tk_widget().pack()
        except Exception as e:
            messagebox.showinfo("Error", str(e))
            logging.error(f"An unexpected error occurred: {e}")

    def plot_distance_vs_price(self, distance_vs_price_data):
        try:
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.scatter(distance_vs_price_data['Distance'], distance_vs_price_data['Price'])
            ax.set_xlabel('Distance')
            ax.set_ylabel('Price')
            ax.set_title('Distance vs. Price Scatter Plot')
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            self.analysis_app.chart_widgets.append(canvas.get_tk_widget())
            canvas.get_tk_widget().pack()
        except Exception as e:
            messagebox.showinfo("Error", str(e))
            logging.error(f"An unexpected error occurred: {e}")

    def plot_driving_type_vs_price(self, driving_type_vs_price_data):
        try:
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(x='DriveType', y='Price', data=driving_type_vs_price_data, ax=ax)
            ax.set_xlabel('DriveType')
            ax.set_ylabel('Price')
            ax.set_title('DriveType vs. Price Bar Plot')
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            self.analysis_app.chart_widgets.append(canvas.get_tk_widget())
            canvas.get_tk_widget().pack()
        except Exception as e:
            messagebox.showinfo("Error", str(e))
            logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CarAnalysisApp(root)
    root.mainloop()
