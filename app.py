from flask import Flask, render_template, request
import json
import os.path

# data = ["Mark", "John"]
data = [""]

app = Flask(__name__)


@app.route("/name/create", methods=["POST"])
def name_create():
    name = request.form["create"]
    data.append(name)
    vals = json.dumps({"delete": name})
    response = f"""
    <tr>
        <td><input style="border: none; width=90%; " readonly type="text" name='{name}' value='{name}'></td>
        <td><span id='clickableAwesomeFont'><i class='fas fa-trash fa-lg' name='{{name}}' hx-post='/name/delete' hx-vals='{vals}' hx-target='closest tr' hx-swap='outerHTML swap:0.5s'></i></span></td>
    </tr>
    """
    return response


@app.route("/name/delete", methods=["POST"])
def name_delete():
    name = request.form["delete"]
    print(f"{name} removed")
    data.remove(name)
    return ""


@app.route("/name/order", methods=["POST"])
def name_order():
    global data
    order = request.form.keys()
    data = list(order)
    print(data)
    return f"Stages reordered - "


@app.route("/")
def index():
    return render_template("index.html", items=data)

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=9000, debug=True) # '0.0.0.0' allows browsing from other devices on the LAN.
