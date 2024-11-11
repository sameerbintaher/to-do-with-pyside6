from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QPushButton, QLineEdit, QListWidget,
                              QInputDialog, QComboBox, QDateEdit, QLabel)
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QFont
import sys

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("✨ Todo List")
        self.setMinimumSize(500, 600)
        
        # Keep the same stylesheet, just add styles for new elements
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f2f5;
            }
            QLineEdit {
                padding: 12px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #2196F3;
            }
            QPushButton {
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                color: white;
                background-color: #2196F3;
                border: none;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton#deleteBtn {
                background-color: #FF5252;
            }
            QPushButton#deleteBtn:hover {
                background-color: #D32F2F;
            }
            QPushButton#editBtn {
                background-color: #4CAF50;
            }
            QPushButton#editBtn:hover {
                background-color: #388E3C;
            }
            QPushButton#clearBtn {
                background-color: #9E9E9E;
            }
            QPushButton#clearBtn:hover {
                background-color: #757575;
            }
            QListWidget {
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
                padding: 5px;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #e0e0e0;
                border-radius: 4px;
            }
            QListWidget::item:hover {
                background-color: #F5F5F5;
            }
            QListWidget::item:selected {
                background-color: #E3F2FD;
                color: #1976D2;
            }
            QComboBox {
                padding: 8px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
                font-size: 14px;
            }
            QComboBox:hover {
                border: 2px solid #2196F3;
            }
            QComboBox:focus {
                border: 2px solid #2196F3;
            }
            QDateEdit {
                padding: 8px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
                font-size: 14px;
            }
            QDateEdit:hover {
                border: 2px solid #2196F3;
            }
            QDateEdit:focus {
                border: 2px solid #2196F3;
            }
            QLabel {
                font-size: 14px;
                color: #555;
            }
            QListWidget::item[status="not_started"] {
                color: #333;
            }
            QListWidget::item[status="in_progress"] {
                color: #1976D2;
            }
            QListWidget::item[status="completed"] {
                color: #388E3C;
                text-decoration: line-through;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Create input area with category and due date
        input_layout = QVBoxLayout()
        
        # Task input
        task_row = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("✍️ Add a new task...")
        task_row.addWidget(self.task_input)
        
        # Category dropdown
        self.category_combo = QComboBox()
        self.category_combo.addItems(["Work", "Personal", "Shopping", "Other"])
        self.category_combo.setFixedWidth(120)
        task_row.addWidget(self.category_combo)
        
        # Due date picker
        self.due_date = QDateEdit(QDate.currentDate())
        self.due_date.setCalendarPopup(True)
        self.due_date.setFixedWidth(120)
        task_row.addWidget(self.due_date)
        
        # Add button
        add_button = QPushButton("Add Task")
        add_button.setFixedWidth(100)
        add_button.clicked.connect(self.add_task)
        task_row.addWidget(add_button)
        
        input_layout.addLayout(task_row)
        
        # Filter row
        filter_row = QHBoxLayout()
        filter_row.addWidget(QLabel("Filter:"))
        
        self.filter_category = QComboBox()
        self.filter_category.addItems(["All", "Work", "Personal", "Shopping", "Other"])
        self.filter_category.currentTextChanged.connect(self.apply_filters)
        filter_row.addWidget(self.filter_category)
        
        filter_row.addStretch()
        input_layout.addLayout(filter_row)
        
        layout.addLayout(input_layout)

        # Task list
        self.task_list = QListWidget()
        self.task_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        layout.addWidget(self.task_list)

        # Control buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        delete_button = QPushButton("Delete")
        delete_button.setObjectName("deleteBtn")
        
        edit_button = QPushButton("Edit")
        edit_button.setObjectName("editBtn")
        
        clear_button = QPushButton("Clear All")
        clear_button.setObjectName("clearBtn")
        
        delete_button.clicked.connect(self.delete_task)
        edit_button.clicked.connect(self.edit_task)
        clear_button.clicked.connect(self.clear_tasks)
        
        button_layout.addWidget(delete_button)
        button_layout.addWidget(edit_button)
        button_layout.addWidget(clear_button)
        layout.addLayout(button_layout)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            category = self.category_combo.currentText()
            due_date = self.due_date.date().toString("yyyy-MM-dd")
            display_text = f"{task} 📋 {category} 📅 {due_date}"
            self.task_list.addItem(display_text)
            self.task_input.clear()

    def apply_filters(self):
        filter_cat = self.filter_category.currentText()
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            if filter_cat == "All":
                item.setHidden(False)
            else:
                # Check if category matches
                item_cat = item.text().split(" 📋 ")[1].split(" 📅 ")[0]
                item.setHidden(item_cat != filter_cat)

    def delete_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            self.task_list.takeItem(self.task_list.row(current_item))

    def edit_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            # Split the text to get original task
            original_task = current_item.text().split(" 📋 ")[0]
            new_text, ok = QInputDialog.getText(
                self, 
                'Edit Task',
                'Edit task:',
                QLineEdit.Normal,
                original_task
            )
            if ok and new_text.strip():
                # Keep the category and date, just update the task text
                category = self.category_combo.currentText()
                due_date = self.due_date.date().toString("yyyy-MM-dd")
                display_text = f"{new_text.strip()} 📋 {category} 📅 {due_date}"
                current_item.setText(display_text)

    def clear_tasks(self):
        self.task_list.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont('Segoe UI', 10))
    window = TodoApp()
    window.show()
    sys.exit(app.exec())