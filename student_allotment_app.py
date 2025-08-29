import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Smart Data Visualizer")
st.write("Upload any CSV file and explore!")

# Upload file
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.write("### Preview of Data")
    st.dataframe(data.head())

       # --- Column Classification ---
    categorical_cols = data.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    numeric_cols = data.select_dtypes(include=["int64", "float64"]).columns.tolist()
    datetime_cols = data.select_dtypes(include=["datetime64"]).columns.tolist()

    # Try to convert any date-like columns
    for col in data.columns:
        try:
            data[col] = pd.to_datetime(data[col])
            if col not in datetime_cols:
                datetime_cols.append(col)
        except Exception:
            pass
      # --- 🔍 Filters Section ---
    st.subheader("🔎 Filter Data")
    filter_col = st.selectbox("Select a column to filter by", data.columns)

    # Show filter options dynamically
    if filter_col in categorical_cols:
        selected_vals = st.multiselect(f"Select values for {filter_col}", data[filter_col].unique())
        if selected_vals:
            data = data[data[filter_col].isin(selected_vals)]

    elif filter_col in numeric_cols:
        min_val, max_val = st.slider(
            f"Select range for {filter_col}",
            float(data[filter_col].min()),
            float(data[filter_col].max()),
            (float(data[filter_col].min()), float(data[filter_col].max()))
        )
        data = data[(data[filter_col] >= min_val) & (data[filter_col] <= max_val)]

    elif filter_col in datetime_cols:
        min_date, max_date = st.date_input(
            f"Select date range for {filter_col}",
            [data[filter_col].min(), data[filter_col].max()]
        )
        if len(min_date) == 2:
            data = data[(data[filter_col] >= pd.to_datetime(min_date[0])) &
                        (data[filter_col] <= pd.to_datetime(min_date[1]))]

    st.write("### Filtered Data Preview")
    st.dataframe(data.head())

    # --- Categorical Visualization ---
    if categorical_cols:
        st.subheader("📌 Categorical Column Visualization")
        cat_col = st.selectbox("Choose a categorical column", categorical_cols)
        cat_counts = data[cat_col].value_counts().reset_index()
        cat_counts.columns = [cat_col, "count"]

        fig_cat = px.bar(cat_counts, x=cat_col, y="count", text="count", title=f"Distribution of {cat_col}")
        st.plotly_chart(fig_cat, use_container_width=True)

    # --- Numeric Visualization ---
    if numeric_cols:
        st.subheader("📌 Numeric Column Visualization")
        num_col = st.selectbox("Choose a numeric column", numeric_cols)

        fig_hist = px.histogram(data, x=num_col, title=f"Histogram of {num_col}")
        st.plotly_chart(fig_hist, use_container_width=True)

        fig_box = px.box(data, y=num_col, title=f"Boxplot of {num_col}")
        st.plotly_chart(fig_box, use_container_width=True)


