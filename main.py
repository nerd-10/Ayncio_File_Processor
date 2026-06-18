import asyncio
import logging
import os

input_dir = 'input'
output_dir = 'output'
report_dir = 'reports'
log_dir = 'logs'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=os.path.join(log_dir, 'app.log')
)

logger = logging.getLogger(__name__)

def scan_files():
    files = [] # List to store file paths
    # Scan the current directory for files and add them to the list
    for filename in os.listdir(input_dir):
        if os.path.isfile(os.path.join(input_dir, filename)):
            files.append(os.path.join(input_dir, filename))
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
            logger.info(f"Processing file: {filename} content ead successfully.")

            await asyncio.sleep(2)  # Simulate processing time
            out_path = os.path.join(output_dir, f"processed_{filename}")
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
    pass


async def main():
    files = scan_files()
    results = await process_files(files)
    print(results)

if __name__ == '__main__':
    asyncio.run(main())