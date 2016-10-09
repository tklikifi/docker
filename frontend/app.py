import flask
import redis


database = redis.Redis(host="redis", port=6379)
channel = redis.StrictRedis(host="redis", port=6379)
app = flask.Flask(__name__)


@app.route("/")
def hello():
    database.incr("hits")
    hits = int(database.get("hits"))
    channel.publish("logger", "Hello number {}.".format(hits))
    return "Hello! You are number {}.\n".format(hits)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
