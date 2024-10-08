import numpy as np
import plotly.graph_objects as go
import streamlit as st

# Set up the Streamlit app
st.title("AACE Equation Alternatives")

# Create two tabs
explore_tab, results_tab = st.tabs(["Explore", "Results"])

# All content goes into the Explore tab
with explore_tab:

    st.markdown(
        '<p class="standard-text">Select an AACE equation and the alternative equation terms & coefficients:</p>',
        unsafe_allow_html=True,
    )
    calculation_type = st.selectbox("", ["BASAL", "CIR", "ISF"], label_visibility="collapsed")

    if calculation_type in ["BASAL", "CIR", "ISF"]:

        # Add custom CSS to style the input boxes
        st.markdown(
            """
        <style>
            .standard-text {
                font-size: 1rem;
                font-weight: 400;
                line-height: 1.6;
            }
            .stSelectbox, .stNumberInput {
                width: 100%;
            }
            .stSelectbox > div > div {
                padding: 2px 8px;
            }
            .stNumberInput > div > div > input {
                padding: 2px 8px;
            }
            .coefficient-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 10px;
            }
            .coefficient-label {
                font-weight: bold;
                margin-right: 5px;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )

        if calculation_type == "BASAL":
            y_term = r"\text{BASAL}_{\text{term}}"
        elif calculation_type == "CIR":
            y_term = r"\text{CIR}_{\text{term}}"
        elif calculation_type == "ISF":
            y_term = r"\text{ISF}_{\text{term}}"

        bmi_term = r"\text{BMI}_{\text{term}}"
        cho_term = r"\text{CHO}_{\text{term}}"
        tdd_term = r"\text{TDD}_{\text{term}}"

        st.latex(f"{y_term} = \\beta_0 + \\beta_1 {bmi_term} + \\beta_2 {cho_term} + \\beta_3 {tdd_term}")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                '<div class="coefficient-row"><span class="coefficient-label">Y Term:</span>', unsafe_allow_html=True
            )
            y_term = st.selectbox(
                "Y Term", [calculation_type, f"ln ({calculation_type})"], key="y_term", label_visibility="collapsed"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown(
                '<div class="coefficient-row"><span class="coefficient-label">X-Intercept (β₀):</span>',
                unsafe_allow_html=True,
            )
            beta0 = st.number_input(
                "X-Intercept", value=0.000, step=1.000, format="%.3f", key="beta0", label_visibility="collapsed"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown(
                '<div class="coefficient-row"><span class="coefficient-label">BMI Coefficent (β₁):</span>',
                unsafe_allow_html=True,
            )
            beta1 = st.number_input(
                "BMI Coefficient", value=0.000, step=1.000, format="%.3f", key="beta1", label_visibility="collapsed"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with col4:
            st.markdown(
                '<div class="coefficient-row"><span class="coefficient-label">BMI Term:</span>', unsafe_allow_html=True
            )
            bmi_term = st.selectbox("BMI Term", ["BMI", "ln (BMI + 1)"], key="bmi_term", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)

        col5, col6, col7, col8 = st.columns(4)

        with col5:
            st.markdown(
                '<div class="coefficient-row"><span class="coefficient-label">CHO Coefficent (β₂):</span>',
                unsafe_allow_html=True,
            )
            beta2 = st.number_input(
                "CHO Coefficient", value=0.00, step=0.01, format="%.2f", key="beta2", label_visibility="collapsed"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with col6:
            st.markdown(
                '<div class="coefficient-row"><span class="coefficient-label">CHO Term:</span>', unsafe_allow_html=True
            )
            cho_term = st.selectbox("CHO Term", ["CHO", "ln (CHO + 1)"], key="cho_term", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)

        with col7:
            st.markdown(
                '<div class="coefficient-row"><span class="coefficient-label">TDD Coefficent (β₃):</span>',
                unsafe_allow_html=True,
            )
            beta3 = st.number_input(
                "TDD Coefficient", value=0.000, step=1.000, format="%.3f", key="beta3", label_visibility="collapsed"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with col8:
            st.markdown(
                '<div class="coefficient-row"><span class="coefficient-label">TDD Term:</span>', unsafe_allow_html=True
            )
            tdd_term = st.selectbox(
                "TDD Term", ["TDD", "ln (TDD + 1)", "1/TDD"], key="tdd_term", label_visibility="collapsed"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        y_term_latex = (
            r"\text{" + calculation_type + r"}"
            if y_term == calculation_type
            else r"\ln(\text{" + calculation_type + r"})"
        )
        bmi_latex = r"\text{BMI}" if bmi_term == "BMI" else r"\ln(\text{BMI} + 1)"
        cho_latex = r"\text{CHO}" if cho_term == "CHO" else r"\ln(\text{CHO} + 1)"
        tdd_latex = (
            r"\text{TDD}"
            if tdd_term == "TDD"
            else (r"\ln(\text{TDD} + 1)" if tdd_term == "ln (TDD + 1)" else r"\frac{1}{\text{TDD}}")
        )

        if calculation_type == "BASAL":
            st.latex(r"BASAL_{\text{AACE}} = 0.5\ TDD")
        elif calculation_type == "CIR":
            st.latex(r"CIR_{\text{AACE}} = \frac{450}{TDD}")
        elif calculation_type == "ISF":
            st.latex(r"ISF_{\text{AACE}} = \frac{1700}{TDD}")

        st.latex(
            f"{y_term_latex} = {beta0:.2f} + {beta1:.2f}\ {bmi_latex} + {beta2:.2f}\ {cho_latex} + {beta3:.2f}\  {tdd_latex}"
        )

    # Create two columns for BMI and CHO selectboxes
    col1, col2 = st.columns(2)

    # Define the options for BMI and CHO
    bmi_options = [12.0, 25.0, 45.0]
    cho_options = [0, 250, 500]

    # Create a list of tuples for all combinations
    combinations = [(bmi, cho) for bmi in bmi_options for cho in cho_options]

    # Create a formatted list of options for the selectbox
    options = [f"BMI: {bmi}, CHO: {cho}" for bmi, cho in combinations]

    # Create a single selectbox for all combinations
    selected_option = st.selectbox("Select BMI and CHO combination", options)

    # Extract the selected BMI and CHO values
    selected_bmi, selected_cho = map(float, selected_option.replace("BMI: ", "").replace("CHO: ", "").split(", "))

    # Use selected_bmi and selected_cho in your calculations
    bmi = selected_bmi
    cho = selected_cho

    # Generate data for the plot
    if calculation_type == "BASAL":
        tdd = np.arange(0, 501)  # Integer values from 0 to 500, inclusive
    else:
        tdd = np.arange(1, 501)  # Integer values from 1 to 500, inclusive

    if calculation_type == "BASAL":
        y_aace = 0.5 * tdd
    elif calculation_type == "CIR":
        y_aace = 450 / tdd
    elif calculation_type == "ISF":
        y_aace = 1700 / tdd

    y_term = calculation_type if y_term == calculation_type else f"ln ({calculation_type})"
    bmi_value = bmi if bmi_term == "BMI" else np.log(bmi + 1)
    cho_value = cho if cho_term == "CHO" else np.log(cho + 1)
    tdd_value = tdd if tdd_term == "TDD" else (np.log(tdd + 1) if tdd_term == "ln (TDD + 1)" else 1 / tdd)

    y_new = np.maximum(0, beta0 + beta1 * bmi_value + beta2 * cho_value + beta3 * tdd_value)

    if y_term.startswith("ln"):
        y_new = np.exp(y_new)  # Exponentiate if the y_term is logarithmic

    if calculation_type == "BASAL":
        br_aace = np.round(y_aace / 24, 2)
        br_new = np.round(y_new / 24, 2)
        y_axis_title = "Basal Insulin"
        aace_formula = "BASAL = 0.5 * TDD"
    elif calculation_type == "CIR":
        y_axis_title = "Carb Insulin Ratio (CIR)"
        aace_formula = "CIR = 450 / TDD"
    elif calculation_type == "ISF":
        y_axis_title = "Insulin Sensitivity Factor (ISF)"
        aace_formula = "ISF = 1700 / TDD"

    new_formula = f"{y_term} = {beta0:.2f} + {beta1:.2f}*{bmi_term} + {beta2:.2f}*{cho_term} + {beta3:.2f}*{tdd_term}"

    hovertemplate_aace = f"AACE<br>TDD: %{{x}}<br>{calculation_type}: %{{y:.2f}}"
    hovertemplate_new = f"NEW<br>TDD: %{{x}}<br>{calculation_type}: %{{y:.2f}}"

    if calculation_type == "BASAL":
        hovertemplate_aace += "<br>BR: %{text:.2f}<extra></extra>"
        hovertemplate_new += "<br>BR: %{text:.2f}<extra></extra>"
    else:
        hovertemplate_aace += "<extra></extra>"
        hovertemplate_new += "<extra></extra>"

    st.write(f"This plot shows the relationship between Total Daily Dose (TDD) and {calculation_type}.")

    # Create the Plotly figure
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=tdd,
            y=y_aace,
            mode="lines",
            name=f"AACE: {aace_formula}",
            hovertemplate=(
                hovertemplate_aace
                if calculation_type == "BASAL"
                else f"AACE<br>TDD: %{{x}}<br>{calculation_type}: %{{y:.2f}}<extra></extra>"
            ),
            text=br_aace if calculation_type == "BASAL" else None,
        )
    )
    fig.add_trace(
        go.Scatter(
            x=tdd,
            y=y_new,
            mode="lines",
            name=f"New: {new_formula}",
            hovertemplate=(
                hovertemplate_new
                if calculation_type == "BASAL"
                else f"NEW<br>TDD: %{{x}}<br>{calculation_type}: %{{y:.2f}}<extra></extra>"
            ),
            text=br_new if calculation_type == "BASAL" else None,
        )
    )

    # Customize the layout
    fig.update_layout(
        xaxis_title="Total Daily Dose (TDD)",
        yaxis_title=y_axis_title,
        title=f"{calculation_type} vs Total Daily Dose",
        hovermode="x",
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    # Set y-axis to log scale for CIR and ISF
    if calculation_type in ["CIR", "ISF"]:
        fig.update_layout(yaxis_type="log")

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Add some explanation
    st.write(
        f"""
    This plot demonstrates two different methods for calculating {calculation_type}:

    1. AACE method: {aace_formula}
       {"This is a simple linear relationship where Basal insulin is half of the Total Daily Dose." if calculation_type == "BASAL" else 
        "This method uses a constant (450 for CIR, 1700 for ISF) divided by the Total Daily Dose." if calculation_type in ["CIR", "ISF"] else 
        "Placeholder explanation for AACE method."}

    2. New method: {new_formula}
       {"This method takes into account the patient's Body Mass Index (BMI) and daily Carbohydrate intake (CHO) in addition to the Total Daily Dose." if calculation_type == "BASAL" else 
        "This new method incorporates the patient's Body Mass Index (BMI) and daily Carbohydrate intake (CHO) along with the Total Daily Dose to provide a more personalized CIR calculation." if calculation_type == "CIR" else
        "This new method takes into account the patient's Body Mass Index (BMI) and daily Carbohydrate intake (CHO) along with the Total Daily Dose to calculate a more personalized ISF value." if calculation_type == "ISF" else
        "Placeholder for new method explanation."}

    You can adjust the BMI and CHO values using the selectboxes to see how they affect the {calculation_type} calculation in the new method.
    """
    )

# Results tab
with results_tab:
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go

    # Load the CSV file
    calculation_type = st.selectbox("Select calculation type:", ["BASAL", "CIR", "ISF"])
    df = pd.read_csv(f"test_eval_results/test_eval__{calculation_type}__2024-09-07.csv")

    # Display AACE model details
    aace_mask = df["is_aace"] == True
    aace_row = df[aace_mask].iloc[0]

    # Filter non-AACE models and sort by test_mdape
    non_aace_models = df[~aace_mask].sort_values("test_mdape")

    # Add rank column
    non_aace_models["Rank"] = range(1, len(non_aace_models) + 1)

    # Create a list of models with their MDAPE, excluding AACE
    models = [
        f"[{row['Rank']}] {row['Equation with Coefficients']} [MdAPE: {row['test_mdape']:.3f},  RMSE: {row['test_rmse']:.3f}]"
        for _, row in non_aace_models.iterrows()
    ]
    selected_model = st.selectbox("Select a model:", models)

    # Get the selected model details
    selected_model_equation = selected_model.split("]")[1].split("[")[0].strip()
    selected_row = non_aace_models[non_aace_models["Equation with Coefficients"] == selected_model_equation].iloc[0]

    # Create a DataFrame with both AACE and selected model
    comparison_data = {
        "Model": ["AACE", "Selected"],
        "Equation": [aace_row["Equation with Coefficients"], selected_row["Equation with Coefficients"]],
        "MdAPE": [f"{aace_row['test_mdape']:.3f}", f"{selected_row['test_mdape']:.3f}"],
        "RMSE": [f"{aace_row['test_rmse']:.3f}", f"{selected_row['test_rmse']:.3f}"],
    }
    comparison_df = pd.DataFrame(comparison_data)

    # Set the index to 'A' for AACE and the rank for the selected model
    comparison_df.index = ["A", str(selected_row["Rank"])]

    # Display the comparison table
    st.table(comparison_df)

    # Generate data for the plot
    tdd = np.arange(1, 501)  # Integer values from 1 to 500, inclusive

    # AACE equation
    if calculation_type == "BASAL":
        y_aace = 0.5 * tdd
        aace_formula = "BASAL = 0.5 * TDD"
    elif calculation_type == "CIR":
        y_aace = 450 / tdd
        aace_formula = "CIR = 450 / TDD"
    elif calculation_type == "ISF":
        y_aace = 1700 / tdd
        aace_formula = "ISF = 1700 / TDD"

    # Parse the selected model equation
    equation = selected_row["Equation with Coefficients"]
    is_log_y = selected_row["is_log_y"]

    # Calculate y values for the selected model
    y_selected = selected_row["X_intercept"] if "X_intercept" in selected_row else 0

    # Create a list of tuples for all combinations
    bmi_options = [12.0, 25.0, 45.0]
    cho_options = [0, 250, 500]
    combinations = [(bmi, cho) for bmi in bmi_options for cho in cho_options]

    # Create a formatted list of options for the selectbox
    options = [f"BMI: {bmi}, CHO: {cho}" for bmi, cho in combinations]

    # Create a single selectbox for all combinations
    selected_option = st.selectbox("Select BMI & CHO Combo", options)

    # Extract the selected BMI and CHO values
    selected_bmi, selected_cho = map(float, selected_option.replace("BMI: ", "").replace("CHO: ", "").split(", "))

    # Update the terms list with the selected BMI and CHO values
    terms = [
        ("BMI", selected_bmi),
        ("log_BMI", np.log(selected_bmi + 1)),
        ("CHO", selected_cho),
        ("log_CHO", np.log(selected_cho + 1)),
        ("TDD", tdd),
        ("log_TDD", np.log(tdd + 1)),
        ("1/TDD", 1 / tdd),
    ]

    for term, value in terms:
        if term in selected_row:
            if pd.notna(selected_row[term]):
                if selected_row[term] != 0:
                    y_selected += selected_row[term] * value

    if is_log_y:
        y_selected = np.exp(y_selected)

    # Create the Plotly figure
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=tdd,
            y=y_aace,
            mode="lines",
            name=f"AACE: {aace_formula}",
            hovertemplate=f"AACE<br>TDD: %{{x}}<br>{calculation_type}: %{{y:.2f}}<extra></extra>",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=tdd,
            y=y_selected,
            mode="lines",
            name=f"Selected: {selected_row['Equation with Coefficients']}",
            hovertemplate=f"Selected<br>TDD: %{{x}}<br>{calculation_type}: %{{y:.2f}}<extra></extra>",
        )
    )

    # Customize the layout
    fig.update_layout(
        xaxis_title="Total Daily Dose (TDD)",
        yaxis_title=calculation_type,
        title=f"{calculation_type} vs Total Daily Dose",
        hovermode="x",
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    # Set y-axis to log scale for CIR and ISF
    if calculation_type in ["CIR", "ISF"]:
        fig.update_layout(yaxis_type="log")

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Add some explanation
    st.write(
        f"""
    This plot demonstrates two different methods for calculating {calculation_type}:

    1. AACE method: {aace_formula}
       {"This is a simple linear relationship where Basal insulin is half of the Total Daily Dose." if calculation_type == "BASAL" else 
        "This method uses a constant (450 for CIR, 1700 for ISF) divided by the Total Daily Dose." if calculation_type in ["CIR", "ISF"] else 
        "Placeholder explanation for AACE method."}

    2. Selected method: (as shown in the legend)
       This method provides an alternative calculation for {calculation_type} based on the Total Daily Dose, BMI, and CHO intake.

    The plot allows you to compare the AACE method with the selected alternative method visually.
    You can adjust the BMI and CHO values using the selectbox to see how they affect the {calculation_type} calculation in the selected method.
    """
    )
