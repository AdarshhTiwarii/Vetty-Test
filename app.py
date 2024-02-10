from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def display_file():
    file_name = request.args.get('file_name', 'file1.txt')
    start_line = int(request.args.get('start_line', 1))
    end_line = int(request.args.get('end_line', -1))

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if end_line == -1:
                content = ''.join(lines[start_line - 1:])
            else:
                content = ''.join(lines[start_line - 1:end_line])

        return render_template('index.html', content=content)
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
