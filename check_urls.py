import sys
import os

# Add the project directory to the Python path
# Assumes check_urls.py is in the project root
sys.path.insert(0, os.path.abspath('.'))

try:
    # Import the main urls module
    from pagination_project import urls

    # Check the type of urlpatterns
    if hasattr(urls, 'urlpatterns'):
        print(f"urlpatterns found. Type: {type(urls.urlpatterns)}")
        if isinstance(urls.urlpatterns, (list, tuple)):
            print("urlpatterns is a list or tuple as expected.")
        else:
            print("urlpatterns is NOT a list or tuple.")
    else:
        print("urlpatterns variable not found in pagination_project/urls.py")

except ImportError as e:
    print(f"Error importing pagination_project.urls: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}") 