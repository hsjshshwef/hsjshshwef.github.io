"""
Hosting on digital ocean
https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
essentially followed the above instructions with some modifications
Major issues with access rights - apache will fail without giving error message
To solve this made the dermdiag direcory and the data directory 777
"""

#done: capitalization not correct small letters on terms e.g. previous DVT
#done: duplicates in list e.g. hand pain
#done: to url not working for 'preceding injury/insect bite' also not working where '-' is in the term
#done: sections my causes main, my causes all, dermdiags
#done: add my curated diagnoses to front page
#TODO: causes are duplicated for non-derm
#TODO: show causes page for new causes
#TODO: fix duplication of causes e.g. renal stone in causes/flank-pain 
#TODO: sync with server
#TODO: sync data with server - also check that data syncs automatically
#l8tr: show 2 way combinations of terms
#done: google analytics


import flask
from flask import Flask,request,render_template,send_file,session,send_from_directory,make_response
from werkzeug.security import generate_password_hash, check_password_hash
import os



app = Flask(__name__)
app.secret_key = 'PRzMGTysVCalsKJVyUYd'
#base = '/media/sf_magnuslynch/Dropbox/Current Work/Programs/web/dermdiag/'
base = os.path.dirname(os.path.realpath(__file__))+'/'




@app.route('/')
def index():
    return render_template('main.html',title='xdiagnosis')


@app.route('/js/<path:filename>')
def send_js(filename):
    return send_from_directory(base+'js', filename)


@app.route('/img/<path:filename>')
def send_img(filename):
    """
    Serve image that is part of design of website / bootstrap
    TODO: better to server from s3 in the longer term
    """
    return send_from_directory(base+'img', filename)

@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory(base+'css', filename)

@app.route('/fonts/<path:filename>')
def send_fonts(filename):
    return send_from_directory(base+'fonts', filename)

    
def run():
    app.debug=True 
    app.run(host='0.0.0.0',use_evalex=True)

def test():
    print 'hello'

def main():
    run()
    #analyse_logs()
    #test()

try:
	if __name__=='__main__': main()
except KeyboardInterrupt:
	traceback.print_exc()
	print 'Break!'
