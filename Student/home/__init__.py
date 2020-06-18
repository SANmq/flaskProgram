from flask import Blueprint, render_template, jsonify

home = Blueprint(__name__, "home")


@home.route('/login', methods=['POST'])
def login():
    return "登录成功"


@home.route('/')
def home_page():
    return render_template('HomePage.html')
