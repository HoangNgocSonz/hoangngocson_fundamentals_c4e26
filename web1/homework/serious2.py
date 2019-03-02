from flask import Flask
app = Flask(__name__)

inf={
  "son": {
        "name":"Hoag Ngoc Son",
        "age":18,
        "school":"Ha Noi national university",
        "hobbies":"code, music, book",
        },
  "huy":{
        "name":"Ngyen Quang Huy",
        "age":28,
        "school":"Ha Noi national university",
        "hobbies":"music",
        },
  "duy": {
        "name":"Trinh Duc Duy",
        "age":19,
        "school":"Ha Noi national university",
        "hobbies":"sharingan",
        }
}
@app.route("/user/<name>")
def me(name):
  if name in inf:
    return str(inf[name])
  else:
    return "User not found"

if __name__ == '__main__':
  app.run(debug=True)
