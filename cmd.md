docker build -t flask-test-server .

docker run -d -p 5000:5000 --name test-server flask-test-server

curl -X POST -F "file=@test.zip" http://localhost:5000/upload

