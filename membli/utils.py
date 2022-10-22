import platform
import subprocess
import logging


def logger():
    logging.basicConfig(level=logging.DEBUG)
    membli_logger = logging.getLogger('membli')
    return membli_logger


def copy_to_clip(copy_str: str) -> bool:
    os_type = platform.system()
    logger().debug('platform is : ' + os_type)

    if os_type == 'Darwin':
        logger().debug('type is macos')
        subprocess.run("pbcopy", universal_newlines=True, input=copy_str)
        return True
    elif os_type == 'Linux':
        logger().debug('type is linux')
        subprocess.run("xsel", universal_newlines=True, input=copy_str)
        return True
    elif os_type == 'Windows':
        logger().debug('type is window')
        subprocess.run("clip", universal_newlines=True, input=copy_str)
        return True
    else:
        logger().warn('Unsupported OS to paste on clipboard ... ')
        return False
    
    
