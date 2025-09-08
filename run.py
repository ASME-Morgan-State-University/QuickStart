import sys

if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("If you can see this, the python and virtual environment has been installed successfully.")
else:
    print("Please create and activate the virtual environment first.")