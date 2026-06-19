# Async File Processor

A pure Python project that processes text files concurrently using `asyncio` and tracks all events with Python's built-in `logging` module.

The application scans an input directory, validates files based on naming conventions, processes valid files asynchronously, generates processed output files, creates execution logs, and produces a final summary report.

## Features

* Concurrent file processing with `asyncio`
* Asynchronous task orchestration using `asyncio.create_task()` and `asyncio.gather()`
* File validation based on naming rules
* Structured logging to a file
* Automatic report generation
* Exception handling and error tracking
* Execution time measurement

## Project Structure

```text
async-file-processor/
│
├── main.py
├── README.md
│
├── input/
│   ├── good_report.txt
│   ├── good_notes.txt
│   └── bad_data.txt
│
├── output/
│   ├── processed_good_report.txt
│   └── processed_good_notes.txt
│
├── logs/
│   └── app.log
│
└── reports/
    └── report.txt
```

## How It Works

1. Scan the `input/` directory for files.
2. Validate files using naming rules:

   * Files starting with `good_` are processed.
   * Files starting with `bad_` are rejected.
3. Create asynchronous tasks for each file.
4. Process files concurrently.
5. Convert file contents to uppercase.
6. Save processed files to the `output/` directory.
7. Generate logs in `logs/app.log`.
8. Create a summary report in `reports/report.txt`.

## Technologies Used

* Python 3
* asyncio
* logging
* os
* time

## Installation

Clone the repository:

```bash
git clone https://github.com/nerd-10/Ayncio_File_Processor
cd async-file-processor
```

## Run the Project

```bash
python main.py
```

Example output:

```text
Completed in 2.01 seconds
```

## Example Report

```text
Files Processing Report
Total Files: 5
Successful: 3
Failed: 2
Errors: 0
```

## Concepts Demonstrated

* Asynchronous programming
* Event loop fundamentals
* Concurrent task execution
* File system operations
* Structured logging
* Exception handling
* Modular code organization

## Future Improvements

* Add support for additional file types
* Implement configurable validation rules
* Add concurrency limits using `asyncio.Semaphore`
* Add a command-line interface
* Support JSON or CSV reports
* Replace simulated processing with real workloads

## License

This project is intended for learning and portfolio purposes.
