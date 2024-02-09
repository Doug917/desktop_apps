
from flask import Flask, render_template, redirect, url_for, request
import re
import sys

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    results = []
    num_results = 0
    count = 0
    if request.method == 'POST':
        if request.form['submit'] == "Submit":
            query = request.form.get('phrase')
            print(query)
            num_results = int(request.form.get('num_results'))
            print(num_results)
            count = 0
            #load in ASV txt.
            file = open("static/asv.txt", "r")
            for line in file.readlines():
                #serach for query in text.
                if re.search(query.lower(), line.lower()):
                    #print line containing query.
                    results.append(line)
                    count += 1
                    if (count > num_results - 1):
                        file.close()
                        break
            if count < num_results:
                print(f"Total # of results: {count}")
            file.close()
        elif request.form['submit'] == 'Reset':
            results = []
        return render_template("index.html", results=results, num_results=num_results, count=count)
    else:
        return render_template("index.html", results=results, num_results=num_results, count=count)



if __name__ == "__main__":
    app.run(debug=True)


