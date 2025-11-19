RepeatWhatYouHeard

🧠 What is RepeatWhatYouHeard?

Forget static worksheets! RepeatWhatYouHeard is a sleek, Streamlit-powered Python application designed for interactive, single-task assessment. It acts as a dynamic teaching tool, randomly selecting one question at a time from a defined subject and difficulty level and immediately allowing the user to submit and check their answer.

This project is a perfect demonstration of using modern Python libraries to create simple yet engaging educational micro-apps.

The Goal: Provide focused, rapid-fire quizzes that allow students to repeat, check, and learn without getting overwhelmed by long task lists.

🎯 Core Features (The Punchlines)

⚡️ Efficient Data Loading: Thanks to Streamlit Session State, subject files are read from the disk only a single time when the application first starts. This minimizes I/O delay and maximizes subsequent performance.

🛠️ Focused Control: Users select the Subject (e.g., German, English, Math) and the Level (1, 2, or 3) using intuitive widgets.

📝 Single Task Generator: The app is designed to present exactly one random, multiple-choice question at a time, promoting focused attention and immediate feedback.

✅ Instant Feedback Loop: Users receive immediate success or error messages upon checking their selected option within the form, reinforcing the learning process.

🧑‍💻 Clean Architecture: Modular functions (ReadAllFiles, PrintTasks, show_form) and the central Student class ensure the code is readable and maintainable.

🚀 Installation & Launch

You will need Python 3.x and Streamlit.

Clone the Repository:

git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME


Install Dependencies:

pip install streamlit


Set Up Data Structure:
The application currently supports levels 1, 2, and 3. Ensure you have the necessary subjects folder containing subfolders for your subjects and corresponding .txt files (e.g., subjects/german/german_level1.txt). Each task within the file must be separated by **=END=**, and multiple-choice options should be structured for the show_form function to parse them correctly.

Run the App:

streamlit run YOUR_MAIN_FILENAME.py


(Replace YOUR_MAIN_FILENAME.py with the actual name of your Python file, e.g., app.py or generator.py)

💡 How It Works (Usage)

Once started, the Streamlit app will open in your browser.

View the welcome header (The name 'Johnny' and level '5' are currently hardcoded in the if __name__ == '__main__' block).

Select the Level (1, 2, or 3) using the slider.

Select the Subject from the dropdown.

A single, random question will be generated.

Select your answer from the dropdown within the form.

Click "Check" to see if your answer is correct, with the outcome displayed in the header.

Result: A focused, interactive quiz experience!

🛠️ Technology Stack

Python: The foundation for all the core logic.

Streamlit: Enables building a beautiful, interactive web application with minimal effort.

Random: Used for the fair and unpredictable selection of homework tasks.

🤝 Contributing

We welcome ideas on how to expand this interactive teaching tool (e.g., adding more difficulty levels, new question types, or a feature to easily upload new task files).

Fork the Repository.

Create your Feature Branch (git checkout -b feature/NewFeature).

Commit your changes (git commit -m 'Add some NewFeature').

Push to the Branch (git push origin feature/NewFeature).

Open a Pull Request.

📄 License

Distributed under the MIT License. See LICENSE for more information.

Built with 🖤 and Python 🐍 by [GilbertZennerDev]