"""
curl -X 'POST' \
  'http://totdemoeric.azurewebsites.net//submit' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Your text here"
}'

curl -X 'POST' \
  'http://totdemoeric.azurewebsites.net/generate-solutions/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "human colonization of Mars",
  "perfect_factors": "The distance between Earth and Mars is very large, making regular resupply difficult"
}'
"""