def parse_resources(api_response_text):
    print("Parsing Response:", api_response_text)  # Debug print

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