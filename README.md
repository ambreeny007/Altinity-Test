# Altnity-Testflows Automation

Altnity Automation using TestFlows with ClickHouse DB.

## Installation

1. Install python and activate venv
2. Download and install ClickHouse DB by following the official instructions for your operating system. You can find the installation guide at [ClickHouse Documentation](https://clickhouse.tech/docs/en/getting-started/install/).

3. Install the required Python dependencies by running the following command:

### 1. Install python and activate venv
1. Install Python if you haven't already. You can download Python from the official website: [python.org](https://www.python.org/downloads/).
2. Create a virtual environment using `venv` by running the following command:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:

      ```
      venv\Scripts\activate
      ```
    
    - On macOS and Linux:
    
      ```
      source venv/bin/activate
      ```
### 2. Download, Install and Run Clickhouse DB
1. Download the Clickhouse with the following command:
   ```bash
   curl https://clickhouse.com/ | sh
   ```
2. Install Clickhouse DB
   ```bash
   sudo ./clickhouse.2 install
   ```
3. Start Clickhouse DB
   ```bash
   sudo clickhouse start
   ```
   
### 3. Install the requirement libraries
1. After cloning the project and applying above steps, now execute the following command to install required libraries:
    ```bash
   pip install -r requirements.txt
   ```
   
## Tests Execution
1. Run the LS tests by running the following command in terminal:
    ```bash
   python ls_test.py
   ```
2. Run the Clickhouse DB test by running the following command in terminal:
    ```bash
   python db_test.py
   ```

3. Run the Selenium tests by running the following command in terminal:
    ```bash
   python selenium_test.py
   ```