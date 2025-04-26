# AA Inflight Tracker

AA Inflight Tracker is a Python-based project designed to fetch and track flight status information using the American Airlines Inflight API.

## Project Setup

### Prerequisites

- Python 3.12 or higher
- `pip` (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd aa-inflight-tracker
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can use `uv` to manage dependencies:
   ```bash
   uv sync
   ```

### Running the Project

1. Set up the environment variable for the project:
   ```bash
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   ```

2. Run the main agent script:
   ```bash
   python aa_inflight_tracker/agent/aa_inflight_agent.py
   ```

### Project Structure

- `aa_inflight_tracker/`
  - `agent/`: Contains the agent responsible for fetching and storing flight status data.
  - `client/`: Contains the client for interacting with the American Airlines Inflight API.
  - `models/`: Contains the data models used in the project.
- `data/`: Stores the flight status data as JSON files.

### Dependencies

The project uses the following dependencies:

- `loguru`: For logging
- `pydantic`: For data validation and parsing
- `requests`: For making HTTP requests

Dependencies are managed in the `pyproject.toml` file.