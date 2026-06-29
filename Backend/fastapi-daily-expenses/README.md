# FastAPI Daily Expenses API

### Overview
This is a backend API project built with FastAPI for managing daily expenses.  
It supports user registration and lays the foundation for authentication and expense tracking.

This project was created as part of my transition into backend engineering.

---
### Features
- User Registration (with password hashing)
- Email uniqueness validation
- SQLite database integration
- Basic API structure using FastAPI
---
### Tech Stack
- Python
- FastAPI
- SQLite
- Passlib (bcrypt for password hashing)
---
### Project Structure
project/
├── main.py
├── database.py
├── security.py
└── expenses.db

---
### Authentication (Current Progress)
- Passwords are hashed using bcrypt
- Email duplication is checked before registration
- Login and JWT authentication are planned as next steps
---
### How to Run
1. Install dependencies:
pip install fastapi uvicorn passlib[bcrypt]
2. Run the server:
uvicorn main:app --reload
3. Open API docs:
http://127.0.0.1:8000/docs
---
### API Example
- Register User
POST /users
- Request:
{
  "name": "test",
  "email": "test@gmail.com",
  "password": "123456"
}
- Response:
{
  "message": "new user added"
}
---
### Future Improvements
- Login system with password verification
- JWT authentication
- User-based transaction access control
- Filtering and analytics for expenses
- Deployment
---
# Author
This project is part of my portfolio as I transition into a backend engineer role.

-----------------------------------------------
### 概要

このプロジェクトは、FastAPIを使用して作成した日々の支出管理用バックエンドAPIです。
ユーザー登録機能を実装し、認証機能の基盤を構築しています。

バックエンドエンジニアへのキャリア転向のために作成しました。

### 機能
- ユーザー登録（パスワードのハッシュ化）
- メールアドレスの重複チェック
- SQLiteデータベース連携
- FastAPIによるAPI構築

---
### 使用技術
- Python
- FastAPI
- SQLite
- Passlib（bcryptによるパスワードハッシュ化）

---
### プロジェクト構成
project/
├── main.py
├── database.py
├── security.py
└── expenses.db

---
### 認証機能（現在の進捗）
- パスワードはbcryptでハッシュ化
- 登録時にメールアドレスの重複をチェック
- ログイン機能およびJWT認証は今後実装予定

---
### 実行方法
- 依存関係をインストール:
pip install fastapi uvicorn passlib[bcrypt]
- サーバー起動:
uvicorn main:app --reload
- APIドキュメント:
http://127.0.0.1:8000/docs

### API例
- ユーザー登録
POST /users
- リクエスト:
{
  "name": "test",
  "email": "test@gmail.com",
  "password": "123456"
}
- レスポンス:
{
  "message": "new user added"
}

### 今後の改善点
- ログイン機能（パスワード検証）
- JWT認証
- ユーザーごとのデータ管理
- フィルタ・分析機能
- デプロイ

### 作成者
バックエンドエンジニアを目指すためのポートフォリオプロジェクトです。
