import sys
import os

# Add nbcheck to PATH
# Would prefer to use pathlib but not sure how it would work
# w/ sys.path
# This adds cd ../ to path
root_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.append(root_dir)
print(root_dir)
