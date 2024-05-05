import os
import logging
import openai

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the OpenAI API client with the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    logger.error("No API key provided. Set the OPENAI_API_KEY environment variable.")
    exit(1)

def parse_resources(api_response_text):
    resources = []
    current_resource = {}
    lines = api_response_text.split('\n')
    # Use a loop to iterate through lines and maintain an order without relying on finding an index.
    for i, line in enumerate(lines):
        line = line.strip()
        if 'Address:' in line:
            if current_resource:  # When a new address is found, store the last resource
                resources.append(current_resource)
                current_resource = {}
            # Assuming the name is directly above the address line
            if i > 0:  # Ensure there is a line before the address
                previous_line = lines[i-1].strip()
                # Clean up to extract the name
                name = previous_line.split('Name:')[-1].strip()
                name = name.split('.')[0].strip()  # In case there's a numbering like "1."
                current_resource['name'] = name
            address = line.split('Address:')[1].strip()
            current_resource['address'] = address
            current_resource['phone'] = 'Please call for more info'
            current_resource['hours'] = 'Please call for hours'
        elif 'Hours:' in line:
            hours = line.split('Hours:')[1].strip()
            current_resource['hours'] = hours
        elif 'Phone:' in line:
            phone = line.split('Phone:')[1].strip()
            current_resource['phone'] = phone

    if current_resource:  # Append the last parsed resource if any
        resources.append(current_resource)
    return resources




def find_resources(problem, location):
    system_message = """
    You are a specialized assistant for supporting homeless individuals in the specified area.
    You are going to get a problem, and a location
    You will respond in the form of a list of resources that can help the individual with their problem in the specified location.
    In this form:
    Name: ....
    Address: .... 
    Hours: ....
    Phone: ....
    """

    user_message = f"Problem: {problem}. Location: {location}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]
        )
        text = response.choices[0]['message']['content']
        return parse_resources(text)
    except Exception as e:
        logger.error(f"Failed to retrieve resources due to an error: {e}")
        return []

def print_resources(resources):
    if not resources:
        print("No relevant resources found.")
    for resource in resources:
        print(f"\nName: {resource.get('name', 'N/A')}")
        print(f"Address: {resource.get('address', 'N/A')}")
        print(f"Hours: {resource.get('hours', 'Please call for hours')}")
        print(f"Phone: {resource.get('phone', 'Please call for more info')}")

def main():
    cont = True
    while cont:
        problem = input("\nWhat is the problem? ")
        location = input("Where are you located? ")
        resources = find_resources(problem, location)
        print_resources(resources)

        cont_input = input("\nDo you need more help? (Y/N) ")
        cont = cont_input.lower() == 'y'

if __name__ == '__main__':
    main()
