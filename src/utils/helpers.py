import re
from datetime import datetime

class Helpers:
    """Class for general helper functions."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate an email address."""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        is_valid = re.match(pattern, email) is not None
        print(f"Email validation for '{email}': {is_valid}")
        return is_valid

    @staticmethod
    def format_date(date_str: str, input_format: str, output_format: str) -> str:
        """Format a date string from input format to output format."""
        try:
            date_obj = datetime.strptime(date_str, input_format)
            formatted_date = date_obj.strftime(output_format)
            print(f"Formatted date: {formatted_date}")
            return formatted_date
        except ValueError as e:
            print(f"Error formatting date: {e}")
            return None

    @staticmethod
    def generate_random_string(length: int) -> str:
        """Generate a random string of specified length."""
        import random
        import string
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        print(f"Generated random string: {random_string}")
        return random_string

# Example usage
if __name__ == "__main__":
    print(Helpers.validate_email("test@example.com"))
    print(Helpers.format_date("2023-02-15", "%Y-%m-%d", "%d/%m/%Y"))
    print(Helpers .generate_random_string(10))
