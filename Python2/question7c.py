'''
Create a function search_log that takes a log file and a search keyword as input.
The function should find and display all lines containing the search keyword.
'''
def search_log(log_file, search_keyword):
    """Searches for the Keyword in the logfile 

    Args:
        log_file (str): logfile
        search_keyword (str): search key word to search for in the log file 
    """
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()

            matching_lines = [line for line in lines if search_keyword in line]

            if matching_lines:
                print(f"Lines containing '{search_keyword}':")
                for line in matching_lines:
                    print(line.strip())
            else:
                print(f"No lines containing '{search_keyword}' found.")
    except FileNotFoundError:
        print(f"File '{log_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
search_log("data.log", "error")