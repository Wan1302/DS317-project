import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set up page configuration
st.set_page_config(page_title="Dashboard", page_icon="🌏", layout="wide")

# Sidebar
st.sidebar.image("image/logo.jpeg", caption="Online Analytics")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Courses", "Prediction & Comparison"],
        icons=["house", "book", "graph-up"],
        menu_icon="cast",
        default_index=0
    )

def predict_course_satisfaction(df, course_name):
    filtered = df[df['name'] == course_name]['course_classification']
    return filtered.iloc[0] if not filtered.empty else None

# Function to display overview statistics
def show_overview_statistics(df):
    total_courses = len(df)
    avg_users = df['num_users'].mean()
    avg_completion_rate = df['average_completion_rate'].mean()
    #dissatisfied_courses = len(df[df['course_classification'] == 'Very satisfied'])
    total_users = df['num_users'].sum()

    st.markdown("""
    <div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
        <div style="text-align: center; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
            <h2 style="color: #4CAF50;">Total Courses</h2>
            <p style="font-size: 24px; font-weight: bold;">{}</p>
        </div>
        <div style="text-align: center; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
            <h2 style="color: #2196F3;">Average Users</h2>
            <p style="font-size: 24px; font-weight: bold;">{:.1f}</p>
        </div>
        <div style="text-align: center; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
            <h2 style="color: #FF9800;">Average Completion Rate</h2>
            <p style="font-size: 24px; font-weight: bold;">{:.2%}</p>
        </div>
        <div style="text-align: center; padding: 20px; background-color: #f9f9f9; border-radius: 10px;">
            <h2 style="color: #f44336;">Total users</h2>
            <p style="font-size: 24px; font-weight: bold;">{}</p>
        </div>
    </div>
    """.format(total_courses, avg_users, avg_completion_rate, total_users), unsafe_allow_html=True)

def load_data():
    train_file_path = 'data/train.csv'  # Data for 2024
    test_file_path = 'data/test.csv'    # Data for 2025
    df_2024 = pd.read_csv(train_file_path)  # Year 2024 data
    df_2025 = pd.read_csv(test_file_path)  # Year 2025 data
    return df_2024, df_2025

# Home Page
if selected == "Home":
    st.title("📊 Course Management Dashboard")

    # Load data
    df_2024, df_2025 = load_data()

    # Check for required columns
    if 'course_classification' not in df_2024.columns or 'course_classification' not in df_2025.columns:
        st.error("The 'course_classification' column is missing in one or both datasets.")
    else:
        # Display overview statistics
        st.markdown("## Overview Statistics for 2024")
        show_overview_statistics(df_2024)

        st.markdown("---")

        # Satisfaction classification distribution
        st.markdown("### Course Classification Distribution")
        col1, col2 = st.columns(2)
        with col1:
            fig1, ax1 = plt.subplots()
            classification_2024 = df_2024['course_classification'].value_counts()
            ax1.pie(
                classification_2024,
                labels=classification_2024.index,
                autopct='%1.1f%%',
                startangle=140
            )
            ax1.axis('equal')
            ax1.set_xlabel("Year 2024", fontsize=16, labelpad=10, fontweight='bold')
            st.pyplot(fig1)
        with col2:
            fig2, ax2 = plt.subplots()
            classification_2025 = df_2025['course_classification'].value_counts()
            ax2.pie(
                classification_2025,
                labels=classification_2025.index,
                autopct='%1.1f%%',
                startangle=140
            )
            ax2.axis('equal')
            ax2.set_xlabel("Year 2025", fontsize=16, labelpad=10, fontweight='bold')
            st.pyplot(fig2)

        # Bar charts comparing metrics
        st.markdown("### Average Numerical Comparisons: 2024 vs 2025")
        required_columns = ['num_users', 'total_cmt', 'number of resources', 'average_completion_rate']

        if all(col in df_2024.columns for col in required_columns) and all(col in df_2025.columns for col in required_columns):
            averages_2024 = df_2024[required_columns].mean()
            averages_2025 = df_2025[required_columns].mean()

            col1, col2 = st.columns(2)

            # Bar Chart for num_users
            with col1:
                fig1, ax1 = plt.subplots()
                ax1.bar(['2024', '2025'], [averages_2024['num_users'], averages_2025['num_users']], color=['#6fa3ef', '#ffb347'])
                ax1.set_xlabel("Number of Users", fontsize=16, labelpad=10, fontweight='bold')
                st.pyplot(fig1)

            # Bar Chart for total_cmt
            with col2:
                fig2, ax2 = plt.subplots()
                ax2.bar(['2024', '2025'], [averages_2024['total_cmt'], averages_2025['total_cmt']], color=['#6fa3ef', '#ffb347'])
                ax2.set_xlabel("Total Comments", fontsize=16, labelpad=10, fontweight='bold')
                st.pyplot(fig2)

            col1, col2 = st.columns(2)

            # Bar Chart for number of resources
            with col1:
                fig3, ax3 = plt.subplots()
                ax3.bar(['2024', '2025'], [averages_2024['number of resources'], averages_2025['number of resources']], color=['#6fa3ef', '#ffb347'])
                ax3.set_xlabel("Number of Resources", fontsize=16, labelpad=10, fontweight='bold')
                st.pyplot(fig3)

            # Bar Chart for average_completion_rate
            with col2:
                fig4, ax4 = plt.subplots()
                ax4.bar(['2024', '2025'], [averages_2024['average_completion_rate'], averages_2025['average_completion_rate']], color=['#6fa3ef', '#ffb347'])
                ax4.set_xlabel("Avg Completion Rate", fontsize=16, labelpad=10, fontweight='bold')
                st.pyplot(fig4)
        else:
            st.warning("Required columns are missing in one or both datasets.")

        # Data Quality Evaluation Table
        st.markdown("### Data Quality Evaluation")
        data = {
            "Table": ["Raw_data", "Improved_data"],
            "Completeness": ["74.66%", "100%"],
            "Accuracy": ["20.16%", "100%"],
            "Consistency": ["100%", "100%"],
            "Uniqueness": ["26.64%", "100%"]
        }
        df_quality = pd.DataFrame(data)
        st.table(df_quality)

elif selected == "Courses":
    st.title("📝 Course Management")

    # Load data
    df_2024, df_2025 = load_data()

    # Dropdown to select a course
    st.markdown("## 🔍Select a Course")
    course_options = df_2025['name'].unique()
    selected_course = st.selectbox("Choose a course:", course_options)

    # Filter data for the selected course
    course = df_2025[df_2025['name'] == selected_course]

    if not course.empty:
        # Display selected course details
        st.markdown(f"### ✅ Course Dashboard: {selected_course}")
        #st.write(course[['name', 'num_users', 'number of resources', 'positive', 'negative', 'neutral']])

        num_users = int(course['num_users'].values[0])
        num_resources = int(course['number of resources'].values[0])
        total_cmt = int(course['total_cmt'].values[0])
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.info('Number of users', icon='📌')
            st.metric(label='🏅',value=num_users)

        with col2:
            st.info('Number of resources', icon='📌')
            st.metric(label='🏅',value=num_resources)

        with col3:
            st.info('Total comments', icon='📌')
            st.metric(label='🏅',value=total_cmt)

        if total_cmt > 0:
            # Retrieve sentiment data (default to 0 if columns are missing)
            sentiment_counts = [
                course.iloc[0]['positive'] if 'positive' in course.columns else 0,
                course.iloc[0]['negative'] if 'negative' in course.columns else 0,
                course.iloc[0]['neutral'] if 'neutral' in course.columns else 0,
            ]

            # Filter out sentiments with values greater than 0
            filtered_counts = [count for count in sentiment_counts if count > 0]
            filtered_labels = [label for count, label in zip(sentiment_counts, ['Positive', 'Negative', 'Neutral']) if count > 0]

            left_col, right_col = st.columns(2)

            with left_col:

                # Create the pie chart
                fig, ax = plt.subplots()
                if len(filtered_counts) > 1:
                    # Plot a standard pie chart if more than one sentiment exists
                    ax.pie(filtered_counts, labels=filtered_labels, autopct='%1.1f%%', startangle=140, colors=['#4CAF50', '#f44336', '#FFC107'])
                else:
                    # Handle case where only one sentiment exists
                    ax.pie(filtered_counts, labels=None, autopct='%1.1f%%', startangle=140, colors=['#4CAF50', '#f44336', '#FFC107'])
                    ax.legend(filtered_labels, loc="upper right")  # Add legend to show the label

                ax.axis('equal')  
                st.markdown("### Sentiment Distribution")  
                st.pyplot(fig) 

            with right_col: 

                # Create the horizontal bar chart
                fig_bar, ax_bar = plt.subplots()
                ax_bar.barh(['Positive', 'Negative', 'Neutral'], sentiment_counts, color=['#4CAF50', '#f44336', '#FFC107'])
                ax_bar.set_xlabel('Count')
                ax_bar.set_title('Sentiment Counts')
                ax_bar.grid(axis='x', linestyle='--', alpha=0.7)

                st.markdown("### Sentiment Count Bar Chart")
                st.pyplot(fig_bar)
        
        else:
            st.warning("This course has no comments yet.")

        # Bar Chart for User and Resource Metrics
        fig, ax = plt.subplots()
        metrics = ['Number of Users', 'Number of Resources']
        values = [course.iloc[0]['num_users'], course.iloc[0]['number of resources']]
        ax.bar(metrics, values, color=['#2196F3', '#FF9800'])
        ax.set_ylabel("Count")
        st.markdown("### User and Resource Metrics")
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected course.")


    
elif selected == "Prediction & Comparison":
    st.title("🔮 Prediction and Comparison")

    # Load data
    df_2024, df_2025 = load_data()

    # Initialize session state for prediction
    if "predicted_satisfaction_2025" not in st.session_state:
        st.session_state.predicted_satisfaction_2025 = None

    # Step 1: Select a course from 2025 for prediction
    st.markdown("## 1️⃣ Select a Course from 2025 for Prediction")
    course_2025_options = df_2025['name'].unique()
    selected_course_2025 = st.selectbox("Choose a course", course_2025_options)

    selected_course_data = df_2025[df_2025['name'] == selected_course_2025]

    if not selected_course_data.empty:
        st.markdown("### Course Details:")
        c1, c2= st.columns(2)
        #st.write(f"**Name**: {selected_course_2025}")

        with c1:
            st.write(f"**📌Total Comments**: {selected_course_data.iloc[0]['total_cmt']}")
            st.write(f"**📌Positive Sentiments**: {selected_course_data.iloc[0]['positive']}")
            st.write(f"**📌Negative Sentiments**: {selected_course_data.iloc[0]['negative']}")
            st.write(f"**📌Neutral Sentiments**: {selected_course_data.iloc[0]['neutral']}")
        with c2:
            st.write(f"**📌Average Completion Rate**: {selected_course_data.iloc[0]['average_completion_rate']}%")
            st.write(f"**📌Number of Users**: {selected_course_data.iloc[0]['num_users']}")
            st.write(f"**📌Number of Resources**: {selected_course_data.iloc[0]['number of resources']}")
        #st.write(f"**Course Classification**: {selected_course_data.iloc[0]['course_classification']}")
    else:
        st.markdown("### No data available for the selected course.")

    predict_button = st.button("Predict Satisfaction Level")
    
    # Step 2: Predict the satisfaction level for the selected course in 2025
    if predict_button:
        st.session_state.predicted_satisfaction_2025 = predict_course_satisfaction(df_2025, selected_course_2025)
        st.success(f"Predicted Satisfaction Level for '{selected_course_2025}' (2025): {st.session_state.predicted_satisfaction_2025}")

    # Step 3: Select a course from 2024 for comparison
    st.markdown("## 2️⃣ Select a Course from 2024 for Comparison")
    course_2024_options = df_2024[df_2024['total_cmt'] > 0]['name'].unique()
    selected_course_2024 = st.selectbox("Choose a course from 2024:", course_2024_options)


    # Step 4: Display comparison results
    if st.button("Compare"):
        if st.session_state.predicted_satisfaction_2025 is not None:
            course_2024 = df_2024[df_2024['name'] == selected_course_2024]
            course_2025 = df_2025[df_2025['name'] == selected_course_2025]

            if not course_2024.empty and not course_2025.empty:
                
                data_2024 = course_2024.iloc[0]
                data_2025 = course_2025.iloc[0]

                
                st.markdown("### 📋 Detailed Information for {}".format(selected_course_2024))
                course_2024_info = {
                    #"Course Name": selected_course_2024,
                    "Total Comments": int(data_2024['total_cmt']),
                    "Positive Sentiments": int(data_2024['positive']),
                    "Negative Sentiments": int(data_2024['negative']),
                    "Neutral Sentiments": int(data_2024['neutral']),
                    "Average Completion Rate": data_2024['average_completion_rate'],
                    "Number of Users": int(data_2024['num_users']),
                    "Number of Resources": int(data_2024['number of resources']),
                    "Course Classification": data_2024['course_classification']
                }
                st.table(pd.DataFrame(course_2024_info, index=[0]))

                sentiment_metrics = ['Total Comments', 'Positive Sentiments', 'Negative Sentiments', 'Neutral Sentiments']
                sentiment_2024 = [
                    data_2024['total_cmt'], 
                    data_2024['positive'], 
                    data_2024['negative'], 
                    data_2024['neutral']
                ]
                sentiment_2025 = [
                    data_2025['total_cmt'], 
                    data_2025['positive'], 
                    data_2025['negative'], 
                    data_2025['neutral']
                ]

                x = np.arange(len(sentiment_metrics))  
                width = 0.35  

                fig, ax = plt.subplots(figsize=(10, 6))
                ax.bar(x - width/2, sentiment_2024, width, label=selected_course_2024 + '(2024)', color='#4CAF50')
                ax.bar(x + width/2, sentiment_2025, width, label=selected_course_2025 + '(2025)', color='#FFC107')
                ax.set_xlabel('Metrics')
                ax.set_ylabel('Counts')
                ax.set_title('Comparison of Comments and Sentiments')
                ax.set_xticks(x)
                ax.set_xticklabels(sentiment_metrics)
                ax.legend()
                st.pyplot(fig)

                resource_metrics = ['Number of Users', 'Number of Resources']
                resources_2024 = [data_2024['num_users'], data_2024['number of resources']]
                resources_2025 = [data_2025['num_users'], data_2025['number of resources']]

                x = np.arange(len(resource_metrics))  

                fig, ax = plt.subplots(figsize=(8, 5))
                ax.bar(x - width/2, resources_2024, width, label=selected_course_2024 + '(2024)', color='#4CAF50')
                ax.bar(x + width/2, resources_2025, width, label=selected_course_2025 + '(2025)', color='#FFC107')
                ax.set_xlabel('Metrics')
                ax.set_ylabel('Counts')
                ax.set_title('Comparison of Users and Resources')
                ax.set_xticks(x)
                ax.set_xticklabels(resource_metrics)
                ax.legend()
                st.pyplot(fig)
            else:
                st.warning("Please select valid courses for comparison.")
        else:
            st.warning("Please predict the satisfaction level for the 2025 course before comparing.")


