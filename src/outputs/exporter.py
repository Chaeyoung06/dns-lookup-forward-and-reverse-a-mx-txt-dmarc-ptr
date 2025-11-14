thonimport json
import logging

def export_results(results):
    try:
        with open('data/output_sample.json', 'w') as file:
            json.dump(results, file, indent=4)
        logging.info("Results exported successfully")
    except Exception as e:
        logging.error(f"Error exporting results: {e}")