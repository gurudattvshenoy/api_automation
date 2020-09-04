from libs.common.Logger import logger
import traceback

class Assertion():
    @staticmethod
    def assert_equal( actual_output, expected_output, msg):
        logger.debug("actual output is:")
        logger.debug(actual_output)
        logger.debug("expected output is:")
        logger.debug(expected_output)
        try:
            assert actual_output == expected_output, msg
        except AssertionError as e:
            logger.error(traceback.format_exc(), "error")
            raise e

    @staticmethod
    def assert_not_equal( actual_output, expected_output, msg):
        logger.debug("actual output is:")
        logger.debug(actual_output)
        logger.debug("expected output is:")
        logger.debug(expected_output)
        try:
            assert actual_output != expected_output, msg
        except AssertionError as e:
            logger.error(traceback.format_exc(), "error")
            raise e