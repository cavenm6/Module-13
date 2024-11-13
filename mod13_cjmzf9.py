from datetime import datetime

def validate_symbol(symbol):
    """Validate that symbol is 1-7 capitalized alpha characters."""
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def validate_chart_type(chart_type):
    """Validate that chart type is either '1' or '2'."""
    return chart_type in ["1", "2"]

def validate_time_series(time_series):
    """Validate that time series is a numeric character between '1' and '4'."""
    return time_series in ["1", "2", "3", "4"]

def validate_date(date_str):
    """Validate that date is in the format YYYY-MM-DD."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
