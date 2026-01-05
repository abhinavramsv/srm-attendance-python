import streamlit as st
import math

st.set_page_config(page_title="SRM Attendance", page_icon="🎓")

st.title("🎓 SRM Attendance Planner")
st.write("Calculate exactly how many classes you can skip or need to attend to maintain 75%.")

col1, col2 = st.columns(2)
with col1:
    total_classes = st.number_input("Total Classes", min_value=1, value=40, step=1)
with col2:
    attended_classes = st.number_input("Classes Attended", min_value=0, value=30, step=1)

if attended_classes > total_classes:
    st.error("⚠️ Error: You cannot attend more classes than the total!")

else:
    current_percentage = (attended_classes / total_classes) * 100
    st.metric(label="Current Attendance", value=f"{current_percentage:.2f}%")

    if current_percentage >= 75:
        bunkable_classes = math.floor((attended_classes / 0.75) - total_classes)
        
        st.success(f"✅ YOU ARE SAFE!")
        st.write(f"You can safely skip the next **{bunkable_classes} classes** and still stay above 75%.")
        
    else:
        needed_classes = math.ceil((0.75 * total_classes - attended_classes) / 0.25)
        
        st.error(f"🚨 ATTENDANCE LOW!")
        st.write(f"You need to attend the next **{needed_classes} classes** straight to hit 75%.")

st.markdown("---")
st.caption("Built with pure Python by Abhinav Ram")

