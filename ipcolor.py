from flask import Flask, request, render_template
from pyhipku import encode
import re

app = Flask(__name__)

def iptocolor(ipaddr):
    #turn ip to rgba value
    iplist = ipaddr.split('.')
    ipcolor = str(iplist[0]) + ',' + str(iplist[1]) + ',' + str(iplist[2]) + ',' + str(1.0) #str(round(int(iplist[3])/255,2))
    return ipcolor
    

@app.route('/', methods=['POST', 'GET'])
def iphaiku():
    if request.method == "GET":
        try:
            IPADDRESS = request.headers.get('X-Forwarded-For', request.remote_addr)
            ipcolor = iptocolor(IPADDRESS)
            ipcolortohex = ipcolor.split((","))
            ipcolortohex = [int(x) for x in ipcolortohex[0:3]]
            hexcolor = "".join([format(val, '02X') for val in ipcolortohex])
            # 02X: format options ~> by 2 elements (or 2 zeros) and hex output UPPERCASED
            # x: hex output lowercased
            return render_template('index.html', ipcolor=ipcolor, hexcolor=hexcolor, ip=IPADDRESS)
        except Exception as e: print(e)
            #return("didn't work")

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
