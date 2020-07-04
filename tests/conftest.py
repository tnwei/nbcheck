import sys
import os

# Add nbcheck to PATH
# Would prefer to use pathlib but not sure how it would work
# w/ sys.path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
