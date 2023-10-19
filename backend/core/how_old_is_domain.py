from datetime import datetime
from dateutil.parser import parse
from urllib.parse import urlparse
import whois


def extract_domain(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    parsed_uri = urlparse(url)
    domain = f'{parsed_uri.netloc}'.replace("www.", "")

    return domain


def get_domain_age_rating(age_in_days):
    if age_in_days <= 30:
        return 90
    elif age_in_days <= 60:
        return 80
    elif age_in_days <= 180:
        return 50
    elif age_in_days <= 360:
        return 40
    elif age_in_days <= 500:
        return 20
    else:
        return 0


def check_domain_registration(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception as e:
        return f"Unable to fetch WHOIS data for {domain_name}. Error: {e}"

    if type(w.creation_date) in [list, tuple]:
        registration_date = w.creation_date[0]
    else:
        registration_date = w.creation_date
    if isinstance(registration_date, str):
        try:
            registration_date = parse(registration_date)
        except:
            return f"Could not determine the registration date for {domain_name}."

    if not registration_date:
        return f"Could not determine the registration date for {domain_name}."

    age = datetime.now() - registration_date
    age_in_days = age.days
    rating = get_domain_age_rating(age_in_days)

    message = f"The domain {domain_name} was registered on {registration_date.date()} and has a rating of {rating} based on its age."
    return {"message": message, "risk_score": rating}


def how_old_is_domain(url):
    domain_name = extract_domain(url)
    return check_domain_registration(domain_name)
