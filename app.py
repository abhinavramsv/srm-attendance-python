import streamlit as st
import math

# --- 1. CONFIGURATION (The Title & Icon) ---
st.set_page_config(page_title="SRM Attendance", page_icon="🎓")

# --- 2. THE UI (Headings & Inputs) ---
st.title("🎓 SRM Attendance Planner")
st.write("Calculate exactly how many classes you can bunk (or need to attend) to maintain 75%.")

# Create two input boxes
col1, col2 = st.columns(2)
with col1:
    total_classes = st.number_input("Total Classes", min_value=1, value=40, step=1)
with col2:
    attended_classes = st.number_input("Classes Attended", min_value=0, value=30, step=1)

# Error handling: Attended cannot be more than Total
if attended_classes > total_classes:
    st.error("⚠️ Error: You cannot attend more classes than the total!")

# --- 3. THE LOGIC (Pure Python) ---
else:
    # Calculate Percentage
    current_percentage = (attended_classes / total_classes) * 100

    # Show the current status
    st.metric(label="Current Attendance", value=f"{current_percentage:.2f}%")

    # --- THE ALGORITHM ---
    if current_percentage >= 75:
        # CASE 1: SAFE (Can Bunk)
        # Math: (Attended) / (Total + X) = 0.75
        # X = (Attended / 0.75) - Total
        bunkable_classes = math.floor((attended_classes / 0.75) - total_classes)
        
        st.success(f"✅ YOU ARE SAFE!")
        st.write(f"You can safely bunk the next **{bunkable_classes} classes** and still stay above 75%.")
        
    else:
        # CASE 2: DANGER (Must Attend)
        # Math: (Attended + Y) / (Total + Y) = 0.75
        # Y = (3 * Total - 4 * Attended)  <-- Simplified formula
        needed_classes = math.ceil((0.75 * total_classes - attended_classes) / 0.25)
        
        st.error(f"🚨 ATTENDANCE LOW!")
        st.write(f"You need to attend the next **{needed_classes} classes** straight (without bunking) to hit 75%.")

# --- 4. FOOTER ---
st.markdown("---")
st.caption("Built with pure Python by Abhinav Ram")