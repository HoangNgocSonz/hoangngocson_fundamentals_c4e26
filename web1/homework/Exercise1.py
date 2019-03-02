from flask import Flask
app = Flask(__name__)

inf={
        "name":"Hoag Ngoc Son",
        "age":18,
        "school":"Ha Noi national university",
        "hobbies":"code, music, book"
}
@app.route("/about-me")
def me():
    return str(inf)

if __name__ == '__main__':
  app.run(debug=True)

