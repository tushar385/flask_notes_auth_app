## call defined app from __init__ 
## by runing this run the application

from website import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True, port=5002)
