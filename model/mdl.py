import logging

logger = logging.getLogger(__name__)

class MDL(object):
    START_COGNATE = ["model","modulo","computer","source","hey","service"]
    STOP_COGNATE = ["stop","shut down","computer stop","model stop","modulo stop","source stop","hey stop","service stop"]

    @classmethod
    def action_command(cls, command):
        return any(cognate in command for cognate in cls.START_COGNATE)

    @classmethod
    def handle_action(cls, command, **kwargs):
        command = command.lower()
        logger.debug("Received command: '%s'", command)

        if not cls.action_command(command):
            return
        if any(cognate in command for cognate in cls.STOP_COGNATE):
            logger.info("Stoping Now!")
        else:
            logger.info("Right Away!")
