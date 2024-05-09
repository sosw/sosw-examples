import os

from aws_lambda_powertools import Logger
from aws_xray_sdk.core import patch_all
from sosw.app import Processor as SoswProcessor, get_lambda_handler, LambdaGlobals


logger = Logger()
patch_all()

IS_PROD = os.getenv('env') == 'prod'  # TEMPORARY


class Processor(SoswProcessor):
    DEFAULT_CONFIG = {
    }


    def get_config(self, name):
        pass


    def __call__(self, event):
        """
        Call the Processor
        """
        logger.info("Hello from Lambda!")


global_vars = LambdaGlobals()
lambda_handler = get_lambda_handler(Processor, global_vars)
