import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {str(validation_status)}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {str(validation_status)}")
            return validation_status
        except Exception as e:
            logger.error(f"Error occurred during validation: {e}")
            return False

        # status = True
        # for file in self.config.ALL_REQUIRED_FILES:
        #     file_path = os.path.join(self.config.root_dir, file)
        #     if not os.path.exists(file_path):
        #         logger.info(f"File {file} is missing.")
        #         status = False
        # return status

    # def run_validation(self) -> None:
    #     status = self.validate_all_files_exist()
    #     with open(self.config.STATUS_FILE, 'w') as f:
    #         f.write(str(status))