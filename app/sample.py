from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os, json, redis

# App
application: Flask = Flask(__name__)

# connect to MongoDB
mongoClient = MongoClient(
    'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ[
        'MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_AUTHDB'])
db = mongoClient[os.environ['MONGODB_DATABASE']]

# connect to Redis
redisClient = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=os.environ.get("REDIS_PORT", 6379),
                          db=os.environ.get("REDIS_DB", 0))

game_col = db.Guessing_Game


@application.route('/')
def index():
    game_col.delete_many({})
    return render_template('index.html')


@application.route('/game')
def game():
    game_col.insert_one({
        "answer": [],
        "end": False,
        "wrong_count": 0,
        "state_count": 0,
    })
    current_game = game_col.find_one({"end": False})
    return render_template('game.html', game=current_game)


@application.route('/a-button/')
def a_button():
    current_game = game_col.find_one({"end": False})
    answer = current_game["answer"]
    state = current_game["state_count"]
    wrong_count = current_game["wrong_count"]

    if 0 <= state <= 3:
        answer.append('A')
        state += 1
        game_col.update_one({"end": False}, {"$set": {"answer": answer, "state_count": state}})
    elif 4 <= state <= 7:
        if answer[state - 4] == 'A':
            if state != 7:
                state += 1
                game_col.update_one({"end": False}, {"$set": {"state_count": state}})
            else:
                game_col.update_one({"end": False}, {"$set": {"end": True}})
                return render_template('end.html', game=current_game)
        else:
            wrong_count += 1
            game_col.update_one({"end": False}, {"$set": {"wrong_count": wrong_count}})
    current_game = game_col.find_one({"end": False})
    return render_template('game.html', game=current_game)


@application.route('/b-button/')
def b_button():
    current_game = game_col.find_one({"end": False})
    answer = current_game["answer"]
    state = current_game["state_count"]
    wrong_count = current_game["wrong_count"]

    if 0 <= state <= 3:
        answer.append('B')
        state += 1
        game_col.update_one({"end": False}, {"$set": {"answer": answer, "state_count": state}})
    elif 4 <= state <= 7:
        if answer[state - 4] == 'B':
            if state != 7:
                state += 1
                game_col.update_one({"end": False}, {"$set": {"state_count": state}})
            else:
                game_col.update_one({"end": False}, {"$set": {"end": True}})
                return render_template('end.html', game=current_game)
        else:
            wrong_count += 1
            game_col.update_one({"end": False}, {"$set": {"wrong_count": wrong_count}})
    current_game = game_col.find_one({"end": False})
    return render_template('game.html', game=current_game)


@application.route('/c-button/')
def c_button():
    current_game = game_col.find_one({"end": False})
    answer = current_game["answer"]
    state = current_game["state_count"]
    wrong_count = current_game["wrong_count"]

    if 0 <= state <= 3:
        answer.append('C')
        state += 1
        game_col.update_one({"end": False}, {"$set": {"answer": answer, "state_count": state}})
    elif 4 <= state <= 7:
        if answer[state - 4] == 'C':
            if state != 7:
                state += 1
                game_col.update_one({"end": False}, {"$set": {"state_count": state}})
            else:
                game_col.update_one({"end": False}, {"$set": {"end": True}})
                return render_template('end.html', game=current_game)
        else:
            wrong_count += 1
            game_col.update_one({"end": False}, {"$set": {"wrong_count": wrong_count}})
    current_game = game_col.find_one({"end": False})
    return render_template('game.html', game=current_game)


@application.route('/d-button/')
def d_button():
    current_game = game_col.find_one({"end": False})
    answer = current_game["answer"]
    state = current_game["state_count"]
    wrong_count = current_game["wrong_count"]

    if 0 <= state <= 3:
        answer.append('D')
        state += 1
        game_col.update_one({"end": False}, {"$set": {"answer": answer, "state_count": state}})
    elif 4 <= state <= 7:
        if answer[state - 4] == 'D':
            if state != 7:
                state += 1
                game_col.update_one({"end": False}, {"$set": {"state_count": state}})
            else:
                game_col.update_one({"end": False}, {"$set": {"end": True}})
                return render_template('end.html', game=current_game)
        else:
            wrong_count += 1
            game_col.update_one({"end": False}, {"$set": {"wrong_count": wrong_count}})
    current_game = game_col.find_one({"end": False})
    return render_template('game.html', game=current_game)


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("FLASK_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("FLASK_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
