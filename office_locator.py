#importing all modules.
import csv
from flask  import Flask,render_template,request,jsonify 

#initialing flask app with a name as file name
app= Flask(__name__)

#code whih takes file name and returns a dictionory.
def read_csv(file):
	with open(file,'rt')as f:
		ids=[]
		data = csv.DictReader(f)
		for x in list(data):
			ids.append(x['ServiceID'])
		return ids
		
#reading service file.
with open('office_service_locations.csv','rt')as f:
    locations= list(csv.DictReader(f))

#taking office ids.
ids=read_csv('3451633_1242974339_OfficeServices.csv')

#defining flask app routing.
@app.route('/')
def hello_world():
    return render_template('office_map.html',ctx={})


#getservices api for dynamic dropdown listing.
@app.route('/getservices')
def get_ajax_services():
    query=request.args.get('query')
    i=0
    results=[]
    for id in ids:
      if(str(query) in id) and i<5:
        i=i+1
        results.append({'id':id})  
    return jsonify(results)

#getoffices services which takes service id as argument and returns json objects of related offices.
@app.route('/getoffices')
def get_offices():
    results=[]
    query=request.args.get('serviceid')
    for location in locations:
        if location['ServiceID'] == query:
            location['phone']=location['Phone Number']
            location['name']=location['Contact Name']
            results.append(location)
    ctx= results
    return render_template('office_map.html',ctx={'ctx':ctx ,'q':query})

	
#running flask app.
if __name__ == '__main__':
   app.run(debug = True)
