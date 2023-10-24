import requests
from bs4 import BeautifulSoup


def detect_forms(url):
    # Fetch the content of the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Check for traditional <form> tags
    forms = soup.find_all('form')
    # Check for <input> tags which might indicate potential data collection
    inputs = soup.find_all('input')
    # Define potential JS indicators of form submission or data handling
    js_form_indicators = ['getElementById', 'addEventListener', 'submit', 'fetch', 'XMLHttpRequest']
    # Check for inline JS scripts
    inline_scripts = soup.find_all('script', type="text/javascript")
    inline_form_detected = any(
        indicator in script.text for indicator in js_form_indicators for script in inline_scripts)
    # Check for external JS scripts
    external_scripts = soup.find_all('script', src=True)
    external_form_detected = False
    for script in external_scripts:
        script_url = script['src']
        # Handle relative URLs
        if not script_url.startswith(('http:', 'https:')):
            script_url = response.url + script_url
            script_content = requests.get(script_url).text
            if any(indicator in script_content for indicator in js_form_indicators):
                external_form_detected = True
                break
    # Check for basic authentication
    basic_auth_detected = False
    if 'www-authenticate' in response.headers:
        www_authenticate = response.headers['www-authenticate']
        basic_auth_detected = www_authenticate.lower().startswith('basic')

    # Determine risk score
    if len(forms) > 0 or len(inputs) > 0 or inline_form_detected or external_form_detected or basic_auth_detected:
        return True
    else:
        return False



def webform_to_transmit_data(url):
    forms_risk_score = 0
    message = ''

    print(url)

    if detect_forms(url):
        message = "The webpage appears to have a form, some form of user input, or basic authentication."
        forms_risk_score = 70
    else:
        message = "No obvious forms, user input mechanisms, or basic authentication were detected on the webpage."
        forms_risk_score = 10

    return {"message": message, "risk_score": forms_risk_score}
