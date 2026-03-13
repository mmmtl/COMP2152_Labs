# ============================================================
#  WEEK 09 LAB — Q1: SYSTEM INFORMATION REPORTER
#  COMP2152 — Maria Tai
# ============================================================

# Built-in packages from installing Python in the system
import os
import sys
import platform


# --- Helper (provided) — error handling example from Week 06 ---
def display(title, data):
    print(f"\n--- {title} ---")
    for k, v in data.items():
        print(f"  {k:<12} : {v}")


def safe_run(label, func, *args):
    try:
        result = func(*args)
        if result is None:
            print(f"  [!] {label} returned None — missing return?")
            return {}
        return result
    except Exception as e:
        print(f"  [ERROR] {label}: {e}")
        return {}


# TODO: Complete get_system_info()
#   Return a dict with keys: "os", "node", "release", "machine"
#   Use: platform.system(), platform.node(),
#        platform.release(), platform.machine()
def get_system_info():
    return{
        "os" : platform.system(), # return operating system
        "node" : platform.node(), # return system name/hostname
        "release" : platform.release(), # return release version
        "machine" : platform.machine() # return CPU
    }


# TODO: Complete get_python_info()
#   Return a dict with keys: "version", "executable", "platform"
#   Use: sys.version, sys.executable, sys.platform
def get_python_info():
    return {
        "version" : sys.version, # return python version
        "executable" : sys.executable, # return path to execute
        "platform" : sys.platform # return OS in which Python interpreter operates
    }


# TODO: Complete get_directory_info(path)
#   Return a dict with keys: "path", "exists", "file_count", "is_directory"
#   Use: os.path.abspath(), os.path.exists(),
#        os.listdir() (count items), os.path.isdir()
def get_directory_info(path):
    return {
        "path" : os.path.abspath(path), # the absolute path of dir
        "exists" : os.path.exists(path), # does it exist?
        "file_count" : len(os.listdir(path)), # how many files are there?
        "is_directory" : os.path.isdir(path) # is it a dir or a file?
    }


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  SYSTEM INFORMATION REPORTER")
    print("=" * 60)

    info = safe_run("System Info", get_system_info)
    if info: display("System Info", info)

    info = safe_run("Python Info", get_python_info)
    if info: display("Python Info", info)

    info = safe_run("Directory Info", get_directory_info, ".")
    if info: display("Directory Info for '.'", info)

    print("\n" + "=" * 60)