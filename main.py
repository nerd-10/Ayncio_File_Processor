import asyncio
import logging
import os
import time

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'
REPORT_DIR = 'reports'
LOG_DIR = 'logs'

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=os.path.join(LOG_DIR, 'app.log')
)

logger = logging.getLogger(__name__)

def scan_files():
    files = [] # List to store file paths
    # Scan the current directory for files and add them to the list
    for filename in os.listdir(INPUT_DIR):
        if os.path.isfile(os.path.join(INPUT_DIR, filename)):
            files.append(os.path.join(INPUT_DIR, filename))
            logger.info(f'Found file: {filename}')
    return files

def validate_file(filepath):
    #to check if the file is good or bad based on file name eg good_file.txt or bad_file.txt
    filename = os.path.basename(filepath)
    if filename.startswith('good_'):
        logger.info(f"Validated file: {filename} is good.")
        return True
    else:
        logger.warning(f"Validated file: {filename} is bad.")
        return False

async def process_file(filepath):
    #simulating the processing of one file
    filename = os.path.basename(filepath)
    logger.info(f"Processing file is started: {filename}")
    #validate the file and return the result
    try:
        if not validate_file(filepath):
            logger.warning(f"Processing file: {filename} failed due to validation error.")
            return {
                'file': filename,
                'status': 'failed',
                'message': f"{filename} processing failed due to validation error."
            }
        with open(filepath, 'r') as f:
            content = f.read()
            processed_content = content.upper()  # Simulate some processing by converting to uppercase
            logger.info(f"Processing file: {filename} content read successfully.")

            await asyncio.sleep(2)  # Simulate processing time
            out_path = os.path.join(OUTPUT_DIR, f"processed_{filename}")
            with open(out_path, 'w') as out_file:
                out_file.write(processed_content)
                logger.info(f"Saved processed file: {out_path} successfully.")

            
            logger.info(f"Processing file: {filename} is completed successfully.")
            return {
                'file': filename,
                'status': 'success',
                "output_path": out_path,
                'message': f"{filename} processed successfully."
            }
    except Exception:
        logger.exception(f"Error occurred while processing file: {filename}.")
        return {
            'file': filename,
            'status': 'error',
            'message': f"{filename} processing failed with an error."
        }

async def process_files(files):
    #simulating the processing of multiple files concurrently using tasks or asyncio.gather
    tasks = []
    for filepath in files:
        task = asyncio.create_task(process_file(filepath))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


def generate_report(results):
    total  = len(results)
    success_count = sum(1 for r in results if r['status'] == 'success')
    failed_count = sum(1 for r in results if r['status'] == 'failed')
    error_count = sum(1 for r in results if r['status'] == 'error')
    report_content = f"Files Processing Report\nTotal Files: {total}\nSuccessful: {success_count}\nFailed: {failed_count}\nErrors: {error_count}\n"
    report_path = os.path.join(REPORT_DIR, 'report.txt')
    with open(report_path, 'w') as report_file:
        report_file.write(report_content)
        logger.info(f"Report generated at: {report_path}")


async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok=True)
    
    start_time = time.perf_counter()

    files = scan_files()
    if not files:
        logger.warning("No files found to process.")
        return

    results = await process_files(files)

    generate_report(results)
    
    end_time = time.perf_counter()
    logger.info(
    f"Completed in {end_time - start_time:.2f} seconds")

    print(f"Completed in {end_time - start_time:.2f} seconds")
if __name__ == '__main__':
    asyncio.run(main())