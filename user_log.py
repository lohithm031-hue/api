user_name=input("Enter your name: ")
user_password=input("Enter your password: ")
inbuilt_user_name="admin"
inbuilt_user_password="admin123"

if user_name==inbuilt_user_name and user_password==inbuilt_user_password:
    print("Login successful!")
else:
    print("Login failed! Please check your username and password.")
    