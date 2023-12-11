# Horse Race Betting System

## Overview

This project is a Django-based web application for simulating a betting system for horse races. It features real-time updates of race odds, allows users to place bets, and calculates dividends based on a tote betting system.

## Reviewer's note

FYI, This is not yet finished and not fully working (due to time constraint). This is using Django and DEF to provide the api and management. It has command that you will parse the csv file and process it based on the events. This also has Celery to handle all the async task. I have also added the docker and docker-compose to make it easier to run the project. I haven't added anything for monitoring but we are using Django's built-in logging and push it to a centralized logging system like ELK or Splunk.

## Features

- Real-time odds updates.
- Ability to place and track bets.
- Automatic calculation of dividends.
- Event-driven architecture with Celery (and channel if needed websocket).
- Asynchronous task processing with Celery.

## Getting Started

### Prerequisites

- Python 3.x
- pip
- Virtualenv (optional but recommended)
- Postgresql
- Docker and Docker Compose

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/travis-south/turbo-octo-palm-tree horse_race_betting
   cd horse_race_betting
   ```

2. **Set up a virtual environment (Optional):**

   ```bash
   virtualenv venv
   source venv/bin/activate  # On Unix/MacOS
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://localhost:8000`.

### Docker and Docker Compose

1. **Build and run docker-compose**

   ```bash
   docker-compose up --build
   ```

   The application will be available at `http://localhost:8000`.

### Configuration

- Modify the `horse_race_betting/settings.py` file for project-specific settings.
- Configure Celery in `horse_race_betting/celery.py` as per your requirements.

## Usage

- Access the Django admin panel at `http://localhost:8000/admin` to manage races, horses, and bets.
- Use the web interface to place bets and view race outcomes and odds.

## Running and parsing the csv file

- Run the command below to parse the csv file and process it based on the events.

  ```bash
  python manage.py process_events /absolute/path/to/events.csv
  ```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Irvin Capagcuan – [irvin@capagcuan.org](mailto:irvin@capagcuan.org)

Project Link: [https://github.com/travis-south/horse_race_betting](https://github.com/travis-south/horse_race_betting)
