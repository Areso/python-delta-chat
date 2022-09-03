# python-delta-chat
pip3 install flask  
python3 -m flask --app deltachat run

```
curl --header "Content-Type: application/json" \
--data '{"msg":"Hello world!"}' \
http://127.0.0.1:5000/post_message
```

```
curl --header "Content-Type: application/json" \
--data '{"timestamp":1662228970}' \
http://127.0.0.1:5000/get_messages
```