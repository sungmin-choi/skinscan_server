from flask import Flask, request, jsonify
from products_list import getProductsList
from ingredient_parse import getIngredirentsInfo
from product_info import getProductInfo
from collections import OrderedDict
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
CORS(app)
DATABASE_URL = os.getenv("DATABASE_URL")
FIREBASE_JSON_DIR = os.getenv("FIREBASE_JSON_DIR")

#Firebase database 인증 및 앱 초기화

print(FIREBASE_JSON_DIR)
cred = credentials.Certificate(FIREBASE_JSON_DIR+'/cnm-project-firebase.json')
firebase_admin.initialize_app(cred)

db=firestore.client()


@app.route('/')
def hello_world():
    return FIREBASE_JSON_DIR

@app.route('/search', methods=['GET'])
def search():
    try:
        url=''
        keyword = request.args.get('query')
        q_dict = request.args.to_dict(flat=False)



        if q_dict.get('query') is not None:
             url=url+q_dict.get('query')[0]
        if q_dict.get('activetab') is not None:
            url=url+'&activetab='+q_dict.get('activetab')[0]
        if q_dict.get('ppage') is not None:
            url+=url+'&ppage='+q_dict.get('ppage')[0]

        

        result= getProductsList(url)

      


        answer = {
            'statuscode': 200,
            'result':result
        }
    except Exception as e:
            answer = {
            'statuscode': 500,
            'result': str(e)
        }
    return jsonify(answer)
    
@app.route('/info', methods=['GET'])
def getIngredientInfo():
    try:
        
        result = OrderedDict()
        
        strs = request.args.get('query')

        [url, title] = strs.split('?title=')

        doc_ref = db.collection('products').document(title)

        doc = doc_ref.get()

        if doc.exists:
            result=doc.to_dict()
        else:
            product_info = getProductInfo(url)
            analyze_info= getIngredirentsInfo(product_info['ingredients'])
            result['product_info'] = product_info
            result['analyze_info'] = analyze_info

            doc_ref.set(result)
            
        answer = {
           'statuscode': 200,
            'result': result
         
        }
    except Exception as e:
            answer = {
            'statuscode': 500,
            'result': str(e)
        }
    return jsonify(answer)

if __name__ == '__main__':
    app.run()