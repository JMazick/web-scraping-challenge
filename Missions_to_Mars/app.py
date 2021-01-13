# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# import libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# %%
app = Flask(__name__)

# %%
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


#template for setting up index
@app.route("/")
def index():
    #listings = mongo.db.listings.find_one()
    #return render_template("index.html", listings=listings)


@app.route("/scrape")
def scraper():
    #listings = mongo.db.listings
    #listings_data = scrape_craigslist.scrape()
    #listings.update({}, listings_data, upsert=True)
    #return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
