import psycopg2
# from psycopg2 import Error
# import streamlit as st
# import psycopg2
# import pandas as pd

# def connect_to_db():
#     connection = psycopg2.connect(
#         database="loyalty_db",
#         user="postgres",
#         password="123456",
#         host="localhost",
#         port="5433"
#     )
#     print("Connection to the database established successfully.")
#     return connection
import streamlit as st
import psycopg2
import pandas as pd

# Kết nối PostgreSQL
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="loyalty_db",
        user="postgres",
        password="123456",
        port="5433"
    )

# Hàm lấy dữ liệu
def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Hàm thêm dữ liệu
def insert_data(query, values):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, values)
    conn.commit()
    conn.close()

# Giao diện
st.title("📊 Popplife Simple Admin")

menu = ["Users", "Merchants", "Products", "Transactions", "Campaigns", "Rewards", "Notifications"]
choice = st.sidebar.selectbox("Chọn bảng", menu)

# CRUD cho từng bảng
if choice == "Users":
    st.subheader("Quản lý Users")
    
    with st.form("add_user"):
        name = st.text_input("Họ tên")
        email = st.text_input("Email")
        phone = st.text_input("Số điện thoại")
        birthday = st.date_input("Ngày sinh")
        gender = st.selectbox("Giới tính", ["Male", "Female", "Other"])
        address = st.text_area("Địa chỉ")
        points = st.number_input("Tổng điểm", min_value=0)
        submitted = st.form_submit_button("Thêm")
        if submitted:
            insert_data(
                "INSERT INTO Users(full_name, email, phone, birthday, gender, address, total_points) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (name, email, phone, birthday, gender, address, points)
            )
            st.success("✅ Đã thêm user!")
    
    st.dataframe(fetch_data("SELECT * FROM Users"))

elif choice == "Merchants":
    st.subheader("Quản lý Merchants")
    with st.form("add_merchant"):
        name = st.text_input("Tên Merchant")
        address = st.text_area("Địa chỉ")
        phone = st.text_input("Số điện thoại")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Thêm")
        if submitted:
            insert_data(
                "INSERT INTO Merchants(name, address, phone, email) VALUES (%s,%s,%s,%s)",
                (name, address, phone, email)
            )
            st.success("✅ Đã thêm merchant!")
    st.dataframe(fetch_data("SELECT * FROM Merchants"))

# Tương tự bạn có thể copy & điều chỉnh code cho Products, Transactions, Campaigns, Rewards, Notifications
