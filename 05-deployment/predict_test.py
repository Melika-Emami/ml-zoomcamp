import requests  # type: ignore[import-untyped]

aws_host = "churn-lab.eba-xgnepixu.eu-west-2.elasticbeanstalk.com"
local_host = "localhost:9696"
url = f"http://{local_host}/predict"
customer = {
    "lead_source": "social_media",
    "industry": "healthcare",
    "employment_status": "employed",
    "location": "africa",
    "annual_income": 45051.0,
    "number_of_courses_viewed": 2,
    "interaction_count": 4,
    "lead_score": 0.47,
    "converted": 1,
}
print(requests.post(url, json=customer).json())
