from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task

tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/')
def view_tasks():
    return "TASK PAGE WORKING"


@tasks_bp.route('/add', methods=["POST"])
def add_task():
    return "ADD WORKING"


@tasks_bp.route('/clear', methods=["POST"])
def clear_tasks():
    return "CLEAR WORKING"