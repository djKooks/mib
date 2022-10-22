import platform
import subprocess


def copy_to_clip(copy_str: str) -> bool:
    os_type = platform.system()
    
    if os_type == 'Darwin':
        print('type is macos')
        subprocess.run("pbcopy", universal_newlines=True, input=copy_str)
        return True
    elif os_type == 'Linux':
        print('type is linux')
        subprocess.run("xsel", universal_newlines=True, input=copy_str)
        return True
    elif os_type == 'Windows':
        print('type is window')
        subprocess.run("clip", universal_newlines=True, input=copy_str)
        return True
    else:
        print('Unsupported OS to paste on clipboard ... ')
        return False
    
    
