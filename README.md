# JamieLiu_Mini2

[![CI](https://github.com/nogibjj/JamieLiu_Mini2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/JamieLiu_Mini2/actions/workflows/cicd.yml)

## Overview

This repo contains work for mini-project 2. It loads the airline safety dataset and generates descriptive statistics on the dataset.

## Features

- `.devcontainer` configuration for a consistent Python development environment using Docker.
- **Makefile** to streamline common tasks like setup, testing, linting.
- **GitHub Actions** for automated CI/CD pipeline (testing, linting, and deployment).
- `requirements.txt` for managing Python dependencies.

## Usage

1. **Clone the repository:**

   ```bash
   git clone git@github.com:nogibjj/JamieLiu_Mini2.git
   ```

2. **Install dependencies:**

   ```bash
   make install
   ```

3. **Format code:**

   ```bash
   make format
   ```

   ![Alt text](format.png)

4. **Lint code:**

   ```bash
   make lint
   ```

   ![Alt text](lint.png)

5. **Test code:**

   ```bash
   make test
   ```

   ![Alt text](test.png)

6. **Run all steps (Install, Format, Lint, Test):**

   ```bash
   make all
   ```

## **Summary Statistics**:

![Alt text](statistics.png)

## **Visualization**:

### Incidents 85-99

![Incidents 85-99](incidents_85_99_over_Airlines.png)

![Incidents 85-99](Frequency_of_incidents_85_99_histogram.png)

### Fatal Accidents 85-99

![Fatal Accidents 85-99](fatal_accidents_85_99_over_Airlines.png)

![Fatal Accidents 85-99](Frequency_of_fatal_accidents_85_99_histogram.png)

### Fatalities 85-99

![Fatalities 85-99](fatalities_85_99_over_Airlines.png)

![Fatalities 85-99](Frequency_of_fatalities_85_99_histogram.png)

### Incidents 00-14

![Incidents 00-14](incidents_00_14_over_Airlines.png)

![Incidents 00-14](Frequency_of_incidents_00_14_histogram.png)

### Fatal Accidents 00-14

![Fatal Accidents 00-14](fatal_accidents_00_14_over_Airlines.png)

![Fatal Accidents 00-14](Frequency_of_fatal_accidents_00_14_histogram.png)

### Fatalities 00-14

![Fatalities 00-14](fatalities_00_14_over_Airlines.png)

![Fatalities 00-14](Frequency_of_fatalities_00_14_histogram.png)
