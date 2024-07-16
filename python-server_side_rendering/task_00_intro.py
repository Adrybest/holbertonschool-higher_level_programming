#bin/usr/python3

def generate_invitations(template, attendees):
    """Generate invitations based on template and attendees
    """
    if not isinstance(template, str):
        raise TypeError("template must be a string")
    if not isinstance(attendees, list):
        raise TypeError("attendees must be a list")
    if not template:
        raise ValueError("template cannot be empty")
    if not attendees:
        raise ValueError("attendees cannot be empty")

    for X, b in enumerate(attendees, start=1):
        content = template
        for placeholders in ["name", "event_title", "event_date", "event_location"]:
                value = b.get(placeholders, "N/A")
                content = content.replace(f"{{{placeholders}}}", value if value else "N/A")

        output = f"output_{X}.txt"
        with open(output, "w") as file:
            file.write(content)
        print(f"Generated {output}")