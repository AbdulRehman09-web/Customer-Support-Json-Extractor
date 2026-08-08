import json

responses = [

'''{
  "customer_name":"Sarah Khan",
  "email":"sarah@gmail.com",
  "issue_type":"Shipping",
  "urgency":"High",
  "summary":"Package delayed for 12 days.",
  "sentiment":"Negative"
}''',

'''{
  "customer_name":"",
  "email":"alex99@yahoo.com",
  "issue_type":"Billing",
  "urgency":"High",
  "summary":"Customer reports being charged twice.",
  "sentiment":"Negative"
}''',

'''{
  "customer_name":"David",
  "email":"",
  "issue_type":"Account",
  "urgency":"Medium",
  "summary":"Account repeatedly logs out.",
  "sentiment":"Negative"
}''',

'''{
  "customer_name":"Emily",
  "email":"emily@test.com",
  "issue_type":"Technical",
  "urgency":"High",
  "summary":"Application crashes during file upload.",
  "sentiment":"Negative"
}''',

'''{
  "customer_name":"",
  "email":"",
  "issue_type":"Other",
  "urgency":"Low",
  "summary":"Customer confirms issue is resolved.",
  "sentiment":"Positive"
}'''

]

for i, response in enumerate(responses, start=1):
    try:
        json.loads(response)
        print(f"Test {i}: Valid JSON")
    except json.JSONDecodeError as e:
        print(f"Test {i}: Invalid JSON - {e}")