#  US Bikeshare Data Exploration with Python and pandas

A command-line Python project to perform exploratory data analysis on bikeshare usage data from Chicago, New York City, and Washington using `pandas`, `numpy`, and basic Python functions.

---

##  Project Overview

This project demonstrates how to use the `pandas` library to analyze and interpret real-world data. The dataset consists of randomly selected bikeshare trip logs for the first six months of 2017, made available by Motivate, a bike share system provider.

Users interact with the script to explore data by city, month, and day of the week, and receive various statistics about bikeshare usage.

---

##  Running the Program

To run the script, navigate to the project directory and use:

```bash
python bikeshare.py
```

_Example tested using Windows PowerShell and Python 3.10._

---

##  Program Features

The program:
1. **Prompts for user input** on:
   - City (`Chicago`, `New York City`, `Washington`)
   - Month (`January` through `June`, or `All`)
   - Day of week (`Monday` through `Sunday`, or `All`)
2. **Optionally displays raw data**, 5 rows at a time
3. **Displays key statistics**:
   - Most common month, day, and start hour
   - Most common start station, end station, and trip combination
   - Total and average trip duration
   - User type breakdown (Customer vs Subscriber)
   - Gender distribution (where available)
   - Earliest, most recent, and most common year of birth (where available)
4. **Gives the user the option to restart**

---

##  Requirements

- **Python**: 3.6 or later
- **Libraries**:
  - `pandas`
  - `numpy`
  - `time`

---

##  Project Files

- `bikeshare.py`: Main Python script for interactive analysis
- `.gitignore`: Ensures data files (e.g. `.csv`) are not tracked by Git
- `README.md`: Project overview and instructions
- `chicago.csv`, `new_york_city.csv`, `washington.csv`: Data files (excluded from GitHub repo per `.gitignore`)

---

##  Built With

- [Python 3.6+](https://www.python.org/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [time](https://docs.python.org/3/library/time.html)

---

##  Author

**masamasri01**  
[GitHub Profile →](https://github.com/masamasri01)

---

##  Acknowledgements

- **Udacity** — For the project prompt and supporting materials as part of the Data Analyst Nanodegree
- **pandas documentation** — Invaluable reference for data handling
- **GitHub open source community** — For examples and structure inspiration

---
