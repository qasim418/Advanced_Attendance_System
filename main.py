import sys ,  datetime 
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5 import QtGui


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem


from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy
import sqlite3

class SideNavMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Side Navbar Menu")
        self.setGeometry(100, 100, 900, 700)

        self.sidebar = QWidget(self)
        self.sidebar.setGeometry(0, 0, 200, self.height())
        self.sidebar.setStyleSheet("background-color: #232931;")

        self.layout = QVBoxLayout(self.sidebar)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.add_button("Records")
        self.add_button("Portal")
        self.add_button("Attendance")

        self.central_widget = QStackedWidget(self)
        self.central_widget.setGeometry(200, 0, self.width() - 200, self.height())

        self.page_home = QWidget()
        self.page_form = QWidget()
        self.page_about = QWidget()

        self.setup_home_page()
        self.setup_form_page()
        self.setup_about_page()

        self.central_widget.addWidget(self.page_home)
        self.central_widget.addWidget(self.page_form)
        self.central_widget.addWidget(self.page_about)

        self.show()

    def add_button(self, text):
        button = QPushButton(text, self.sidebar)
        button.setStyleSheet(
            """
            QPushButton {
                background-color: #232931;
                color: white;
                border: none;
                padding-top: 10px;
                padding-bottom: 10px;
                padding-left: 15px;
                text-align: center;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #393e46;
            }
            """
        )
        button.clicked.connect(lambda: self.handle_button_click(text))
        self.layout.addWidget(button)

    def handle_button_click(self, button_text):
        if button_text == "Records":
            self.central_widget.setCurrentWidget(self.page_home)
        elif button_text == "Portal":
            self.central_widget.setCurrentWidget(self.page_form)
        elif button_text == "Attendance":
            self.central_widget.setCurrentWidget(self.page_about)



    # def setup_home_page(self):
    #     layout = QVBoxLayout(self.page_home)
    #     layout.setAlignment(QtCore.Qt.AlignTop)

    #     # Create the heading
    #     heading_label = QLabel("Students Record")
    #     heading_label.setStyleSheet("font-size: 20px; font-weight: bold;")
    #     layout.addWidget(heading_label)

    #     # Create the search option
    #     search_layout = QHBoxLayout()
    #     search_label = QLabel("Search:")
    #     search_label.setStyleSheet("font-size: 16px; margin-right: 5px;")
    #     self.search_input_students = QLineEdit()
    #     self.search_input_students.setStyleSheet("font-size: 16px; padding: 5px;")
    #     search_button = QPushButton("Search")
    #     search_button.setStyleSheet(
    #         """
    #         QPushButton {
    #             padding: 5px 10px;
    #             background-color: #4CAF50;
    #             color: white;
    #             font-size: 16px;
    #             border: none;
    #         }
    #         QPushButton:hover {
    #             background-color: #45a049;
    #         }
    #         """
    #     )
    #     refresh_button = QPushButton("Refresh")
    #     refresh_button.setStyleSheet(
    #         """
    #         QPushButton {
    #             padding: 5px 10px;
    #             background-color: #f44336;
    #             color: white;
    #             font-size: 16px;
    #             border: none;
    #         }
    #         QPushButton:hover {
    #             background-color: #d32f2f;
    #         }
    #         """
    #     )
    #     search_layout.addWidget(search_label)
    #     search_layout.addWidget(self.search_input_students)
    #     search_layout.addWidget(search_button)
    #     search_layout.addWidget(refresh_button)
    #     layout.addLayout(search_layout)

    #     # Create the table to display student records
    #     self.table_students = QTableWidget()
    #     self.table_students.setColumnCount(6)
    #     self.table_students.setHorizontalHeaderLabels(["No.", "Image", "Name", "Class", "Contact Info", "Address"])

    #     # Populate the table with data
    #     self.update_student_table()

    #     layout.addWidget(self.table_students)

    #     # Connect the search button to the search functionality
    #     search_button.clicked.connect(self.search_students)
    #     refresh_button.clicked.connect(self.refresh_student_table)

    def setup_home_page(self):
        layout = QVBoxLayout(self.page_home)
        layout.setAlignment(QtCore.Qt.AlignTop)

        # Create the heading
        heading_label = QLabel("Students Record")
        heading_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(heading_label)

        # Create the search option
        search_layout = QHBoxLayout()
        search_label = QLabel("Search:")
        search_label.setStyleSheet("font-size: 16px; margin-right: 5px;")
        self.search_input_students = QLineEdit()
        self.search_input_students.setStyleSheet("font-size: 16px; padding: 5px;")
        search_button = QPushButton("Search")
        search_button.setStyleSheet(
            """
            QPushButton {
                padding: 5px 10px;
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )
        refresh_button = QPushButton("Refresh")
        refresh_button.setStyleSheet(
            """
            QPushButton {
                padding: 5px 10px;
                background-color: #f44336;
                color: white;
                font-size: 16px;
                border: none;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
            """
        )
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input_students)
        search_layout.addWidget(search_button)
        search_layout.addWidget(refresh_button)
        layout.addLayout(search_layout)

        # Create the table to display student records
        self.table_students = QTableWidget()
        self.table_students.setColumnCount(6)
        self.table_students.setHorizontalHeaderLabels(["Image", "ID No", "Name", "Class", "Contact Info", "Address"])

        # Populate the table with data
        self.update_student_table()

        layout.addWidget(self.table_students)

        # Connect the search button to the search functionality
        search_button.clicked.connect(self.search_students)
        refresh_button.clicked.connect(self.refresh_student_table)

    def extract_student_record1(self):
        # Connect to the SQLite database
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Execute the query to retrieve student records
        cursor.execute("SELECT * FROM students_record")
        student_records = cursor.fetchall()

        # Close the connection
        conn.close()

        return student_records


    # def update_student_table(self):
    #     # Clear the table
    #     self.table_students.clearContents()

    #     # Get the student records
    #     student_records = self.extract_student_record1()

    #     # Set the number of rows in the table
    #     self.table_students.setRowCount(len(student_records))

    #     # Populate the table with data
    #     for row, record in enumerate(student_records):
    #         for column, value in enumerate(record):
    #             if column == 1:
    #                 # Display the image in the table cell
    #                 image_path = value  # Assuming the image path is stored in the second column
    #                 pixmap = QtGui.QPixmap(image_path).scaledToWidth(50)
    #                 item = QTableWidgetItem()
    #                 item.setIcon(QtGui.QIcon(pixmap))
    #                 self.table_students.setItem(row, column, item)
    #             else:
    #                 # Display the other data in the table cell
    #                 item = QTableWidgetItem(str(value))
    #                 self.table_students.setItem(row, column, item)

    def update_student_table(self, student_records=None):
        # Clear the table
        self.table_students.clearContents()

        # Get the student records if not provided
        if student_records is None:
            student_records = self.extract_student_record1()


        # Set the number of rows in the table
        self.table_students.setRowCount(len(student_records))

        # Define the desired width and height for the image
        medium_width = 100
        medium_height = 100

        # Populate the table with data
        for row, record in enumerate(student_records):
            for column, value in enumerate(record):
                if column == 0:
                    # Display the image in the table cell (first column)
                    image_path = value  # Assuming the image path is stored in the first column
                    pixmap = QtGui.QPixmap(image_path).scaled(medium_width, medium_height, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                    label = QLabel()
                    label.setPixmap(pixmap)
                    label.setScaledContents(True)
                    self.table_students.setCellWidget(row, column, label)
                else:
                    # Display the other data in the table cells
                    item = QTableWidgetItem(str(value))
                    self.table_students.setItem(row, column, item)

        # Set the row height
        self.table_students.verticalHeader().setDefaultSectionSize(medium_height)


    def search_students(self):
        # Get the search query
        query = self.search_input_students.text()

        # Retrieve all student records
        student_records = self.extract_student_record1()

        # Filter the records based on the search query
        filtered_records = []
        for record in student_records:
            if query.lower() in str(record).lower():
                filtered_records.append(record)

        # Update the table with the filtered records
        print(filtered_records)
        self.update_student_table(filtered_records)


    def refresh_student_table(self):
        # Clear the search input
        self.search_input_students.clear()

        # Retrieve all student records
        student_records = self.extract_student_record1()

        # Update the table with all student records
        self.update_student_table(student_records)





#     def setup_home_page(self):
#         # def setup_students_page(self):
#         layout = QVBoxLayout(self.page_home)
#         layout.setAlignment(QtCore.Qt.AlignTop)

#         # Create the heading
#         heading_label = QLabel("Students Record")
#         heading_label.setStyleSheet("font-size: 20px; font-weight: bold;")
#         layout.addWidget(heading_label)

#         # Create the search option
#         search_layout = QHBoxLayout()
#         search_label = QLabel("Search:")
#         search_label.setStyleSheet("font-size: 16px; margin-right: 5px;")
#         self.search_input_students = QLineEdit()
#         self.search_input_students.setStyleSheet("font-size: 16px; padding: 5px;")
#         search_button = QPushButton("Search")
#         search_button.setStyleSheet(
#             """
#             QPushButton {
#                 padding: 5px 10px;
#                 background-color: #4CAF50;
#                 color: white;
#                 font-size: 16px;
#                 border: none;
#             }
#             QPushButton:hover {
#                 background-color: #45a049;
#             }
#             """
#         )
#         refresh_button = QPushButton("Refresh")
#         refresh_button.setStyleSheet(
#             """
#             QPushButton {
#                 padding: 5px 10px;
#                 background-color: #f44336;
#                 color: white;
#                 font-size: 16px;
#                 border: none;
#             }
#             QPushButton:hover {
#                 background-color: #d32f2f;
#             }
#             """
#         )
#         search_layout.addWidget(search_label)
#         search_layout.addWidget(self.search_input_students)
#         search_layout.addWidget(search_button)
#         search_layout.addWidget(refresh_button)
#         layout.addLayout(search_layout)

#         # Create the table to display student records
#         self.table_students = QTableWidget()
#         self.table_students.setColumnCount(6)
#         self.table_students.setHorizontalHeaderLabels(["No.", "Image", "Name", "Class", "Contact Info", "Address"])

#         # Example data (replace with your actual data)
#         self.student_records = extract_student_record1()

#         # Populate the table with data
#         update_student_table()

#         layout.addWidget(self.table_students)

#         # Connect the search button to the search functionality
#         search_button.clicked.connect(self.search_students)
#         refresh_button.clicked.connect(self.refresh_student_table)

# def extract_student_record1():
#     # Connect to the SQLite database
#     conn = sqlite3.connect('example.db')
#     cursor = conn.cursor()

#     # Execute the query to retrieve student records
#     cursor.execute("SELECT * FROM students_record")
#     student_records = cursor.fetchall()

#     # Close the connection
#     conn.close()

#     return student_records


# def update_student_table(self, student_records):
#     # Clear the table
#     self.table_students.clearContents()

#     # Set the number of rows in the table
#     self.table_students.setRowCount(len(student_records))

#     # Populate the table with data
#     for row, record in enumerate(student_records):
#         for column, value in enumerate(record):
#             if column == 1:
#                 # Display the image in the table cell
#                 image_path = value  # Assuming the image path is stored in the second column
#                 pixmap = QtGui.QPixmap(image_path).scaledToWidth(50)
#                 item = QTableWidgetItem()
#                 item.setIcon(QtGui.QIcon(pixmap))
#                 self.table_students.setItem(row, column, item)
#             else:
#                 # Display the other data in the table cell
#                 item = QTableWidgetItem(str(value))
#                 self.table_students.setItem(row, column, item)


# def search_students(self):
#     # Get the search query
#     query = self.search_input_students.text()

#     # Retrieve all student records
#     student_records = extract_student_record1()

#     # Filter the records based on the search query
#     filtered_records = []
#     for record in student_records:
#         if query.lower() in str(record).lower():
#             filtered_records.append(record)

#     # Update the table with the filtered records
#     self.update_student_table(filtered_records)


# def refresh_student_table(self):
#     # Clear the search input
#     self.search_input_students.clear()

#     # Retrieve all student records
#     student_records = extract_student_record1()

#     # Update the table with all student records
#     self.update_student_table(student_records)



    # def setup_about_page(QWidget):
    #     def __init__(self):
    #         super().__init__()

    #         # Create the layout
    #         layout = QVBoxLayout(self)

    #         # Create the heading
    #         heading_label = QLabel("Attendance Record")
    #         heading_label.setStyleSheet("font-size: 20px; font-weight: bold;")
    #         layout.addWidget(heading_label)

    #         # Create the search option
    #         search_layout = QHBoxLayout()
    #         search_label = QLabel("Search:")
    #         search_input = QLineEdit()
    #         search_button = QPushButton("Search")
    #         search_layout.addWidget(search_label)
    #         search_layout.addWidget(search_input)
    #         search_layout.addWidget(search_button)
    #         layout.addLayout(search_layout)

    #         # Create the table to display record details
    #         table = QTableWidget()
    #         table.setColumnCount(5)
    #         table.setHorizontalHeaderLabels(["No", "ID No", "Time", "Expression", "Uniform"])

    #         # Example data (replace with your actual data)
    #         records = [
    #             (1, 123456, "09:00:00", "Happy", "Complete"),
    #             (2, 789012, "10:30:00", "Sad", "Incomplete"),
    #             (3, 345678, "12:15:00", "Angry", "Complete"),
    #         ]

    #         # Populate the table with data
    #         table.setRowCount(len(records))
    #         for row, record in enumerate(records):
    #             for col, data in enumerate(record):
    #                 table.setItem(row, col, QTableWidgetItem(str(data)))

    #         layout.addWidget(table)

    #          # Set the layout for the widget
    #         self.show()
    #     # layout = QVBoxLayout(self.page_about)
    #     # layout.setAlignment(QtCore.Qt.AlignCenter)

    #     # label = QLabel("About Page")
    #     # label.setStyleSheet("font-size: 24px;")
    #     # layout.addWidget(label)

    # def setup_about_page(self):
    #     layout = QVBoxLayout(self.page_about)
    #     layout.setAlignment(QtCore.Qt.AlignCenter)

    #     # Create the heading
    #     heading_label = QLabel("Attendance Record")
    #     heading_label.setStyleSheet("font-size: 20px; font-weight: bold;")
    #     layout.addWidget(heading_label)

    #     # Create the table to display record details
    #     table = QTableWidget()
    #     table.setColumnCount(5)
    #     table.setHorizontalHeaderLabels(["No", "ID No", "Time", "Expression", "Uniform"])

    #     # Example data (replace with your actual data)
    #     records = [
    #         (1, 123456, "09:00:00", "Happy", "Complete"),
    #         (2, 789012, "10:30:00", "Sad", "Incomplete"),
    #         (3, 345678, "12:15:00", "Angry", "Complete"),
    #     ]

    #     # Populate the table with data
    #     table.setRowCount(len(records))
    #     for row, record in enumerate(records):
    #         for col, data in enumerate(record):
    #             table.setItem(row, col, QTableWidgetItem(str(data)))

    #     layout.addWidget(table)


    def setup_about_page(self):
        layout = QVBoxLayout(self.page_about)
        layout.setAlignment(QtCore.Qt.AlignTop)

        # Create the heading
        heading_label = QLabel("Attendance Record")
        heading_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(heading_label)

        # Create the search option
        search_layout = QHBoxLayout()
        search_label = QLabel("Search:")
        search_label.setStyleSheet("font-size: 16px; margin-right: 5px;")
        self.search_input = QLineEdit()
        self.search_input.setStyleSheet("font-size: 16px; padding: 5px;")
        search_button = QPushButton("Search")
        search_button.setStyleSheet(
            """
            QPushButton {
                padding: 5px 10px;
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )
        refresh_button = QPushButton("Refresh")
        refresh_button.setStyleSheet(
            """
            QPushButton {
                padding: 5px 10px;
                background-color: #f44336;
                color: white;
                font-size: 16px;
                border: none;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
            """
        )
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        search_layout.addWidget(refresh_button)
        layout.addLayout(search_layout)

        # Create the table to display record details
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([ "ID No", "Time", "Name", "Expression", "Uniform"])

        # Example data (replace with your actual data)
        self.records =extract_attendance_records()

        # Populate the table with data
        self.update_table()

        layout.addWidget(self.table)

        # Connect the search button to the search functionality
        search_button.clicked.connect(self.search_records)
        refresh_button.clicked.connect(self.refresh_table)

    def update_table(self):
        self.table.setRowCount(len(self.records))
        for row, record in enumerate(self.records):
            for col, data in enumerate(record):
                self.table.setItem(row, col, QTableWidgetItem(str(data)))

    def search_records(self):
        search_text = self.search_input.text().lower()
        filtered_records = []
        for record in self.records:
            if search_text in str(record).lower():
                filtered_records.append(record)
        self.records = filtered_records
        self.update_table()

    def refresh_table(self):
        self.search_input.clear()
        self.records = extract_attendance_records()
        self.update_table()


    def setup_form_page(self):
        layout = QVBoxLayout(self.page_form)
        layout.setAlignment(QtCore.Qt.AlignCenter)

        heading_label = QLabel("File Selection")
        heading_label.setFont(QFont("Arial", 20, QFont.Bold))
        layout.addWidget(heading_label)

        self.file_path_label = QLabel("Selected File: No file selected")
        layout.addWidget(self.file_path_label)

        button_select_file = QPushButton("Select File")
        button_select_file.clicked.connect(self.select_file)
        layout.addWidget(button_select_file)

        button_submit = QPushButton("Submit")
        button_submit.clicked.connect(submit_function)
        layout.addWidget(button_submit)

        # Apply styling using style sheets
        self.setStyleSheet(
            """
            QLabel {
                font-size: 18px;
                padding: 10px;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )

        # Set layout margins and spacing
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(20)

        self.show()

   

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")
        if file_path:
            self.file_path_label.setText(f"Selected File: {file_path}")
        else:
            self.file_path_label.setText("Selected File: No file selected")


def submit_function():
    file_path = window.file_path_label.text().split(": ")[-1]
    print("Selected File:", file_path)
    # Process the file further or call other functions for processing
    import cv2
    from deepface import DeepFace
    img = cv2.imread(file_path)
    import matplotlib.pyplot as plt
    predictions =  DeepFace.analyze(img, 
        actions = [ 'emotion']
    )
    expression = str((predictions[0]['dominant_emotion']))

    dfs = DeepFace.find(
        img,  
        db_path = "employees")
    
    print(dfs[0])
    file_path = str((dfs[0]["identity"][0]))
    print(file_path)
    

    # Extract the substring after the last '/' and before the '.'
    extracted_string = file_path[file_path.rindex('/') + 1:file_path.rindex('.')]
    add_attendance_record(extracted_string, expression)
    print("data passed")

def extract_attendance_records():
    

    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Execute the SELECT query to retrieve all rows from the table
    cursor.execute("SELECT * FROM attendance_record")
    rows = cursor.fetchall()

    # Print or process the retrieved data
    for row in rows:
        print(row)  # Replace with your desired processing

    cursor.close()
    conn.close()
    return rows if rows else []


def add_attendance_record(id_no, expression):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Get user input for time, expressions, and uniform_status
    time = datetime.datetime.now().strftime('%H:%M:%S')
    expressions = expression
    uniform_status = "complete"
    name = extract_name_by_emp_id(id_no)

    # Insert the data into the table
    cursor.execute("""
        INSERT INTO attendance_record (id_no, time, name, expressions, uniform_status)
        VALUES (?, ?, ?, ?, ?)
    """, (id_no, time, name, expressions, uniform_status))

    conn.commit()
    cursor.close()
    conn.close()
    print("data saved successfully")




def extract_name_by_emp_id(emp_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Execute the query to retrieve the name based on emp_id
    cursor.execute("SELECT name FROM students_record WHERE emp_id=?", (emp_id,))
    result = cursor.fetchone()

    # Close the connection
    conn.close()

    if result:
        return result[0]  # Extract the name from the result
    else:
        return None  # No name found for the given emp_id



   





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SideNavMenu()
    sys.exit(app.exec_())