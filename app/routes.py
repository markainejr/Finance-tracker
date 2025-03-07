from flask import request, jsonify
from app.models import Transaction
from database import db

def init_routes(app):
    @app.route('/transactions', methods=['POST'])
    def add_transaction():
        data = request.get_json()
        if not data or not all(key in data for key in ['description', 'amount', 'date']):
            return jsonify({"error": "Missing required fields"}), 400

        new_transaction = Transaction(
            description=data['description'],
            amount=data['amount'],
            date=data['date']
        )
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify({"message": "Transaction added!", "id": new_transaction.id}), 201

    @app.route('/transactions', methods=['GET'])
    def get_transactions():
        transactions = Transaction.query.all()
        transactions_list = [{
            "id": t.id,
            "description": t.description,
            "amount": t.amount,
            "date": t.date.isoformat()
        } for t in transactions]
        return jsonify(transactions_list), 200

    @app.route('/transactions/<int:transaction_id>', methods=['GET'])
    def get_transaction(transaction_id):
        transaction = Transaction.query.get_or_404(transaction_id)
        return jsonify({
            "id": transaction.id,
            "description": transaction.description,
            "amount": transaction.amount,
            "date": transaction.date.isoformat()
        }), 200

    @app.route('/transactions/<int:transaction_id>', methods=['PUT'])
    def update_transaction(transaction_id):
        transaction = Transaction.query.get_or_404(transaction_id)
        data = request.get_json()

        if 'description' in data:
            transaction.description = data['description']
        if 'amount' in data:
            transaction.amount = data['amount']
        if 'date' in data:
            transaction.date = data['date']

        db.session.commit()
        return jsonify({"message": "Transaction updated!"}), 200

    @app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
    def delete_transaction(transaction_id):
        transaction = Transaction.query.get_or_404(transaction_id)
        db.session.delete(transaction)
        db.session.commit()
        return jsonify({"message": "Transaction deleted!"}), 200

    @app.route('/balance', methods=['GET'])
    def get_balance():
        transactions = Transaction.query.all()
        total_balance = sum(t.amount for t in transactions)
        return jsonify({"total_balance": total_balance}), 200

    @app.route('/transactions/filter', methods=['GET'])
    def filter_transactions():
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        if not start_date or not end_date:
            return jsonify({"error": "Please provide both start_date and end_date"}), 400

        transactions = Transaction.query.filter(
            Transaction.date.between(start_date, end_date))
        transactions_list = [{
            "id": t.id,
            "description": t.description,
            "amount": t.amount,
            "date": t.date.isoformat()
        } for t in transactions]
        return jsonify(transactions_list), 200

    @app.route('/transactions/category/<string:category>', methods=['GET'])
    def get_transactions_by_category(category):
        transactions = Transaction.query.filter_by(category=category).all()
        transactions_list = [{
            "id": t.id,
            "description": t.description,
            "amount": t.amount,
            "date": t.date.isoformat(),
            "category": t.category
        } for t in transactions]
        return jsonify(transactions_list), 200