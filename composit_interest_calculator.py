import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("Compound Interest Calculator")

# Create two columns
left_column, right_column = st.columns(2)

# Inputs in the left column
with left_column:
    # Select compound frequency
    compound_frequency = st.selectbox(
        "Select the compound frequency:",
        ("Weekly", "Biweekly", "Monthly", "Quarterly", "Yearly")
    )

    # Input for the additional amount to add with a default value of 1000
    add_on = st.number_input("Enter the constant amount to add to the principal each period:", min_value=0.0, value=1000.0, step=0.01)

    # Input for principal amount and interest rate
    principal = st.number_input("Enter the principal amount:", min_value=0.0, value=10000.0, step=100.0)
    interest_rate = st.number_input("Enter the annual interest rate (in %):", min_value=0.0, value=5.0, step=0.1)
    years = st.number_input("Enter the number of years:", min_value=1, value=5, step=1)

# Outputs in the right column
with right_column:
    st.write("This is where the output will be displayed.")

# Results in the right column
with right_column:
    # Calculate total amount for each frequency
    total_amounts = {}
    for frequency in ["Weekly", "Biweekly", "Monthly", "Quarterly", "Yearly"]:
        if frequency == "Weekly":
            periods = years * 52
        elif frequency == "Biweekly":
            periods = years * 26
        elif frequency == "Monthly":
            periods = years * 12
        elif frequency == "Quarterly":
            periods = years * 4
        elif frequency == "Yearly":
            periods = years

# Input for principal, rate, time, and n in the right column
with col2:
    principal = st.number_input("Enter the principal amount: ", value=10000)
    rate = st.number_input("Enter the annual interest rate (%): ", value=12) / 100
    time = st.number_input("Enter the time period (in years): ", value=10)
    n = st.number_input("Enter the number of times that interest is compounded per year: ", value=12)

if st.button("Calculate"):
    result = calculate_compound_interest(principal, rate, time, n) + add_on
    st.write("The compound interest with add on is", result)

# Initialize variables for total principal and current balance
total_principal = principal  # Assuming initial_principal is defined earlier
current_balance = principal

# Lists to store values for plotting and table
years = []
principals = []
balances = []

# Calculate total principal and current balance over the years
for year in range(1, int(time) + 1):  # Assuming number_of_years is defined
    current_balance = (current_balance + add_on) * (1 + rate)  # Assuming interest_rate is defined
    total_principal += add_on  # Update total principal
    
    # Store values for plotting and table
    years.append(year)
    principals.append(total_principal)
    balances.append(current_balance)

# Display total principal and current balance
st.write(f"Total Principal: {total_principal}")
st.write(f"Current Balance: {current_balance}")

# Create a DataFrame for the table
data = {
    'Year': years,
    'Total Principal': principals,
    'Current Balance': balances
}
df = pd.DataFrame(data)

# Display the table
st.write("### Time vs Principal and Balance")
st.table(df)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(years, principals, label='Total Principal', marker='o')
plt.plot(years, balances, label='Current Balance', marker='o')
plt.title('Total Principal vs Current Balance Over Time')
plt.xlabel('Years')
plt.ylabel('Amount')
plt.legend()
plt.grid()
plt.tight_layout()

# Show the plot in Streamlit
fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=principals, mode='lines+markers', name='Total Principal'))
fig.add_trace(go.Scatter(x=years, y=balances, mode='lines+markers', name='Current Balance'))
fig.update_layout(title_text='Total Principal vs Current Balance Over Time', xaxis_title='Years', yaxis_title='Amount', template='plotly_white')
st.plotly_chart(fig)
