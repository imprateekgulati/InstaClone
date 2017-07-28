from clarifai.rest import ClarifaiApp


app = ClarifaiApp (api_key='d9cdd283a5754aef87ed239a4b47b876')
model = app.models.get('travel-v1.0')
responce = model.predict_by_url('http://crisscrosstvl.com/wp-content/uploads/2016/05/sunset-plane.png')
print responce