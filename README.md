# STREAMLIT

# 📊 Smart Data Visualizer

An interactive Streamlit web app that allows users to upload CSV files, apply filters, and explore data with dynamic visualizations powered by Plotly.

# 🚀 Features

Upload any .csv file and preview the data.

Automatic detection of categorical, numeric, and datetime columns.

Apply filters dynamically:

Categorical filters – select specific values.

Numeric filters – use sliders to filter ranges.

Datetime filters – select a date range.

# Visualize data:

Bar charts for categorical distributions.

Histograms and Boxplots for numeric columns.

Responsive and interactive charts with Plotly Express.

# 🛠️ Tech Stack

Python

Streamlit

Pandas

Plotly

# 📂 Project Structure
smart-data-visualizer/
│── app.py              # Main Streamlit app  
│── requirements.txt    # Python dependencies  
│── README.md           # Project documentation  
│── sample.csv          # Example dataset (optional)  

# ⚙️ Installation
1. Clone the repo
git clone https://github.com/your-username/smart-data-visualizer.git
cd smart-data-visualizer

2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the Streamlit app
streamlit run app.py

# 📦 Requirements

Create a requirements.txt file with:

streamlit
pandas
plotly

# 📊 Usage

Launch the app with streamlit run app.py.

Upload a CSV file.

Apply filters and explore the data.

View dynamic visualizations (bar, histogram, boxplot).

# 🖼️ Demo Screenshots

(Add screenshots here after running the app)

# 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

# 📜 License

This project is licensed under the MIT License.
