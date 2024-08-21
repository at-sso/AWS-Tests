from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import User, Book, Loan
from datetime import datetime

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


### User Management ###
@main_bp.route("/users", methods=["GET", "POST"])
def manage_users():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        new_user = User(username=username, email=email)  # type: ignore[reportCallIssue]
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("main.manage_users"))

    users = User.query.all()
    return render_template("users.html", users=users)


@main_bp.route("/users/delete/<int:id>", methods=["POST"])
def delete_user(id: int):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("main.manage_users"))


@main_bp.route("/users/update/<int:id>", methods=["GET", "POST"])
def update_user(id: int):
    user = User.query.get_or_404(id)
    if request.method == "POST":
        user.username = request.form["username"]
        user.email = request.form["email"]
        db.session.commit()
        return redirect(url_for("main.manage_users"))

    return render_template("update_user.html", user=user)


### Book Management ###
@main_bp.route("/books", methods=["GET", "POST"])
def manage_books():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        new_book = Book(title=title, author=author)  # type: ignore[reportCallIssue]
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("main.manage_books"))

    books = Book.query.all()
    return render_template("books.html", books=books)


@main_bp.route("/books/delete/<int:id>", methods=["POST"])
def delete_book(id: int):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("main.manage_books"))


@main_bp.route("/books/update/<int:id>", methods=["GET", "POST"])
def update_book(id: int):
    book = Book.query.get_or_404(id)
    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        db.session.commit()
        return redirect(url_for("main.manage_books"))

    return render_template("update_book.html", book=book)


### Loan Management ###
@main_bp.route("/loans", methods=["GET", "POST"])
def manage_loans():
    if request.method == "POST":
        user_id = request.form["user_id"]
        book_id = request.form["book_id"]
        loan_date = datetime.now()
        new_loan = Loan(user_id=user_id, book_id=book_id, loan_date=loan_date)  # type: ignore[reportCallIssue]
        db.session.add(new_loan)
        db.session.commit()
        return redirect(url_for("main.manage_loans"))

    loans = Loan.query.all()
    return render_template("loans.html", loans=loans)


@main_bp.route("/loans/delete/<int:id>", methods=["POST"])
def delete_loan(id: int):
    loan = Loan.query.get_or_404(id)
    db.session.delete(loan)
    db.session.commit()
    return redirect(url_for("main.manage_loans"))


@main_bp.route("/loans/update/<int:id>", methods=["GET", "POST"])
def update_loan(id: int):
    loan = Loan.query.get_or_404(id)
    if request.method == "POST":
        loan.user_id = request.form["user_id"]
        loan.book_id = request.form["book_id"]
        loan.loan_date = datetime.strptime(request.form["loan_date"], "%Y-%m-%d")
        db.session.commit()
        return redirect(url_for("main.manage_loans"))

    return render_template("update_loan.html", loan=loan)


@main_bp.route("/helloworld")
def hello():
    return render_template("hello_world.html")
