
def explore_menu():
    print("\n----> Explore Module Attributes (dir()) <----")
    module_name = input("\nEnter the name of a module (like:- math, datetime, ...): ")
    try:
        module = __import__(module_name)
        print(f"\nAttributes of '{module_name}' module:")
        print("-" * 40)
        for attr in dir(module):
            print(attr)
    except ModuleNotFoundError:
        print("\nModule not found. Make sure it's a valid built-in or installed module.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
