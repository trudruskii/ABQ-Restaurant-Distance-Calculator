# Imports
import time
from Goodbye import Goodbye as gb
from GeoPoint import GeoPoint


# Function Definitions
# Create a function to display the program header
def display_header():
    """Display the program header."""
    print('Welcome to the Which Restaurant is Closer Calculator.')
    print('This program will calculate the distance between your location and a list of Restaurants.\n')

# Create a function that reads the coordinates and descriptions from a file
def load_points_from_file(file_name):
    """
    Read the coordinates from a specified file and create a variable to store the values.
    """
    # Create an empty list to store the values from the file
    points = []
    try:
        # Open the file to read
        with open(file_name, 'r') as file:
            # Read each line in the file with a for loop
            for line in file:
                # create variables for the latitude, longitude, and description from each line and strip any whitespace
                lat, lon, description = line.strip().split(', ')
                # Create a new GeoPoint variable that can be added to the list using the stripped and split variables for latitude, longitude, and description
                new_point = GeoPoint(float(lat), float(lon), description)
                # Append the new variable to the list
                points.append(new_point)

        # Create a list comprehension to get the descriptions from the points list
        descriptions = [point.Description for point in points]
        # Print the descriptions for the user
        print(" | ".join(descriptions))

    # Handle file not found error
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    # Return the list of coords and descriptions
    return points


# Function to determine the cardinal direction of the latitude and longitude
def cardinal_direction(lat, lon):
    """Determine the cardinal direction of the latitude and longitude."""
    lat_dir = 'N' if lat > 0 else 'S'
    lon_dir = 'E' if lon > 0 else 'W'
    return lat_dir, lon_dir


# Function to display the results to the user
def display_results(closest_point):
    """Display the results to the user."""
    # Create a conditional statement to check if the closest_point does not exist
    if closest_point is None:
        # Print a message if the closest_point does not exist
        print("No coordinates available for comparison.")
        return

    # Create variables for the latitude and longitude of the closest_point
    lat, lon = closest_point.Point
    # Create variables for the cardinal direction of the latitude
    lat_dir, lon_dir = cardinal_direction(lat, lon)
    # Print the results to the user
    print(f'You are closest to: {closest_point.Description}\nWhich is located at: {abs(lat)}° {lat_dir}, {abs(lon)}° {lon_dir}.')


# Main Code
# Display the header
display_header()

# Load points from the Points.txt file by using the file as the argument
point_list = load_points_from_file('Points.txt')

# Initialize the do_another variable to 'y'
do_another = 'y'
# Start the loop
while do_another.lower() == 'y':
    # Ask the user for their location and strip any whitespace
    user_location = input('''To determine which of the restaurants listed above are the closet to a location.\nEnter the location coordinates in this format: 'latitude, longitude': ''').strip()

    # Error handling for invalid input if the user does not separate their coordinates with a comma
    if ',' not in user_location:
        # Print statement to let the user know to separate their coordinates with a comma
        print('Please separate your coordinates with a comma.')
        continue

    # Interim message for better user experience
    print('Calculating the distance from your location to each point...\n')
    time.sleep(1.8)

    try:
        # Split the user's input to be separated by a comma for the latitude and longitude list
        lat, lon = user_location.split(',')
        # Create a GeoPoint variable for the user's location with the latitude and longitude split with a comma
        user_point = GeoPoint(float(lat), float(lon), 'User\'s Location')

        # Use min() to find the closest point by comparing each point in the point_list with the user_point using the Distance method from the GeoPoint class to find the minimum distance and set the default to None if no points are found for comparison
        closest_point = min(point_list, key=lambda point: point.Distance(user_point), default=None)

        # Display the results to the user
        display_results(closest_point)

    # Handle invalid input
    except ValueError:
        print("Invalid input format. Please enter coordinates as latitude, longitude.")

    # Ask the user if they would like to check another location's closest restaurant
    do_another = input('Would you like to check another location? (y/n): ')
    time.sleep(2)
# Goodbye message
print('\nThank you for using the Which Restaurant is Closer Calculator.')
# Call the Goodbye function from the Library package
gb.Goodbye()
