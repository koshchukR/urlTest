import requests
from bs4 import BeautifulSoup


def count_external_resources(url):
    # Fetch the content of the URL
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Count the number of total and external resources
    total_resources = 0
    external_resources = 0

    # Check for scripts, images, link tags (for CSS), and other relevant tags
    tags_to_check = ['script', 'img', 'link', 'video', 'audio', 'iframe', 'source']
    attrs_to_check = ['src', 'data-src', 'href']

    for tag in tags_to_check:
        elements = soup.find_all(tag)
        total_resources += len(elements)
        for element in elements:
            for attr in attrs_to_check:
                resource = element.get(attr)
                if resource and resource.startswith(('http://', 'https://')) and not resource.startswith(url):
                    external_resources += 1
                    break  # If one external resource is found, break out of the attributes loop
                # Calculate the percentage of external resources
                if total_resources > 0:
                    external_percentage = (external_resources / total_resources) * 100
                else:
                    external_percentage = 0

                return external_resources, total_resources, external_percentage


def calculate_risk_score(percentage):
    if percentage <= 10:
        return 10
    elif percentage <= 20:
        return 20
    elif percentage <= 30:
        return 30
    elif percentage <= 40:
        return 50
    elif percentage <= 60:
        return 60
    else:
        return 70


def content_is_loaded_externally(url):
    external_count, total_count, external_percentage = count_external_resources(url)
    risk_score = calculate_risk_score(external_percentage)

    message = f"Out of {total_count} total resources, {external_count} external resources are loaded from the provided URL. That's {external_percentage:.2f}% external resources."

    return {"message": message, "risk_score": risk_score}
