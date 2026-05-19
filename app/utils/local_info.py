import os
import platform

"""
List the apps the user has locally, default browsers, etc. 
"""
try:
    if platform.system() == 'Darwin':  # macOS
        locally_installed_apps: list[str] = [app for app in os.listdir('/Applications') if app.endswith('.app')]
    elif platform.system() == 'Windows':  # Windows
        # Get programs from common installation directories
        program_files = []
        if 'PROGRAMFILES' in os.environ:
            program_files.append(os.environ['PROGRAMFILES'])
        if 'PROGRAMFILES(X86)' in os.environ:
            program_files.append(os.environ['PROGRAMFILES(X86)'])
        
        locally_installed_apps = []
        for pf in program_files:
            if os.path.exists(pf):
                for item in os.listdir(pf):
                    if os.path.isdir(os.path.join(pf, item)):
                        locally_installed_apps.append(item)
    else:  # Linux and others
        locally_installed_apps: list[str] = ["Unknown"]
except:
    locally_installed_apps: list[str] = ["Unknown"]

operating_system: str = platform.platform()
